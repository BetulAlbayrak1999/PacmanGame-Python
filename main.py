import coin
import map
import readfromoutside
import pacman
import solid_data
from solid_data import OPPOSITE_MOVES as op
from OpenGL.GL import *
from OpenGL.GL import glBegin
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
ESCAPE = '\033'

maze1 = [[0 for x in range(20)] for y in range(20)]
maze2 = [[0 for x in range(20)] for y in range(20)]
maze3 = [[0 for x in range(20)] for y in range(20)]
maze4 = [[0 for x in range(20)] for y in range(20)]
pacmanRotate = 0

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


    def key_pressed(self, key, x, y):
        """The function called whenever a key is pressed.
        Note the use of Python tuples to pass in: (key, x, y)

        :param args: string represented pushed key
        """

        if key == ESCAPE:
            sys.exit()

    def key_pressed_special(self, key, x, y):
        """The function called whenever a key is pressed.
        Note the use of Python tuples to pass in: (key, x, y)

        :param args: integer represented pushed key
        """
        # działanie klawiszy w osobnej funkcji

        if key == 100:
            self.pacman.next_direction = solid_data.OPPOSITE_MOVES('W')

        elif key == 102:
            self.pacman.next_direction = solid_data.OPPOSITE_MOVES('E')

        elif key == 101:
            self.pacman.next_direction = solid_data.OPPOSITE_MOVES('N')

        elif key == 103:
            self.pacman.next_direction = solid_data.OPPOSITE_MOVES('S')

    def key_pressed_special_up(self, key, x, y):
        """"""
        pass

    def pacman_move(self):
        """"""
        directions = self.board.knots.get(
            (self.pacman.x, self.pacman.z)
        )
        if not self.pacman.was_eaten:
            if directions:
                if self.pacman.next_direction in directions:
                    self.pacman.direction = self.pacman.next_direction
                    self.pacman.move()
                elif self.pacman.direction in directions:
                    self.pacman.move()
                else:
                    pass   # PacMan no moves

            elif self.pacman.next_direction == op[self.pacman.direction]:
                self.pacman.direction = self.pacman.next_direction
                self.pacman.move()
            else:
                self.pacman.move()


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
    glutKeyboardFunc(start_game.key_pressed)
    glutSpecialFunc(start_game.key_pressed_special)
    glutSpecialUpFunc(start_game.key_pressed_special_up)
    start_game.InitGL()
    glutMainLoop()


main()
   # pacman key press
'''
    def key_pressed(self, *args, null):
        if args[0] == b'':
            sys.exit()
        glutPostRedisplay()

    def key_pressed_special(self, *args, null):

        if args[0] == 100:
            self.z -= self.step
            self.rotate = 90

        elif args[0] == 102:
            self.z += self.step
            self.rotate = 270

        elif args[0] == 101:
            self.x -= self.step
            self.rotate = 180

        elif args[0] == 103:
            self.x += self.step
            self.rotate = 0

            self.x, self.z = round(self.x, 2), round(self.z, 2)

        glutPostRedisplay()

    def key_pressed_special_up(self,*args, null):
        pass
'''