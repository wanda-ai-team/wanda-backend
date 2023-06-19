import os

def readFile(filePath: str) -> str:
    output = ''
    with open(filePath, 'r') as file:
        output = file.read()

    os.remove(filePath)
    return output
