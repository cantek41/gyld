# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod


class Capsule(ABC):
    """Abstract Base Capsule classes that is inherited to all classes"""
    @abstractmethod
    def __init__(self, request):
        self.request = request

    @abstractmethod
    def run(self):
        return []

