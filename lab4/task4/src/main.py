import random

def compute_hashes(s, x, m):
    n = len(s)
    h = [0] * (n + 1)
    for i in range(1, n + 1):
        h[i] = (x * h[i - 1] + ord(s[i - 1])) % m
    return h


def get_hash(h, a, l, x_pow, m):
    return (h[a + l] - x_pow[l] * h[a] % m + m) % m


def preprocess_powers(x, max_len, m):
    x_pow = [1] * (max_len + 1)
    for i in range(1, max_len + 1):
        x_pow[i] = (x_pow[i - 1] * x) % m
    return x_pow


if __name__ == "__main__":
    # Чтение входных данных
    with open("../txtf/input.txt", "r") as f:
        s = f.readline().strip()
        q = int(f.readline().strip())
        queries = [tuple(map(int, f.readline().split())) for _ in range(q)]

    n = len(s)
    m1, m2 = 10 ** 9 + 7, 10 ** 9 + 9
    x = random.randint(1, 10 ** 9)

    h1 = compute_hashes(s, x, m1)
    h2 = compute_hashes(s, x, m2)

    x_pow1 = preprocess_powers(x, n, m1)
    x_pow2 = preprocess_powers(x, n, m2)

    results = []
    for a, b, l in queries:
        hash_a1 = get_hash(h1, a, l, x_pow1, m1)
        hash_b1 = get_hash(h1, b, l, x_pow1, m1)
        hash_a2 = get_hash(h2, a, l, x_pow2, m2)
        hash_b2 = get_hash(h2, b, l, x_pow2, m2)

        if hash_a1 == hash_b1 and hash_a2 == hash_b2:
            results.append("Yes")
        else:
            results.append("No")

    with open("../txtf/output.txt", "w") as f:
        f.write("\n".join(results) + "\n")