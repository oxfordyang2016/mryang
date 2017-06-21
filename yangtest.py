from colors import *
import sys,traceback
from traceback import *

def exceptinfo():
    print(yellow("++++++++++++++++++++++++++++++++++++Except info start++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"))
    print(traceback.format_exc())
    print(yellow("+++++++++++++++++++++++++++++++++++++Except info  end++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"))













def dividingline():
    print yellow('<===============================Dividing line=============================================>')

pos="""

                                                                 

                                                                 /\
                                                                /  \ 
                                                               /    \
                                                               \    / 
                                                                \  /
                                                                 \/





"""

pos1="""                                                                   
                                                                          ||
                                                                          ||
                                                                          || 
                                                                          ||
                                                                          ||
                                                                          ||
                                                                          vv
                                                                          88
                                                                          vv  

"""
def position():
    print(green(pos1))
    


def yangshow(var):
    linenumber1=linenumber()
    print(yellow('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  '+str(var)+'  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'))



from inspect import currentframe

def linenumber():
    cf = currentframe()
    print yellow(str(cf.f_back.f_lineno))
    return 'linenumber->'+str(cf.f_back.f_lineno)


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