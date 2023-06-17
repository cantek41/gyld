

# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
import cv2


class ObjectDetection(ABC):
    """Abstract Base ObjectDetection classes that is inherited to all classes"""
    @abstractmethod
    def __init__(self, request):
        self.request = request

    @abstractmethod
    def run(self):
        return []

    def convert_to_RGB(self,img):
        return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    @abstractmethod
    def detection(self):
        return str

    @abstractmethod
    def build_model(self):
        return str

    @abstractmethod
    def roi(self):
        return str