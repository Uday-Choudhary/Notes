#Maximum points you can obtain from cards #1423

def maxScore(nums , k):
    left_sum = 0
    right_sum = 0
    max_sum = 0

    for i in range(k):
        left_sum+= nums[i]
    max_sum = left_sum

    right_index = len(nums) - 1
    for i in range(k-1 , -1 , -1):
        left_sum -= nums[i]
        right_sum+= nums[right_index]
        right_index-= 1
        max_sum = max(max_sum , left_sum+right_sum)
        # print(max_sum)

    return max_sum

nums = list(map(int , input().split()))
k = int(input())

print(maxScore(nums , k))
