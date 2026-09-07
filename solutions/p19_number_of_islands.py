"""
============================================================
LeetCode 200. 岛屿数量 (Number of Islands) — Hot 100
============================================================
难度：中等

题目：给你一个由 '1'（陆地）和 '0'（水）组成的二维网格，请计算岛屿数量。
      陆地只能在水平或竖直方向相连，网格四条边均被水包围。

示例：
  输入: grid = [["1","1","0"],["0","1","0"],["1","0","1"]]
  输出: 3

============================================================
Python 语法要点（C++ 对比）
============================================================

1. collections.deque 双端队列
   C++:  queue<pair<int, int>> queue;
   Python: queue = deque([(i, j)])
   → deque 支持两端 O(1) 操作，适合实现 BFS 队列

2. popleft() 与 appendleft()
   C++:  auto [x, y] = queue.front(); queue.pop();
   Python: x, y = queue.popleft()
   → popleft() 从左端出队；appendleft(value) 可从左端入队

3. 用元组保存四个方向
   C++:  int directions[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};
   Python: directions = ((1,0), (-1,0), (0,1), (0,-1))
   → 每个方向是一个 (dx, dy) 元组，遍历时直接解包

4. 原地标记已访问陆地
   C++:  grid[x][y] = '0';
   Python: grid[x][y] = "0"
   → 直接把访问过的陆地改为水，不需要额外 visited 集合
"""

from collections import deque


def numIslands(grid: list[list[str]]) -> int:
    """
    扫描网格；每发现一块新陆地，就用 BFS 将整座岛标记为水。
    时间复杂度 O(mn)，空间复杂度 O(mn)
    """
    if not grid:
        return 0

    m = len(grid)
    n = len(grid[0])
    count = 0
    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

    for i in range(m):
        for j in range(n):
            if grid[i][j] != "1":
                continue

            count += 1
            grid[i][j] = "0"
            queue = deque([(i, j)])

            # BFS 将与起点相连的整座岛屿标记为水
            while queue:
                x, y = queue.popleft()

                for dx, dy in directions:
                    nx = x + dx
                    ny = y + dy

                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == "1":
                        grid[nx][ny] = "0"
                        queue.append((nx, ny))

    return count


# =============================================================================
# 测试代码
# =============================================================================
if __name__ == "__main__":
    grid1 = [["1", "1", "0"], ["0", "1", "0"], ["1", "0", "1"]]
    result1 = numIslands(grid1)
    assert result1 == 3, f"示例1失败: {result1}"
    assert numIslands([["0", "0"], ["0", "0"]]) == 0, "全水域测试失败"
    assert numIslands([["1"]]) == 1, "单块陆地测试失败"
    print("✅ P19 岛屿数量 全部测试通过")
