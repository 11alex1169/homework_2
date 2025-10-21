def has_unique_characters(Z):
    seen = set()
    for char in Z:
        if char in seen:
            return False
        seen.add(char)
    return True

def count_characters(Z):
    result = {}
    for char in Z:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result

def reverse_string(Z):
    reversed_str = ""
    for i in range(len(Z)-1, -1, -1):
        reversed_str += Z[i]
    return reversed_str


