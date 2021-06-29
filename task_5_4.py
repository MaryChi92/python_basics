src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

result_1 = [src[i+1] for i in range(len(src) - 1) if src[i+1] > src[i]]   # способ 1
result_2 = [num_2 for num_1, num_2 in zip(src, src[1:]) if num_2 > num_1]   # способ 2

print(f'{result_1} or {result_2}')
