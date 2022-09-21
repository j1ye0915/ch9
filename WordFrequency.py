def count (infile):
    x = {}
    f = open(infile, "r")
    lines = f.readlines() 
    for line in lines:
        words = line.split()
    for word in words:
        if word in x:
            x[word] += 1
        else:
            x[word] = 1
    return x


def main ():
    infile = "sometext.txt"
    x = count(infile)
    
    for i in x:
        print(i,x[i])



main ()