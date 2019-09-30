import os

from setuptools import find_packages, setup


with open(os.path.join(os.path.dirname(__file__), "README.rst")) as readme:
    long_description = readme.read()

classifiers = [
    "Development Status :: 6 - Mature",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: Implementation :: CPython",
]

setup(
    name="composition",
    url="https://github.com/Julian/composition",

    description="What You Crave",
    long_description=long_description,

    author="Julian Berman",
    author_email="Julian+ButDontSendMeEmailsAboutThisOne@GrayVines.com",

    py_modules=["composition"],

    install_requires=["forbiddenfruit!=0.1.3"],

    version="867530.9",
    classifiers=classifiers,
)
