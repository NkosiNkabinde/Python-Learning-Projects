import curses 
from curses import wrapper
import queue
import time



start_point = (0,1)
end_point = (4, 7)
end_point = (7,1)


maze = [
    [ "#", "O","#","#" ,"#" ,"#" ,"#" ,"#"],
    [ "#", " "," "," " ," " ," " ," " ,"#"],
    [ "#", "#","#"," " ," " ,"#" ," " ,"#"],
    [ "#", "#","#"," " ,"#" ,"#" ," " ,"X"],
    [ "#", "#","#"," " ," " ,"#" ," " ," "],
    [ "#", " "," "," " ," " ,"#" ,"#" ,"#"],
    [ "#", " ","#"," " ,"#" ,"#" ,"#" ,"#"],
    [ "#", " ","#"," " ,"#" ,"#" ,"#" ,"#"],
    [ "#", "X","#","#" ,"#" ,"#" ,"#" ,"#"],
]




def print_maze(maze, stdscr, path=[]):
    Blue = curses.color_pair(1)
    RED = curses.color_pair(2)
    GREEN = curses.color_pair(3)

    for i, rwo in enumerate(maze):
        for j, value in enumerate(rwo):
            stdscr.addstr(i, j* 3 , value,Blue )
    
def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
    blue_black = curses.color_pair(1)
    red_black = curses.color_pair(2)
    green_black = curses.color_pair(3)

    stdscr.clear()
    stdscr.addstr(0, 0, "Welcome to the maze game")
    time.sleep(5)
    stdscr.clear()
    print_maze(maze, stdscr)
    stdscr.refresh()
    time.sleep(2)
    stdscr.getch()
    
wrapper(main)

    