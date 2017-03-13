n, numlist = int(input()), list(map(int, input().split()))
print(all([len(list(filter(lambda x: x > 0, numlist))) == n, any([str(num) == str(num)[::-1] for num in numlist])]))
