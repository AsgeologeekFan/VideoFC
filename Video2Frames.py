"""
pass
"""
import os
import shutil

import cv2 as cv


class Video2Frames:
    """
    pathIn
    output_video_info, pathOut, split_by_interval, by_number, isColor
    """

    def __init__(self, pathIn):
        self.pathIn = pathIn

    def output_video_info(self):
        """

        :return:
        """
        # 打开视频文件
        self.video_name = os.path.basename(self.pathIn)
        self.prefix = os.path.splitext(self.video_name)[0]
        self.cap = cv.VideoCapture(self.pathIn)

        # 视频的帧率
        self.fps = self.cap.get(cv.CAP_PROP_FPS)

        # 视频的帧数
        self.n_frames = int(self.cap.get(cv.CAP_PROP_FRAME_COUNT))
        # 视频的时长
        self.dur = self.n_frames / self.fps

        return self.fps, self.n_frames, self.dur

    def split_by_interval(
            self,
            initial_extract_time,
            end_extract_time,
            extract_time_interval,
            jpg_quality):
        """

        :return:
        """
        self.initial_extract_time = initial_extract_time
        self.end_extract_time = end_extract_time
        self.extract_time_interval = extract_time_interval
        self.jpg_quality = jpg_quality

        self.video_output_path = os.path.dirname(self.pathIn)
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


# aaa = Video2Frames(r'F:\WP_Matlab\frames_11_120_5\IMG_4046.MOV')
# aaa.output_video_info()
# aaa.split_by_interval(10, 20, 2, 50)
