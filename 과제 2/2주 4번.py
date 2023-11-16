import OpenGL.GL as gl
import OpenGL.GLU as glu
import OpenGL.GLUT as glut
import numpy as np

# Light position
lightPosition = [3, 4, 3, 1]

def drawAxis():
    # Vẽ trục X màu đỏ
    gl.glPushMatrix()
    gl.glBegin(gl.GL_LINES)
    gl.red = [1.0, 0.0, 0.0]  # RGB cho màu đỏ
    gl.glMaterialfv(gl.GL_FRONT, gl.GL_AMBIENT, gl.red)
    gl.glVertex3f(0, 0, 0)
    gl.glVertex3f(6.5, 0, 0)
    gl.glEnd()
    gl.glPopMatrix()

    # Vẽ trục Y màu xanh lá
    gl.glPushMatrix()
    gl.glBegin(gl.GL_LINES)
    gl.green = [0.0, 1.0, 0.0]  # RGB cho màu xanh lá
    gl.glMaterialfv(gl.GL_FRONT, gl.GL_AMBIENT, gl.green)
    gl.glVertex3f(0, 0, 0)
    gl.glVertex3f(0, 4, 0)
    gl.glEnd()
    gl.glPopMatrix()

    # Vẽ trục Z màu xanh lam
    gl.glPushMatrix()
    gl.glBegin(gl.GL_LINES)
    gl.blue = [0.0, 0.0, 1.0]  # RGB cho màu xanh lam
    gl.glMaterialfv(gl.GL_FRONT, gl.GL_AMBIENT, gl.blue)
    gl.glVertex3f(0, 0, 0)
    gl.glVertex3f(0, 0, -8)
    gl.glEnd()
    gl.glPopMatrix()

def drawPlane():
    # Xác định màu trắng
    gl.white = [1.0, 1.0, 1.0]  # RGB cho màu trắng

    # Thiết lập vật liệu màu trắng
    gl.glMaterialfv(gl.GL_FRONT, gl.GL_AMBIENT, gl.white)

    # Bắt đầu vẽ dạng đường thẳng
    gl.glBegin(gl.GL_LINES)

    # Vẽ các đường trên mặt phẳng
    i = 0
    while i <= 6:
        gl.glVertex3f(i, 0, -6)
        gl.glVertex3f(i, 0, 0)
        gl.glVertex3f(6, 0, -i)
        gl.glVertex3f(0, 0, -i)
        i += 0.25
    # Kết thúc vẽ
    gl.glEnd()


def drawObjects():
    # Vẽ hình lập phương màu tím
    gl.glPushMatrix()
    gl.glTranslatef(4.0, 0.5, -1.3)
    Purple = [0.0 / 255.0, 0.0 / 255.0, 255.0 / 255.0]
    gl.glMaterialfv(gl.GL_FRONT, gl.GL_AMBIENT, Purple)
    glut.glutSolidCube(0.75)
    gl.glPopMatrix()

    # Vẽ ấm trà màu xanh lá
    gl.glPushMatrix()
    gl.glTranslatef(1.5, 0.5, -3.3)
    gl.glRotatef(180.0, 0.0, 1.0, 0.0)
    Green = [155.0 / 255.0, 228.0 / 255.0, 102.0 / 255.0]
    gl.glMaterialfv(gl.GL_FRONT, gl.GL_AMBIENT, Green)
    glut.glutSolidTeapot(0.6)
    gl.glPopMatrix()

    # Vẽ hình nón màu cam
    gl.glPushMatrix()
    gl.glTranslatef(3.0, 0.0, -5.0)
    orange = [255.0 / 255.0, 255.0 / 255.0, 0.0]
    gl.glMaterialfv(gl.GL_FRONT, gl.GL_AMBIENT, orange)
    gl.glRotatef(-90.0, 1.0, 0.0, 0.0)
    glut.glutSolidCone(0.5, 1, 20, 20)
    gl.glPopMatrix()


