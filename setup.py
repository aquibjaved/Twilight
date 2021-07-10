import os
import io
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

with io.open(os.path.join(here, "README.md")) as f:
    README = "\n" + f.read()

# Load requirements file
with open(os.path.join(here, "requirements.txt")) as f:
    INSTALL_PACKAGES = f.read().splitlines()

setup(
    name='twilight-nlp',
    url='https://github.com/aquibjaved/Twilight',
    version='0.1.1',
    description='A no code tool to quickly understand text-based document and it provides an intuitive UI to explore insights from text.',
    author='Sahoo Subranjit , Khan Aquib Javed',
    author_email='subhranjit93@gmail.com, aquib_marwan@protonmail.com',
    python_requires='>=3.6.*',
    install_requires=INSTALL_PACKAGES,
    long_description=README,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Scientific/Engineering",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Operating System :: MacOS",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)