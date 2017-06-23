import os
def dlvideo(videolist):
    """
	this functon is used to downoad video
    """
    for idx,url in  enumerate(videolist):
    	print('-------------------------------------------')
    	try:
    		from colors import *
    		print(green('this is the '+idx))
    	except:
    	    print('this is the ',idx)	
    	print('u are dealing the url=======>'+str(url))	
    	os.system('youtube-dl -f best -i '+url )



    	
