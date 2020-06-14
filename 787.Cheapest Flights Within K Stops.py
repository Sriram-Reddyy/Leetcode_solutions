"""
787. Cheapest Flights Within K Stops
Medium
There are n cities connected by m flights. Each flight starts from city u
and arrives at v with a price w. Now given all the cities and flights, together
with starting city src and the destination dst, your task is to find the cheapest
price from src to dst with up to k stops. If there is no such route, output -1.

Example 1:
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
Output: 200

The cheapest price from city 0 to city 2 with at most 1 stop costs 200,
as marked red in the picture.
"""
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        if src == dst:
            return 0
        if not flights:
            return -1
        flights_graph = defaultdict(list)
        for s, d, p in flights:
            flights_graph[s].append((d,p))
        max_stop = K + 1
        cost_heap = [(0,src,0)]
        while cost_heap:
            cur_p, cur, stop = heapq.heappop(cost_heap)
            if cur == dst:
                return cur_p
            for nxt, nxt_p in flights_graph[cur]:
                if stop < max_stop:
                    heapq.heappush(cost_heap, (cur_p+nxt_p, nxt, stop+1))
        return -1
