def maximum_neatness_value(N, X, weights):
    weights.sort()
    neatness_value = 0
    total_weight = 0

    for weight in weights:
        if total_weight + weight <= X:
            neatness_value += 1
            total_weight += weight
        else:
            break

    return neatness_value

T = int(input())
for _ in range(T):
    N, X = map(int, input().split())
    weights = list(map(int, input().split()))
    print(maximum_neatness_value(N, X, weights))