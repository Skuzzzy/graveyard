from sets import Set
import re

# + * 3 x * ^ x 2 2
# 2 x 2 ^ *

operators = ['*', '/', '+', '^', '-']
operator_set = Set(operators)

test = ['2', 'x', '2', '^', '*']

def label_tokens(tok_arr):
    labeled = []
    for token in tok_arr:
        labeled.append(label(token))
    return labeled

def numerical(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def label(token):
    # ( TOKEN, TYPE )
    if token in operator_set:
        return (token, 'OPERATOR')
    if numerical(token):
        return (token, 'CONSTANT')
    if re.match(r'^[A-z]+$', token):
        return (token, 'IDENTIFIER')

    return (token, 'UNKNOWN')

