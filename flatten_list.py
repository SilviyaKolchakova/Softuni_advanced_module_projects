string = input().split('|')

result = []

for i in range(len(string) - 1, -1, -1):
    next_list = string[i].split()
    result += next_list

print(' '.join(result))
