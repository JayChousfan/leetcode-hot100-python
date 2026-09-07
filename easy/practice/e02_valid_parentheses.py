"""LeetCode 20. 有效的括号｜难度：简单
题目：判断字符串中的括号是否全部正确配对。
示例："()[]{}" → True
函数：fun(s)"""
# TODO: 在这里写出完整的 def fun(...): 函数
def fun(s):
    mp= {"(":")","{":"}","[":"]"}
    stack = []
    for ch in s:
        if ch in "({[":
            stack.append(ch)
        elif not stack or stack.pop !=mp[ch]:
            return False
    return not stack


if __name__ == "__main__":
    assert fun("()[]{}"), "示例1失败"
    assert not fun("(]"), "错误匹配测试失败"
    print("✅ E02 有效的括号 通过！")
