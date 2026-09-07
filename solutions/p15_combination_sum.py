"""
============================================================
LeetCode 39. 组合总和 (Combination Sum) — Hot 100
============================================================
难度：中等

题目：给你一个无重复元素的整数数组 candidates 和目标整数 target，找出
      candidates 中数字和为 target 的所有不同组合，同一个数字可以重复选取。

示例：
  输入: candidates = [2,3,6,7], target = 7
  输出: [[2,2,3],[7]]

============================================================
Python 语法要点（C++ 对比）
============================================================

1. 内层函数形成闭包
   C++:  function<void(int, int)> backtrack = [&](int start, int remaining) { ... };
   Python: def backtrack(start: int, remaining: int) -> None: ...
   → 内层函数能直接读取外层的 result、path 和 candidates

2. 修改外层可变对象
   C++:  lambda 使用 [&] 捕获后修改 result 和 path
   Python: result.append(...); path.append(...)
   → 修改外层列表的内容不需要 nonlocal；只有重新绑定外层变量时才需要

3. append() 与 pop() 撤销选择
   C++:  path.push_back(candidates[i]); path.pop_back();
   Python: path.append(candidates[i]); path.pop()
   → 回溯返回后用 pop() 恢复进入递归前的路径状态

4. copy() 保存当前路径
   C++:  result.push_back(path);
   Python: result.append(path.copy())
   → 必须保存副本；直接 append(path) 会让所有结果引用同一个可变列表
"""


def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
    """
    排序后回溯搜索；每层从 start 开始枚举，使组合保持有序并避免重复。
    时间复杂度 O(n^(target/min))，空间复杂度 O(target/min)
    """
    candidates.sort()
    result: list[list[int]] = []
    path: list[int] = []

    def backtrack(start: int, remaining: int) -> None:
        if remaining == 0:
            result.append(path.copy())
            return

        for i in range(start, len(candidates)):
            # 排序后当前数字过大，后面的数字也一定过大
            if candidates[i] > remaining:
                break

            # 做选择 → 递归 → 撤销选择
            path.append(candidates[i])
            backtrack(i, remaining - candidates[i])
            path.pop()

    backtrack(0, target)
    return result


# =============================================================================
# 测试代码
# =============================================================================
if __name__ == "__main__":
    result1 = combinationSum([2, 3, 6, 7], 7)
    expected1 = [[2, 2, 3], [7]]
    assert result1 == expected1, f"示例1失败: {result1}"
    assert combinationSum([2], 1) == [], "无解测试失败"
    result3 = combinationSum([2, 3, 5], 8)
    expected3 = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    assert result3 == expected3, f"多解测试失败: {result3}"
    print("✅ P15 组合总和 全部测试通过")
