from colors import *
import sys,traceback
from traceback import *
import time

#test a runtime of a function














def exceptinfo():
    print(yellow("++++++++++++++++++++++++++++++++++++Except info start++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"))
    print(traceback.format_exc())
    print(yellow("+++++++++++++++++++++++++++++++++++++Except info  end++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"))













def dividingline():
    print(yellow('<===============================Dividing line=============================================>'))

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
    print(yellow(str(cf.f_back.f_lineno)))
    return 'linenumber->'+str(cf.f_back.f_lineno)
