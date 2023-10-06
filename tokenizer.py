import re


def lexical_analysis(source_code):
    # Define regular expressions
    patterns = [
        (r"\b(void|int|for)\b", "keyword"),
        (r"[a-zA-Z_][a-zA-Z0-9_]*", "identifier"),
        (r"\d+(\.\d+)?(E[+-]?\d+)?", "num"),
        (r"[=+<(){};.]", "symbol"),
        (r"\s+", "whitespace"),
    ]

    tokens = []
    position = 0

    while position < len(source_code):
        match = None
        for pattern, token_type in patterns:
            regex = re.compile(pattern)
            match = regex.match(source_code, position)
            if match:
                value = match.group(0)
                if token_type != "whitespace":
                    tokens.append((token_type, value))
                break

        if not match:
            # Handle unrecognized characters
            tokens.append(("error", source_code[position]))

        position = match.end()

    return tokens


# Read the input file
with open("code.cpp", "r") as file:
    source_code = file.read()

# Perform lexical analysis
tokens = lexical_analysis(source_code)

# Output the tokens
for token_type, value in tokens:
    print(f"{token_type} : {value}")