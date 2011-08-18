import pickle as pl

pkfile = open('max.out','rb')
pkfile2 = open('min.out','rb')

max = pl.load(pkfile)
min = pl.load(pkfile2)
print max, min

pkfile.close()
