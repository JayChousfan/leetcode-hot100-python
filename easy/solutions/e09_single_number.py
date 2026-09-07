"""LeetCode 136. 只出现一次的数字 (Single Number) — Hot 100
难度：简单
题目：数组中只有一个数出现一次，其余都出现两次，找出这个数。
示例：[4,1,2,1,2] → 4
思路：使用异或让相同数字互相抵消。"""


def fun(nums):
    """异或全部元素。时间 O(n)，空间 O(1)。"""
    result = 0
    for num in nums:
        result ^= num
    return result


if __name__ == "__main__":
    assert fun([2, 2, 1]) == 1, "示例1失败"
    assert fun([4, 1, 2, 1, 2]) == 4, "示例2失败"
    print("✅ E09 只出现一次的数字 全部测试通过")
