# setup.py
from setuptools import setup, find_packages

setup(
    name="math_quiz",
    version="0.1",
    packages=find_packages(),
    description="A simple Python math quiz game",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Mahmoud Elboghdady",
    author_email="mahmoud.m.elboghdady@gmail.com",
    url="https://github.com/M-Elboghdady/DSSS_Homeworks",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "math_quiz=math_quiz.math_quiz:math_quiz"
        ]
    },
)
