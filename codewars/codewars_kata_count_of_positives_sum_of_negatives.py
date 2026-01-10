def count_positives_sum_negatives(arr: list) -> list:
    if not arr:
        return []
    count_positive = sum_negatives = 0
    for x in arr:
        if x > 0:
            count_positive += 1
        elif x < 0:
            sum_negatives +=x

    return [count_positive, sum_negatives]