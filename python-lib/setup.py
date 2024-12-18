from setuptools import setup, find_packages

setup(
    name='examplelibrary',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    description='Example library for Python',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)