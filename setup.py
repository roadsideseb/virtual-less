#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import json
import shutil
import zipfile

from urllib2 import urlopen
from setuptools import setup
from cStringIO import StringIO

BASE_URL = "https://github.com/less/less.js"
DEFAULT_VERSION = os.getenv('LESS_VERSION', '2.5.0')
PROJECT_DIR = os.environ.get('PROJECT_DIR')

# Force node version
# (https://github.com/elbaschid/virtual-node#install-specific-version-of-node)
os.environ["NODE_VERSION"] = "0.12.2"

def get_version():
    if not PROJECT_DIR:
        return DEFAULT_VERSION
    package_file = os.path.join(PROJECT_DIR, 'package.json')
    try:
        package_json = json.load(open(package_file))
    except (IOError, ValueError):
        print "cannot find custom node version in package.json, using default"
    else:
        version = package_json.get('dependencies', {}).get('less', '')
        if version.startswith('=='):
            return version.replace('==', '')
    return DEFAULT_VERSION

env_path = os.getenv('VIRTUAL_ENV')
less_zip = urlopen("%s/archive/v%s.zip" % (BASE_URL, get_version()))
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
        data_files.append((os.path.join(env_path, path), [info.filename]))

    elif info.filename.startswith(bin_dir) and os.path.isfile(info.filename):
        scripts.append(info.filename)

setup(
    name='virtual-less',
    version='0.0.2',
    description='Install lessc into your virtualenv',
    author='Sebastian Vetter',
    author_email='sebastian@roadside-developer.com',
    url='http://github.com/elbaschid/virtual-less',
    long_description="%s\n\n%s" % (open('README.rst').read(),
                                   open('CHANGELOG.rst').read()),
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
    install_requires=[
        'virtual-node>=0.1.0',
    ],
    license='BSD',
    scripts=scripts,
    data_files=data_files,
)

# remove extracted files
shutil.rmtree(root_dir)
