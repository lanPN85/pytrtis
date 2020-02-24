import os

from setuptools import setup, find_packages

setup(
    name='pytrtis',
    description='Generated Python code for NVIDIA TensorRT Inference Server gRPC',
    version='0.1.0',
    url='',
    author='lanpn',
    author_email='lanpn@vdsense.com',
    classifiers=[
        'Programming Language :: Python :: 3.5'
    ],
    package_dir={'pytrtis': 'pytrtis'},
    packages=find_packages(exclude='tests'),
    python_requires='>=3.5, <4',
    install_requires=[
        'grpcio-tools', 'grpclib'
    ]
)
