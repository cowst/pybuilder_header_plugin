#   pybuilder_header_plugin
#   Copyright 2014 Michael Gruber
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import sys

sys.path.insert(0, 'src/main/python')

from pybuilder.core import Author, init, use_plugin
from pybuilder_header_plugin import check_source_file_headers

use_plugin('python.core')
use_plugin('python.distutils')
use_plugin('python.flake8')
use_plugin('python.install_dependencies')

use_plugin('pypi:pybuilder_release_plugin')

name = 'pybuilder_header_plugin'
version = '0.0.2'

authors = [Author('Michael Gruber', 'aelgru@gmail.com')]
url = 'https://github.com/aelgru/pybuilder_header_plugin'
description = 'Please visit {0} for more information!'.format(url)
license = 'Apache License, Version 2.0'
summary = 'PyBuilder Header Plugin'

default_task = ['analyze', 'publish', 'check_source_file_headers']


@init
def set_properties(project):
    project.depends_on('committer')
    project.depends_on('wheel')

    project.set_property('flake8_verbose_output', True)
    project.set_property('flake8_break_build', True)

    project.set_property('pybuilder_header_plugin_break_build', True)
    project.set_property('pybuilder_header_plugin_expected_header', open('header.py').read())

    project.get_property('distutils_commands').append('bdist_wheel')
    project.set_property('distutils_classifiers', [
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Utilities'])
