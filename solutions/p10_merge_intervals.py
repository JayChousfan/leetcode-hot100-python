"""
============================================================
LeetCode 56. 合并区间 (Merge Intervals) — Hot 100
============================================================
难度：中等

题目：给定一个区间数组 intervals，其中 intervals[i] = [start, end]。
      合并所有重叠区间，并返回互不重叠且覆盖原输入的区间数组。

示例：
  输入: intervals = [[1,3],[2,6],[8,10],[15,18]]
  输出: [[1,6],[8,10],[15,18]]

============================================================
Python 语法要点（C++ 对比）
============================================================

1. lambda 匿名函数指定排序键
   C++:  sort(intervals.begin(), intervals.end(), comparator);
   Python: intervals.sort(key=lambda interval: interval[0])
   → key 函数返回用于比较的值，这里按区间起点升序排列

2. 直接遍历区间列表
   C++:  for (const auto& interval : intervals)
   Python: for interval in intervals:
   → interval[0] 是起点，interval[1] 是终点，名称与题目描述保持一致

3. 负数索引访问最后一个元素
   C++:  result.back()
   Python: result[-1]
   → result[-1][1] 表示最后一个已合并区间的终点

4. 原地修改嵌套列表
   C++:  result.back()[1] = max(result.back()[1], end);
   Python: result[-1][1] = max(result[-1][1], end)
   → 内层区间也是可变列表，可以直接更新终点
"""


def merge(intervals: list[list[int]]) -> list[list[int]]:
    """
    按起点排序，依次与结果中的最后一个区间比较并合并。
    时间复杂度 O(n log n)，空间复杂度 O(n)
    """
    intervals.sort(key=lambda interval: interval[0])  # 按区间起点升序排序
    result: list[list[int]] = []

    for interval in intervals:
        # 无重叠时直接加入新区间
        if not result or result[-1][1] < interval[0]:
            result.append(interval)
        # 有重叠时更新最后一个区间的右端点
        else:
            result[-1][1] = max(result[-1][1], interval[1])

    return result


# =============================================================================
# 测试代码
# =============================================================================
if __name__ == "__main__":
    result1 = merge([[1, 3], [2, 6], [8, 10], [15, 18]])
    expected1 = [[1, 6], [8, 10], [15, 18]]
    assert result1 == expected1, f"示例1失败: {result1}"
    assert merge([[1, 4], [4, 5]]) == [[1, 5]], "端点重叠测试失败"
    assert merge([[1, 4]]) == [[1, 4]], "单区间测试失败"
    print("✅ P10 合并区间 全部测试通过")
