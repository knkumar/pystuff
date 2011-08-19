import pickle as pl

pkfile = open('max.out','rb')
pkfile2 = open('min.out','rb')

max = pl.load(pkfile)
min = pl.load(pkfile2)
print max, min

pkfile.close()

"""                                                                                                                                                                                           
#ls for log files in the audit directory and search for the ones between the start and end time                                                                                               
# not opening the log file                                                                                                                                                                    
def find_timestamp(start,end):                                                                                                                                                                
    import time                                                                                                                                                                               
    rbegin = int( time.mktime(start.timetuple()) )                                                                                                                                            
    rend = int( time.mktime(start.timetuple()) )                                                                                                                                              
    from subprocess import Popen,PIPE                                                                                                                                                         
    # really idiotic Popen doesnt take absolute paths, considering its a subprocess!!                                                                                                         
    pwd = Popen(["pwd"],stdout=PIPE)                                                                                                                                                          
    Popen(["cd","%s"%config['reissue_logs']], shell=True)                                                                                                                                     
    ls = Popen(["ls","-lrt"],stdout=PIPE)                                                                                                                                                     
    grep = Popen(["grep","^-"],stdin=ls.stdout,stdout=PIPE)                                                                                                                                   
    ls.stdout.close()                                                                                                                                                                         
    output = grep.communicate()[0].split('\n')                                                                                                                                                
    Popen(["cd","%s"%pwd.communicate()[0].strip('\n')], shell=True)                                                                                                                           
    if output:                                                                                                                                                                                
        output.pop()                                                                                                                                                                          
    fname=[]                                                                                                                                                                                  
    for i,val in enumerate(output):                                                                                                                                                           
        fname.append(val.split(None,7)[7])                                                                                                                                                    
    return search_filename(rbegin,rend,fname)"""
