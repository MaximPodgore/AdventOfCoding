from collections import defaultdict
'''
Have a set of all nums in the array(excl last one).
+hashmap of positions so that we can tell if num is further down the set
Store last num somewhere
check if num higher exists in the set.
if not, keep this num
'''


batteries = """
987654321111111
811111111111119
234234234234278
818181911112111
"""
# with open('day3_input.txt') as f:
#     batteries = f.read()

banks = batteries.strip().split('\n')

def max_subsequence_of_length_k(s: str, k: int) -> str:
    deletions = len(s) - k
    stack = []
    for c in s:
        while deletions > 0 and stack and stack[-1] < c:
            stack.pop()
            deletions -= 1
        stack.append(c)
    if deletions > 0:
        stack = stack[:-deletions]
    return ''.join(stack[:k])

k = 12

total = 0
results = []
for bank in banks:
    result = max_subsequence_of_length_k(bank.strip(), k)
    results.append(result)
    total += int(result)

for r in results:
    print(r)
print(total)