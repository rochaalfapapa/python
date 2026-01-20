def better_than_average(class_points: list, your_points: int) ->bool:
    return your_points > (sum(class_points) + your_points) / (len(class_points) + 1)

#Solução simplificada
def better_than_average(class_points: list, your_points: int) ->bool:
    return your_points > sum(class_points) / len(class_points)