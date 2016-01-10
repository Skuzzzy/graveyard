
from parse import get_token_type, get_token_value, construct_binary_ast_node, label

def derive(expression, respect_to):
    # TODO Fix access for operator expressions
    # EX * 5 x
    token_type = get_token_type(expression[0])
    token_value = get_token_value(expression[0])

    if token_type in ['CONSTANT']:
        return construct_binary_ast_node(
                    label('*'),
                    expression,
                    label(respect_to)
                )
    if token_type in ['IDENTIFIER']:
        # Check if in respect to identifier
        if token_type == respect_to:
            return construct_binary_ast_node(
                        label('^'),
                        expression,
                        label('2')
                    )
        else:
            return construct_binary_ast_node(
                        label('*'),
                        expression,
                        label(respect_to)
                    )
    if token_type in ['OPERATOR']:
        # TODO implement this monster by implementing each operator individually
        raise Exception('TODO Not Implemented')

