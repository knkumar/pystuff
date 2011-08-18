import  numpy as np
import datetime as dt
import sys
import time
from mpl_toolkits.mplot3d import axes3d
import matplotlib as plt
plt.use('PS')
from pylab import *
import pickle as pl

class flickdata:
    def __init__(self, laln, tags):
        self.count = 1
        self.laln = laln
        self.tags = tags
    def __update__(self, laln, tags):
        self.count++
        if list(laln) not in self.laln:
            self.laln.append(laln)
        self.tags.extend(tags)

def findbin(udate):
    minpkl = open('min.out','rb')
    fmin = pl.load(minpl)
    return (time.mktime(udate.timetuple()) - time.mktime(fmin.timetuple()))/(4*60*60)

def plot3d(data):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    Z, T1, T2, T3, X, Y = zip(*data)
    X = np.array(X)
    Y = np.array(Y)
    Z = np.array(Z)
    print X, Y, Z
    print "XYZ printed"
    print X.shape
    print Y.shape
    print Z.shape
    ax.plot_surface(X, Y, Z) #,rstride=8, cstride=8, alpha=0.3)
    #cset = ax.contour(X, Y, Z, zdir='z', offset=-100)
    #cset = ax.contour(X, Y, Z, zdir='x', offset=-40)
    #cset = ax.contour(X, Y, Z, zdir='y', offset=40)
    ax.set_xlabel('Latitude')
    #ax.set_xlim3d(-40, 40)
    ax.set_ylabel('Longitude')
    #ax.set_ylim3d(-40, 40)
    ax.set_zlabel('Time')
    #ax.set_zlim3d(-100, 100)
    plt.savefig("fig1.ps")

def dateConvert(date):
    ret = dt.datetime.strptime(date,"%Y-%m-%d")
    return ret

def timeConvert(time):
    ret = dt.datetime.strptime(time,"%H:%M:%S")
    return ret

#find the max value from the file <can take column as the parameter>
def findmax():
    fmax = dt.datetime(1,1,dt.MINYEAR)
    mxfile = open('sample.dat','rb')
    for line in mxfile:
        cols = line.strip().split()
         date =  dt.datetime.strptime(cols[2]+" "+clos[3], "%Y-%m-%d %H:%M:%S")
        if(date > fmax):
            fmax = date
    outmax = open('max.out','wb')
    pl.dump(fmax, outmax)
    outmax.close()
    
#find the min value from the file <can take column as the parameter>
def findmin():
    fmin = dt.datetime.today()
    mxfile = open('sample.dat','rb')
    for line in mxfile:
        cols = line.strip().split()
        date =  dt.datetime.strptime(cols[2]+" "+clos[3], "%Y-%m-%d %H:%M:%S")
        if(date < fmin):
            fmin = date
    outmin = open('min.out','wb')
    pl.dump(fmin, outmin)
    outmin.close()

def makebins():
    maxpkl = open('max.out','rb')
    minpkl = open('min.out','rb')
    """fmax = pl.load(maxpl)
    fmin = pl.load(minpl)
    noOfFiles = (max-min)
    add4hours = dt.timedelta(hours=4)
    mint = fmin
    while mint < fmax:
        filec = open("flickr"+mint.ctime(),'wb')
        filec.close()
        mint = mint + datetime.timedelta(hours=4)"""
    infile = open('sample.dat','rb')
    fldict = shelve.open("flickrshelf",writeback=True)
    for line in infile:
        cols = line.strip().split()
        date =  dt.datetime.strptime(cols[2]+" "+cols[3], "%Y-%m-%d %H:%M:%S")
        laln = list(cols[9],cols[10])
        print(laln)
        bin = findbin(date)
        tags = cols[20].split(',')
        try: 
            userDict = fldict[cols[0]]
        except KeyError: 
            fldict[cols[0]] = dict(bin=flickdata(laln, tags))
        else:
            try:
                binDict = userDict[bin]
            except KeyError:
                userDict[bin] = flickdata(laln,tags)
            else:
                binDict.update(laln,tags)
                userDict[bin] = binDict
                fldict[cols[0]] = userDict
    fldict.close()

def main():
    try:
        findmax()
        findmin()
        makebins()
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

if __name__ == "__main__":
    sys.exit(main())
