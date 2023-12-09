def min_vehicles(banana_weight, max_weight):
  """
  Find the minimum number of vehicles needed to transport bananas.

  Args:
    banana_weight: A list of integers representing the weights of bananas in each godown.
    max_weight: An integer representing the maximum weight capacity of the vehicle.

  Returns:
    An integer representing the minimum number of vehicles needed.
  """
  # Sort the banana weights in descending order.
  banana_weight.sort(reverse=True)

  # Initialize the number of vehicles and current vehicle weight.
  vehicles = 0
  current_weight = 0

  # Iterate over the banana weights.
  for weight in banana_weight:
    # If the current vehicle can accommodate the weight, add it.
    if current_weight + weight <= max_weight:
      current_weight += weight
    # Otherwise, create a new vehicle and add the weight.
    else:
      vehicles += 1
      current_weight = weight

  # If there is a remaining weight, add one more vehicle.
  if current_weight > 0:
    vehicles += 1

  return vehicles

# Read input
n = int(input())
banana_weight = [int(x) for x in input().split()]
max_weight = int(input())

# Find minimum number of vehicles
min_vehicles_needed = min_vehicles(banana_weight, max_weight)

# Print output
print(min_vehicles_needed)