import docx2txt

def read_docx(filename):
    my_text = docx2txt.process("upload/" + str(filename))
    return my_text

def read_odt(filename):
    with open(filename, 'r') as in_file:
        odt = in_file.read()
    return odt

def get_format(filename):
    dot = "."
    s = filename.find(dot)
    return filename[s:]

