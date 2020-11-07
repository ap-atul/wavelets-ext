"""Discrete Wavelet and Inverse Transform implementation for Coiflet 1"""

cimport numpy as np
import numpy as np
cimport cython

@cython.boundscheck(False)
@cython.wraparound(False)
cpdef dwt(double[:] arrTime, int level):

    cdef np.ndarray decompositionLowFilter = np.array([
        -0.01565572813546454,
        -0.0727326195128539,
        0.38486484686420286,
        0.8525720202122554,
        0.3378976624578092,
        -0.0727326195128539,
    ])
    cdef np.ndarray decompositionHighFilter = np.array([
        0.0727326195128539,
        0.3378976624578092,
        -0.8525720202122554,
        0.38486484686420286,
        0.0727326195128539,
        -0.01565572813546454,
    ])

    cdef double[:] decompHF = decompositionHighFilter
    cdef double[:] decompLF = decompositionLowFilter

    cdef np.ndarray arrHilbert = np.zeros(level)
    cdef double[:] arrHilbert_view = arrHilbert

    # shrinking value 8 -> 4 -> 2
    cdef int a = level >> 1
    cdef int i
    cdef int j
    cdef int k
    cdef int motherWaveletLength = 6

    for i in range(a):
        for j in range(motherWaveletLength):
            k = (i << 1) + j

            # circulate the array if scale is higher
            while k >= level:
                k -= level

            # approx & detail coefficient
            arrHilbert_view[i] += arrTime[k] * decompLF[j]
            arrHilbert_view[i + a] += arrTime[k] * decompHF[j]

    return arrHilbert


@cython.boundscheck(False)
@cython.wraparound(False)
cpdef idwt(double[:] arrHilbert, int level):
    cdef np.ndarray reconstructionLowFilter = np.array([
        -0.0727326195128539,
        0.3378976624578092,
        0.8525720202122554,
        0.38486484686420286,
        -0.0727326195128539,
        -0.01565572813546454,
    ])
    cdef np.ndarray reconstructionHighFilter = np.array([
        -0.01565572813546454,
        0.0727326195128539,
        0.38486484686420286,
        -0.8525720202122554,
        0.3378976624578092,
        0.0727326195128539,
    ])

    cdef double[:] reconLF = reconstructionLowFilter
    cdef double[:] reconHF = reconstructionHighFilter

    cdef np.ndarray arrTime = np.zeros(level)
    cdef double[:] arrTime_view = arrTime

    # shrinking value 8 -> 4 -> 2
    cdef int a = level >> 1
    cdef int i
    cdef int j
    cdef int k
    cdef int motherWaveletLength = 6

    for i in range(a):
        for j in range(motherWaveletLength):
            k = (i << 1) + j

            # circulating the array if scale is higher
            while k >= level:
                k -= level

            # summing the approx & detail coefficient
            arrTime_view[k] += (arrHilbert[i] *  reconLF[j] +
                           arrHilbert[i + a] * reconHF[j])

    return arrTime
