# Timer with PyMsgBox
import time
import pymsgbox

# Ask the user how many seconds to count down
response = pymsgbox.prompt('How many seconds should the timer run for?', 'Timer')

# Handle cancel button or empty input
if response is None:
    pymsgbox.alert('Timer cancelled!')
else:
    seconds = int(response)
    pymsgbox.alert('Timer started! Counting down ' + str(seconds) + ' seconds.')
    
    time.sleep(seconds)
    
    pymsgbox.alert("Time's up!")