import sys
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


def has_common_substring(s, t, length, x, m1, m2):
    h1_s, h2_s = compute_hashes(s, x, m1), compute_hashes(s, x, m2)
    h1_t, h2_t = compute_hashes(t, x, m1), compute_hashes(t, x, m2)

    x_pow1, x_pow2 = preprocess_powers(x, max(len(s), len(t)), m1), preprocess_powers(x, max(len(s), len(t)), m2)

    hashes_s = {}
    for i in range(len(s) - length + 1):
        hash_pair = (get_hash(h1_s, i, length, x_pow1, m1), get_hash(h2_s, i, length, x_pow2, m2))
        hashes_s[hash_pair] = i

    for j in range(len(t) - length + 1):
        hash_pair = (get_hash(h1_t, j, length, x_pow1, m1), get_hash(h2_t, j, length, x_pow2, m2))
        if hash_pair in hashes_s:
            return hashes_s[hash_pair], j, length

    return None


def longest_common_substring(s, t):
    left, right = 0, min(len(s), len(t))
    best_result = (0, 0, 0)

    m1, m2 = 10 ** 9 + 7, 10 ** 9 + 9
    x = random.randint(1, 10 ** 9)

    while left <= right:
        mid = (left + right) // 2
        result = has_common_substring(s, t, mid, x, m1, m2)

        if result:
            best_result = result
            left = mid + 1
        else:
            right = mid - 1

    return best_result


if __name__ == "__main__":
    with open("../txtf/input.txt", "r") as f:
        lines = f.read().strip().split("\n")

    results = []
    for line in lines:
        s, t = line.split()
        i, j, l = longest_common_substring(s, t)
        results.append(f"{i} {j} {l}")

    with open("../txtf/output.txt", "w") as f:
        f.write("\n".join(results) + "\n")
