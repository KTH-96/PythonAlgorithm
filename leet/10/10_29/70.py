def climbStairs(self, n: int) -> int:
    memory = {}

    def climbing(hei: int) -> int:
        if hei <= 2:
            return hei

        if hei not in memory:
            memory[hei] = climbing(hei - 1) + climbing(hei - 2)

        return memory[hei]

    return climbing(n)
