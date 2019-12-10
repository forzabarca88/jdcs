import os

def placeholder_text(file=None):
    if not file:
        file = os.path.join('static', 'placeholder.txt')
    with open(file, 'r', newline='') as opened_file:
            return ''.join(line for line in opened_file.readlines())