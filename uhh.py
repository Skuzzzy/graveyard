
class Text_Reader(object):
    def __init__(self, text):
        self.text = text
        self.pointer = 0

    def next(self):
        self.pointer += 1

    def eof(self):
        return self.pointer < len(self.text)

    def peek(self):
        return self.text[self.pointer]

class String_Blob(object):
    def __init__(self, string):
        self.string = string

    def display(self):
        return '<span>' + self.string + '</span>'

class Paragraph_Blob(object):
    def __init__(self):
        self.elements = []

    def append(self, element):
        self.elements.append(element)

    def extend(self, elements):
        self.elements.extend(elements)

    def display(self):
        body = " ".join([element.display() for element in self.elements])
        return '<p>' + body + '</p>'

class Strong_Blob(object):
    def __init__(self):
        self.elements = []

    def append(self, element):
        self.elements.append(element)

    def extend(self, elements):
        self.elements.extend(elements)

    def display(self):
        body = " ".join([element.display() for element in self.elements])
        return '<b>' + body + '</b>'

class Newline_Element(object):
    def __init__(self):
        pass

    def display(self):
        return '</br>'

def parse_markdan(text):
    reader = Text_Reader(text)

    while not reader.eof():
        if reader.peek() == '!':
            pass
        if reader.peek() != "\\":
            pass

parse_markdan("")

