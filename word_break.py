n = int(input().strip())
words = [input().strip() for _ in range(n)]
word = input().strip()

def word_break(wordList, word): 
    if word == '': 
        return True
    else: 
        wordLen = len(word) 
        return any([(word[:i] in wordList) and wordBreak(wordList, word[i:]) for i in range(1, wordLen+1)]) 

if word_break(words, word):
    print('yes')
else:
    print('no')
