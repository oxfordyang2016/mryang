#in order to get urls
import re
def get_allyoutubeurls_vid(thethingswillbedeal):
	'''
	the function is used to deal with a string
	and get all urls_vid
	'''
	youtube_regex = (
        r'(https?://)?(www\.)?'
        '(youtube|youtu|youtube-nocookie)\.(com|be)/'
        '(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')
    urls_vid = re.findall(youtube_regex,thethingswillbedeal)
    urls_vid = [k[-1] for k in urls_vid]
    return urls_vid