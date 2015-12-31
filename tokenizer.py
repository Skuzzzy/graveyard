from __future__ import print_function
import re

# http://www-formal.stanford.edu/jmc/recursive.pdf
def tokenize_m_expr(expression):
    meta_pattern = re.compile(r"""
        ([a-z][a-z0-9]*\s?\[)   |
        (\])                    |
        ([a-z][a-z0-9]*)        |
        (!)                     |
        (&)                     |
        (\|)                     |
        (->)                    |
        (;)
        """, re.X)
    match = re.finditer(meta_pattern, expression)

    tokens = [each.group() for each in match]
    return tokens

def label_m_tokens(str_tokens):
    labels = []
    for token in str_tokens:
        if token[-1] == "[":
            labels.append((token, "OPEN"))
        elif token == "]":
            labels.append((token, "CLOSE"))
        elif token == "!":
            labels.append((token, "NOT"))
        elif token == ";":
            labels.append((token, "SEPR"))
        elif token == "->":
            labels.append((token, "IMP"))
        elif token == "&":
            labels.append((token, "AND"))
        elif token == "|":
            labels.append((token, "OR"))
        else:
            labels.append((token, "ID"))
    return labels

def m_expr_ast(labels):
    pass

res =  tokenize_m_expr("pair[x; y] = [null[x] & null[y] -> NIL; !atom[x] & !atom[y] -> cons[list[car[x]; car[y]]; pair[cdr[x]; cdr[y]]]")
print (res)
lab = label_m_tokens(res)
print()
print (lab)
