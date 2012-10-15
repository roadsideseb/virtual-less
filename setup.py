#!/usr/bin/env python

import os
import shutil
import zipfile
from cStringIO import StringIO
from urllib2 import urlopen
from distutils.core import setup

current_dir = os.getcwd()

less_zip = urlopen("https://github.com/cloudhead/less.js/zipball/master")
less_dir = zipfile.ZipFile(StringIO(less_zip.read()))

for entry in less_dir.namelist():
    root_dir, __ = entry.split('/', 1)
    break

less_dir.extractall()

scripts = []
data_files = []

lib_dir = os.path.join(root_dir, 'lib')
bin_dir = os.path.join(root_dir, 'bin')

for info in less_dir.infolist():
    if info.filename.startswith(lib_dir) and info.filename.endswith('.js'):
        path = '/'.join(info.filename.split('/')[1:-1])
        data_files.append((path, [info.filename]))

    elif info.filename.startswith(bin_dir) and os.path.isfile(info.filename):
        scripts.append(info.filename)

setup(
    name='virtual-less',
    version='0.0.1a',
    description='Install lessc into your virtualenv',
    author='Sebastian Vetter',
    author_email='sebastian@roadside-developer.com',
    url='http://github.com/elbaschid/virtual-less',
    long_description=open('README.rst', 'r').read(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Programming Language :: JavaScript',
        'Topic :: Software Development :: Libraries',
    ],
    license='BSD',
    scripts=scripts,
    data_files=data_files,
)

# remove extracted files
shutil.rmtree(root_dir)
