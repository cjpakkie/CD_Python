#part 1

def draw_stars(x):
    for idx in range(0, len(x)):
        print x[idx] * "*"
draw_stars([4,6,1,3,5,7,25])

#part 2

def draw_stars2(x):
    for idx in range(0, len(x)):
        if isinstance(x[idx], int):
            print x[idx] * "*"
        else:
            print x[idx][0].lower() *len(x[idx])

draw_stars2([4,"Tom",1,"Michael",5,7,"Jimmy Smith"])
