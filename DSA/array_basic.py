# Subarray generation
def generate_subarrays(arr):
    subarrays = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr) + 1):
            subarrays.append(arr[i:j])
    return subarrays

# Example usage:
arr = [1, 2, 3]
subarrays = generate_subarrays(arr)
print(subarrays)

# Output: [[1], [1, 2], [1, 2, 3], [2], [2, 3], [3]]
# Subsequence generation
def generate_subsequences(arr):
    subsequences = []
    
    def backtrack(index, current_subsequence):
        if index == len(arr):
            subsequences.append(current_subsequence[:])  # Append a copy of the current subsequence
            return
        
        # Include the current element in the subsequence
        current_subsequence.append(arr[index])
        backtrack(index + 1, current_subsequence)
        
        # Exclude the current element from the subsequence
        current_subsequence.pop()
        backtrack(index + 1, current_subsequence)
    
    backtrack(0, [])
    return subsequences

# Example usage:
arr = [1, 2, 3]
subsequences = generate_subsequences(arr)
print(subsequences)
# Output: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]