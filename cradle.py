from __future__ import print_function
import readchar
import sys

tab = "\t"

look = ' '

def getChar():
    global look
    look = readchar.readchar()

def error(err):
    print("Error: " + str(err) + ".")

def abort(s):
    error(s)
    sys.exit()

def expected(s):
    abort(s + " Expected")

def match(x):
    if look == x:
        getChar()
    else:
        expected("\'" + x + "\'")

def isAlpha(char):
    return char.isalpha()

def isDigit(char):
    return char.isdigit()

def getName():
    if not isAlpha(look):
        expected("Name")

    val = look.upper()
    getChar()
    return val

def getNum():
    if not isDigit(look):
        expected("Integer")

    val = look
    getChar()
    return val

def emit(s):
    sys.stdout.write(tab + str(s))
    sys.stdout.flush()

def emitLn(s):
    emit(str(s) + "\n")

def init():
    getChar();

def term():
    emitLn("MOVE #" + getNum() + ",D0")

def add():
    match("+")
    term()
    emitLn("ADD D1,D0")

def subtract():
    match("-")
    term()
    emitLn("SUB D1,D0")

def expression():
    term()
    emitLn("MOVE D0,D1")
    if look == "+":
        add()
    if look == "-":
        subtract()
    else:
        expected("Addop")

if __name__ == "__main__":
    init()
    expression()
