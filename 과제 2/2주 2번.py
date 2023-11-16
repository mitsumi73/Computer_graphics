import OpenGL.GL as gl
import OpenGL.GLU as glu
import OpenGL.GLUT as glut
import numpy as np


def drawAxis():
    gl.glBegin(gl.GL_LINES)
    gl.glColor3f(1, 0, 0)
    gl.glVertex3f(0, 0, 0)
    gl.glVertex3f(6.5, 0, 0)

    gl.glColor3f(0, 1, 0)
    gl.glVertex3f(0, 0, 0)
    gl.glVertex3f(0, 4, 0)

    gl.glColor3f(0, 0, 1)
    gl.glVertex3f(0, 0, 0)
    gl.glVertex3f(0, 0, -8)
    gl.glEnd()


def drawPlane():
    gl.glColor3f(1.0, 1.0, 1.0)

    gl.glBegin(gl.GL_LINES)
    for i in np.arange(0, 6.25, 0.25):
        gl.glVertex3f(i, 0, -6)
        gl.glVertex3f(i, 0, 0)
        gl.glVertex3f(6, 0, -i)
        gl.glVertex3f(0, 0, -i)
    gl.glEnd()


def drawObjects():
    # Cube
    gl.glPushMatrix()
    gl.glTranslatef(4.0, 0.0, -1.3)
    gl.glColor3f(138 / 255, 43 / 255, 226 / 255)
    glut.glutSolidCube(0.75)
    gl.glPopMatrix()

    # Teapot
    gl.glPushMatrix()
    gl.glTranslatef(1.5, 0.0, -3.3)
    gl.glRotatef(180.0, 0.0, 1.0, 0.0)
    gl.glColor3f(155 / 255, 228 / 255, 102 / 255)
    glut.glutSolidTeapot(0.6)
    gl.glPopMatrix()

    # Cone
    gl.glPushMatrix()
    gl.glTranslatef(3.0, 0.0, -5.0)
    gl.glColor3f(248 / 255, 155 / 255, 0 / 255)
    gl.glRotatef(-90.0, 1.0, 0.0, 0.0)
    glut.glutSolidCone(0.5, 1, 20, 20)
    gl.glPopMatrix()


def display():
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)

    drawPlane()
    drawAxis()
    drawObjects()

    glut.glutSwapBuffers()


def init():
    gl.glClearColor(0.6, 0.6, 0.6, 1.0)

    gl.glMatrixMode(gl.GL_PROJECTION)
    gl.glLoadIdentity()

    # Cube
    # glu.gluPerspective(60, 4 / 3, 1, 6.5)
    # Teapot
    # glu.gluPerspective(60, 4 / 3, 6.8, 9)
    # Cone
    glu.gluPerspective(60, 4/3, 9, 15)

    glu.gluLookAt(3, 3, 4.5, 3, -2, -20, 0, 1, 0)


glut.glutInit()
glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGB)
glut.glutInitWindowPosition(120, 80)
glut.glutInitWindowSize(1280, 980)
glut.glutCreateWindow("Viewing Volume")
glut.glutDisplayFunc(display)
init()
glut.glutMainLoop()