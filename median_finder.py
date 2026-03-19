import heapq


class MedianFinder:
    def __init__(self):
        self.small = []  # max heap using negative values
        self.large = []  # min heap

    def add_num(self, num: int) -> None:
        heapq.heappush(self.small, -num)

        if self.small and self.large and (-self.small[0] > self.large[0]):
            value = -heapq.heappop(self.small)
            heapq.heappush(self.large, value)

        if len(self.small) > len(self.large) + 1:
            value = -heapq.heappop(self.small)
            heapq.heappush(self.large, value)

        if len(self.large) > len(self.small):
            value = heapq.heappop(self.large)
            heapq.heappush(self.small, -value)

    def find_median(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2.0


mf = MedianFinder()
mf.add_num(10)
mf.add_num(20)
print(mf.find_median())
mf.add_num(30)
print(mf.find_median())
mf.add_num(40)
print(mf.find_median())
