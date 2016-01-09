import os

def clear():
    """
    Clear method for python repl use
    """
    os.system('clear')

def c():
    """
    Alias for clear
    """
    clear()

def pretty_dir(obj):
    print ("\n".join(dir(obj)))

def pdir(obj):
    pretty_dir(obj)
def doc(obj):
    print (obj.__doc__)
