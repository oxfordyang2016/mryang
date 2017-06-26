import os
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
        os.system('youtube-dl -f best -i '+url )



    	
