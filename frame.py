#! /usr/bin/env python3


class Frame:
    def __init__(self, ):
        self.time = 0
        self.hitboxes = []
        self.__texture_crop = {'x': 0, 'y': 0, 'width': 0, 'height': 0}

    @classmethod
    def load(self, conf, texture):
        frame = Frame()
        frame.time = conf['time']
        frame.__texture_crop = {'x': conf['texture_crop_x'],
                                'y': conf['texture_crop_y'],
                                'width': conf['texture_crop_width'],
                                'height': conf['texture_crop_height']}
        frame.texture = texture.copy(frame.__texture_crop['x'],
                                     frame.__texture_crop['y'],
                                     frame.__texture_crop['width'],
                                     frame.__texture_crop['height'])
        frame.hitboxes = conf['hitboxes']
        return frame

    def save(self):
        pass
