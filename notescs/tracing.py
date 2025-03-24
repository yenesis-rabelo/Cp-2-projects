#Yenesis Rabelo, Tracing notes

#############################################################################################################################################################################################################
#What is tracing?
#Debugging method that lets you see what is happening with your function
#Tracing allows us to know where functions are being called from; stuff about functions

#python -m trace --trace notescs\tracing.py

"""
--trace (displays function lines as they are executed)
--count (displays the number of times each function is executed; instead of second trace at the terminal thingy)
--listfuncs (displays the functions in the project; instead of second trace at the terminal thingy)
--trackcalls (shows relationship between functions; instead of second trace at the terminal thingy)
"""

import trace
import sys

tracer = trace.Trace(count=False, trace=True)
def trace_calls(frame, event, arguement):
    if event == 'call':
        print(f'Calling fdunction: {frame.f_code.co_name}')
    return trace_calls
sys.settrace(trace_calls)

###############################################################################################################################################################################################################

#What are some ways we can debug by tracing?







###############################################################################################################################################################################################################

#How do you access the debugger in VS Code?









###############################################################################################################################################################################################################

#What is testing?








###############################################################################################################################################################################################################

#What are boundary conditions?

###############################################################################################################################################################################################################

#How do you handle when users give strange inputs?








def add(numone,numtwo):
    return numone+numtwo

def sub(numone,numtwo):
    return numone-numtwo

print (add(5,4))
print (sub(5,4))

tracer.run('sub(8,2)')