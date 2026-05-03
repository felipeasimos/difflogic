from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension, CppExtension
import torch
import os


def get_extensions():
    use_cuda = False

    if torch.cuda.is_available():
        use_cuda = True

    # Optional: also check CUDA_HOME / nvcc
    from torch.utils.cpp_extension import CUDA_HOME
    if CUDA_HOME is None:
        use_cuda = False

    if use_cuda:
        return [CUDAExtension('difflogic_cuda', [
            'difflogic/cuda/difflogic.cpp',
            'difflogic/cuda/difflogic_kernel.cu',
        ], extra_compile_args={'nvcc': ['-lineinfo']})],
    return []

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='difflogic',
    version='0.1.0',
    author='Felix Petersen',
    author_email='ads0600@felix-petersen.de',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Felix-Petersen/difflogic',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    package_dir={'difflogic': 'difflogic'},
    packages=['difflogic'],
    ext_modules=get_extensions(),
    cmdclass={'build_ext': BuildExtension},
    python_requires='>=3.6',
    install_requires=[
        'torch>=1.6.0',
        'numpy',
    ],
)
