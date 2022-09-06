"""
mplwidget.py 模块需要自己构建，在对应的路径下自己建一个mplwidget.py文件，
主要功能是创建一个同时继承了FigureCanvas与QWidget的类，按照上面预定义的，将其命名为mplwidget类。
该操作使原来的widget窗体具有了matplotlib画布功能，可以在上面绘图了。
"""
from PySide6.QtWidgets import QSizePolicy, QWidget, QVBoxLayout
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure


# class MplCanvas(FigureCanvas):
#     """
#     pass
#     """
#     def __init__(self):
#         self.fig = Figure()  # setup Matplotlib Figure and Axis
#         self.ax = self.fig.add_subplot(111)
#         FigureCanvas.__init__(self, self.fig)  # initialization of the canvas
#         FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)  # we define the widget as expandable
#         FigureCanvas.updateGeometry(self)  # notify the system of updated policy


# class MplWidget(QWidget):
#     """
#     pass
#     """
#     def __init__(self, parent=None):
#         QWidget.__init__(self, parent)  # initialization of Qt MainWindow widget
#         self.canvas = MplCanvas()  # set the canvas to the Matplotlib widget
#         self.navi_toolbar = NavigationToolbar(self.canvas, self)  # create a navigation toolbar for our plot canvas
#         self.vbl = QVBoxLayout()  # create a vertical box layout
#         self.vbl.addWidget(self.canvas)  # add mpl widget to vertical box
#         self.vbl.addWidget(self.navi_toolbar)  # add the navigation toolbar to vertical box
#         self.setLayout(self.vbl)  # set the layout to vertical box


class MplWidget(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.canvas = FigureCanvas(Figure())
        self.navi_toolbar = NavigationToolbar(self.canvas, self)#
        self.vertical_layout = QVBoxLayout()
        self.vertical_layout.addWidget(self.canvas)
        self.vertical_layout.addWidget(self.navi_toolbar)#
        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.setLayout(self.vertical_layout)