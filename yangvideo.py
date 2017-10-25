import os
from mryang import yangfile#i donnot understand why now???it should be import yangfile,fuck
#from colors import *

def dlvideo(videolist):
    """
	this functon is used to downoad video for youtube
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
def getvideoname(url):#this url also be vid
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



#get all id of a playlist
def get_all_vid_and_url_of_a_playlist(playlisturl):
    '''
    this is used to get all vid
    '''
    os.system('youtube-dl --get-id -i '+str(playlisturl)+('>allvid.txt'))
    allvid = yangfile.getfileeverylinetolist('allvid.txt')
    allurl=[]
    for k in allvid:
        allurl.append('https://www.youtube.com/watch?v='+str(k))
    return [allvid,allurl]


def embedsubtile():
    filename=os.listdir('.')





def high_quality_dl(videolist):
    """
    this functon is used to downoad high qualityvideo for youtube
    https://askubuntu.com/questions/486297/how-to-select-video-quality-from-youtube-dl
     !youtube-dl -f bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaud
     io --merge-output-format mp4  https://www.youtube.com/watch?v=iQM0btlf
     O1o&feature=youtu.be

    """
    for idx,url in  enumerate(videolist):
        print('this file includes '+str(len(videolist))+' url+may include empty!')
        print('=========================================')
        try:
            print(green('this is the '+idx))
        except:
            print('this is the ',idx)
        print('u are dealing the url=======>'+str(url))
        try:
            os.system('youtube-dl -f bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio --merge-output-format mp4 '+url )
        except:
            os.system('youtube-dl --write-sub  --sub-lang en -f best -i  '+url )




