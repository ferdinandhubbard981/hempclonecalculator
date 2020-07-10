genetics = ["ggxyhh", "hxwygg", "gghyyy", "ggyghy", "ygyhgh"]
weights = {"g" : 0.5, "h": 0.5, "y": 0.5, "x": 0.6, "w": 0.6}

for x in range(len(genetics)):
    for y in range(len(genetics)):
        for z in range(len(genetics)):
            checkoutput(genetics[x], genetics[y], genetics[z])
def checkoutput(currentgenetics):
    count = {"g" : 0, "h": 0, "y": 0, "x": 0, "w": 0}
    for x in range(6):

        
