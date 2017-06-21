import os
def dlvideo(videolist):
	"""
	this functon is used to downoad video
	"""
    for url in videolist:
    	print('-------------------------------------------')
    	print('u are dealing the url=======>'+str(url))
    	os.system('youtube-dl -f best -i '+url )



    	