from functools import cache

@cache
def min_vehicles(weights, max_weight_limit, left_pointer=0, right_pointer=None):
    if right_pointer is None:
        right_pointer = len(weights) - 1

    weights.sort(reverse=True)  # Sort weights in descending order
    vehicles_count = 0

    while left_pointer <= right_pointer:
        current_weight = weights[left_pointer]

        # Check if the current weight can be paired with the weight at the right pointer
        if current_weight + weights[right_pointer] <= max_weight_limit:
            right_pointer -= 1

        # Move to the next weight
        left_pointer += 1
        vehicles_count += 1

    return vehicles_count

# Input processing
weights = list(map(int, input().split()))
max_weight_limit = int(input())

# Output the result
result = min_vehicles(weights, max_weight_limit)
print(result)
