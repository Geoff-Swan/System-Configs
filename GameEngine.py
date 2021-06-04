# this is a very simple game engine that renders to the console with text. It is not very good but it is in development.

#imports
import os # this handles console output; i.e. clearing the screen to refresh the output.

#define display dimensions & generate empty display buffer. The display buffer is an array, which can be written to as a normal array, and displayed with the flush() method.
height = 20
width = 20

displayBuffer = [0] * height
for i in range (height):
    displayBuffer[i] = 0 * width

# define shades of grey, will be used later for basic shading 
shades = [".","*",";","/","%","@","#"] 

# detect the system and select the correct command for clearing the console
def clearDisplay():
    command = 'clear'
    if os.name in ('nt, dos'): # check if the machine is running windows; only NT is really needed, but dos is there just in case.
        command = 'cls'
    os.system(command)

def flush():
    for i in range (height):
        for j in range (width):
            shade = displayBuffer[i][j]

# a basic gradient demo script:

def demo():
    for i in range (len(shades)):
        for j in range (width):
            displayBuffer[i][j] = i

def main():
    flush()

main()
