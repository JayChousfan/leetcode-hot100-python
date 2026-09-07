"""
============================================================
LeetCode 739. 每日温度 (Daily Temperatures) — Hot 100
============================================================
难度：中等

题目：给定每日温度数组 temperatures，返回一个数组 result，其中 result[i]
      表示第 i 天之后要等多少天才会有更高温度；没有则为 0。

示例：
  输入: temperatures = [73,74,75,71,69,72,76,73]
  输出: [1,1,4,2,1,1,0,0]

============================================================
Python 语法要点（C++ 对比）
============================================================

1. list 直接充当栈
   C++:  stack<int> stack;
   Python: stack: list[int] = []
   → Python 通常不单独导入栈类型，list 的末尾就是栈顶

2. pop() 返回被删除的元素
   C++:  int prev_i = stack.top(); stack.pop();
   Python: prev_i = stack.pop()
   → Python 的 pop() 同时完成读取栈顶和弹栈

3. 空列表的布尔值
   C++:  !stack.empty()
   Python: stack
   → 空列表为 False，非空列表为 True，可直接写在 while 条件中

4. 局部变量类型注解
   C++:  vector<int> result(n, 0);
   Python: result: list[int] = [0] * len(temperatures)
   → 注解帮助阅读和静态检查，不限制运行时放入的对象类型
"""


def dailyTemperatures(temperatures: list[int]) -> list[int]:
    """
    维护温度单调递减的下标栈，遇到更高温度时结算栈顶等待天数。
    时间复杂度 O(n)，空间复杂度 O(n)
    """
    result: list[int] = [0] * len(temperatures)
    stack: list[int] = []

    for i, temp in enumerate(temperatures):
        # 当前温度更高时，依次结算栈中较低温度的等待天数
        while stack and temperatures[stack[-1]] < temp:
            prev_i = stack.pop()
            result[prev_i] = i - prev_i

        # 栈中保存尚未找到更高温度的下标
        stack.append(i)

    return result


# =============================================================================
# 测试代码
# =============================================================================
if __name__ == "__main__":
    result1 = dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
    expected1 = [1, 1, 4, 2, 1, 1, 0, 0]
    assert result1 == expected1, f"示例1失败: {result1}"
    assert dailyTemperatures([30, 40, 50, 60]) == [1, 1, 1, 0], "递增温度测试失败"
    assert dailyTemperatures([60, 50, 40, 30]) == [0, 0, 0, 0], "递减温度测试失败"
    print("✅ P16 每日温度 全部测试通过")
