# -*- coding: utf-8 -*-

'''
@Author  :   Xu

@Software:   PyCharm

@File    :   setup.py

@Time    :   2019-12-30 11:22

@Desc    :

'''

import io
import os
import sys
from shutil import rmtree
from setuptools import setup, find_packages, Command, convert_path

about = {}
here = os.path.abspath(os.path.dirname(__file__))

with io.open(os.path.join(here, 'dingtalkchatbot', '__about__.py'), encoding='utf-8') as f:
    exec(f.read(), about)

with io.open("README.rst", encoding='utf-8') as f:
    long_description = f.read()

install_requires = ["requests"]

def _version():
    ns = {}
    with open(convert_path("version.py"), "r") as fh:
        exec(fh.read(), ns)
    return ns['__version__']



setup(
    name=about['__title__'],
    version=about['__version__'],
    packages=find_packages(),
    description=about['__description__'],
    long_description=long_description,
    author=about['__author__'],
    author_email=about['__author_email__'],
    url=about['__url__'],
    license=about['__license__'],
    python_requires='!=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, <4',
    keywords='钉钉 机器人 dingtalk chatbot robot bot',
    install_requires=install_requires,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    # python setup.py upload
    cmdclass={
        'upload': UploadCommand
    }
)
