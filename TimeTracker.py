import time
import datetime
import sys

now = str(datetime.datetime.now())
fileHandle = open ( '/Users/ian/life-log/timetracker.log', 'a' )
msg = now + ', ' + ' '.join(sys.argv[1:]) + '\n'
fileHandle.write(msg)
fileHandle.close()
print msg
