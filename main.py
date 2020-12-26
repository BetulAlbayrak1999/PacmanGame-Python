import coin
import map
import readfromoutside
import pacman
from OpenGL.GL import *
from OpenGL.GL import glBegin
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

maze1 = [[0 for x in range(20)] for y in range(20)]
maze2 = [[0 for x in range(20)] for y in range(20)]
maze3 = [[0 for x in range(20)] for y in range(20)]
maze4 = [[0 for x in range(20)] for y in range(20)]
pacmanRotate = 0


def key_pressed(key, x, y):
    if key == b'\033':
        sys.exit()


class Main:
    def draw(self):
        global maze1, maze2, maze3, maze4
        glClearColor(1.0, 1.0, 1.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-1.0, 20.0, -1.0, 15.0, 0, 10)
        glActiveTexture(GL_TEXTURE0)
        add_image = readfromoutside.Readfromoutside()
        add_image.LoadTexture("tre2.jpg", 1)
        add_image.LoadTexture("floor3.jpg", 2)
        add_image.LoadTexture("co.jpg", 3)
        glEnable(GL_TEXTURE_2D)
        Read_text = readfromoutside.Readfromoutside()
        Draw_maze = map.Map()
        Call_coin = coin.Coin()
        Call_pacman = pacman.PacMan(7.6, 0.4, 1)

        # gluLookAt(0.0, 0.0,8.0, -2.0, 1.0, 0.0, 2.0, 50.0, -8.0)
        gluLookAt(0.0, -1.0, 8.0, -2.0, 0.0, 4.0, -9.0, 156.0, 17.0)
        if Call_coin.score() == 0:
            # draw pacman
            glPushMatrix()
            Call_pacman.drawPacman()
            glPopMatrix()
            glPushMatrix()
            maze1 = Read_text.readObj("maze1.txt", 1)
            Call_coin.drawcoin(0, 0, maze1)
            Draw_maze.drawmaze(0, 0, maze1)
            glPopMatrix()
        if Call_coin.score() > 500:
            # draw pacman
            glPushMatrix()
            Call_pacman.drawPacman()
            glPopMatrix()
            glPushMatrix()
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            maze2 = Read_text.readObj("maze2.txt", 2)
            Draw_maze.drawmaze(0, 0, maze2)
            Call_coin.drawcoin(0, 0, maze2)
            glPopMatrix()
        if Call_coin.score() > 100:
            # draw pacman
            glPushMatrix()
            Call_pacman.drawPacman()
            glPopMatrix()
            glPushMatrix()
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            maze3 = Read_text.readObj("maze3.txt", 3)
            Draw_maze.drawmaze(0, 0, maze3)
            Call_coin.drawcoin(0, 0, maze3)
            glPopMatrix()
        if Call_coin.score() > 150:
            # draw pacman
            glPushMatrix()
            Call_pacman.drawPacman()
            glPopMatrix()
            glPushMatrix()
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            maze4 = Read_text.readObj("maze4.txt", 4)
            Draw_maze.drawmaze(20, 20, maze4)
            Call_coin.drawcoin(0, 0, maze4)
            glPopMatrix()
        glFlush()

    def InitGL(self):
        glClearColor(0.0, 0.0, 0.0, 0.0)
        glClearDepth(1.0)
        glDepthFunc(GL_LESS)
        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_SMOOTH)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glMatrixMode(GL_MODELVIEW)



def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DEPTH)
    glutInitWindowSize(1000, 650)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"PACMAN GAME NEW UPDATE")
    glClearColor(0.0, 0.0, 0.0, 0.0)
    start_game = Main()
    glutDisplayFunc(start_game.draw)
    glutIdleFunc(start_game.draw)
    # glutMouseWheelFunc(MouseWheel)
    # glutMotionFunc(MouseWheelMotion)
    # Register the function called when the keyboard is pressed.
    Call_pacman = pacman.PacMan(7.6, 0.4, 1)
    glutKeyboardFunc(Call_pacman.key_pressed)
    glutSpecialFunc(Call_pacman.key_pressed_special)
    glutSpecialUpFunc(Call_pacman.key_pressed_special_up)
    start_game.InitGL()
    glutMainLoop()


main()
