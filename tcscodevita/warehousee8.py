def minimum_vehicles(weights, limit):
    weights.sort(reverse=True)
    vehicles, current_weight = 0, 0

    for weight in weights:
        if current_weight + weight <= limit:
            current_weight += weight
        else:
            vehicles += 1
            current_weight = weight

    if current_weight > 0:
        vehicles += 1

    return vehicles

# Input processing
weights_input = input().split()
weights = list(map(int, weights_input[:-1]))  # Exclude the last element, which is the vehicle limit
limit = int(weights_input[-1])  # Last element is the vehicle limit

# Output the result
result = minimum_vehicles(weights, limit)
print(result)
