def points(games):
    points_x = 0
    for match in games:
        x, y = map(int, match.split(':'))
        if x > y:
            points_x += 3
        elif x == y:
            points_x += 1
    return points_x

#solução one-liner
def points(games):
    return sum(3 if match[0] > match[2] else 1 if match[0] == match[2] else 0 for match in games)