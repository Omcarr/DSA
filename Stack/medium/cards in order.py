class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        res=[0]*len(deck)
        q=deque(range(len(deck)))
        for i in deck:
            n=q.popleft()
            #print(n,q)
            res[n]=i
            if q:
              q.append(q.popleft())
        return res

