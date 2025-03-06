def generate_permutations(prefix, remaining):
    if not remaining:
        print(" ".join(map(str, prefix)))
    else:
        for i in range(len(remaining)):
            generate_permutations(prefix + [remaining[i]], remaining[:i] + remaining[i + 1:])


n = int(input())
numbers = list(range(1, n + 1))
generate_permutations([], numbers)