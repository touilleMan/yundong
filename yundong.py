#! /usr/bin/env python3

import sys
from PySide import QtGui, QtCore
import argparse

from mainwindow import Ui_MainWindow
from sprite import Sprite


def build_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("infile", type=argparse.FileType('r'),
                        help="yundong file", nargs='?')
    parser.add_argument("--verbose", "-v", help="increase verbosity",
                        action="store_true")
    return parser.parse_args()


class ControlMainWindow(QtGui.QMainWindow):

    def __init__(self, parent=None):
        super(ControlMainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionNew.triggered.connect(self.new)
        self.ui.actionOpen.triggered.connect(self.open)
        self.ui.actionSave.triggered.connect(self.save)

        def next_frame():
            self.change_frame(1)
        self.ui.button_next.clicked.connect(next_frame)

        def previous_frame():
            self.change_frame(-1)
        self.ui.button_previous.clicked.connect(previous_frame)

        self.tree_view_model = None
        self.ui.tree_view.clicked[QtCore.QModelIndex].connect(self.select_anim)
        self.sprite = None
        self.selected_animation = None
        self.current_frame = 0
        if ARGS.infile:
            self.load_yd(ARGS.infile.name)

    def new(self):
        pass

    def open(self):
        file_name, attr = QtGui.QFileDialog.getOpenFileName(self, 'Open file')
        try:
            self.load_yd(file_name)
        except Exception as e:
            QtGui.QMessageBox.warning(self, "Error",
                                      "Cannot load file {} ({})".format(file_name, e))
            if ARGS.verbose:
                raise

    def load_yd(self, file_name):
        self.sprite = Sprite(file_name)
        self.ui.widget_frame.setImage(self.sprite.texture)
        self.tree_view_model = QtGui.QStandardItemModel()
        parent_item = self.tree_view_model.invisibleRootItem()
        sprite_item = QtGui.QStandardItem(self.sprite.name)
        parent_item.appendRow(sprite_item)
        for anim in self.sprite.animations:
            sprite_item.appendRow(QtGui.QStandardItem(anim))
        self.ui.tree_view.setModel(self.tree_view_model)

    def select_anim(self, index):
        item = self.tree_view_model.itemFromIndex(index)
        if item.parent():
            # Item is an animation
            self.selected_animation = self.sprite.animations[item.text()]
            self.current_frame = 0
            self.ui.widget_frame.setImage(
                self.selected_animation.frames[0].texture)
        else:
            # Item is the top level sprite
            self.ui.widget_frame.setImage(self.sprite.texture)

    def change_frame(self, offset=1):
        if self.selected_animation:
            self.current_frame = (self.current_frame + offset) % len(
                self.selected_animation.frames)
            # Item is an animation
            self.ui.widget_frame.setImage(
                self.selected_animation.frames[self.current_frame].texture)

    def save(self):
        self.sprite.save()


if __name__ == "__main__":
    ARGS = build_args()
    app = QtGui.QApplication(sys.argv)
    mySW = ControlMainWindow()
    mySW.show()
    sys.exit(app.exec_())
