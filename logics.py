import difflib

def _compare(text1, text2):
    text1_split = text1.splitlines()
    text2_split = text2.splitlines()

    diff = difflib.Differ().compare(text1_split, text2_split)
    return '\n'.join(diff)
