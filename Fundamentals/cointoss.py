

def cointoss():
    tails = 0
    heads = 0
    import random
    for num in range(1,5001):
        random_num = random.random()
        x = random_num
        x_rounded = round(x)
        if x_rounded == 0:
            coin = "head"
            heads += 1
        else:
            coin = "tail"
            tails += 1
        print "Attempt #{}: Throwing coin... It's a {}!...Got {}head(s) so far and {} tail(s) so far".format(num, coin, heads, tails)
    print "Ending Program. Thank You!"
cointoss()
