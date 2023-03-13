"""
pass
"""
import glob
import math
import os.path
import shutil
import sys

import cv2 as cv
import webbrowser

import imageio.v3 as iio
import matplotlib.pyplot as plt
from PIL import Image, ImageEnhance, ImageChops
from PySide6.QtGui import QIcon, QMovie
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QFileDialog,
    QMessageBox,
    QSlider, QProgressBar
)
import rc_resource
from datetime import datetime

from ui_main import Ui_MainWindow


class QmyMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.MplWidget = None

        self.sum_rotate_angle_shun = 0
        self.sum_rotate_angle_ni = 0
        self.sum_rotate_angle = 0

        #self.ui.progressBar.setValue(0)
        self.toggle_extract_method()

        self.ui.pushButton_video.clicked.connect(self.get_video)
        self.ui.comboBox_extract_method.currentIndexChanged.connect(self.toggle_extract_method)
        self.ui.pushButton_extract.clicked.connect(self.extract_video)

        self.ui.pushButton_choose.clicked.connect(self.choose_directory)
        self.ui.pushButton_rotate_ni.clicked.connect(self.rotate_image_ni)
        self.ui.pushButton_rotate_shun.clicked.connect(self.rotate_image_shun)
        self.ui.pushButton_rotate_ni.clicked.connect(self.get_rotate_angle)
        self.ui.pushButton_rotate_shun.clicked.connect(self.get_rotate_angle)
        self.ui.pushButton_rotate_ni.clicked.connect(self.preview_image)
        self.ui.pushButton_rotate_shun.clicked.connect(self.preview_image)

        self.ui.comboBox.currentIndexChanged.connect(self.preview_image)
        self.ui.horizontalSlider.valueChanged.connect(self.preview_image)

        self.ui.spinBox_No.valueChanged.connect(self.preview_image)

        self.ui.spinBox_leftup_x.valueChanged.connect(self.preview_image)
        self.ui.spinBox_leftup_y.valueChanged.connect(self.preview_image)
        self.ui.spinBox_rightdown_x.valueChanged.connect(self.preview_image)
        self.ui.spinBox_rightdown_y.valueChanged.connect(self.preview_image)
        self.ui.pushButton_preview.clicked.connect(self.open_preview)
        self.ui.pushButton_refresh.clicked.connect(self.refresh_img)

        self.ui.checkBox.stateChanged.connect(self.toggle_crop_method)
        self.ui.pushButton_crop.clicked.connect(self.crop_save)
        self.ui.pushButton_reset.clicked.connect(self.reset_directory)

        self.ui.pushButton_gif_home.clicked.connect(self.choose_gif_directory)
        self.ui.spinBox_gif_time.valueChanged.connect(self.preview_gif)
        self.ui.label_gif_display.setScaledContents(True)
        self.ui.pushButton_gif_save.clicked.connect(self.create_gif)

        self.ui.actionCopyright.triggered.connect(self.clickcopyright)
        self.setWindowIcon(QIcon(":/V2F.ico"))

        self.ui.progressBar = QProgressBar()
        self.ui.statusbar.addPermanentWidget(self.ui.progressBar)


    def toggle_extract_method(self):
        """

        """
        if self.ui.comboBox_extract_method.currentText() == "指定起止时刻":
            self.ui.lineEdit.setPlaceholderText('请输入起止时刻和间隔秒数（空格分隔）  例如：00:00:42 00:04:20 5 表示从第00分42秒开始，第4分20秒截止，每隔5秒提取一张')
        elif self.ui.comboBox_extract_method.currentText() == "提取特定秒":
            self.ui.lineEdit.setPlaceholderText('请输入要提取的视频时刻 (空格分隔)   例如：00:00:42 00:04:20 04:20:00')
        elif self.ui.comboBox_extract_method.currentText() == "提取特定帧":
            self.ui.lineEdit.setPlaceholderText('请输入要提取的视频帧 (空格分隔)   例如：0 42 420')

    def toggle_crop_method(self):
        """

        :return:
        """

        if self.ui.checkBox.isChecked() == True:  # 手动输入
            self.ui.spinBox_leftup_x.setEnabled(True)
            self.ui.spinBox_leftup_x.setMaximum(self.height)
            self.ui.spinBox_leftup_y.setEnabled(True)
            self.ui.spinBox_leftup_y.setMaximum(self.height)
            self.ui.spinBox_rightdown_x.setEnabled(True)
            self.ui.spinBox_rightdown_x.setMaximum(self.width)
            self.ui.spinBox_rightdown_x.setValue(self.width)
            self.ui.spinBox_rightdown_y.setEnabled(True)
            self.ui.spinBox_rightdown_y.setMaximum(self.height)
            self.ui.spinBox_rightdown_y.setValue(self.height)
        elif self.ui.checkBox.isChecked() == False:  # 自动画线
            self.ui.spinBox_leftup_x.setEnabled(False)
            self.ui.spinBox_leftup_y.setEnabled(False)
            self.ui.spinBox_rightdown_x.setEnabled(False)
            self.ui.spinBox_rightdown_y.setEnabled(False)
            self.ui.spinBox_leftup_x.setValue(int(self.ui.label_leftupx.text()))
            self.ui.spinBox_leftup_y.setValue(int(self.ui.label_leftupy.text()))
            self.ui.spinBox_rightdown_x.setValue(int(self.ui.label_rightdownx.text()))
            self.ui.spinBox_rightdown_y.setValue(int(self.ui.label_rightdowny.text()))

    def clickcopyright(self):
        """

        :return:
        """
        # msgBox = QMessageBox()
        # msgBox.setWindowTitle("关于作者")
        # msgBox.setText(r"https://www.asgeologeekfan.top")
        # msgBox.exec()

        webbrowser.open(r"https://www.asgeologeekfan.top/posts/videofc")

    def get_video(self):
        """

        :return:
        """

        self.video_directory = QFileDialog.getOpenFileName(
            QMainWindow(), caption="选择要转换的视频", filter="Videos (*.mov *.avi *.mp4 *.mkv)"
        )
        self.ui.label_videopath.setText(self.video_directory[0])
        self.video = self.video_directory[0]

        # 打开视频文件
        # os.path.basename(path) 返回文件名
        self.video_name = os.path.basename(self.video_directory[0])

        # os.path.splittext(path) 分割路径，返回路径名和文件扩展名的元组
        self.prefix = os.path.splitext(self.video_name)[0]
        self.cap = cv.VideoCapture(self.video)

        # 视频的帧率
        self.fps = self.cap.get(cv.CAP_PROP_FPS)

        # 视频的帧数
        self.n_frames = int(self.cap.get(cv.CAP_PROP_FRAME_COUNT))
        # 视频的时长
        self.dur = self.n_frames / self.fps
        # 视频的高度
        self.frame_origin_width = int(self.cap.get(cv.CAP_PROP_FRAME_WIDTH))
        # 视频的宽度
        self.frame_origin_height = int(self.cap.get(cv.CAP_PROP_FRAME_HEIGHT))

        self.ui.statusbar.showMessage(
            "当前视频共有{:.2f}秒，帧率为{:.1f}, 总帧数为{}, 宽度为{}px，高度为{}px".format(self.dur, self.fps, self.n_frames, self.frame_origin_width, self.frame_origin_height)
        )

    def extract_video(self):
        """

        :return:
        """

        self.jpg_quality = self.ui.spinBox_quality.value()

        ## 按起止时间和时间间隔提取  00:01:03 00:02:04 3
        if self.ui.comboBox_extract_method.currentText() == "指定起止时刻":
            self.time_tuple = tuple(self.ui.lineEdit.text().split())  # return ('00:01:03','00:02:04', '3')
            self.initial_h, self.initial_m, self.initial_s = self.time_tuple[0].strip().split(':')  # return '00' '01' '03'
            self.end_h, self.end_m, self.end_s = self.time_tuple[1].strip().split(':')  # return '00' '01' '03'
            self.initial_time_second = int(self.initial_h) * 3600 + int(self.initial_m) * 60 + int(self.initial_s) # return 63
            self.end_time_second =  int(self.end_h) * 3600 + int(self.end_m) * 60 + int(self.end_s) # return 124
            self.time_tuple_number_name = [self.time_tuple[0].replace(':', ''), self.time_tuple[1].replace(':', ''), self.time_tuple[2]] # return ['000103', '000204', '3']

            self.video_output_path = os.path.dirname(self.video_directory[0])
            self.pathOut_name = (
                "frame_from_time"
                + self.time_tuple_number_name[0]
                + "to"
                + self.time_tuple_number_name[1]
                + "interval"
                + self.time_tuple_number_name[2]
            )

            try:
                self.frame_sum = math.ceil((self.end_time_second - self.initial_time_second) / int(self.time_tuple_number_name[2])) + 1   # (124-63)/3+1=21.33  (9-1)/3+1=3.67
            except (ValueError,ZeroDivisionError):
                self.ui.statusbar.showMessage("提取失败，间隔需为大于0的整数")
                msgBox = QMessageBox()
                msgBox.setWindowTitle("警告")
                msgBox.setText("提取失败，间隔需为大于0的整数")
                msgBox.exec()

            else:
                self.pathOut = os.path.join(self.video_output_path, self.pathOut_name)
                if os.path.exists(self.pathOut) and os.path.isdir(self.pathOut):
                    shutil.rmtree(self.pathOut)
                os.makedirs(self.pathOut, exist_ok=False)

                self.count = 0
                ret = True
                while ret and self.count < self.frame_sum:
                    self.cap.set(
                        cv.CAP_PROP_POS_MSEC,
                        (
                            1000 * self.initial_time_second
                            + self.count * 1000 * int(self.time_tuple_number_name[2])
                        ),
                    )
                    ret, self.image = self.cap.read()
                    self.frame_length = int(self.ui.lineEdit_length.text())
                    self.frame_width = int(self.ui.lineEdit_width.text())
                    self.image_resized = cv.resize(self.image, (self.frame_length, self.frame_width),interpolation=cv.INTER_AREA)
                    self.now_time_second = self.initial_time_second + self.count * int(self.time_tuple_number_name[2])
                    m, s = divmod(self.now_time_second, 60)
                    h, m = divmod(m, 60)
                    self.now_time_str = "%02d"%h + str("%02d"%m) + str("%02d"%s)   #return 080506
                    cv.imwrite(
                        os.path.join(
                            self.pathOut,
                            "{}_time_{}.jpg".format(self.prefix, self.now_time_str),
                        ),
                        self.image_resized,
                        [int(cv.IMWRITE_JPEG_QUALITY), self.jpg_quality],
                    )  # save frame as JPEG file
                    self.count += 1


                    self.ui.progressBar.setRange(0, self.frame_sum)
                    self.ui.statusbar.showMessage(
                        "已提取第 {} 张图像，共 {} 张".format(self.count, int(self.frame_sum))
                    )
                    self.ui.progressBar.setValue(self.count)

                msgBox = QMessageBox()
                msgBox.setWindowTitle("提示")
                msgBox.setText("提取完成！")
                msgBox.setInformativeText(
                    "已提取至：" + os.path.dirname(self.video) + "/" + self.pathOut_name
                )
                msgBox.exec()
        ## 指定特定时间点 文字框内的内容空格分隔 00:06:23代表00时06分23秒
        elif self.ui.comboBox_extract_method.currentText() == "提取特定秒":
            # os.path.dirname(path) 返回文件路径
            self.frame_tuple = tuple(self.ui.lineEdit.text().split())   # return ('00:01:03','00:02:04',...,'00:05:08')
            self.frame_tuple_number = []
            for i in range(len(self.frame_tuple)):
                self.frame_tuple_number.append(self.frame_tuple[i].replace(':', ''))    # '00:01:03' -> '000103'
            self.video_output_path = os.path.dirname(self.video_directory[0])
            self.pathOut_name = (
                "frame_list_"
                + str(self.frame_tuple_number[0])
                + "to"
                + str(self.frame_tuple_number[-1])
            )
            self.pathOut = os.path.join(self.video_output_path, self.pathOut_name)
            if os.path.exists(self.pathOut) and os.path.isdir(self.pathOut):
                shutil.rmtree(self.pathOut)
            os.makedirs(self.pathOut, exist_ok=False)

            self.count = 0
            ret = True
            while ret and self.count < len(self.frame_tuple):
                #self.frame_tuple_time = self.frame_tuple[self.count]
                h, m, s = self.frame_tuple[self.count].strip().split(':')
                self.frame_tuple_second = int(h) * 3600 + int(m) * 60 + int(s)
                self.cap.set(
                    cv.CAP_PROP_POS_MSEC, 1000 * self.frame_tuple_second
                )
                ret, self.image = self.cap.read()
                self.frame_length = int(self.ui.lineEdit_length.text())
                self.frame_width = int(self.ui.lineEdit_width.text())
                self.image_resized = cv.resize(self.image, (self.frame_length, self.frame_width),
                                               interpolation=cv.INTER_AREA)
                cv.imwrite(
                    os.path.join(
                        self.pathOut,
                        "{}_time_{}.jpg".format(self.prefix, self.frame_tuple_number[self.count]),
                    ),
                    self.image_resized,
                    [int(cv.IMWRITE_JPEG_QUALITY), self.jpg_quality],
                )  # save frame as JPEG file
                self.count += 1
                self.ui.progressBar.setRange(0, len(self.frame_tuple))
                self.ui.statusbar.showMessage(
                    "已提取第 {} 张图像，共 {} 张".format(self.count, len(self.frame_tuple))
                )
                self.ui.progressBar.setValue(self.count)

            msgBox = QMessageBox()
            msgBox.setWindowTitle("提示")
            msgBox.setText("提取完成！")
            msgBox.setInformativeText(
                "已提取至：" + os.path.dirname(self.video) + "/" + self.pathOut_name
            )
            msgBox.exec()
        elif self.ui.comboBox_extract_method.currentText() == "提取特定帧":
            # os.path.dirname(path) 返回文件路径 请输入帧值，空格键分隔
            self.frame_tuple = tuple(self.ui.lineEdit.text().split())   # return ('1' '3000' '6000')
            self.video_output_path = os.path.dirname(self.video_directory[0])
            self.pathOut_name = (
                "frame_list_frame"
                + self.frame_tuple[0]
                + "to_frame"
                + self.frame_tuple[-1]
            )
            self.pathOut = os.path.join(self.video_output_path, self.pathOut_name)
            if os.path.exists(self.pathOut) and os.path.isdir(self.pathOut):
                shutil.rmtree(self.pathOut)
            os.makedirs(self.pathOut, exist_ok=False)

            self.count = 0
            ret = True
            while ret and self.count < len(self.frame_tuple):
                self.cap.set(
                    cv.CAP_PROP_POS_FRAMES, int(self.frame_tuple[self.count])
                )
                ret, self.image = self.cap.read()
                self.frame_length = int(self.ui.lineEdit_length.text())
                self.frame_width = int(self.ui.lineEdit_width.text())
                self.image_resized = cv.resize(self.image, (self.frame_length, self.frame_width),
                                               interpolation=cv.INTER_AREA)
                cv.imwrite(
                    os.path.join(
                        self.pathOut,
                        "{}_frame_{}.jpg".format(self.prefix, self.frame_tuple[self.count]),
                    ),
                    self.image_resized,
                    [int(cv.IMWRITE_JPEG_QUALITY), self.jpg_quality],
                )  # save frame as JPEG file
                self.count += 1
                self.ui.progressBar.setRange(0, len(self.frame_tuple))
                self.ui.statusbar.showMessage(
                    "已提取第 {} 张图像，共 {} 张".format(self.count, len(self.frame_tuple))
                )
                self.ui.progressBar.setValue(self.count)

            msgBox = QMessageBox()
            msgBox.setWindowTitle("提示")
            msgBox.setText("提取完成！")
            msgBox.setInformativeText(
                "已提取至：" + os.path.dirname(self.video) + "/" + self.pathOut_name
            )
            msgBox.exec()


    def choose_directory(self):
        """

        :return:
        """
        self.file_directory = QFileDialog.getExistingDirectory(QMainWindow(), "选择文件夹")
        self.ui.label_path.setText(self.file_directory)

        self.now = datetime.now()
        self.stamp = self.now.strftime("%Y%m%d%H%M%S")

        self.output_path = os.path.join(self.file_directory, "./output"+self.stamp)
        self.temp_path = os.path.join(self.file_directory, "./temp"+self.stamp)

        self.file_num = 0
        fileExtensions = ["*.jpg", "*.jpeg", "*.png", "*.bmp", "*.gif"]
        for extension in fileExtensions:
            self.file_num += len(glob.glob(os.path.join(self.file_directory, extension)))
        #self.file_num = len(os.listdir(self.file_directory))

        # if os.path.exists(self.output_path) and os.path.isdir(self.output_path):
        #     shutil.rmtree(self.output_path)
        if os.path.exists(self.temp_path) and os.path.isdir(self.temp_path):
            shutil.rmtree(self.temp_path)
        # os.makedirs(self.output_path, exist_ok=False)
        os.makedirs(self.temp_path, exist_ok=False)

        self.preview_img_num = self.ui.spinBox_No.value()

        self.file_list = os.listdir(self.file_directory)
        self.ui.spinBox_No.setMaximum(self.file_num)
        self.img_ref = Image.open(os.path.join(self.file_directory, self.file_list[0]))
        self.width = self.img_ref.width
        self.height = self.img_ref.height
        self.size = self.img_ref.size

        self.ui.statusbar.showMessage(
            "当前文件夹共有{}张图片，原始图片宽度为：{}px, 高度为：{}px".format(
                self.file_num, self.width, self.height
            )
        )

        self.ui.label_leftupx.setText("0")
        self.ui.label_leftupy.setText("0")
        self.ui.label_rightdownx.setText(str(self.width))
        self.ui.label_rightdowny.setText(str(self.height))

        self.preview_img = Image.open(
            os.path.join(self.file_directory, self.file_list[self.preview_img_num - 1])
        )
        self.temp_output_fullname = os.path.join(
            self.file_directory, self.file_list[self.preview_img_num - 1]
        )
        self.ui.MplWidget.canvas.axes.imshow(self.preview_img)
        self.ui.MplWidget.canvas.draw()

        # self.preview_img = Image.open(self.temp_output_fullname)

        self.fig = plt.figure(self.temp_output_fullname)
        self.ax = self.fig.add_subplot(111)
        self.preview_image()

    def choose_gif_directory(self):
        """

        :return:
        """
        self.gif_directory = QFileDialog.getExistingDirectory(QMainWindow(), "选择GIF素材文件夹")
        self.ui.label_GIFhome.setText(self.gif_directory)
        self.gif_file_num = 0
        self.gif_list = []
        fileExtensions = ["*.jpg", "*.jpeg", "*.png", "*.bmp"]
        for extension in fileExtensions:
            self.gif_file_num += len(glob.glob(os.path.join(self.gif_directory, extension)))
            self.gif_list += glob.glob(os.path.join(self.gif_directory, extension))


        self.img_ref = Image.open(self.gif_list[0])
        self.gif_ratio = self.img_ref.height / self.img_ref.width
        if self.gif_ratio < 1.0:
            self.ui.label_gif_display.resize(600, 600 * self.gif_ratio)
        elif self.gif_ratio > 1.0:
            self.ui.label_gif_display.resize(600, 600 / self.gif_ratio)
        else:
            self.ui.label_gif_display.resize(600, 600)


        self.preview_gif()

    def preview_gif(self):
        """

        """
        self.gif_time = self.ui.spinBox_gif_time.value()
        self.gif_frames = []
        self.ui.label_gif_display.setText("正在加载预览...")
        for i in range(len(self.gif_list)):
            self.gif_frames.append(iio.imread(os.path.join(self.gif_directory, self.gif_list[i])))
        iio.imwrite(os.path.join(self.gif_directory, "temp.gif"), self.gif_frames, duration = self.gif_time, loop=0)

        self.movie = QMovie()
        self.movie.setFileName(os.path.join(self.gif_directory, "temp.gif"))
        self.ui.label_gif_display.setMovie(self.movie)
        self.movie.start()

    def create_gif(self):
        """

        """
        self.gif_time = self.ui.spinBox_gif_time.value()
        self.gif_frames = []
        for i in range(len(self.gif_list)):
            self.gif_frames.append(iio.imread(os.path.join(self.gif_directory, self.gif_list[i])))
        iio.imwrite(os.path.join(self.gif_directory, "output.gif"), self.gif_frames, duration = self.gif_time, loop=0)


        msgBox = QMessageBox()
        msgBox.setWindowTitle("提示")
        msgBox.setText("保存完成！")
        msgBox.setInformativeText(
            "已保存GIF至素材文件夹内 :)"
        )
        msgBox.exec()
        # msgBox.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
        # msgBox.setDefaultButton(QMessageBox.Discard)
        # ret = msgBox.exec()

        # if ret == QMessageBox.Save:
        #     pass
        # elif ret == QMessageBox.Discard:
        #     os.remove(os.path.join(self.gif_directory, "temp.gif"))
        # elif ret == QMessageBox.Cancel:
        #     pass


    def on_press(self, event):
        """

        :return:
        """
        # print('you pressed', event.button, event.xdata, event.ydata)

        if event.button == 1:  # 鼠标左键点击
            print("add position:", event.button, event.xdata, event.ydata)
            self.ui.label_leftupx.setText(str(round(event.xdata)))
            self.ui.label_leftupy.setText(str(round(event.ydata)))

            self.horizontal_line1 = self.ui.MplWidget.canvas.axes.axhline(
                color="r", lw=0.8, ls="--"
            )
            self.vertical_line1 = self.ui.MplWidget.canvas.axes.axvline(
                color="r", lw=0.8, ls="--"
            )
            self.horizontal_line1.set_ydata(event.ydata)
            self.vertical_line1.set_xdata(event.xdata)
            self.horizontal_line1.set_visible(True)
            self.vertical_line1.set_visible(True)
            self.ui.MplWidget.canvas.draw()

            self.horizontal_line1out = self.ax.axhline(color="r", lw=0.8, ls="--")
            self.vertical_line1out = self.ax.axvline(color="r", lw=0.8, ls="--")
            self.horizontal_line1out.set_ydata(event.ydata)
            self.vertical_line1out.set_xdata(event.xdata)
            self.horizontal_line1out.set_visible(True)
            self.vertical_line1out.set_visible(True)
            self.ax.figure.canvas.draw()

        elif event.button == 3:  # 鼠标右键点击
            print("add position:", event.button, event.xdata, event.ydata)
            self.ui.label_rightdownx.setText(str(round(event.xdata)))
            self.ui.label_rightdowny.setText(str(round(event.ydata)))

            self.horizontal_line2 = self.ui.MplWidget.canvas.axes.axhline(
                color="b", lw=0.8, ls="--"
            )
            self.vertical_line2 = self.ui.MplWidget.canvas.axes.axvline(
                color="b", lw=0.8, ls="--"
            )
            self.horizontal_line2.set_ydata(event.ydata)
            self.vertical_line2.set_xdata(event.xdata)
            self.horizontal_line2.set_visible(True)
            self.vertical_line2.set_visible(True)
            self.ui.MplWidget.canvas.draw()

            self.horizontal_line2out = self.ax.axhline(color="b", lw=0.8, ls="--")
            self.vertical_line2out = self.ax.axvline(color="b", lw=0.8, ls="--")
            self.horizontal_line2out.set_ydata(event.ydata)
            self.vertical_line2out.set_xdata(event.xdata)
            self.horizontal_line2out.set_visible(True)
            self.vertical_line2out.set_visible(True)
            self.ax.figure.canvas.draw()

    def preview_image(self):
        """

        :return:
        """
        self.preview_img_num = self.ui.spinBox_No.value()
        # try:
        #     self.first_image = Image.open(
        #     os.path.join(self.file_directory, self.file_list[self.preview_img_num - 1])
        #     )
        # except PermissionError:
        #     pass

        self.first_image = Image.open(
            os.path.join(self.file_directory, self.file_list[self.preview_img_num - 1])
            )


        if self.ui.comboBox.currentText() == "原始彩图":
            self.img_ref = Image.open(
                os.path.join(
                    self.file_directory, self.file_list[self.preview_img_num - 1]
                )
            )
            self.img_ref_rotate = self.img_ref.rotate(-self.sum_rotate_angle)
            self.preview_img_num = self.ui.spinBox_No.value()
            self.bright_num = self.ui.horizontalSlider.value() / 20.0
            self.img_ref_color = ImageEnhance.Brightness(self.img_ref_rotate)

            self.temp_output_fullname = (
                self.temp_path
                + "/"
                + "temp_color_"
                + self.file_list[self.preview_img_num - 1]
            )
            self.img_ref_color.enhance(self.bright_num).save(self.temp_output_fullname)

            self.ui.label_adjustpara.setText("亮度")
            self.ui.horizontalSlider.setMinimum(10)
            self.ui.horizontalSlider.setMaximum(40)
            self.ui.horizontalSlider.setTickInterval(5)
            self.ui.horizontalSlider.setTickPosition(QSlider.TicksAbove)
            self.ui.horizontalSlider.setMouseTracking(True)
            self.ui.horizontalSlider.setEnabled(True)
        elif self.ui.comboBox.currentText() == "灰度处理":
            self.img_ref = Image.open(
                os.path.join(
                    self.file_directory, self.file_list[self.preview_img_num - 1]
                )
            )
            self.img_ref_rotate = self.img_ref.rotate(-self.sum_rotate_angle)
            self.preview_img_num = self.ui.spinBox_No.value()
            self.img_ref2grey = self.img_ref_rotate.convert("L")
            self.contrast_num = self.ui.horizontalSlider.value() / 20.0
            self.img_ref2grey_enh = ImageEnhance.Contrast(self.img_ref2grey)

            self.temp_output_fullname = (
                self.temp_path
                + "/"
                + "temp_grey_"
                + self.file_list[self.preview_img_num - 1]
            )
            self.img_ref2grey_enh.enhance(self.contrast_num).save(
                self.temp_output_fullname
            )

            self.ui.label_adjustpara.setText("对比度")
            self.ui.horizontalSlider.setMinimum(10)
            self.ui.horizontalSlider.setMaximum(40)
            self.ui.horizontalSlider.setTickInterval(5)
            self.ui.horizontalSlider.setTickPosition(QSlider.TicksAbove)
            self.ui.horizontalSlider.setMouseTracking(True)
            self.ui.horizontalSlider.setEnabled(True)
        elif self.ui.comboBox.currentText() == "二值化处理":
            self.img_ref = Image.open(
                os.path.join(
                    self.file_directory, self.file_list[self.preview_img_num - 1]
                )
            )
            self.img_ref_rotate = self.img_ref.rotate(-self.sum_rotate_angle)
            self.img_ref2grey = self.img_ref_rotate.convert("L")
            self.preview_img_num = self.ui.spinBox_No.value()
            self.threshold = self.ui.horizontalSlider.value()
            self.table = []
            for i in range(256):
                if i < self.threshold:
                    self.table.append(0)
                else:
                    self.table.append(1)
            self.img_bin = self.img_ref2grey.point(self.table, "1")

            self.temp_output_fullname = (
                self.temp_path
                + "/"
                + "temp_bin_"
                + self.file_list[self.preview_img_num - 1]
            )
            self.img_bin.save(self.temp_output_fullname)

            self.ui.label_adjustpara.setText("阈值")
            self.ui.horizontalSlider.setMinimum(0)
            self.ui.horizontalSlider.setMaximum(255)
            self.ui.horizontalSlider.setTickInterval(32)
            self.ui.horizontalSlider.setTickPosition(QSlider.TicksAbove)
            self.ui.horizontalSlider.setMouseTracking(True)
            self.ui.horizontalSlider.setEnabled(True)
        elif self.ui.comboBox.currentText() == "反相处理":
            self.preview_img_num = self.ui.spinBox_No.value()
            self.img_ref = Image.open(
                os.path.join(
                    self.file_directory, self.file_list[self.preview_img_num - 1]
                )
            )
            self.img_ref_rotate = self.img_ref.rotate(-self.sum_rotate_angle)
            self.img_ref_inverted = ImageChops.invert(self.img_ref_rotate)
            self.bright_num = self.ui.horizontalSlider.value() / 20.0
            self.img_ref_inverted_bright = ImageEnhance.Brightness(
                self.img_ref_inverted
            )

            self.temp_output_fullname = (
                self.temp_path
                + "/"
                + "temp_inverted_"
                + self.file_list[self.preview_img_num - 1]
            )
            self.img_ref_inverted_bright.enhance(self.bright_num).save(
                self.temp_output_fullname
            )

            self.ui.label_adjustpara.setText("亮度")
            self.ui.horizontalSlider.setMinimum(10)
            self.ui.horizontalSlider.setMaximum(40)
            self.ui.horizontalSlider.setTickInterval(5)
            self.ui.horizontalSlider.setTickPosition(QSlider.TicksAbove)
            self.ui.horizontalSlider.setMouseTracking(True)
            self.ui.horizontalSlider.setEnabled(True)

        self.ui.MplWidget.canvas.axes.clear()

        self.preview_img = Image.open(self.temp_output_fullname)

        self.ui.MplWidget.canvas.axes.imshow(
            self.preview_img, animated=True, cmap="binary_r"
        )  # binary_r

        if self.ui.checkBox.isChecked() == True:
            self.ui.label_leftupx.setText(str(self.ui.spinBox_leftup_x.value()))
            self.ui.label_leftupy.setText(str(self.ui.spinBox_leftup_y.value()))
            self.ui.label_rightdownx.setText(str(self.ui.spinBox_rightdown_x.value()))
            self.ui.label_rightdowny.setText(str(self.ui.spinBox_rightdown_y.value()))
        elif self.ui.checkBox.isChecked() == False:
            self.ui.MplWidget.canvas.mpl_connect("button_press_event", self.on_press)

        self.horizontal_line1 = self.ui.MplWidget.canvas.axes.axhline(
            color="r", lw=0.8, ls="--"
        )
        self.vertical_line1 = self.ui.MplWidget.canvas.axes.axvline(
            color="r", lw=0.8, ls="--"
        )
        self.horizontal_line1.set_ydata(int(self.ui.label_leftupy.text()))
        self.vertical_line1.set_xdata(int(self.ui.label_leftupx.text()))
        self.horizontal_line1.set_visible(True)
        self.vertical_line1.set_visible(True)

        self.horizontal_line2 = self.ui.MplWidget.canvas.axes.axhline(
            color="b", lw=0.8, ls="--"
        )
        self.vertical_line2 = self.ui.MplWidget.canvas.axes.axvline(
            color="b", lw=0.8, ls="--"
        )
        self.horizontal_line2.set_ydata(int(self.ui.label_rightdowny.text()))
        self.vertical_line2.set_xdata(int(self.ui.label_rightdownx.text()))
        self.horizontal_line2.set_visible(True)
        self.vertical_line2.set_visible(True)

        self.ui.MplWidget.canvas.draw()

    def refresh_img(self):
        """
        pass
        """
        self.horizontal_line1.set_visible(False)
        self.vertical_line1.set_visible(False)
        self.horizontal_line2.set_visible(False)
        self.vertical_line2.set_visible(False)
        self.ui.MplWidget.canvas.draw()

        self.horizontal_line1out.set_visible(False)
        self.vertical_line1out.set_visible(False)
        self.horizontal_line2out.set_visible(False)
        self.vertical_line2out.set_visible(False)
        self.ax.figure.canvas.draw()


    def open_preview(self):
        """

        :return:
        """
        self.preview_img = Image.open(self.temp_output_fullname)
        self.fig = plt.figure(self.temp_output_fullname)
        self.ax = self.fig.add_subplot(111)
        plt.imshow(self.preview_img)
        self.fig.canvas.mpl_connect("button_press_event", self.on_press)
        plt.show()

    def rotate_image_shun(self):
        """

        :return:
        """

        self.sum_rotate_angle_shun += 1

    def rotate_image_ni(self):
        """

        :return:
        """

        self.sum_rotate_angle_ni -= 1

    def get_rotate_angle(self):
        """

        :return:
        """
        self.sum_rotate_angle = self.sum_rotate_angle_shun + self.sum_rotate_angle_ni
        self.ui.lcdNumber.display(self.sum_rotate_angle)

    def delete_temp(self):
        """
        Delete temporary files generated during preview.

        :return:
        """
        shutil.rmtree(self.temp_path)

    def reset_directory(self):
        """
        Reread images after pressing crop_save.
        """

        self.now = datetime.now()
        self.stamp = self.now.strftime("%Y%m%d%H%M%S")

        self.output_path = os.path.join(self.file_directory, "./output"+self.stamp)
        self.temp_path = os.path.join(self.file_directory, "./temp"+self.stamp)

        # if os.path.exists(self.output_path) and os.path.isdir(self.output_path):
        #     shutil.rmtree(self.output_path)
        if os.path.exists(self.temp_path) and os.path.isdir(self.temp_path):
            shutil.rmtree(self.temp_path)
        # os.makedirs(self.output_path, exist_ok=False)
        os.makedirs(self.temp_path, exist_ok=False)


        self.horizontal_line1.set_visible(False)
        self.vertical_line1.set_visible(False)
        self.horizontal_line2.set_visible(False)
        self.vertical_line2.set_visible(False)
        self.ui.MplWidget.canvas.draw()

        self.horizontal_line1out.set_visible(False)
        self.vertical_line1out.set_visible(False)
        self.horizontal_line2out.set_visible(False)
        self.vertical_line2out.set_visible(False)
        self.ax.figure.canvas.draw()




    def crop_save(self):
        """

        :return:
        """
        if os.path.exists(self.output_path) and os.path.isdir(self.output_path):
            shutil.rmtree(self.output_path)
        os.makedirs(self.output_path, exist_ok=False)

        self.lux = int(self.ui.label_leftupx.text())
        self.luy = int(self.ui.label_leftupy.text())
        self.rdx = int(self.ui.label_rightdownx.text())
        self.rdy = int(self.ui.label_rightdowny.text())

        sum_i = 0

        self.ui.progressBar.setRange(0, self.file_num)
        self.bright_num = self.ui.horizontalSlider.value() / 20.0
        self.contrast_num = self.ui.horizontalSlider.value() / 20.0
        self.threshold = self.ui.horizontalSlider.value()

        if self.ui.comboBox.currentText() == "原始彩图":
            for each_image in os.listdir(self.file_directory):
                self.image_input_fullname = self.file_directory + "/" + each_image
                try:
                    self.img = Image.open(self.image_input_fullname)
                except:
                    pass
                finally:
                    self.img_rotate = self.img.rotate(-self.sum_rotate_angle)
                    self.box = (self.lux, self.luy, self.rdx, self.rdy)
                    self.roi_area = self.img_rotate.crop(self.box)
                    self.roi_area_color = ImageEnhance.Brightness(self.roi_area)
                    self.image_output_fullname = (
                        self.output_path + "/" + "crop_color_" + each_image
                    )
                    try:
                        self.roi_area_color.enhance(self.bright_num).save(
                            self.image_output_fullname
                        )
                    except:
                        pass
                    finally:
                        sum_i += 1
                        self.ui.progressBar.setValue(sum_i)
        elif self.ui.comboBox.currentText() == "灰度处理":
            for each_image in os.listdir(self.file_directory):
                self.image_input_fullname = self.file_directory + "/" + each_image
                try:
                    self.img = Image.open(self.image_input_fullname)
                except:
                    pass
                finally:
                    self.img_rotate = self.img.rotate(-self.sum_rotate_angle)
                    self.box = (self.lux, self.luy, self.rdx, self.rdy)
                    self.roi_area = self.img_rotate.crop(self.box)
                    self.roi2grey = self.roi_area.convert("L")
                    self.roi_area_enh = ImageEnhance.Contrast(self.roi2grey)
                    self.image_output_fullname = (
                        self.output_path + "/" + "crop_grey_" + each_image
                    )
                    try:
                        self.roi_area_enh.enhance(self.contrast_num).save(
                            self.image_output_fullname
                        )
                    except:
                        pass
                    finally:
                        sum_i += 1
                        self.ui.progressBar.setValue(sum_i)
        elif self.ui.comboBox.currentText() == "二值化处理":
            for each_image in os.listdir(self.file_directory):
                self.image_input_fullname = self.file_directory + "/" + each_image
                try:
                    self.img = Image.open(self.image_input_fullname)
                except:
                    pass
                finally:
                    self.img_rotate = self.img.rotate(-self.sum_rotate_angle)
                    self.box = (self.lux, self.luy, self.rdx, self.rdy)
                    self.roi_area = self.img_rotate.crop(self.box)
                    self.roi2grey = self.roi_area.convert("L")
                    self.table = []
                    for i in range(256):
                        if i < self.threshold:
                            self.table.append(0)
                        else:
                            self.table.append(1)
                    self.roi_area_bin = self.roi2grey.point(self.table, "1")
                    self.image_output_fullname = (
                        self.output_path + "/" + "crop_bin_" + each_image
                    )
                    try:
                        self.roi_area_bin.save(self.image_output_fullname)
                    except:
                        pass
                    finally:
                        sum_i += 1
                        self.ui.progressBar.setValue(sum_i)
        elif self.ui.comboBox.currentText() == "反相处理":
            for each_image in os.listdir(self.file_directory):
                self.image_input_fullname = self.file_directory + "/" + each_image
                try:
                    self.img = Image.open(self.image_input_fullname)
                except:
                    pass
                finally:
                    self.img_rotate = self.img.rotate(-self.sum_rotate_angle)
                    self.box = (self.lux, self.luy, self.rdx, self.rdy)
                    self.roi_area = self.img_rotate.crop(self.box)
                    self.roi_area_inverted = ImageChops.invert(self.roi_area)
                    self.roi_area_inverted_bright = ImageEnhance.Brightness(
                        self.roi_area_inverted
                    )
                    self.image_output_fullname = (
                        self.output_path + "/" + "crop_inverted_bright_" + each_image
                    )
                    try:
                        self.roi_area_inverted_bright.enhance(self.bright_num).save(
                            self.image_output_fullname
                        )
                    except:
                        pass
                    finally:
                        sum_i += 1
                        self.ui.progressBar.setValue(sum_i)

        msgBox = QMessageBox()
        msgBox.setWindowTitle("提示")

        msgBox.setText("已导出至：" + self.file_directory + "/output")
        msgBox.setInformativeText("是否保留临时文件？")
        msgBox.setStandardButtons(
            QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel
        )
        msgBox.setDefaultButton(QMessageBox.Discard)
        ret = msgBox.exec()

        if ret == QMessageBox.Save:
            pass
            # self.reset_directory()
        elif ret == QMessageBox.Discard:
            self.delete_temp()
            # self.reset_directory()
            # sys.exit()
            # os.makedirs(self.temp_path, exist_ok=False)
        elif ret == QMessageBox.Cancel:
            pass
            # self.reset_directory()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QmyMainWindow()
    window.show()
    sys.exit(app.exec())

