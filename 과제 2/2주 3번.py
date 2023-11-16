import OpenGL.GL as gl
import OpenGL.GLU as glu
import OpenGL.GLUT as glut
import numpy as np

def drawAxis():
    gl.glBegin(gl.GL_LINES)
    gl.glColor3f(1, 0, 0);
    gl.glVertex3f(0, 0, 0);
    gl.glVertex3f(6.5, 0, 0)
    gl.glColor3f(0, 1, 0);
    gl.glVertex3f(0, 0, 0);
    gl.glVertex3f(0, 4, 0)
    gl.glColor3f(0, 0, 1);
    gl.glVertex3f(0, 0, 0);
    gl.glVertex3f(0, 0, -8)
    gl.glEnd()

def drawPlane():
    gl.glColor3f(1.0, 1.0, 1.0)

    gl.glBegin(gl.GL_LINES)
    for i in np.arange(0, 6.1, 0.25):
        gl.glVertex3f(i, 0, -6)
        gl.glVertex3f(i, 0, 0)
        gl.glVertex3f(6, 0, -i)
        gl.glVertex3f(0, 0, -i)
    gl.glEnd()

# Displaying their x, y, and z coordinates
def drawCoordinates(x, y, z):
    coordinate_str = f"({x:.5f}, {y:.5f}, {z:.5f})"
    gl.glRasterPos3f(x, y, z)
    for char in coordinate_str:
        glut.glutBitmapCharacter(glut.GLUT_BITMAP_8_BY_13, ord(char))

def drawObjects():
    # Cube
    cube_x, cube_y, cube_z = 4.0, 0.0, -1.3
    gl.glPushMatrix()
    gl.glTranslatef(cube_x, cube_y, cube_z)
    gl.glColor3f(138.0 / 255.0, 43.0 / 255.0, 226.0 / 255.0)
    glut.glutSolidCube(0.75)
    gl.glPopMatrix()
    drawCoordinates(cube_x, cube_y, cube_z)

    # Teapot
    teapot_x, teapot_y, teapot_z = 1.5, 0.0, -3.3
    gl.glPushMatrix()
    gl.glTranslatef(teapot_x, teapot_y, teapot_z)
    gl.glRotatef(180.0, 0.0, 1.0, 0.0)
    gl.glColor3f(155.0 / 255.0, 228.0 / 255.0, 102.0 / 255.0)
    glut.glutSolidTeapot(0.6)
    gl.glPopMatrix()
    drawCoordinates(teapot_x, teapot_y, teapot_z)

    # Cone
    cone_x, cone_y, cone_z = 3.0, 0.0, -5.0
    gl.glPushMatrix()
    gl.glTranslatef(cone_x, cone_y, cone_z)
    gl.glColor3f(248.0 / 255.0, 155.0 / 255.0, 0.0 / 255.0)
    gl.glRotatef(-90.0, 1.0, 0.0, 0.0)
    glut.glutSolidCone(0.5, 1, 20, 20)
    gl.glPopMatrix()
    drawCoordinates(cone_x, cone_y, cone_z)



def display():
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)

    # Set up viewport for the bottom-right corner
    window_width, window_height = 1280, 980
    viewport_width, viewport_height = 640, 480  # Size of the viewport
    viewport_x = window_width - viewport_width  # X position (from left)
    viewport_y = 0  # Y position (from bottom)

    gl.glViewport(viewport_x, viewport_y, viewport_width, viewport_height)

    # Render your content here
    drawPlane()
    drawAxis()
    drawObjects()

    gl.glFlush()

def init():
    gl.glClearColor(0.6, 0.6, 0.6, 1.0)

    gl.glMatrixMode(gl.GL_PROJECTION)
    gl.glLoadIdentity()
    glu.gluPerspective(60.0, 4.0 / 3.0, 1.0, 15.0)
    glu.gluLookAt(3, 3, 4.5, 3, -2, -20, 0, 1, 0)

def main():
    glut.glutInit()
    glut.glutInitDisplayMode(glut.GLUT_SINGLE | glut.GLUT_RGB)
    glut.glutInitWindowPosition(120, 80)
    glut.glutInitWindowSize(1280, 980)
    glut.glutCreateWindow("Viewport")
    glut.glutDisplayFunc(display)
    init()
    glut.glutMainLoop()

if __name__ == "__main__":
    main()
