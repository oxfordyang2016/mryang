import os

def upload(comment='allok'):
	'''
	i dislike to repeat every step every time!!!!fuck
	usage:
	yanggit.upload('add comment of upload function')
	'''
	os.system('git add .')
	os.system('git commit -m " '+str(comment)+'"')
	os.system('git push origin master')