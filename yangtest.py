#from colors import *
import sys,traceback
from traceback import *
import time

#test a runtime of a function














def exceptinfo():
    print("++++++++++++++++++++++++++++++++++++Except info start++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print(traceback.format_exc())
    print("+++++++++++++++++++++++++++++++++++++Except info  end++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")













def dividingline():
    print('<===============================Dividing line=============================================>')

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
    print(pos1)



def yangshow(var):
    linenumber1=linenumber()
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  '+str(var)+'  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')



from inspect import currentframe

def linenumber():
    cf = currentframe()
    print(str(cf.f_back.f_lineno))
    return 'linenumber->'+str(cf.f_back.f_lineno)
