def binary_search(numbers, target):
    start = 0
    end = len(numbers) -1


    while start <= end:
        middle = (start + end) // 2

        if numbers[middle] == target: return middle

        if numbers[middle] < target:
            start = middle + 1
        else:
            end = middle - 1

    return - 1

teste = [1,2,3,4,5,6,7,8,9]
print(binary_search(teste, 0))