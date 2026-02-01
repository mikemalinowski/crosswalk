import os
from pyfbsdk import *


def name():
    return ".".join(os.path.basename(path()).split(".")[:-1])

def path():
    app = FBApplication()
    return app.FBXFileName


def save():
    save_as(path())


def save_as(filepath):
    app = FBApplication()
    app.FileSave(filepath)


def open(filepath, force=False):
    app = FBApplication()
    show_ui = not force
    app.FileOpen(filepath, show_ui)
    return
