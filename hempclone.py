weights = {"g" : 0.5, "h": 0.5, "y": 0.5, "x": 0.6, "w": 0.6}
import itertools
def checkoutput(currentgenetics, middleplant):
    outputgene = ""
    for x in range(6):
        count = {"g" : 0, "h": 0, "y": 0, "x": 0, "w": 0}
        for i in currentgenetics:
            count[i[x]] += 1

        for i in count:
            count[i] *= weights[i]
        mostfrequentletter = list(count.keys())[0]

        for y in range(len(count))[1:]:
            if list(count.values())[y] > count[mostfrequentletter]:
                mostfrequentletter = list(count.keys())[y]
        if count[mostfrequentletter] <= weights[middleplant[x]]:
            mostfrequentletter = middleplant[x]
        outputgene += mostfrequentletter
    return outputgene


def numofletters(gene, letter):
    total = 0
    for i in gene:
        if i == letter:
            total += 1
    return total



genetics = ["ggxyhh", "hxwygg", "gghyyy", "ggyghy", "ygyhgh", "ggygyy"]

if __name__ == "__main__":
    for x in range(len(genetics)):
        templist = genetics[:]
        templist.pop(x)
        for i in itertools.combinations(templist, 3):
            outputgene = checkoutput(list(i), genetics[x])
            if numofletters(outputgene, "g")  == 4 and numofletters(outputgene, "y")  == 2:
                print("\n\n\noutputgene: \n" + outputgene + "\n\ninputgenes:" + str(list(i)) + "\n\nmiddle gene:\n" + genetics[x])
