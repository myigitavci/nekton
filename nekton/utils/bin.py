#!/bin/sh
import subprocess
import os

from os.path import abspath
from os.path import dirname as d

parent_dir = f"{d(d(abspath(__file__)))}"
PATH_TO_BIN = os.path.join(parent_dir, "bins/dcm2nii")


def make_exec_bin():
    """makes the binary executable on host PC"""
    process = subprocess.Popen(
        ["chmod", "+x", PATH_TO_BIN],
        stdout=subprocess.PIPE,
        universal_newlines=True,
    )
    process.communicate()


def run_bin(path: str, outpath:str = None,ignore_flag:bool = False):
    """run the binary on a given directory

    Args:
        path ([str]): directory where dicom exists
    """
    if outpath is None and ignore_flag is False:
        process = subprocess.Popen(
            [PATH_TO_BIN, "-z", "y", path],
            stdout=subprocess.PIPE,
            universal_newlines=True,
        )
    elif outpath is None and ignore_flag is True:
        process = subprocess.Popen(
            [PATH_TO_BIN, "-z", "y","-i","y", path],
            stdout=subprocess.PIPE,
            universal_newlines=True,
        )
    elif outpath is not None and ignore_flag is False:
        process = subprocess.Popen(
            [PATH_TO_BIN, "-z", "y","-o", outpath, path],
            stdout=subprocess.PIPE,
            universal_newlines=True,
        )
    else:
        process = subprocess.Popen(
            [PATH_TO_BIN, "-z", "y","-i","y","-o", outpath, path],
            stdout=subprocess.PIPE,
            universal_newlines=True,
        )
    process.communicate()
