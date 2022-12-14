"""
pass
"""
import os.path
import shutil
import sys


import cv2 as cv
import webbrowser
import matplotlib.pyplot as plt
from PIL import Image, ImageEnhance, ImageChops
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QSlider
import rc_resource

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

        self.ui.progressBar.setValue(0)

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
        self.ui.pushButton_refresh.clicked.connect(self.preview_image)

        self.ui.pushButton_crop.clicked.connect(self.crop_save)
        self.ui.pushButton_video.clicked.connect(self.get_video)
        self.ui.pushButton_extract.clicked.connect(self.extract_video)
        self.ui.checkBox.stateChanged.connect(self.toggle_crop_method)

        self.ui.actionCopyright.triggered.connect(self.clickcopyright)
        self.setWindowIcon(QIcon(':/V2F.ico'))

    def toggle_crop_method(self):
        """

        :return:
        """

        if self.ui.checkBox.isChecked() == True: # ????????????
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
        elif self.ui.checkBox.isChecked() == False: # ????????????
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
        # msgBox.setWindowTitle("????????????")
        # msgBox.setText(r"https://www.asgeologeekfan.top")
        # msgBox.exec()

        webbrowser.open(r"https://www.asgeologeekfan.top/posts/videofc")

    def get_video(self):
        """

        :return:
        """

        self.video_directory = QFileDialog.getOpenFileName(QMainWindow(), caption="????????????????????????", filter="Videos (*.mov *.avi *.mp4)")
        self.ui.label_videopath.setText(self.video_directory[0])
        self.video = self.video_directory[0]

        # ??????????????????
        # os.path.basename(path) ???????????????
        self.video_name = os.path.basename(self.video_directory[0])

        # os.path.splittext(path) ?????????????????????????????????????????????????????????
        self.prefix = os.path.splitext(self.video_name)[0]
        self.cap = cv.VideoCapture(self.video)

        # ???????????????
        self.fps = self.cap.get(cv.CAP_PROP_FPS)

        # ???????????????
        self.n_frames = int(self.cap.get(cv.CAP_PROP_FRAME_COUNT))
        # ???????????????
        self.dur = self.n_frames / self.fps

        self.ui.statusbar.showMessage(
            "??????????????????{:1f}???????????????{:1f}, ????????????{}".format(self.dur, self.fps, self.n_frames)
        )

    def extract_video(self):
        """

        :return:
        """
        self.initial_extract_time = self.ui.spinBox_initialtime.value()
        self.end_extract_time = self.ui.spinBox_endtime.value()
        self.extract_time_interval = self.ui.spinBox_interval.value()
        self.jpg_quality = self.ui.spinBox_quality.value()


        ## ????????????????????????????????????
        # os.path.dirname(path) ??????????????????
        self.video_output_path = os.path.dirname(self.video_directory[0])
        self.pathOut_name = (
            "frame_"
            + str(self.initial_extract_time)
            + "_"
            + str(self.end_extract_time)
            + "_"
            + str(self.extract_time_interval)
        )

        self.pathOut = os.path.join(self.video_output_path, self.pathOut_name)
        if os.path.exists(self.pathOut) and os.path.isdir(self.pathOut):
            shutil.rmtree(self.pathOut)
        os.makedirs(self.pathOut, exist_ok=False)

        self.frame_sum = (self.end_extract_time - self.initial_extract_time) / self.extract_time_interval + 1
        self.count = 0
        ret = True
        while ret and self.count < self.frame_sum:
            self.cap.set(
                cv.CAP_PROP_POS_MSEC,
                (
                    1000 * self.initial_extract_time
                    + self.count * 1000 * self.extract_time_interval
                ),
            )
            ret, self.image = self.cap.read()
            print("Write a new frame: {}th".format(self.count + 1))
            cv.imwrite(
                os.path.join(
                    self.pathOut, "{}_frame_{:06d}.jpg".format(self.prefix, self.count + 1)
                ),
                self.image,
                [int(cv.IMWRITE_JPEG_QUALITY), self.jpg_quality],
            )  # save frame as JPEG file
            self.count += 1
            self.ui.progressBar_video.setRange(0, self.frame_sum)
            self.ui.statusbar.showMessage(
                "??????????????? {} ??????????????? {} ???".format(self.count, int(self.frame_sum))
            )
            self.ui.progressBar_video.setValue(self.count)


        ## ?????????????????????
        # os.path.dirname(path) ??????????????????
        self.video_output_path = os.path.dirname(self.video_directory[0])
        self.pathOut_name = (
            "frame_"
            + str(self.initial_extract_time)
            + "_"
            + str(self.end_extract_time)
            + "_"
            + str(self.extract_time_interval)
        )
        self.pathOut = os.path.join(self.video_output_path, self.pathOut_name)
        if os.path.exists(self.pathOut) and os.path.isdir(self.pathOut):
            shutil.rmtree(self.pathOut)
        os.makedirs(self.pathOut, exist_ok=False)


        msgBox = QMessageBox()
        msgBox.setWindowTitle("??????")
        msgBox.setText("???????????????")
        msgBox.setInformativeText("???????????????" + os.path.dirname(self.video) + '/' + self.pathOut_name)
        msgBox.exec()

    def choose_directory(self):
        """

        :return:
        """
        self.file_directory = QFileDialog.getExistingDirectory(QMainWindow(), "???????????????")
        self.ui.label_path.setText(self.file_directory)

        self.output_path = os.path.join(self.file_directory, "./output")
        self.temp_path = os.path.join(self.file_directory, "./temp")

        if os.path.exists(self.output_path) and os.path.isdir(self.output_path):
            shutil.rmtree(self.output_path)
        if os.path.exists(self.temp_path) and os.path.isdir(self.temp_path):
            shutil.rmtree(self.temp_path)
        os.makedirs(self.output_path, exist_ok=False)
        os.makedirs(self.temp_path, exist_ok=False)

        self.preview_img_num = self.ui.spinBox_No.value()
        self.file_num = len(os.listdir(self.file_directory)) - 2
        self.file_list = os.listdir(self.file_directory)
        self.ui.spinBox_No.setMaximum(self.file_num)
        self.img_ref = Image.open(os.path.join(self.file_directory, self.file_list[0]))
        self.width = self.img_ref.width
        self.height = self.img_ref.height
        self.size = self.img_ref.size

        self.ui.statusbar.showMessage(
            "?????????????????????{}????????????????????????????????????{}px, ????????????{}px".format(self.file_num, self.width, self.height)
        )

        self.ui.label_leftupx.setText('0')
        self.ui.label_leftupy.setText('0')
        self.ui.label_rightdownx.setText(str(self.width))
        self.ui.label_rightdowny.setText(str(self.height))

        self.preview_img = Image.open(os.path.join(self.file_directory, self.file_list[self.preview_img_num - 1]))
        self.temp_output_fullname = os.path.join(self.file_directory, self.file_list[self.preview_img_num - 1])
        self.ui.MplWidget.canvas.axes.imshow(self.preview_img)
        self.ui.MplWidget.canvas.draw()

        #self.preview_img = Image.open(self.temp_output_fullname)

        self.fig = plt.figure(self.temp_output_fullname)
        self.ax = self.fig.add_subplot(111)
        self.preview_image()



    def on_press(self, event):
        """

        :return:
        """
        #print('you pressed', event.button, event.xdata, event.ydata)


        if event.button == 1:  # ??????????????????
            print("add position:", event.button, event.xdata, event.ydata)
            self.ui.label_leftupx.setText(str(round(event.xdata)))
            self.ui.label_leftupy.setText(str(round(event.ydata)))

            self.horizontal_line1 = self.ui.MplWidget.canvas.axes.axhline(color='r', lw=0.8, ls='--')
            self.vertical_line1 = self.ui.MplWidget.canvas.axes.axvline(color='r', lw=0.8, ls='--')
            self.horizontal_line1.set_ydata(event.ydata)
            self.vertical_line1.set_xdata(event.xdata)
            self.horizontal_line1.set_visible(True)
            self.vertical_line1.set_visible(True)
            self.ui.MplWidget.canvas.draw()

            self.horizontal_line1out = self.ax.axhline(color='r', lw=0.8, ls='--')
            self.vertical_line1out = self.ax.axvline(color='r', lw=0.8, ls='--')
            self.horizontal_line1out.set_ydata(event.ydata)
            self.vertical_line1out.set_xdata(event.xdata)
            self.horizontal_line1out.set_visible(True)
            self.vertical_line1out.set_visible(True)
            self.ax.figure.canvas.draw()

        elif event.button == 3:  # ??????????????????
            print("add position:", event.button, event.xdata, event.ydata)
            self.ui.label_rightdownx.setText(str(round(event.xdata)))
            self.ui.label_rightdowny.setText(str(round(event.ydata)))

            self.horizontal_line2 = self.ui.MplWidget.canvas.axes.axhline(color='b', lw=0.8, ls='--')
            self.vertical_line2 = self.ui.MplWidget.canvas.axes.axvline(color='b', lw=0.8, ls='--')
            self.horizontal_line2.set_ydata(event.ydata)
            self.vertical_line2.set_xdata(event.xdata)
            self.horizontal_line2.set_visible(True)
            self.vertical_line2.set_visible(True)
            self.ui.MplWidget.canvas.draw()

            self.horizontal_line2out = self.ax.axhline(color='b', lw=0.8, ls='--')
            self.vertical_line2out = self.ax.axvline(color='b', lw=0.8, ls='--')
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

        self.first_image = Image.open(os.path.join(self.file_directory, self.file_list[self.preview_img_num - 1]))

        if self.ui.comboBox.currentText() == '????????????':
            self.img_ref = Image.open(os.path.join(self.file_directory, self.file_list[self.preview_img_num - 1]))
            self.img_ref_rotate = self.img_ref.rotate(-self.sum_rotate_angle)
            self.preview_img_num = self.ui.spinBox_No.value()
            self.bright_num = self.ui.horizontalSlider.value() / 20.0
            self.img_ref_color = ImageEnhance.Brightness(self.img_ref_rotate)

            self.temp_output_fullname = self.temp_path + "/" + "temp_color_" + self.file_list[self.preview_img_num - 1]
            self.img_ref_color.enhance(self.bright_num).save(self.temp_output_fullname)

            self.ui.label_adjustpara.setText('??????')
            self.ui.horizontalSlider.setMinimum(10)
            self.ui.horizontalSlider.setMaximum(40)
            self.ui.horizontalSlider.setTickInterval(5)
            self.ui.horizontalSlider.setTickPosition(QSlider.TicksAbove)
            self.ui.horizontalSlider.setMouseTracking(True)
            self.ui.horizontalSlider.setEnabled(True)
        elif self.ui.comboBox.currentText() == '????????????':
            self.img_ref = Image.open(os.path.join(self.file_directory, self.file_list[self.preview_img_num - 1]))
            self.img_ref_rotate = self.img_ref.rotate(-self.sum_rotate_angle)
            self.preview_img_num = self.ui.spinBox_No.value()
            self.img_ref2grey = self.img_ref_rotate.convert('L')
            self.contrast_num = self.ui.horizontalSlider.value() / 20.0
            self.img_ref2grey_enh = ImageEnhance.Contrast(self.img_ref2grey)

            self.temp_output_fullname = self.temp_path + "/" + "temp_grey_" + self.file_list[self.preview_img_num - 1]
            self.img_ref2grey_enh.enhance(self.contrast_num).save(self.temp_output_fullname)

            self.ui.label_adjustpara.setText('?????????')
            self.ui.horizontalSlider.setMinimum(10)
            self.ui.horizontalSlider.setMaximum(40)
            self.ui.horizontalSlider.setTickInterval(5)
            self.ui.horizontalSlider.setTickPosition(QSlider.TicksAbove)
            self.ui.horizontalSlider.setMouseTracking(True)
            self.ui.horizontalSlider.setEnabled(True)
        elif self.ui.comboBox.currentText() == '???????????????':
            self.img_ref = Image.open(os.path.join(self.file_directory, self.file_list[self.preview_img_num - 1]))
            self.img_ref_rotate = self.img_ref.rotate(-self.sum_rotate_angle)
            self.img_ref2grey = self.img_ref_rotate.convert('L')
            self.preview_img_num = self.ui.spinBox_No.value()
            self.threshold = self.ui.horizontalSlider.value()
            self.table = []
            for i in range(256):
                if i < self.threshold:
                    self.table.append(0)
                else:
                    self.table.append(1)
            self.img_bin = self.img_ref2grey.point(self.table, '1')

            self.temp_output_fullname = self.temp_path + "/" + "temp_bin_" + self.file_list[self.preview_img_num - 1]
            self.img_bin.save(self.temp_output_fullname)

            self.ui.label_adjustpara.setText('??????')
            self.ui.horizontalSlider.setMinimum(0)
            self.ui.horizontalSlider.setMaximum(255)
            self.ui.horizontalSlider.setTickInterval(32)
            self.ui.horizontalSlider.setTickPosition(QSlider.TicksAbove)
            self.ui.horizontalSlider.setMouseTracking(True)
            self.ui.horizontalSlider.setEnabled(True)
        elif self.ui.comboBox.currentText() == '????????????':
            self.preview_img_num = self.ui.spinBox_No.value()
            self.img_ref = Image.open(os.path.join(self.file_directory, self.file_list[self.preview_img_num - 1]))
            self.img_ref_rotate = self.img_ref.rotate(-self.sum_rotate_angle)
            self.img_ref_inverted = ImageChops.invert(self.img_ref_rotate)
            self.bright_num = self.ui.horizontalSlider.value() / 20.0
            self.img_ref_inverted_bright = ImageEnhance.Brightness(self.img_ref_inverted)

            self.temp_output_fullname = self.temp_path + "/" + "temp_inverted_" + self.file_list[self.preview_img_num - 1]
            self.img_ref_inverted_bright.enhance(self.bright_num).save(self.temp_output_fullname)

            self.ui.label_adjustpara.setText('??????')
            self.ui.horizontalSlider.setMinimum(10)
            self.ui.horizontalSlider.setMaximum(40)
            self.ui.horizontalSlider.setTickInterval(5)
            self.ui.horizontalSlider.setTickPosition(QSlider.TicksAbove)
            self.ui.horizontalSlider.setMouseTracking(True)
            self.ui.horizontalSlider.setEnabled(True)


        self.ui.MplWidget.canvas.axes.clear()

        self.preview_img = Image.open(self.temp_output_fullname)

        self.ui.MplWidget.canvas.axes.imshow(self.preview_img, animated=True, cmap='binary_r') #binary_r

        if self.ui.checkBox.isChecked() == True:
            self.ui.label_leftupx.setText(str(self.ui.spinBox_leftup_x.value()))
            self.ui.label_leftupy.setText(str(self.ui.spinBox_leftup_y.value()))
            self.ui.label_rightdownx.setText(str(self.ui.spinBox_rightdown_x.value()))
            self.ui.label_rightdowny.setText(str(self.ui.spinBox_rightdown_y.value()))
        elif self.ui.checkBox.isChecked() == False:
            self.ui.MplWidget.canvas.mpl_connect('button_press_event', self.on_press)



        self.horizontal_line1 = self.ui.MplWidget.canvas.axes.axhline(color='r', lw=0.8, ls='--')
        self.vertical_line1 = self.ui.MplWidget.canvas.axes.axvline(color='r', lw=0.8, ls='--')
        self.horizontal_line1.set_ydata(int(self.ui.label_leftupy.text()))
        self.vertical_line1.set_xdata(int(self.ui.label_leftupx.text()))
        self.horizontal_line1.set_visible(True)
        self.vertical_line1.set_visible(True)

        self.horizontal_line2 = self.ui.MplWidget.canvas.axes.axhline(color='b', lw=0.8, ls='--')
        self.vertical_line2 = self.ui.MplWidget.canvas.axes.axvline(color='b', lw=0.8, ls='--')
        self.horizontal_line2.set_ydata(int(self.ui.label_rightdowny.text()))
        self.vertical_line2.set_xdata(int(self.ui.label_rightdownx.text()))
        self.horizontal_line2.set_visible(True)
        self.vertical_line2.set_visible(True)

        self.ui.MplWidget.canvas.draw()

    def open_preview(self):
        """

        :return:
        """
        self.preview_img = Image.open(self.temp_output_fullname)
        self.fig = plt.figure(self.temp_output_fullname)
        self.ax = self.fig.add_subplot(111)
        plt.imshow(self.preview_img)
        self.fig.canvas.mpl_connect('button_press_event', self.on_press)
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

    def crop_save(self):
        """

        :return:
        """

        self.lux = int(self.ui.label_leftupx.text())
        self.luy = int(self.ui.label_leftupy.text())
        self.rdx = int(self.ui.label_rightdownx.text())
        self.rdy = int(self.ui.label_rightdowny.text())

        sum_i = 0

        self.ui.progressBar.setRange(0, self.file_num)
        self.bright_num = self.ui.horizontalSlider.value() / 20.0
        self.contrast_num = self.ui.horizontalSlider.value() / 20.0
        self.threshold = self.ui.horizontalSlider.value()

        if self.ui.comboBox.currentText() == '????????????':
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
                    self.image_output_fullname = self.output_path + "/" + "crop_color_" + each_image
                    try:
                        self.roi_area_color.enhance(self.bright_num).save(self.image_output_fullname)
                    except:
                        pass
                    finally:
                        sum_i += 1
                        self.ui.progressBar.setValue(sum_i)
        elif self.ui.comboBox.currentText() == '????????????':
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
                    self.roi2grey = self.roi_area.convert('L')
                    self.roi_area_enh = ImageEnhance.Contrast(self.roi2grey)
                    self.image_output_fullname = self.output_path + "/" + "crop_grey_" + each_image
                    try:
                        self.roi_area_enh.enhance(self.contrast_num).save(self.image_output_fullname)
                    except:
                        pass
                    finally:
                        sum_i += 1
                        self.ui.progressBar.setValue(sum_i)
        elif self.ui.comboBox.currentText() == '???????????????':
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
                    self.roi2grey = self.roi_area.convert('L')
                    self.table = []
                    for i in range(256):
                        if i < self.threshold:
                            self.table.append(0)
                        else:
                            self.table.append(1)
                    self.roi_area_bin = self.roi2grey.point(self.table, "1")
                    self.image_output_fullname = self.output_path + "/" + "crop_bin_" + each_image
                    try:
                        self.roi_area_bin.save(self.image_output_fullname)
                    except:
                        pass
                    finally:
                        sum_i += 1
                        self.ui.progressBar.setValue(sum_i)
        elif self.ui.comboBox.currentText() == '????????????':
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
                    self.roi_area_inverted_bright = ImageEnhance.Brightness(self.roi_area_inverted)
                    self.image_output_fullname = self.output_path + "/" + "crop_inverted_bright_" + each_image
                    try:
                        self.roi_area_inverted_bright.enhance(self.bright_num).save(self.image_output_fullname)
                    except:
                        pass
                    finally:
                        sum_i += 1
                        self.ui.progressBar.setValue(sum_i)

        msgBox = QMessageBox()
        msgBox.setWindowTitle("??????")

        msgBox.setText("???????????????" + self.file_directory + "/output")
        msgBox.setInformativeText("???????????????????????????")
        msgBox.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
        msgBox.setDefaultButton(QMessageBox.Discard)
        ret = msgBox.exec()

        if ret == QMessageBox.Save:
            pass
        elif ret == QMessageBox.Discard:
            self.delete_temp()
            sys.exit()
            # os.makedirs(self.temp_path, exist_ok=False)
        elif ret == QMessageBox.Cancel:
            pass



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QmyMainWindow()
    window.show()
    sys.exit(app.exec())
