src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

unique_nums = set()
temporary = set()

for num in src:
    if num not in temporary:
        unique_nums.add(num)
    else:
        unique_nums.discard(num)
    temporary.add(num)

unique_nums = [num for num in src if num in unique_nums]

print(unique_nums)
