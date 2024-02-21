#!/usr/bin/env python

# --------------------------------------------------------------------------------------------
# Copyright (c) FoundationaLLM. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from codecs import open
from setuptools import setup, find_packages
import sys

try:
    from fllm_cli_bdist_wheel import cmdclass
except ImportError:
    from distutils import log as logger

    logger.warn("Wheel is not available, disabling bdist_wheel hook")
    cmdclass = {}

VERSION = "1.0.0b2"
# If we have source, validate that our version numbers match
# This should prevent uploading releases with mismatched versions.
try:
    with open('foundationallm/cli/__main__.py', 'r', encoding='utf-8') as f:
        content = f.read()
except OSError:
    pass
else:
    import re

    m = re.search(r'__version__\s*=\s*[\'"](.+?)[\'"]', content)
    if not m:
        print('Could not find __version__ in foundationallm/cli/__main__.py')
        sys.exit(1)
    if m.group(1) != VERSION:
        print('Expected __version__ = "{}"; found "{}"'.format(VERSION, m.group(1)))
        sys.exit(1)

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Intended Audience :: System Administrators',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
]

DEPENDENCIES = [
    "antlr4-python3-runtime~=4.13.1",
    'chardet~=3.0.4',
    'colorama~=0.4.4',
    # On Linux, the distribution (Ubuntu, Debian, etc) and version are checked for `fllm feedback`
    'distro; sys_platform == "linux"',
    'fabric~=2.4',
    'javaproperties~=0.5.1',
    'jsondiff~=2.0.0',
    'packaging>=20.9',
    'pycomposefile>=0.0.29',
    'PyGithub~=1.38',
    'PyNaCl~=1.5.0',
    'scp~=0.13.2',
    'semver==2.13.0',
    'six>=1.10.0',  # six is still used by countless extensions
    'sshtunnel~=0.1.4',
    'urllib3',
    'websocket-client~=1.3.1',
    'xmltodict~=0.12'
]

with open('README.rst', 'r', encoding='utf-8') as f:
    README = f.read()

setup(
    name='fllm-cli',
    version=VERSION,
    description='FoundationaLLM Command-Line Tools',
    long_description=README,
    license='MIT',
    author='FoundationaLLM',
    author_email='fllm@solliance.net',
    url='https://github.com/solliancenet/fllm-cli',
    zip_safe=False,
    classifiers=CLASSIFIERS,
    scripts=[
        'fllm',
        'fllm.completion.sh',
        'fllm.bat',
        'fllmps.ps1'
    ],
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    install_requires=DEPENDENCIES,
    python_requires='>=3.8.0',
    package_data={
        
    },
    cmdclass=cmdclass
)
