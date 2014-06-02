#! /usr/bin/env python3

import json
from pyQt4 import QtGui

from animation import Animation


class Sprite:
    def __init__(self):
        self.animations = []
        self.texture = None

    @staticmethod
    def load(path):
        with open(path, 'r') as fd:
            conf = json.load(fd)
        sprite = conf['sprite']
        sprite = Sprite()
        sprite.name = sprite['name']
        sprite.texture = QtGui.Image(sprite['texture_path'])
        for anim_conf in sprite['animations']:
            sprite.animations.append(Animation.load(anim_conf, sprite.texture))
        return sprite

    def save(self, path):
        pass
