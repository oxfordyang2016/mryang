import re,yangtest
def getfileeverylinetolist(fname):
    '''
    this fucntion is  used to get 
    everyline to a list 
    '''
    with open(fname) as f:
       content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]
    return content


def extractstuff(source,index):
    targetgroup=[]
    for k in source:
        target=k.split()
        yangtest.yangshow(target)
        try:
            targetgroup.append(target[index])
        except:
            pass
    return targetgroup






