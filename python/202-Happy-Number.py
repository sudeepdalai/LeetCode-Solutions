class Solution:
    def isHappy(self, n: int) -> bool:

        def generate_next(n):
            total_sum = 0
            while n > 0:
                rem = n % 10
                total_sum += rem ** 2
                n = n // 10
            return total_sum

        visited = set()
        while n != 1 and n not in visited:
            visited.add(n)
            n = generate_next(n)

        return n == 1
