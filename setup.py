""" Setup script for installing Alyn """

from distutils.core import setup

setup(
    name="alyn",
    version="0.1.0",
    author="Kakul Chandra",
    author_email="kakulchandra911@gmail.com",
    url='https://github.com/kakul/Alyn.git',
    download_url='https://github.com',
    keywords=['image-processing', 'image-deskew', 'deskew', 'rotate', 'text'],
    packages=['alyn'],
    install_requires=['numpy', 'matplotlib', 'scipy', 'scikit-image'],
    classifiers=[])
