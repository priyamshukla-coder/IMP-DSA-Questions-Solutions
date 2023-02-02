class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        mp={order[i]:i for i in range(len(order))}

        print(mp)

        # for i in range(len(order)):

        #     mp[order[i]]=i

        for i in range(len(words)-1):

            for j in range(0,len(words[i])):

                if j>=len(words[i+1]):

                    return False

                if words[i][j]!=words[i+1][j]:

                    if mp[words[i][j]]>mp[words[i+1][j]]:

                        return False

                    break

        return True
                