def two_sum(numbers: list[int], target: int) -> tuple[int, int]:
    seen = {}
    for i, num in enumerate(numbers):
        remaining = target - num
        if remaining in seen:
            return (seen[remaining], i)
        else:
            seen[num] = i