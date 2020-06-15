"""
Cheapest Flights Within K Stops

link: https://leetcode.com/problems/cheapest-flights-within-k-stops/

There are n cities connected by m flights. Each flight starts from city u and arrives at v with a price w.
Now given all the cities and flights, together with starting city src and the destination dst, your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.

Example 1:
Input:
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
Output: 200
Explanation:
The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.

Example 2:
Input:
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 0
Output: 500

Explanation:
The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.
"""
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        dic = collections.defaultdict(dict)
        for source, destination, price in flights:
            dic[source][destination] = price
        heap = [(0, src, K+1)]
        seen = {}
        while heap:
            price, source, K = heapq.heappop(heap)
            seen[source] = K
            if source == dst:
                return price
            if K > 0:
                for v in dic[source]:
                    if v in seen and K-1 <= seen[v]:
                        continue
                    heapq.heappush(heap, (price+dic[source][v], v, K-1))
        return -1
