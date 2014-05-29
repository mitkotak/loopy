#!/usr/bin/env python
# -*- coding: latin1 -*-

from setuptools import setup

try:
    from distutils.command.build_py import build_py_2to3 as build_py
except ImportError:
    # 2.x
    from distutils.command.build_py import build_py

ver_dic = {}
version_file = open("loopy/version.py")
try:
    version_file_contents = version_file.read()
finally:
    version_file.close()

exec(compile(version_file_contents, "pyopencl/version.py", 'exec'), ver_dic)

setup(name="loo.py",
      version=ver_dic["VERSION_TEXT"],
      description="A code generator for array-based code on CPUs and GPUs",
      long_description=open("README.rst", "rt").read(),
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'Intended Audience :: Other Audience',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Programming Language :: Python',
          'Topic :: Scientific/Engineering',
          'Topic :: Scientific/Engineering :: Information Analysis',
          'Topic :: Scientific/Engineering :: Mathematics',
          'Topic :: Scientific/Engineering :: Visualization',
          'Topic :: Software Development :: Libraries',
          'Topic :: Utilities',
          ],

      install_requires=[
          "pytools>=2013.5.2",
          "pyopencl>=2013.1",
          "pymbolic>=2013.2",
          "cgen",
          "islpy>=2014.1"
          ],

      author="Andreas Kloeckner",
      url="http://mathema.tician.de/software/loopy",
      author_email="inform@tiker.net",
      license="MIT",
      packages=[
          "loopy",
          "loopy.codegen",
          "loopy.kernel",
          "loopy.library",
          ],

      # 2to3 invocation
      cmdclass={'build_py': build_py})
