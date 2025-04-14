import lis # type: ignore

numbers = [10, 22, 9, 33, 21, 50, 41, 60, 80, 5, 6, 7, 8, 9]
result = lis.longest_increasing_subsequence(numbers)
print(f"Input array: {numbers}")
print(f"Longest increasing subsequence: {result}")