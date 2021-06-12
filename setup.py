import os
from setuptools import setup


def get_install_requirements():
    with open(os.path.join(os.path.dirname(__file__), 'requirements.txt')) as f:
        return [line for line in map(str.strip, f) if line and not line.startswith('-')]


setup(
    name='twilight',
    version='0.0.0',
    description='A no code tool to quickly understand text-based document and it provides an intuitive UI to explore insights from text.',
    author='Sahoo Subranjit , Khan Aquib Javed',
    author_email='subhranjit93@gmail.com, aquib_marwan@protonmail.com',
    python_requires='==3.6.*',
    install_requires=get_install_requirements(),
    classifiers=[
        "Programming Language :: Python",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: Apache License",
        "Topic :: Scientific/Engineering",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Operating System :: MacOS",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.8",
    ],
)