# # Maximum points you can obtain from cards #1423

# def maxScore(nums, k):
#     left_sum = 0
#     right_sum = 0
#     max_sum = 0

#     for i in range(k):
#         left_sum += nums[i]
#     max_sum = left_sum

#     right_index = len(nums) - 1
#     for i in range(k-1, -1, -1):
#         left_sum -= nums[i]
#         right_sum += nums[right_index]
#         right_index -= 1
#         max_sum = max(max_sum, left_sum+right_sum)
#         # print(max_sum)

#     return max_sum


# nums = list(map(int, input().split()))
# k = int(input())

# print(maxScore(nums, k))
# # phele 4 term ka sum liya left me dala fir kam karte gye or right add karte gye of sabka max jo banta jaa rha tha usko max me update karte gye


# Search in Rotated Sorted Arr
nums = list(map(int, input().split()))
target = int(input())
point = 0

# Find rotation point correctly
       for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                point = i
                break

        def rotatedSearch1(nums, target):
            low = point 
            high = len(nums) - 1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
            return -1

        def rotatedSearch2(nums, target):
            low = 0
            high = point - 1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
            return -1

        ans1 = rotatedSearch1(nums, target)
        ans2 = rotatedSearch2(nums, target)

        # If both failed, print -1
        if ans1 == -1 and ans2 == -1:
            print(-1)
        else:
           print(ans1 if ans1 != -1 else ans2)
