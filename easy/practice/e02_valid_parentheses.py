"""LeetCode 20. 有效的括号｜难度：简单
函数：fun(s) -> bool"""
# TODO: 在这里写出完整的 def fun(...): 函数
if __name__ == "__main__":
    assert fun("()[]{}"), "示例1失败"
    assert not fun("(]"), "错误匹配测试失败"
    print("✅ E02 有效的括号 通过！")
