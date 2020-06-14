"""
1267. Count Servers that Communicate
You are given a map of a server center, represented as a m * n integer matrix
grid, where 1 means that on that cell there is a server and 0 means that
it is no server. Two servers are said to communicate if they are on the
same row or on the same column.Return the number of servers that
communicate with any other server."""
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        R = defaultdict(int)
        C = defaultdict(int)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]):
                    R[i]+=1
                    C[j]+=1
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j] and (R[i]>1 or C[j]>1)):
                    count+=1
        return count
        
