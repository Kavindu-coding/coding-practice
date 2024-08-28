n = int(input())
arr = list(map(int, input().split()))

max_score = max(arr)
new_scores = []

for num in arr:
    if num!=max_score:
        new_scores.append(num)

print(max(new_scores))



