#! /usr/bin/env python3

from frame import Frame


class Animation:
    def __init__(self):
        self.name = None
        self.frames = []

    @staticmethod
    def load(conf, texture):
        animation = Animation()
        animation.name = conf['name']
        for frame_conf in conf['frames']:
            animation.frames.append(Frame.load(frame_conf, texture))

    def save(self):
        pass
