from PySide import QtGui, QtCore


class UiWorld(QtGui.QWidget):

    """Qt widget representing the world
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__last_point = None
        self.image = QtGui.QImage(800, 600, QtGui.QImage.Format_ARGB32)
        self.image.fill(QtCore.Qt.white)
        self.pen = QtGui.QPen(QtCore.Qt.black, 10, QtCore.Qt.SolidLine)
        # Create a timer to refresh the image
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(1000 / 60)

    def setImage(self, image):
        self.image = image

    def clear(self):
        self.image.fill(QtCore.Qt.white)

    def paintEvent(self, e):
        qp = QtGui.QPainter()
        qp.begin(self)
        qp.drawImage(e.rect(), self.image, e.rect())
        qp.end()

    def mousePressEvent(self, e):
        # Draw line on left click
        if e.button() == QtCore.Qt.LeftButton:
            self.__last_point = e.pos()
            self.__drawto(e.pos())
        if e.button() == QtCore.Qt.RightButton:
            # Move the robot on right click
            self.robot.pos_x = e.pos().x()
            self.robot.pos_y = e.pos().y()

    def mouseMoveEvent(self, e):
        # Draw line on left click
        if e.buttons() == QtCore.Qt.LeftButton:
            self.__drawto(e.pos())
        if e.button() == QtCore.Qt.RightButton:
            # Move the robot on right click
            self.robot.pos_x = e.pos().x()
            self.robot.pos_y = e.pos().y()

    def __drawto(self, pos):
        painter = QtGui.QPainter(self.image)
        painter.setPen(self.pen)
        painter.drawLine(self.__last_point, pos)
        self.__last_point = pos
        self.update()
