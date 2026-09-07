"""LeetCode 169. 多数元素 (Majority Element) — Hot 100
难度：简单
题目：找出数组中出现次数超过一半的元素。
示例：[3,2,3] → 3
思路：Boyer-Moore 投票，相同加票，不同抵消。"""


def fun(nums):
    """维护候选人与票数。时间 O(n)，空间 O(1)。"""
    candidate = 0
    count = 0
    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1
    return candidate


if __name__ == "__main__":
    assert fun([3, 2, 3]) == 3, "示例1失败"
    assert fun([2, 2, 1, 1, 1, 2, 2]) == 2, "示例2失败"
    print("✅ E12 多数元素 全部测试通过")
