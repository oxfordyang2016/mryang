
__version__ = 1.0



def goal():
	'''
	the main goal of this script is to
	help myself to grasp python basic
	core and develop the profucity
	'''
	print('make a good basic of python')



def help():
	helpinfo='''
    1.get the help info ,the main function is

    help(x),it will print the info included included

    function head comment sector!
	'''
	print(helpinfo)

def rename():
    renameinfo='''
    Use os.rename(src, dst) to rename or move a file or a directory
    '''
    print(renameinfo)

def dir():
    '''
	this function is to generate what the object include!
	such as,fucntion,variable,etc.
	example:
	dir(os)
    '''
    print(233)
    dirobject = """
    dir(yangfile)
    ['__builtins__',
     '__cached__',
     '__doc__',
     '__file__',----the file (yangfile) position
     '__loader__',
     '__name__',------the moudule name
     '__package__',----the package name
     '__spec__',
     'extractstuff',------the function by writer
     'getfileeverylinetolist',
     're'-----------------the moudle import by the moudle
     ]
     """
    print(dirobject)


def list():
	'''
	list append method
	eg:
	a=[]
	for k in range(5):
		a.append(k)
	'''
	return

def writefile():
    a="""
	1.write string
    with open('somefile.txt', 'a') as the_file:
	     the_file.write('Hello\n')
    2.write  variable
	 with open('cap.txt','w') as test:
     for k in final:
         if str(k)!='<br/>':
             test.write(k+'\n')
   



	"""
    print(a)
