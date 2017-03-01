""" Setup script for installing Alyn """

from setuptools import setup

setup(
    name="alyn",
    version="0.1.1",
    author="Kakul Chandra",
    description="Fix skew in images",
    author_email="kakulchandra911@gmail.com",
    url='https://github.com/kakul/Alyn.git',
    download_url='https://github.com',
    keywords=['image-processing', 'image-deskew', 'deskew', 'rotate', 'text'],
    packages=['alyn'],
    classifiers=[],
    license='MIT',
    install_requires=['numpy', 'scikit-image', 'scipy', 'matplotlib'])
