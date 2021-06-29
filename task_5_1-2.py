# 5_1
def odd_nums(n):
    for num in range(1, n+1, 2):
        yield num


odd_to_105 = odd_nums(105)

print(next(odd_to_105))
print(next(odd_to_105))
print(next(odd_to_105))
print('-'*30)
for i in odd_to_105:
    print(i)

# 5_2
odd_nums = (num for num in range(1, 31 + 1, 2))

for i in odd_nums:
    print(i)