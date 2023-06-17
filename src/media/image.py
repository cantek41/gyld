# -*- coding: utf-8 -*-

import cv2
import base64
import numpy as np



class Image:
    @staticmethod
    def get_images(data):
        pass

    @staticmethod
    def get_uID(data,name):
        for img in data:
            if img.name==name:
                return img.uID


    @staticmethod
    def encode64(image,mime_type):
        mime_type=mime_type.split("/")
        bin = cv2.imencode("."+str(mime_type[1]), image)[1]
        data = str(base64.b64encode(bin), "utf-8")
        return data

    @staticmethod
    def decode64(image_data):
        b64_decoded_img = base64.b64decode(image_data)
        image = np.asarray(bytearray(b64_decoded_img), dtype=np.uint8)
        img = cv2.imdecode(image, cv2.IMREAD_COLOR)
        return img
