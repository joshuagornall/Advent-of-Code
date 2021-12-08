"""
Super speedy data reading and formatting prefix in the code. It seems all data is given in a format pretty similar.
"""
with open("input.txt", "r") as f:
    src = data = f.read()

if data and data[-1] == "\n":
    data = data[:-1]

original = data
lines = data.splitlines()

py_input = input

def input():
    global data
    if data:
        try:
            line, data = data.split("\n", 1)
        except:
            line = data
            data = ""
        return line
    return py_input()
