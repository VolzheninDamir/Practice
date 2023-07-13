def find_combinations(numbers, target_sum):
    combinations = []
    current_combination = []

    def backtrack(start_index, current_sum):
        if current_sum == target_sum:
            combinations.append(current_combination[:])
            return
        if current_sum > target_sum:
            return

        for i in range(start_index, len(numbers)):
            current_combination.append(numbers[i])
            backtrack(i, current_sum + numbers[i])
            current_combination.pop()

    backtrack(0, 0)
    return combinations


# Пример использования
numbers = [2, 4, 6, 8]
target_sum = 10

combinations = find_combinations(numbers, target_sum)
print("Уникальные комбинации суммы", target_sum, ":", combinations)
