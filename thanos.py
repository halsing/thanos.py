#!/usr/bin/python3

"""
Module contain thanos.py main functionality like:
    - checking dirnames
    - walk through directries for collecting all files
    - remove randomly half of the files
"""

import os
import random
import sys
import time

from typing import List

ListStrType = List[str]


class ThanosGlove:
    """
    Class contains functionality of Thanos.py
    """

    @staticmethod
    def check_dirname(dir_path: str) -> bool:
        """
        Method check if path is path of directory, not a file
        """
        return os.path.isdir(dir_path)

    @staticmethod
    def list_of_files(dirname: str) -> ListStrType:
        """
        Return list of files in directory and every subdirectories
        """
        filenames = []

        for root, dirs, files in os.walk(dirname):
            for current_file in files:
                full_path = os.path.join(root, current_file)
                filenames.append(full_path)

        return filenames

    @staticmethod
    def remove_files(list_of_files: ListStrType) -> int:
        """Function remove random pernamently files from the list_of_files"""

        list_length = len(list_of_files)

        for n_time in range(round(list_length / 2)):
            del_file = random.choice(list_of_files)
            os.remove(del_file)
            list_of_files.remove(del_file)
        return len(list_of_files)
