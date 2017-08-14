from bs4 import BeautifulSoup
#https://stackoverflow.com/questions/7225900/how-to-pip-install-packages-according-to-requirements-txt-from-a-local-directory
#pip install beautifulsoup4
#BeautifulSoup need to be installed
import requests,os,re
from mryang import yangvideo,yangfile,yangtest

#get youtube videoid and name
def getvidandname(url):
    if '&' in url:
        position = url.index('&')
        url = url[0:position]
    name=yangvideo.getvideoname(url)
    try:
        os.system('youtube-dl --get-id -i '+str(url)+' >vid.txt')
        vid = yangfile.getfileeverylinetolist('vid.txt')[0]
        finalvid = vid
    except:
        yangtest.exceptinfo()
        vid = re.findall(r'v=\w+',url)
        finalvid=vid[0][2:]
    #if '&' in vid:
    #    position = vid.index('&')
    #    vid=vid[0:position]

    print('filename is the fellowing')
    print(name)
    print('vid is the fellowing')
    print(finalvid)
    return [name,finalvid]



#from the caption diy to get subtitle html
# this is for automatical caption from youtube!
def getsubtitle(name,vid):
    a=requests.get('http://diycaptions.com/php/get-automatic-captions-as-srt.php?id='+str(vid))
    #get html as string
    content=a.content
    #parser html
    soup=BeautifulSoup(content)
    c=soup.find_all('pre')
    final=c[0]
    with open(str(name)+'.en.srt','w',encoding='utf-8') as test:
        for k in final:
            print(k)
            if str(k).isdigit()==True:
                test.write(''+'\n')#there is a bug  that lead to a long time to slove,that is,test.write(' '+'\n')
            if str(k)!='<br/>':
                test.write(k+'\n')

            '''
            else:
                emp=' '
                test.write(emp+'\n')
            '''


def ultimategetsub(url):
    '''
    the function donnot design the minichan of specify directory
    subtile in pwd!
    '''
    res=getvidandname(url)
    getsubtitle(res[0],res[1])


def getsubtitle_of_playlist(playlisturl):
    '''
    example:
    getsubtitle_of_playlist('https://www.youtube.com/playlist?list=PLar0ZIPrNX9ftDSmaD2tO32wjjSEAYU-P')

    '''
    a = yangvideo.get_all_vid_and_url_of_a_playlist(playlisturl)
    allurls = a[1]
    dealinfo = []
    for url in allurls:
        print('i am dealing with '+str(url))
        try:
            ultimategetsub(url)
            dealinfo.append({str(url):'success'})
        except:
            dealinfo.append({str(url):'fail'})
    return dealinfo
