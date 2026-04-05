class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        D, R = deque(), deque()

        for i, c in enumerate(senate):
            if c == "R":
                R.append(i)
            else:
                D.append(i)

        while D and R:
            dTurn = D.popleft()
            rTurn = R.popleft()

            if dTurn > rTurn:
                R.append(n + rTurn)
            else:
                D.append(n + dTurn)

        return "Radiant" if R else "Dire"