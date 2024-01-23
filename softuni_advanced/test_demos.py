from collections import deque
r, c = (int(x) for x in input().split())
word_matrix = [] * r
word = input()

for i in range(r):
    word_matrix.append([])
    for j in range(c):
        word_matrix[i].append([x for x in word])
print(word_matrix)
matrix = []

for _ in range(r):
    matrix.append([])

print(matrix)
for re in range(r - 1):
    for ce in range(c - 1):
        if re % 2 == 0:
            matrix[r].append(word.pop())
        else:
            matrix[r].append(word.pop())



