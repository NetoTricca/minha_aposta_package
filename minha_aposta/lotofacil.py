import random

def lotofacil(wnumbers=15,wrange=25):
    wcont = int(wnumbers)
    wlista=[]
    while wcont > 0:
        d1 = random.randrange(1,wrange)
        if not (d1 in wlista):
            wlista.append(d1)
            print(d1)
            wcont = wcont -1
