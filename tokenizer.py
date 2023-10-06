import re

def tokenize_file(file_path):
    with open(file_path, 'r') as file:
        code_string = file.read()

    # Define regular expressions for different types of tokens
    regex_patterns = [
        ('keyword', r'\b(void|int|for)\b'),
        ('identifier', r'\b[a-zA-Z_]\w*\b'),
        ('num', r'\b\d+(?:\.\d+)?(?:[eE][-+]?\d+)?\b'),
        ('SYMBOL', r'[()+\-=;{},.]'),
        ('WHITESPACE', r'\s+')
    ]

    tokens = []
    line_number = 1

    while code_string:
        match = None
        for token_type, pattern in regex_patterns:
            match = re.match(pattern, code_string)
            if match:
                token_value = match.group(0)
                if token_type != 'WHITESPACE':
                    tokens.append((line_number, token_type, token_value))
                break

        if not match:
            raise ValueError(f"Invalid token at line {line_number}")

        code_string = code_string[match.end():]
        if '\n' in token_value:
            line_number += token_value.count('\n')

    return tokens

# Usage example
file_path = 'input_file.txt'
tokens = tokenize_file(file_path)

for line_number, token_type, token_value in tokens:
    print(f"Line {line_number}: {token_type} - '{token_value}'")