from sets import Set
import re

# + * 3 x * ^ x 2 2
# 2 x 2 ^ *

binary_operators = ['*', '/', '+', '^', '-']
operator_set = Set(binary_operators)


def label_tokens(tok_arr):
    labeled = []
    for token in tok_arr:
        labeled.append(label(token))
    return labeled

def construct_binary_ast_node(op_token, expr1, expr2):
    return (op_token, expr1, expr2)

def construct_const_ast_node(const_token):
    return (const_token)


def construct_ast(labeled_arr):
    param_stack = []
    get_tok_type = lambda token: token[1]
    get_tok_value = lambda token: token[0]
    for labeled in labeled_arr:
        print param_stack
        token_type = get_tok_type(labeled)
        token_value = get_tok_value(labeled)

        if token_type == 'UNKNOWN':
            raise Exception('Unknown Token Type')
        if token_type in ['OPERATOR']:
            if token_value in binary_operators:
                node = construct_binary_ast_node(labeled, param_stack.pop(), param_stack.pop())
                param_stack.append(node)
            else:
                # TODO
                raise Exception('TODO Not Implemented')
        if token_type in ['CONSTANT', 'IDENTIFIER']:
            param_stack.append(construct_const_ast_node(labeled))

    if len(param_stack) != 1:
        raise Exception('Param stack at unexpected size')

    return param_stack

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

# test = ['2', 'x', '2', '^', '*']
# labeled = label_tokens(test)
# print labeled
# ast = construct_ast(labeled)
# print ast
