import re

def tokenize(code_string):
    # Regular expressions for different types of tokens
    patterns = {
        'keyword': r'(void|int|for)',
        'identifier': r'[a-zA-Z_]\w*',
        'operator': r'[+\-*/=]',
        'number': r'\d+(\.\d+)?(?:[eE][+-]?\d+)?',
        'symbol': r'[{()}]',
        'semicolon': r';'
    }

    tokens = []

    # Combine all the regex patterns into a single regex pattern
    combined_pattern = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in patterns.items())

    for match in re.finditer(combined_pattern, code_string):
        for name, value in match.groupdict().items():
            if value:
                tokens.append((name, value))

    return tokens

# Input code string
code_string = """
void main ()
{
int sum = 0;
for(int j=0; j < 10; j=j+1)
{
sum = sum + j + 10.43 + 34E4 + 45.34E-4 + E43 + .34;
}
}
"""

# Tokenize the code string
tokens = tokenize(code_string)

# Print the tokens
for token in tokens:
    print(token)
