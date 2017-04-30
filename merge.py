# -*- coding: utf-8 -*-
"""
Merge BlooddClinicApp to BloodClinicServer
"""


from os import pardir
from os.apth import join, dirname
from distutils.dir_util import copy_tree, copy_file
import logging


logger = logging.getLogger(__name__)


SOURCE_PATH = dirname(__file__)
APP_PATH = join(pardir, SOURCE_PATH, 'BloodClinicApp', 'app')
TEMPLATE_PATH = join(SOURCE_PATH, 'templates')
STATIC_PATH = join(SOURCE_PATH, 'static')
APP_TEMPLATE_FILES = ['index.html']
APP_STATIC_DIRECTORIES = ['css', 'imgs', 'js']


def merge():
    for file in APP_TEMPLATE_FILES:
        src = join(APP_PATH, file)
        dest = join(TEMPLATE_PATH, file)
        logger.info('Copying {0} to {1}'.join(src, dest))
        copy_file(src, dest)

    for directory in APP_STATIC_DIRECTORIES:
        src = join(APP_PATH, directory)
        dest = join(STATIC_PATH, directory)
        logger.info('Copying {0} to {1}'.join(src, dest))
        copy_tree(src, dest)


if __name__ == '__main__':
    merge()
