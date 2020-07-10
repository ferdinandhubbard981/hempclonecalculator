genetics = ["ggxyhh", "hxwygg", "gghyyy", "ggyghy", "ygyhgh"]
weights = {"g" : 0.5, "h": 0.5, "y": 0.5, "x": 0.6, "w": 0.6}

def checkoutput(currentgenetics):
    outputgene = ""
    for x in range(6):
        count = {"g" : 0, "h": 0, "y": 0, "x": 0, "w": 0}
        for i in currentgenetics:
            count[i[x]] += 1

        for i in count:
            count[i] *= weights[i]
        mostfrequentletter = count.values()[0]
        for y in range(len(count)):
            if count.values()[y + 1] > count.values()[y]:
                mostfrequentletter = count.items()[y]
        outputgene += mostfrequentletter
    print(outputgene)
    return outputgene




for x in range(len(genetics)):
    for y in range(len(genetics)):
        for z in range(len(genetics)):
            checkoutput([genetics[x], genetics[y], genetics[z]])
