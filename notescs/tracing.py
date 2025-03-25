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
    elif event == 'line':
        print(f'Executing line: {frame.f_lineco} in  {frame.f_code.co_name}')
    elif event == 'return':
        print (f'{frame.f_code.co_name} returned {arg}')
    elif event == 'exception':
       print (f'Excepption in {frame.f_code.co_name}: {arg}')
    
    return trace_calls
sys.settrace(trace_calls)

###############################################################################################################################################################################################################

#What are some ways we can debug by tracing?

#Make a function that lets us see how our functions are interacting 


###############################################################################################################################################################################################################

#How do you access the debugger in VS Code?

#F5


###############################################################################################################################################################################################################

#What is testing?

#Going througfh the code trying to break it, having testers be not people who wrote the code


###############################################################################################################################################################################################################

#What are boundary conditions?
#User inputs that are strange/likely to cause issues
# Extremes, high and lows, ones usually done wrong
age = 18
if age >= 18:
    print("You can vote")
elif age >= 16:
    print("You can drive")

###############################################################################################################################################################################################################

#How do you handle when users give strange inputs?
#try/excepts
#conditionals 
#loop back


def add(numone,numtwo):
    return numone+numtwo

def sub(numone,numtwo):
    return numone-numtwo

print (add(5,4))
print (sub(5,4))

tracer.run('sub(8,2)')