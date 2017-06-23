import re
def getfileeverylinetolist(fname):
    '''
    this fucntion is  used to get 
    everyline to a list 
    '''
    with open(fname,encoding='utf8') as f:
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






