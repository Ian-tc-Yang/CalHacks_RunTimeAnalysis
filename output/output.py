import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from tree import TreeNode

outputs = ["1", "logN", "N", "N^", "^N", "N!"]

def output(tree):
    output = traverse_tree(tree)
    return output


def traverse_tree(tree):
    if tree.is_leaf():
        return tree.label()
    branches = [traverse_tree(b) for b in tree.branches()]
    max_branch = max_runtime(branches)
    return multiply(max_branch, tree.label())
        

def max_runtime(strings):
    def element_priority(element):
        """Returns the priority of an element based on the output list."""
        output_list = ["1", "logN", "N", "N^", "^N", "N!"]
        # Handle cases like 'N^5' and '6^N' dynamically.
        if "^N" in element:
            return output_list.index("^N")
        elif "N^" in element:
            return output_list.index("N^")
        return output_list.index(element)

    def extract_base_and_exp(element):
        """Extracts the base and exponent from elements like 'a^N' or 'N^b'."""
        if "^N" in element:
            base = int(element.split("^")[0])
            return base, None  # (base, None) for cases like '6^N'
        elif "N^" in element:
            exp = int(element.split("^")[1])
            return None, exp  # (None, exp) for cases like 'N^5'
        return None, None  # For other elements

    def compare_elements(e1, e2):
        """Compare two individual elements."""
        # Handle the 'N!' case: if either element is 'N!', it wins.
        if e1 == "N!" or e2 == "N!":
            return e1 if e1 == "N!" else e2

        # Handle 'a^N' comparisons: check which has the larger base.
        base1, _ = extract_base_and_exp(e1)
        base2, _ = extract_base_and_exp(e2)
        if base1 is not None and base2 is not None:
            return e1 if base1 > base2 else e2

        # Handle 'N^b' comparisons: check which has the larger exponent.
        _, exp1 = extract_base_and_exp(e1)
        _, exp2 = extract_base_and_exp(e2)
        if exp1 is not None and exp2 is not None:
            return e1 if exp1 > exp2 else e2

        # Compare based on priority if not 'a^N' or 'N^b'.
        return e1 if element_priority(e1) > element_priority(e2) else e2

    def compare_strings(s1, s2):
        """Compare two strings containing multiple elements."""
        elements1 = s1.split()
        elements2 = s2.split()

        # Compare corresponding elements one by one.
        for e1, e2 in zip(elements1, elements2):
            winner = compare_elements(e1, e2)
            if winner == e1:
                return s1  # s1 wins if any element of s1 is better
            elif winner == e2:
                return s2  # s2 wins if any element of s2 is better

        # If all elements are tied, return the longer string.
        return s1 if len(s1) >= len(s2) else s2

    # Start with the first string as the current max.
    max_str = strings[0]

    # Compare each string with the current max.
    for s in strings[1:]:
        max_str = compare_strings(max_str, s)

    return max_str


def multiply(current_value, new_value):
    def contains_n_element(s):
        # Split the string into individual elements based on spaces
        elements = s.split()
        # Check if 'N' is present as a standalone element
        return "N" in elements
    
    # Check if new value has a^N and current value also contains it
    if new_value == "1":
        return current_value
    if "^N" in new_value and "^N" in current_value:
        # Extract bases from current and new values
        current_base_str = current_value[current_value.index("^N") - 1]  # Get the base a from current
        new_base_str = new_value[new_value.index("^N") - 1]  # Get the base a from new
        current_base = int(current_base_str)  # Convert to integer
        new_base = int(new_base_str)  # Convert to integer
        new_combined_base = current_base * new_base  # Multiply the bases
        # Update the current value string
        current_value = current_value.replace(f"{current_base_str}^N", f"{new_combined_base}^N")
        return current_value
    
    # Check if new value has N^a and current value also contains it
    elif "N^" in new_value and "N^" in current_value:
        # Extract exponents from current and new values
        current_exponent_str = current_value[current_value.index("N^") + 2]  # Get exponent b from current
        new_exponent_str = new_value[new_value.index("N^") + 2]  # Get exponent b from new
        current_exponent = int(current_exponent_str)  # Convert to integer
        new_exponent = int(new_exponent_str)  # Convert to integer
        new_combined_exponent = current_exponent + new_exponent  # Add the exponents
        # Update the current value string
        current_value = current_value.replace(f"N^{current_exponent_str}", f"N^{new_combined_exponent}")
        return current_value
    
    # Handle case: N multiplied by N^a = N^(a+1)
    if contains_n_element(current_value) and "N^" in new_value:
        new_exponent_str = new_value[new_value.index("N^") + 2]
        new_exponent = int(new_exponent_str)  # Convert to integer
        return current_value.replace("N", f"N^{new_exponent + 1}")

    if contains_n_element(new_value) and "N^" in current_value:
        current_exponent_str = current_value[current_value.index("N^") + 2]
        current_exponent = int(current_exponent_str)  # Convert to integer
        return current_value.replace(f"N^{current_exponent}", f"N^{current_exponent + 1}")
    
    if contains_n_element(new_value) and contains_n_element(current_value):
        return current_value.replace(f"N", f"N^{2}")
    
    # If current value contains N! and new value does not have ^N, return just N!
    if "N!" in current_value and "^N" not in new_value:
        return "N!"
    
    # Otherwise, concatenate the new value to the current value
    current_value += f" {new_value}"  # Add a space before concatenating
    return current_value