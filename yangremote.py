from  mryang import yangfile
import os
def syn():
    os.system('git pull origin master')
    #u need to understand the pwd dir
    a = yangfile.getfileeverylinetolist('./yangming')
    return a
