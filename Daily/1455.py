class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):

        sentence = sentence.split()
        for word in sentence:
            if word[0:len(searchWord)] == searchWord:
                return sentence.index(word) + 1
        return -1

sentence = "i love eating burger"
searchWord = "burg"
solution = Solution()
print(solution.isPrefixOfWord(sentence, searchWord))