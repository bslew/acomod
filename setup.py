# from distutils.core import setup, Extension
from setuptools import setup
import os

import codecs
try:
    codecs.lookup('mbcs')
except LookupError:
    ascii = codecs.lookup('ascii')
    func = lambda name, enc=ascii: {True: enc}.get(name=='mbcs')
    codecs.register(func)
    
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()
os.environ["CC"] = "c++" 
os.environ["CXX"] = "c++"

# # Common flags for both release and debug builds.
# extra_compile_args = sysconfig.get_config_var('CFLAGS').split()
# extra_compile_args += ["-std=c++11", "-Wall", "-Wextra"]
# if _DEBUG:
#     extra_compile_args += ["-g3", "-O0", "-DDEBUG=%s" % _DEBUG_LEVEL, "-UNDEBUG"]
# else:
#     extra_compile_args += ["-DNDEBUG", "-O3"]
    
    
#     libraries=['CPEDS','Mscscore','Mscsfn','hdf5'],
# cpedsRotation = Extension(
#     'pyCPEDScommonFunctions/cpedsRotation',
#     sources=['pyCPEDScommonFunctions/cpedsRotation.cpp'],
#     include_dirs=['/usr/local/include/cpems', '/usr/lib64/python2.7/site-packages/numpy/core/include/numpy'],
#     library_dirs=['/usr/local/lib/cpems'],
#     libraries=['nova',  'gsl', 'gslcblas', 'm', 'proj', 
#                'QtCore', 'fftw3', 'fftw3l', 'hdf5', 'CGAL', 'gmp','cfitsio', 'CPEDS', 'Mscsfn', 
#                'Mscscore', 'Mscsplot', 'MscsWMAP', 'armadillo', 
#                'gsl', 'gslcblas', 'm', 'proj', 'QtCore', 'fftw3', 'ccSHT3', 'novas', 'velKB', 'slaRefr', 
#                'fftw3l', 'hdf5', 'CGAL', 'gmp', 'cfitsio', 'cpgplot', 'armadillo'],
#     language='C++',
#     )

reqired_packages=[
    'PyQt5',
    'numpy',
    'matplotlib',
    'sounddevice',
    'soundfile',
    'scipy',
    ]

setup(name='acomod',
      version='0.1.2',
      description='Acoustic Oscillations Viewer',
      long_description=read('README.md'),
      author='Bartosz Lew',
      author_email='bartosz.lew@protonmail.com',
      url='https://github.com/bslew/acomod',
      install_requires=reqired_packages,
      package_dir = {'': 'src'},
      packages = ['acomod',
                  ],
      entry_points={ 'gui_scripts': [ 'acoustic_mode_viewer = acomod.sonidist:main',
               ],
                    },
      package_data={'acomod': ['*.ui',
                               ]},
      eager_resources={'acomod': ['data/*.wav','data/*.WAV',
                               ]},
      classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License"
        ],
     )
