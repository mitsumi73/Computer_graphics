import OpenGL.GL as gl
import OpenGL.GLU as glu
import OpenGL.GLUT as glut
import numpy as np

cameraPositions = np.array([
    [3, 3, 4.5],
    [10.5, 3, -3],
    [3, 3, -10.5],
    [-4.5, 3, -3]
])

cameraTargets = np.array([
    [3, -2, -20],
    [-20, -2, -3],
    [3, -2, 20],
    [20, -2, -3]
])

currentCameraPosition = 0


def drawAxis():
    gl.glPushMatrix()
    gl.glBegin(gl.GL_LINES)
    gl.red = [1.0, 0.0, 0.0]
    gl.glMaterialfv(gl.GL_FRONT, gl.GL_AMBIENT, gl.red)
    gl.glVertex3f(0, 0, 0)
    gl.glVertex3f(6.5, 0, 0)
    gl.glEnd()
    gl.glPopMatrix()

    gl.glPushMatrix()
    gl.glBegin(gl.GL_LINES)
    gl.green = [0.0, 1.0, 0.0]
    gl.glMaterialfv(gl.GL_FRONT, gl.GL_AMBIENT, gl.green)
    gl.glVertex3f(0, 0, 0)
    gl.glVertex3f(0, 4, 0)
    gl.glEnd()
    gl.glPopMatrix()

    gl.glPushMatrix()
    gl.glBegin(gl.GL_LINES)
    gl.blue = [0.0, 0.0, 1.0]
    gl.glMaterialfv(gl.GL_FRONT, gl.GL_AMBIENT, gl.blue)
    gl.glVertex3f(0, 0, 0)
    gl.glVertex3f(0, 0, -8)
    gl.glEnd()
    gl.glPopMatrix()


def drawPlane():
    gl.white = [1.0, 1.0, 1.0]

    gl.glMaterialfv(gl.GL_FRONT, gl.GL_AMBIENT, gl.white)

    gl.glBegin(gl.GL_LINES)
    for i in np.arange(0, 6.1, 0.25):
        gl.glVertex3f(i, 0, -6)
        gl.glVertex3f(i, 0, 0)
        gl.glVertex3f(6, 0, -i)
        gl.glVertex3f(0, 0, -i)

    gl.glEnd()


def drawObjects():
    gl.glPushMatrix()
    gl.glTranslatef(4.0, 0.5, -1.3)
    gl.purple = [138.0 / 255.0, 43.0 / 255.0, 226.0 / 255.0]
    gl.glMaterialfv(gl.GL_FRONT, gl.GL_AMBIENT, gl.purple)
    glut.glutSolidCube(0.75)
    gl.glPopMatrix()

    gl.glPushMatrix()
    gl.glTranslatef(1.5, 0.5, -3.3)
    gl.glRotatef(180.0, 0.0, 1.0, 0.0)
    gl.green = [155.0 / 255.0, 228.0 / 255.0, 102.0 / 255.0]
    gl.glMaterialfv(gl.GL_FRONT, gl.GL_AMBIENT, gl.green)
    glut.glutSolidTeapot(0.6)
    gl.glPopMatrix()

    gl.glPushMatrix()
    gl.glTranslatef(3.0, 0.0, -5.0)
    gl.orange = [248.0 / 255.0, 155.0 / 255.0, 0.0 / 255.0]
    gl.glMaterialfv(gl.GL_FRONT, gl.GL_AMBIENT, gl.orange)
    gl.glRotatef(-90.0, 1.0, 0.0, 0.0)
    glut.glutSolidCone(0.5, 1, 20, 20)
    gl.glPopMatrix()


def init():
    gl.glClearColor(0.6, 0.6, 0.6, 1.0)

    gl.glMatrixMode(gl.GL_PROJECTION)
    gl.glLoadIdentity()
    glu.gluPerspective(60.0, 4.0 / 3.0, 1.0, 15.0)

    gl.glMatrixMode(gl.GL_MODELVIEW)
    gl.glLoadIdentity()
    glu.gluLookAt(3, 3, 4.5, 3, -2, -20, 0, 1, 0)

    black = [0.0, 0.0, 0.0, 1.0]
    yellow = [1.0, 1.0, 0.0, 1.0]
    cyan = [0.0, 0.5, 0.5, 1.0]
    white = [1.0, 1.0, 1.0, 1.0]
    direction = [-1.0, 4.0, 7.0, 1.0]

    gl.glMaterialfv(gl.GL_FRONT, gl.GL_AMBIENT_AND_DIFFUSE, cyan)
    gl.glMaterialfv(gl.GL_FRONT, gl.GL_SPECULAR, white)
    gl.glMaterialf(gl.GL_FRONT, gl.GL_SHININESS, 20)

    gl.glLightfv(gl.GL_LIGHT0, gl.GL_AMBIENT, black)
    gl.glLightfv(gl.GL_LIGHT0, gl.GL_DIFFUSE, cyan)
    gl.glLightfv(gl.GL_LIGHT0, gl.GL_SPECULAR, white)
    gl.glLightfv(gl.GL_LIGHT0, gl.GL_POSITION, direction)

    gl.glEnable(gl.GL_LIGHTING)
    gl.glEnable(gl.GL_LIGHT0)
    gl.glEnable(gl.GL_DEPTH_TEST)


def display():
    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)

    gl.glMatrixMode(gl.GL_MODELVIEW)
    gl.glLoadIdentity()
    glu.gluLookAt(
        cameraPositions[currentCameraPosition][0],
        cameraPositions[currentCameraPosition][1],
        cameraPositions[currentCameraPosition][2],
        cameraTargets[currentCameraPosition][0],
        cameraTargets[currentCameraPosition][1],
        cameraTargets[currentCameraPosition][2],
        0, 1, 0
    )

    drawObjects()
    drawAxis()
    drawPlane()

    gl.glFlush()


def moveCameraWithKey(key, x, y):
    global currentCameraPosition
    if key == glut.GLUT_KEY_RIGHT:
        currentCameraPosition = (currentCameraPosition + 1) % 4
    elif key == glut.GLUT_KEY_LEFT:
        currentCameraPosition = (currentCameraPosition - 1 + 4) % 4

    glut.glutPostRedisplay()


def main():
    glut.glutInit()
    glut.glutInitDisplayMode(glut.GLUT_SINGLE | glut.GLUT_RGB | glut.GLUT_DEPTH)
    glut.glutInitWindowPosition(120, 80)
    glut.glutInitWindowSize(1280, 980)
    glut.glutCreateWindow("I/O function")
    glut.glutDisplayFunc(display)
    glut.glutSpecialFunc(moveCameraWithKey)

    init()

    glut.glutMainLoop()


if __name__ == "__main__":
    main()
