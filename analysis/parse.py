import re

def parse_text(text):
    # Tokenize the input text based on parentheses and words
    # tokens = re.findall(r'\{|\}|for|while+', text)
    tokens = re.findall(r'\{|\}|\(|\)|\+|\-|\*|\/|\=|\<|\>|\;|\w+', text)


    print(f"Tokens: {tokens}")
    
    def parse_tokens(tokens, idx=0):
        result = []
        i = 0
        while idx < len(tokens):
            token = tokens[idx]
            
            if token == '{':
                # Start a new subtree
                i += 2
                subtree, idx = parse_tokens(tokens, idx + 1)
                result.append(subtree)
            elif token == '}':
                # End current subtree
                return result, idx
            else:
                # Add the token as a leaf node
                if (not result or i >= len(result)):
                    result.append(token)
                else:
                    result[i]+= " " + token

                
            
            idx += 1
        return result, idx
    
    # Start parsing from the first token
    parsed_tree, _ = parse_tokens(tokens)
    return parsed_tree

# Example input text
text = "for (int row =1;row<=3;row++){for (int col = 1; col <= 5; col = g(col+1)+f(i)) { System.out.print(\"*\");            }            System.out.println()        }    }"

# Parse the input text recursively
parsed_output = parse_text(text)
print("Parsed Output:")
print(parsed_output)
