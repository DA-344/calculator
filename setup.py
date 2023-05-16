from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name = "calculator",
    version = "2.0.0",
    description = "A complex-made-like calculator with multiple functions.",
    long_description=long_description,
    url = "https://github.com/Developer-Anony/calculator",
    author= "Developer Anonymous",
    classifiers=[
        "Velopment Status :: 3 - Prerelease",
        "Topic :: Helper :: Tools",
        "Programming Language ::Python :: 3.x"
    ],
    keywords="tools",

    packages= find_packages(where="src")
)