#!/usr/bin/python
import subprocess
target = 1
up = 0
down = 0
iplist=["192.168.0.1","192.168.0.104"]
#unread ='Unreachable'
while (target < 5):
#for ip in iplist:
        ip = "192.168.0." +str(target)
        output = subprocess.Popen('ping -n 3 ' + ip ,stdout = subprocess.PIPE).communicate()[0]
        #p = subprocess.Popen('ping 127.0.0.1',stdout = subprocess.PIPE)
        #output.wait()
        #print(output)
        if (b'\xa5\xd8\xaa\xba\xa6a\xa5D\xbe\xf7\xb5L\xaak\xb3s\xbdu' in output):
                print (('Host ') + ip + (" is offline or unavailable"))
                down+= 1
        else:
                print (("Host ") + ip + (" is online"))
                up+= 1

        target = target+1


print (("A total of ") + str(up+down) + " hosts were scanned.")
print (str(up) + (" hosts were alive, and " )+ str(down) + (" hosts were unreachable. "))
quit()
