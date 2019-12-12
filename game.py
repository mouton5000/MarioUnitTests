import curses
stdscr = curses.initscr()
import model


curses.noecho()
curses.cbreak()
curses.curs_set(0)
stdscr.keypad(True)

stdscr.clear()
stdscr.timeout(100)

width = curses.COLS - 1
height = 23
level = model.Level(stdscr, width, height, height - 2, 0)
level.set_platform(height - 1, 0, width)
level.set_platform(20, 10, 5)
level.set_spikes(20, 15, 5)
level.set_platform(20, 20, 5)
level.display()


i = 0
while True:
    i += 1
    c = stdscr.getch()
    if c == ord('a'):
        break
    elif c == curses.KEY_LEFT:
        level.move_mario(-1, True)
    elif c == curses.KEY_RIGHT:
        level.move_mario(1, True)
    elif c == curses.KEY_UP:
        level.jump_mario()

    level.update()
    level.display()
    stdscr.addstr(0, 0, str(i))
    stdscr.refresh()

stdscr.keypad(False)
curses.nocbreak()
curses.echo()
curses.endwin()
