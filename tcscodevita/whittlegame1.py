def win_game(nails, m):
    def area(x1, y1, x2, y2, x3, y3):
        return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2)

    def find_area_order(nail1, nail2, nail3):
        return area(nail1[0], nail1[1], nail2[0], nail2[1], nail3[0], nail3[1])

    nails.sort(key=lambda x: (x[1], x[0]))

    for i in range(m):
        min_area = float('inf')
        removed_nail = None

        for j in range(len(nails) - 1):
            for k in range(j + 1, len(nails)):
                current_area = find_area_order(nails[j], nails[k], nails[0])

                if current_area < min_area:
                    min_area = current_area
                    removed_nail = (nails[j][0], nails[j][1])

        print(removed_nail[0], removed_nail[1])
        nails.remove((removed_nail[0], removed_nail[1]))

    if len(nails) % 2 == 0:
        print("YES")
    else:
        print("NO")


# Input processing
n = int(input())
nails = [tuple(map(int, input().split())) for _ in range(n)]
m = int(input())

# Output the result
win_game(nails, m)
