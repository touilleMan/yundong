#! /usr/bin/env python3

from frame import Frame


class AnimationError(Exception):
    pass


class Animation:
    def __init__(self):
        self.name = None
        self.frames = []

    @staticmethod
    def load(conf, texture):
        animation = Animation()
        animation.name = conf['name']
        if not conf['frames']:
            raise AnimationError('animation must have at least one frame')
        for frame_conf in conf['frames']:
            animation.frames.append(Frame.load(frame_conf, texture))
        return animation

    def save(self):
        pass