def init():
    # Cài đặt màu nền
    gl.glClearColor(0.6, 0.6, 0.6, 1.0)

    # Cài đặt và khởi tạo ma trận chiếu (Projection matrix)
    gl.glMatrixMode(gl.GL_PROJECTION)
    gl.glLoadIdentity()
    glu.gluPerspective(60.0, 4.0 / 3.0, 1.0, 15.0)

    # Cài đặt và khởi tạo ma trận modelview
    gl.glMatrixMode(gl.GL_MODELVIEW)
    gl.glLoadIdentity()
    glu.gluLookAt(3, 3, 4.5, 3, -2, -20, 0, 1, 0)

    # Cài đặt các tham số cho đối tượng vật liệu và ánh sáng
    black = [0.0, 0.0, 0.0, 1.0]
    yellow = [1.0, 1.0, 0.0, 1.0]
    cyan = [0.0, 0.5, 0.5, 1.0]
    white = [1.0, 1.0, 1.0, 1.0]
    direction = [3.0, 4.0, 2.0, 1.0]

    gl.glMaterialfv(gl.GL_FRONT, gl.GL_AMBIENT_AND_DIFFUSE, cyan)
    gl.glMaterialfv(gl.GL_FRONT, gl.GL_SPECULAR, white)
    gl.glMaterialf(gl.GL_FRONT, gl.GL_SHININESS, 20)

    # Cài đặt các tham số cho nguồn sáng
    gl.glLightfv(gl.GL_LIGHT0, gl.GL_AMBIENT, black)
    gl.glLightfv(gl.GL_LIGHT0, gl.GL_DIFFUSE, cyan)
    gl.glLightfv(gl.GL_LIGHT0, gl.GL_SPECULAR, white)
    gl.glLightfv(gl.GL_LIGHT0, gl.GL_POSITION, direction)

    # Kích hoạt hệ thống đèn và bật kiểm tra độ sâu
    gl.glEnable(gl.GL_LIGHTING)
    gl.glEnable(gl.GL_LIGHT0)
    gl.glEnable(gl.GL_DEPTH_TEST)

def display():
    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)

    gl.glPushMatrix()
    gl.glLightfv(gl.GL_LIGHT0, gl.GL_POSITION, lightPosition)

    # Giả định các hàm này đã được định nghĩa ở đâu đó trong code
    drawObjects()
    drawAxis()
    drawPlane()

    gl.glPopMatrix()

    gl.glFlush()

def key_input(key, x, y):
    global lightPosition

    if key == glut.GLUT_KEY_UP:
        lightPosition = np.array([3, 4, -8, 1])
    elif key == glut.GLUT_KEY_DOWN:
        lightPosition = np.array([3, 4, 2, 1])
    elif key == glut.GLUT_KEY_LEFT:
        lightPosition = np.array([-2, 4, -3, 1])
    elif key == glut.GLUT_KEY_RIGHT:
        lightPosition = np.array([8, 4, -3, 1])

    glut.glutPostRedisplay()


def main():
    # Khởi tạo GLUT
    glut.glutInit()
    glut.glutInitDisplayMode(glut.GLUT_SINGLE | glut.GLUT_RGB | glut.GLUT_DEPTH)

    # Thiết lập vị trí và kích thước cửa sổ
    glut.glutInitWindowPosition(120, 80)
    glut.glutInitWindowSize(1280, 980)

    # Tạo cửa sổ với tiêu đề
    glut.glutCreateWindow("Lighting System")

    # Đăng ký hàm callback cho việc hiển thị và xử lý sự kiện bàn phím
    glut.glutDisplayFunc(display)
    glut.glutSpecialFunc(key_input)

    # Khởi tạo các thiết lập OpenGL
    init()

    # Vào vòng lặp chính của GLUT
    glut.glutMainLoop()

if __name__ == "__main__":
    main()
