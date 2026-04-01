class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # create DAG based on chars of each word
        dag = {c: set() for w in words for c in w}
        # show incoming edges for each char
        inD = {c:0 for c in dag}

        # compare each pair of words
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            # if w1 is longer and the words have been equal so far, we have reached a cycle
            if len(w1) > len(w2) and (w1[:minLen] == w2[:minLen]):
                return ""
            # if letters are not equal, add letters if not in DAG
            for j in range(minLen):
                if w1[j] != w2[j]:
                    if w2[j] not in dag[w1[j]]:
                        dag[w1[j]].add(w2[j])
                        inD[w2[j]] += 1
                    break
        
        # establish queue
        q = deque([c for c in inD if inD[c] == 0])
        res = []
        # process each letter in the queue and bfs!
        while q:
            char = q.popleft()
            res.append(char)
            for nei in dag[char]:
                inD[nei] -= 1
                if inD[nei] == 0:
                    q.append(nei)
        
        return "".join(res) if len(res) == len(inD) else ""