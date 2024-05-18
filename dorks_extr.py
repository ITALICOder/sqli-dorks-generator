import pyperclip
def deleteandcopy(file_path, d_line):
    with open(file_path, 'r') as file:
        righe = [next(file) for _ in range(d_line)]
        pyperclip.copy(''.join(righe))
    with open(file_path, 'r') as file:
        for _ in range(d_line):
            next(file) 
        contenuto = file.read()
    with open(file_path, 'w') as file:
        file.write(contenuto)
file_path = 'dorks.txt'
d_line = 666
deleteandcopy(file_path, d_line)
