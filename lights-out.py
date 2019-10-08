# Simon Gigli

# I have added two dimensionality as an extra function to the initial game.
# Before each game starts, the computer will ask the user for the number
# of lights the user would like per row and then the number of rows the
# user would like. A light is then toggled by responding to two prompts by
# the computer: the first, in which row is the light you like to toggle?;
# the second, what is the position of the light you would like to toggle?.

import random

def create_grid(li_per_row, num_of_rows):
    grid=[]
    while num_of_rows != 0:
        l=li_per_row
        g=""
        while l != 0:
            r=random.randint(0, 1)
            if r==0:
                g = g + "0 "
            if r==1:
                g = g + "* "
            l=l-1
        grid=grid + [g]
        num_of_rows=num_of_rows - 1
    return grid
 

def print_grid(grid):
    x=grid
    while x != []:
        y=x[0]
        print y
        x=x[1:]

def check(grid):
    x=grid
    yes_light=False
    x_empty=False
    while (yes_light or x_empty) == False:
        if x==[]:
            check=0
            x_empty=True
            break
        y=x[0]
        i=0
        while i < len(y):
            if y[i]=='*':
                check=1
                yes_light=True
                i=len(y)
            else:
                i=i+1
        x=x[1:]       
            
    return check

def toggle(t_row, t_light):
    if (t_row) == len(grid):
        down=False
    else:
        down=True
    if (t_row - 1) == 0:
        up=False
    else:
        up=True
    if (t_light + t_light) == len(grid[t_row - 1]):
        right=False
    else:
        right=True
    if (t_light - 1) == 0:
        left=False
    else:
        left=True
                            
    x=grid[t_row - 1]
    y=t_light-2
    z=x[t_light + y]
    if y==-1:
        if z == '0':
            x = x[:t_light + y] + '*' + x[t_light + y + 1:]
            grid[t_row - 1] = x
        if z == '*':
            x = x[:t_light + y] + '0' + x[t_light + y + 1:]
            grid[t_row - 1] = x
    else:                
        if z == '0':
            x = x[:t_light + y - 1] + ' *' + x[t_light + y + 1:]
            grid[t_row - 1] = x
        if z == '*':
            x = x[:t_light + y - 1] + ' 0' + x[t_light + y + 1:]
            grid[t_row - 1] = x 
    
    
    if down:
        x=grid[t_row]
        y=t_light-2
        z=x[t_light + y]
        if y==-1:
            if z == '0':
                x = x[:t_light + y] + '*' + x[t_light + y + 1:]
                grid[t_row] = x
            if z == '*':
                x = x[:t_light + y] + '0' + x[t_light + y + 1:]
                grid[t_row] = x
        else:                
            if z == '0':
                x = x[:t_light + y - 1] + ' *' + x[t_light + y + 1:]
                grid[t_row] = x
            if z == '*':
                x = x[:t_light + y - 1] + ' 0' + x[t_light + y + 1:]
                grid[t_row] = x                

    if up:
        x=grid[t_row - 2]
        y=t_light-2
        z=x[t_light + y]
        if y==-1:
            if z == '0':
                x = x[:t_light + y] + '*' + x[t_light + y + 1:]
                grid[t_row - 2] = x
            if z == '*':
                x = x[:t_light + y] + '0' + x[t_light + y + 1:]
                grid[t_row - 2] = x
        else:                
            if z == '0':
                x = x[:t_light + y - 1] + ' *' + x[t_light + y + 1:]
                grid[t_row - 2] = x
            if z == '*':
                x = x[:t_light + y - 1] + ' 0' + x[t_light + y + 1:]
                grid[t_row - 2] = x

    if right:
        x=grid[t_row - 1]
        z=x[t_light + t_light]
        if z == '0':
            x = x[:t_light + t_light] + '*' + x[t_light + t_light + 1:]
            grid[t_row - 1] = x
        if z == '*':
            x = x[:t_light + t_light] + '0' + x[t_light + t_light + 1:]
            grid[t_row - 1] = x

    if left:
        x=grid[t_row - 1]
        y=t_light - 4
        z=x[t_light + y]
        if z == '0':
            x = x[:t_light + y] + '*' + x[t_light + y + 1:]
            grid[t_row - 1] = x
        if z == '*':
            x = x[:t_light + y] + '0' + x[t_light + y + 1:]
            grid[t_row - 1] = x
            
    return grid

try:
    lights_per_row=int(raw_input("How many lights would you like per row?: "))
except ValueError:
    print "Please enter a positive integer."
    lights_per_row=int(raw_input("How many lights would you like per row?: "))
try:
    number_of_rows=int(raw_input("How many rows would you like?: "))
except ValueError:
    print "Please enter a positive integer."
    number_of_rows=int(raw_input("How many rows would you like?: "))
grid=create_grid(lights_per_row, number_of_rows)
play=True

while play==True:
    print_grid(grid)
    check_grid=check(grid)
    if check_grid==0:
        print "Congratulations! You win!"
        play=False
    else:
        try:
            toggle_row=int(raw_input("In which row is the light you would like to toggle?: "))
        except ValueError:
            s=len(grid)
            print "Please enter a positive integer less than or equal to " + str(s) + "."
            toggle_row=int(raw_input("In which row is the light you would like to toggle?: "))
        if toggle_row==0:
            play=False
        else:
            try:
                toggle_light=int(raw_input("Which light would you like to toggle? (its position): "))
            except:
                s=len(grid[0])
                s=(.5*s)
                print "Please enter a positive integer less than or equal to " + str(s) + "."
                toggle_light=int(raw_input("Which light would you like to toggle? (its position): "))
            if toggle_light==0:
                play=False
            else:
                try:
                    grid=toggle(toggle_row, toggle_light)
                except:
                    s=len(grid)
                    print "Please make sure you have entered a positive integer "
                    print "less than or equal to " + str(s) + " for the row that "
                    print "contains the light you would like to toggle."
                    s=len(grid[0])
                    s=.5*s
                    print "Please also make sure you have entered a positive integer "
                    print "less than or equal to " + str(s) + " for the position of "
                    print "the light you would like to toggle."
                    toggle_row=int(raw_input("In which row is the light you would like to toggle?: "))
                    toggle_light=int(raw_input("Which light would you like to toggle? (its position): "))
                    grid=toggle(toggle_row, toggle_light)
                    


        
