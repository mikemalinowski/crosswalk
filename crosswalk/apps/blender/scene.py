import os
import bpy


def name():
    return ".".join(os.path.basename(path()).split(".")[:-1])


def path():
    return bpy.data.filepath


def save():
    return bpy.ops.wm.save_mainfile()


def save_as(filepath):
    return bpy.ops.wm.save_as_mainfile(filepath=filepath)


def open(filepath, force=False):
    return bpy.ops.wm.open_mainfile(filepath=filepath)
