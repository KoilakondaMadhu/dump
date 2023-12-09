import heapq

def pick_up_service(n, cities):
    graph = {}
    goods = {}
    entry_tax = {}

    for i in range(n-1):
        city1, city2, g, tax = cities[i].split()
        g, tax = int(g), int(tax)
        
        if city1 not in graph:
            graph[city1] = []
        graph[city1].append((city2, g, tax))
        
        if city2 not in graph:
            graph[city2] = []
        graph[city2].append((city1, g, tax))

    start_city = list(graph.keys())[0]
    route_map = [start_city]
    total_tax = 0

    pq = [(0, start_city, 0)]  # Priority queue to store (entry tax, city, goods)
    visited = set()

    while pq:
        current_tax, current_city, current_goods = heapq.heappop(pq)
        visited.add(current_city)

        if current_city != start_city:
            route_map.append(current_city)
            total_tax += current_tax

        for neighbor, goods, tax in graph[current_city]:
            if neighbor not in visited:
                heapq.heappush(pq, (tax, neighbor, goods))

    route_map = '-'.join(route_map)
    return route_map, total_tax

# Input processing
n = int(input())
cities = [input() for _ in range(n-1)]

# Output the result
result_map, result_tax = pick_up_service(n, cities)
print(result_map)
print(result_tax)
