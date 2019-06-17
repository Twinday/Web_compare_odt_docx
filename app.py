import os
from flask import Flask, render_template, request, json

import logics as l
import readDoc as r


app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

files = []


@app.route("/", methods=['GET'])
def main():
    return render_template('index.html')


@app.route("/upload", methods=['POST'])
def upload():
    target = os.path.join(APP_ROOT, 'upload/')

    if not os.path.isdir(target):
        os.mkdir(target)
    print(len(request.files.getlist("file")))
    print(request.files.getlist("file")[0].filename)
    print(request.files.getlist("file")[1].filename)
    for file in request.files.getlist("file"):
        filename = file.filename
        if filename != "":
            files.append(filename)
            destination = "/".join([target, filename])
            file.save(destination)

    return render_template("compare.html")


@app.route("/compare", methods=['POST'])
def compare():
    text1 = ""
    text2 = ""
    if len(files) > 1:
        if r.get_format(files[0]) == ".docx":
            text1 = r.read_docx(files[0])
        elif r.get_format(files[0]) == ".odt":
            text1 = r.read_odt(files[0])

        if r.get_format(files[1]) == ".docx":
            text2 = r.read_docx(files[1])
        elif r.get_format(files[1]) == ".odt":
            text2 = r.read_odt(files[1])

    if text1 == "" or text2 == "":
        files.clear()
        return json.dumps({'message': "Вы загрузили слишком мало файлов."})

    result = l._compare(text1, text2)
    files.clear()
    return json.dumps({'message': result})


if __name__ == "__main__":
    app.run(debug=True)
