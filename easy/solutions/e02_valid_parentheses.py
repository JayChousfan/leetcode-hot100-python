"""LeetCode 20. 有效的括号 (Valid Parentheses) — Hot 100
难度：简单
Python list 的 append()/pop() 可直接实现栈。"""


def fun(s):
    """用栈匹配左右括号。时间 O(n)，空间 O(n)。"""
    mp = {")": "(", "]": "[", "}": "{"}
    stack = []
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        elif not stack or stack.pop() != mp[ch]:
            return False
    return not stack


if __name__ == "__main__":
    assert fun("()[]{}"), "示例1失败"
    assert not fun("(]"), "错误匹配测试失败"
    print("✅ E02 有效的括号 全部测试通过")
