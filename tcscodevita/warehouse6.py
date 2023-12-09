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

# Take input from the user
weights_input = input("Enter weights of bananas (space-separated): ")
weights = list(map(int, weights_input.split()))

limit = int(input("Enter the maximum weight limit of the vehicle: "))

# Output the result
result = minimum_vehicles(weights, limit)
print(f"Minimum number of vehicles needed: {result}")
