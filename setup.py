"""Setup Tensorflow TTS libarary."""

import os
import sys
from distutils.version import LooseVersion

import pip
from setuptools import find_packages, setup

if LooseVersion(sys.version) < LooseVersion("3.6"):
    raise RuntimeError(
        "Tensorflow TTS requires python >= 3.6, "
        "but your Python version is {}".format(sys.version)
    )

if LooseVersion(pip.__version__) < LooseVersion("19"):
    raise RuntimeError(
        "pip>=19.0.0 is required, but your pip version is {}. "
        'Try again after "pip install -U pip"'.format(pip.__version__)
    )

# TODO(@dathudeptrai) update console_scripts.
entry_points = {
    "console_scripts": [
        "tensorflow-tts-preprocess=tensorflow_tts.bin.preprocess:preprocess",
        "tensorflow-tts-compute-statistics=tensorflow_tts.bin.preprocess:compute_statistics",
        "tensorflow-tts-normalize=tensorflow_tts.bin.preprocess:normalize",
    ]
}

dirname = os.path.dirname(__file__)
setup(
    name="TensorFlowTTS",
    version="0.0",
    url="https://github.com/tensorspeech/TensorFlowTTS",
    author="Minh Nguyen Quan Anh, Eren Gölge, Kuan Chen, Dawid Kobus, Takuya Ebata, Trinh Le Quang, Yunchao He, Alejandro Miguel Velasquez",
    author_email="nguyenquananhminh@gmail.com",
    description="TensorFlowTTS: Real-Time State-of-the-art Speech Synthesis for Tensorflow 2",
    long_description=open(os.path.join(dirname, "README.md"), encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    license="Apache-2.0",
    packages=find_packages(include=["tensorflow_tts*"]),
    entry_points=entry_points,
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Intended Audience :: Science/Research",
        "Operating System :: POSIX :: Linux",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
