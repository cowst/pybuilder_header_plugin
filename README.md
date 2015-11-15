PyBuilder Header Plugin [![Build Status](https://travis-ci.org/cowst/pybuilder_header_plugin.svg?branch=master)](https://travis-ci.org/cowst/pybuilder_header_plugin)
=======================

Ensures that all your source files contain the same file header.

How to use pybuilder_header_plugin
----------------------------------

Add plugin dependency to your `build.py`
```python
use_plugin('pypi:pybuilder_header_plugin')
```

Configure the plugin within your `init` function:
```python
@init
def init(project):
    project.set_property('pybuilder_header_plugin_break_build', True)
    project.set_property('pybuilder_header_plugin_expected_header', "# Copyright\n")
    project.set_property('pybuilder_header_plugin_exclude_patterns', ['src/main/python/thirdparty/', 'src/main/python/another_file.py'])
```

This will break the build if one of your source files does not start with the comment line `# Copyright`.

It will also ignore files within the exclusion pattern.
