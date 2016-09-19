def myhash(s):
    limite_bits = 2**64
    h = 0
    num_primo1 = 997
    num_primo2 = 7
    num_primo3 = 11

    for c in s:
        c = ord(c)
        h += c
        h += h << num_primo2
        h += c * num_primo1
        h += h >> num_primo3

    h = h % limite_bits
    return h


i=0
col=0
noncol = 0
d=dict()
with open('words.txt') as f:
    for line in f:
        i=i+1
        z = myhash(line) % 400000
        if z in d:
        	col = col + 1
        	d[z]+=1
        else:
        	noncol = noncol+1
        	d[z]=1


print "Number of lines in file: "+str(i)
print "Collisions: " +str(col)
print "Non Collisions: "+str(noncol)
print "Total keys: "+str(col+noncol)

