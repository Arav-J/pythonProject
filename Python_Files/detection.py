from typing import List
# Array
test_cases = [1, 2, 1, 3, 4, 2, 5, 6, 6]

def is_repeating(l: List[int]) -> None:
# Looks at full range
    for i in range(0, len(l)):
# Goes through each value specifically
        for j in range(i+1, len(l)):
# Looks at index and then each value specifically and stores overlapping value
            if l[i] == l[j]:
                print(l[j])

is_repeating(test_cases)
