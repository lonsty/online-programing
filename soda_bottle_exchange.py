# Author: Allen
# Date: 2020-4-15 21:56:25
"""
有这样一道智力题：“某商店规定：三个空汽水瓶可以换一瓶汽水。小张手上有十个空汽水瓶，
她最多可以换多少瓶汽水喝？”答案是5瓶，方法如下：先用9个空瓶子换3瓶汽水，喝掉3瓶满的，
喝完以后4个空瓶子，用3个再换一瓶，喝掉这瓶满的，这时候剩2个空瓶子。然后你让老板先借
给你一瓶汽水，喝掉这瓶满的，喝完以后用3个空瓶子换一瓶满的还给老板。如果小张手上有n个
空汽水瓶，最多可以换多少瓶汽水喝？
"""


def exchange(empty):
    global exchanged
    rest = 0
    excha = empty // 3
    exchanged += excha
    rest += empty % 3 + excha
    
    if rest >= 3:
        return exchange(rest)
    elif rest == 2:
        exchanged += 1
    return(exchanged)


while 1:
    try:
        empty_num = int(input())
        if empty_num == 0:
            break
        exchanged = 0
        print(exchange(empty_num))
    except:
        break
