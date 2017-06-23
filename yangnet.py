import os
def pinghost(hostname):
    """
    this function is used to stimulate the ping command
    """
    response = os.system("ping -c 1 " + hostname)

    #anthen check the response...
    if response == 0:
        print(hostname, 'is up!')
        result='ok'
    else:
        print(hostname, 'is down!')
        result='no'
    return result
