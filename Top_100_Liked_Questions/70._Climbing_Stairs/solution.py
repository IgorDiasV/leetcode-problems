class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2 :
            return n
        qtd = 0
        ant = 1
        ant2 = 2

        for i in range(3, n+1) :
            qtd = ant + ant2
            ant = ant2
            ant2 = qtd

        return qtd 