"""
题目描述
判断所给的字符串是否由所给的词典中的若干个词组成。

如已知词典["code", "sangfor", "org"]
则字符串"codesangfororg" 由上述词典组成，
字符串"codesangforsangfororg" 也由上述词典组成，
但字符串"sangforcom" 则不由上述词典组成。

输入描述:
第一行一个数字K 表示词典个数
后面若干行则为具体的输入词典，一个词典一行
最后一行输入待判定的字符串

输出描述:
若字符串为对应的词典组成，则输出yes，否则输出no
"""

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
