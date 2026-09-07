"""LeetCode 448. 找到所有数组中消失的数字 (Find All Numbers Disappeared in an Array) — Hot 100
难度：简单
题目：找出 1 到 n 中没有出现在长度为 n 的数组里的数字。
示例：[4,3,2,7,8,2,3,1] → [5,6]
思路：利用负号在原数组中标记已经出现的数字。"""


def fun(nums):
    """原地负号标记出现过的数字。时间 O(n)，空间 O(1)。"""
    for num in nums:
        i = abs(num) - 1
        nums[i] = -abs(nums[i])

    result = []
    for i, num in enumerate(nums):
        if num > 0:
            result.append(i + 1)
    return result


if __name__ == "__main__":
    assert fun([4, 3, 2, 7, 8, 2, 3, 1]) == [5, 6], "示例1失败"
    assert fun([1, 1]) == [2], "重复元素测试失败"
    print("✅ E18 找到所有数组中消失的数字 全部测试通过")
