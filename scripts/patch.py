#!/usr/bin/env python3
"""
patch.py
Copyright 2020 Henrik Böving

Patch all the SVDs mentioned in a certain directory

Usage: python3 scripts/patch.py devices/
"""

import subprocess
from os import listdir
from os.path import isfile, join
import argparse
import os

def main(device_path):
    device_files = [f for f in listdir(device_path) if isfile(join(device_path, f))]
    [subprocess.Popen(["svd", "patch", f"{device_path}/{f}"]) for f in device_files]

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("devices", help="Path to device YAML files")
    args = parser.parse_args()
    main(args.devices)
