def min_vehicles(weights, max_weight_limit):
    weights.sort(reverse=True)  # Sort weights in descending order
    vehicles_count = 0

    while weights:
        current_weight = weights.pop(0)

        # Find the heaviest available weight that can be paired with the current weight
        pair_index = -1
        for i in range(len(weights) - 1, -1, -1):
            if current_weight + weights[i] <= max_weight_limit:
                pair_index = i
                break

        if pair_index != -1:
            weights.pop(pair_index)

        vehicles_count += 1

    return vehicles_count


# Input processing
weights = list(map(int, input().split()))
max_weight_limit = int(input())

# Output the result
result = min_vehicles(weights, max_weight_limit)
print(result)