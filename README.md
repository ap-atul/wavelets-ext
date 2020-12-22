# Wavelets-Extension
A re-implementation of Wavelets package using Cython to improve the speed. 

All the functions are similar to the main Wavelets repository. The sole purpose of this project is to 
be used in audio de-noising of sound files. 

## Building
* Clone the repo
* Run the setup to generate the shared object/ dll files
```
$ python setup_dev.py build_ext --inplace
```
* Just like other api calls

## API
* I only needed the Compressors and the wavelet decomposition and reconstruction
* For other implementations you can use the main repo or help me port the code!
