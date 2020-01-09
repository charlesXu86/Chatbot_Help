# -*- coding: utf-8 -*-

'''
@Author  :   Xu

@Software:   PyCharm

@File    :   setup.py

@Time    :   2019-12-30 11:22

@Desc    :

'''

from setuptools import setup, find_packages, Command, convert_path

def _version():
    ns = {}
    with open(convert_path("version.py"), "r") as fh:
        exec(fh.read(), ns)
    return ns['__version__']

__version = _version()

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(
    name="chatbot_help",
    version=__version,
    keywords='钉钉 机器人 dingtalk chatbot robot bot 微信机器人 qq机器人',
    description="An useful tool to help your chatbot to connect third platform, such as dingtalk, wetalk",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    author="Xu",
    author_email="charlesxu86@163.com",
    url="https://github.com/charlesXu86/Chatbot_Help",
    license="MIT Licence",
    python_requires='!=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, <4',
    packages=find_packages(),
    package_data={"": ["*.txt", "*.rst"]},
    install_requires=[],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
)
print("Welcome to Chatbot_Help")