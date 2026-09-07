"""LeetCode 136. 只出现一次的数字｜难度：简单
题目：数组中只有一个数出现一次，其余都出现两次，找出这个数。
示例：[4,1,2,1,2] → 4
函数：fun(nums)"""
# TODO: 在这里写出完整的 def fun(...): 函数
def fun(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

if __name__ == "__main__":
    assert fun([4, 1, 2, 1, 2]) == 4, "示例1失败"
    print("✅ E09 只出现一次的数字 通过！")
