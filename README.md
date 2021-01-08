# Wavelets-Extension
A re-implementation of Wavelets package using Cython to improve the speed. 

All the functions are similar to the main Wavelets repository. The sole purpose of this project is to 
be used in audio de-noising of sound files. 

[ref wavelet](https://github.com/AP-Atul/wavelets)

## Building
1. Install directly via pip
```console
pip install git+https://github.com/AP-Atul/wavelets-ext.git
```

2. Clone the repo and run the setup
```console
git clone https://github.com/AP-Atul/wavelets-ext.git
python setup.py build_ext --inplace
```
