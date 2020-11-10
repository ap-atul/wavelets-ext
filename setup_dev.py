from distutils.core import setup

import numpy
from Cython.Build import cythonize

# compiling the cython files, no install
setup(
    name="wavelet",
    version='0.0.2',
    author='AP-Atul',
    author_email='atulpatare99@gmail.com',
    packages=['wavelet/',
              'wavelet/exceptions',
              'wavelet/extension',
              'wavelet/util',
              'wavelet/wavelets/',
              'wavelet/compression'],
    ext_modules=cythonize(["./wavelet/extension/wavelet_transform.pyx",
                           "./wavelet/extension/base_transform.pyx"]),
    include_dirs=[numpy.get_include()],
    zip_safe=False,
    url='https://github.com/AP-Atul/Wavelets',
    long_description=open('README.md').read(),
)
