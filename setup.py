from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='uwseds-group-zero',

    version='1.0',

    description='an object detection project for UW CSE583 17Au',
    long_description=long_description,

    url='https://github.com/UWSEDS-aut17/uwseds-group-zero',

    author='Li Junlin, Li Tianqi, Nan Qiao, Dizhi Ma, Xiaohan Wang',
    author_email='{jlli0410, tqli3, nqiao, dizhim, xhwang}@uw.edu',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3.5',
    ],

    keywords='object detection',

    packages=find_packages(),

    install_requires=['tensorflow', 'tkinter', 'Pillow', 'opencv-python'],

    python_requires='>=3.5, !=3.6.*, <4',

)