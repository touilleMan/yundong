#! /usr/bin/env python3

import json
from PySide import QtGui

from animation import Animation
import os


class Sprite:

    def __init__(self, conf_path=None):
        self.animations = {}
        self.texture = None
        self.path = conf_path
        if conf_path:
            self.load(conf_path)

    def load(self, conf_path):
        dirname = os.path.dirname(conf_path)
        with open(conf_path, 'r') as fd:
            conf = json.load(fd)
            self.conf = conf['sprite']
            self.name = self.conf['name']
            self.texture = QtGui.QImage(
                dirname + '/' + self.conf['texture_path'])
            for anim_conf in self.conf['animations']:
                anim = Animation.load(anim_conf, self.texture)
                self.animations[anim.name] = anim

    def save(self, path):
        pass
        # conf = {'sprite': {
        #     'name': self.name,
        #     'texture_path': self.conf['texture_path'],
        #     'animations': self.animations.save()
        # }}
        # with open(conf_path, 'w') as fd:
        #     fd.write()
