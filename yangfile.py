import re,os
def getfileeverylinetolist(fname):
    '''
    this fucntion is  used to get
    everyline to a list
    '''
    try:
        with open(fname,encoding='utf8') as f:
            content = f.readlines()
    except:
        '''
        this line is designed for python2
        '''
        with open(fname) as f:
            content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]
    return content


def extractstuff(source,index):
    '''
    i have forgeted what is the function used to ?
    '''
    targetgroup=[]
    for k in source:
        target=k.split()
        yangtest.yangshow(target)
        try:
            targetgroup.append(target[index])
        except:
            pass
    return targetgroup


def getfilename(pathorname):
    base=os.path.basename(pathorname)
    print('The filename including extension ')
    print(base)
    name=os.path.splitext(base)[0]
    print('The filename without extension')
    print(name)
