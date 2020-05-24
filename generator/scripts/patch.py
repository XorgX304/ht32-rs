#!/usr/bin/env python3
"""
patch.py
Copyright 2020 Henrik Böving

Patch all the SVDs mentioned in a certain directory

Usage: python3 scripts/patch.py devices/
"""

from os import listdir
from os.path import isfile, join
import argparse
import os
import svdtools
from pathlib import Path
from loguru import logger

def patch_files(device_path: Path):
    device_files = [f for f in device_path.iterdir() if f.is_file()]
    for path in device_files:
        logger.debug("patching {}...", path)
        svdtools.patch.main(f"{path.absolute()}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("devices", help="Path to device YAML files")
    args = parser.parse_args()
    patch_files(Path(args.devices))
