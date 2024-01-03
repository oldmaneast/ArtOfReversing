def do_swap(word, a, b):
    if word[a] != word[b]:
        word[a], word[b] = word[b], word[a]

def get_permutation(word, k, m, n_to_stop, n_counter, result):
    if n_counter[0] >= n_to_stop:
        return

    if k == m:
        n_counter[0] += 1
        if n_counter[0] == n_to_stop:
            result.append(''.join(word))
            return
    else:
        for i in range(k, m + 1):
            do_swap(word, k, i)
            get_permutation(word, k + 1, m, n_to_stop, n_counter, result)
            do_swap(word, k, i)

def nPr(n, r):
    return factorial_divide(n, n - r)

def factorial_divide(top_factorial, divide_factorial):
    result = 1
    for i in range(top_factorial, divide_factorial, -1):
        result *= i
    return result

word = list("123456789abcd")
n_to_stop = nPr(len(word), len(word))
n_to_stop = n_to_stop/2
n_counter = [0]
result = []

get_permutation(word, 0, len(word) - 1, n_to_stop, n_counter, result)

result[0] if result else "No permutation found"

