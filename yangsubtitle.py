from bs4 import BeautifulSoup
#BeautifulSoup need to be installed
import requests,os,re
from mryang import yangvideo


#get youtube videoid and name
def getvidandname(url):
    name=yangvideo.getvideoname(url)
    vid=re.findall(r'v=\w+',url)
    finalvid=vid[0][2:]
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
