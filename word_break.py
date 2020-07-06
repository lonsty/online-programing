n = int(input().strip())
words = [input().strip() for _ in range(n)]
word = input().strip()

def word_break(word_list, word): 
    if word == '': 
        return True
    else: 
        word_len = len(word) 
        return any([(word[:i] in word_list) and word_break(word_list, word[i:]) for i in range(1, word_len + 1)]) 

if word_break(words, word):
    print('yes')
else:
    print('no')
