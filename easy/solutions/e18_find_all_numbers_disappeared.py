"""LeetCode 448. 找到所有数组中消失的数字 (Find All Numbers Disappeared in an Array) — Hot 100
难度：简单
利用元素绝对值定位下标，再用负号原地标记已经出现。"""


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
