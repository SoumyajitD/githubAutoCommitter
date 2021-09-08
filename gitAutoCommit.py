import os
import time
def makeCommit():
    os.system('git add .')
    os.system('git commit -m "Auto Commit by github auto commiter"')
    time.sleep(3600)

while True:    
    makeCommit()