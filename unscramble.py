# Unscramble unique characters and actual output

def reorder_strings(jumbled_base, jumbled_other):
    original = "123456789abcd"
    index_map = {char: i for i, char in enumerate(jumbled_base)}
    reordered_base = ''.join(sorted(jumbled_base, key=lambda x: index_map[x]))
    reordered_other = ''.join(jumbled_other[index_map[char]] for char in original)

    return reordered_base, reordered_other

jumbled_base = "32561d4c78a9b"
jumbled_other = "cathhtkeepaln"

original_base, original_other = reorder_strings(jumbled_base, jumbled_other)
original_base, original_other