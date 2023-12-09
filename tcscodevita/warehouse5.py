def min_vehicles(weights, max_weight_limit):
    weights.sort(reverse=True)  # Sort weights in descending order
    left, right = 0, len(weights) - 1
    vehicles_count = 0

    while left <= right:
        if weights[left] + weights[right] <= max_weight_limit:
            left += 1
        right -= 1
        vehicles_count += 1

    return vehicles_count

# Input processing
weights = list(map(int, input().split()))
max_weight_limit = int(input())

# Output the result
result = min_vehicles(weights, max_weight_limit)
print(result)
