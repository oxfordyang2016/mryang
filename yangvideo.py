import os
from mryang import yangfile#i donnot understand why now???it should be import yangfile,fuck
from colors import *

def dlvideo(videolist):
    """
	this functon is used to downoad video
    """
    for idx,url in  enumerate(videolist):
        print('this file includes '+str(len(videolist))+' url+may include empty!')
        print('=========================================')
        try:
            print(green('this is the '+idx))
        except:
    	    print('this is the ',idx)
        print('u are dealing the url=======>'+str(url))
        os.system('youtube-dl --write-sub  --sub-lang en -f best -i  '+url )



# get youtube video filename
def getvideoname(url):
    allinfo=os.system('youtube-dl --get-filename '+str(url)+('> filename.txt'))
    a=yangfile.getfileeverylinetolist('filename.txt')
    print('the filename is the fellowing')
    namespace=[]
    for name in a:
        print(name)
        namefinal=name
        base=os.path.basename(namefinal)
        filename=os.path.splitext(base)[0]
        namespace.append(filename)
    return namespace[0]
