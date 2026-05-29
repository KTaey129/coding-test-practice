# 문제 1. 두 수의 합 — 해시맵 기본 조회
# 난이도: Easy
# 정수 배열 nums와 정수 target이 주어진다. 두 원소를 더해 target이 되는 두 원소의 인덱스를 반환하라. 정답은 유일하게 존재하며, 같은 원소를 두 번 쓸 수 없다.
# 입력:  nums = [2, 7, 11, 15], target = 9
# 출력:  [0, 1]          # nums[0] + nums[1] = 2 + 7 = 9

# 입력:  nums = [3, 2, 4], target = 6
# 출력:  [1, 2]
# 제약: 2 ≤ len(nums) ≤ 10⁴, 한 번의 순회(O(n))로 풀 것.

def two_sum(nums, target):
    num_to_index = {}
    # save each number and its index in a hash map
    for i, num in enumerate(nums):
        # enumerate() is a built-in function that adds a counter to an iteratable and returns it as an enumerate object. 
        # It can be used to get both the index and the value of each element in a list during iteration.
        complement = target - num
        # compleement is the number we need to find in the hash map to reach the target when added to the current number
        if complement in num_to_index:
        # if the complement is already in the hash map, it means we have found the two numbers that add up to the target
            return [num_to_index[complement], i]
            # return the indices of the two numbers
        num_to_index[num] = i
        # if the complement is not in the hash map, we add the current numeber and its index to the hash map for future reference
        return None
        # if we finish the loop without finding a solution, we return None

assert two_sum([2, 7, 11, 15], 9) == [0, 1]
assert two_sum([3, 2, 4], 6) == [1, 2]