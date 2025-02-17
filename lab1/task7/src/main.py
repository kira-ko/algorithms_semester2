def max_boots(k, n, times):
    times.sort()

    total_time = 0
    cnt = 0

    for time in times:
        if total_time + time <= k:
            total_time += time
            cnt += 1
        else:
            break #выход если время работы превышает K
    return cnt

if __name__ == "__main__":
    with open('../txtf/input.txt', 'r') as f:
        k, n = map(int, f.readline().split())
        times = list(map(int, f.readline().split()))

    result = max_boots(k, n, times)

    with open('../txtf/output.txt', 'w') as f:
        f.write(str(result))


