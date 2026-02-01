import os
from pymxs import runtime as rt


def name():
    return rt.maxFileName


def path():
    return os.path.join(
        rt.maxFilePath,
        rt.maxFileName,
    )


def save():
    return rt.saveMaxFile()


def save_as(filepath):
    return rt.saveMaxFile(filepath)


def open(filepath, force=False):
    return rt.loadMaxFile(
        filepath,
        quiet=force,
    )
