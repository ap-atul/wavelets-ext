from distutils.core import setup

import numpy
from Cython.Build import cythonize

# compiling the cython files, no install
setup(
    name="C test",
    ext_modules=cythonize(["./wavelet/extension/wavelet_transform.pyx",
                           "./wavelet/extension/base_transform.pyx"]),
    include_dirs=[numpy.get_include()],
    zip_safe=False
)
