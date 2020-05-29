#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
rid
~~~~~~~~~~~

"The Regressive Imagery Dictionary (RID) is a coding scheme for text analysis
that is designed to measure 'primordial' and conceptual content. Primordial
thought is the kind of free-form, associative thinking involved in fantasy
and dreams. Like Freud's id, I guess. Conceptual (or secondary) thought is
logical, reality-based and focused on problem solving."

via: John Wiseman (http://lemonodor.com/archives/001511.html)

"""

from setuptools import setup, find_packages

setup(
    name="regressive-imagery-dictionary",
    version="0.2.0",
    url="https://github.com/jefftriplett/rid.py",
    license="MIT",
    description='The Regressive Imagery Dictionary (RID) is a coding scheme for text analysis that is designed to measure "primordial" and conceptual content.',
    long_description=__doc__,
    maintainer="Jeff Triplett",
    maintainer_email="jeff.triplett@gmail.com",
    packages=find_packages(),
    package_data={},
    py_modules=["rid"],
    entry_points={"console_scripts": ["rid = rid:main",]},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: Public Domain",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Utilities",
    ],
)
