from  mryang import yangfile
import os
def syn():
    os.system('git pull origin master')
    a = yangfile.getfileeverylinetolist('./yangming')
    return a
