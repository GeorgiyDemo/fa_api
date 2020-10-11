from setuptools import setup
from os import path

curr_dir = path.abspath(path.dirname(__file__))
with open(path.join(curr_dir, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="fa_api",
    version="1.0",
    author="Georgiy Demenchuk",
    author_email="demenchuk.george@protonmail.com",
    license="GPLv3",
    url="https://github.com/GeorgiyDemo/fa_api",
    keywords="python api wrapper ruz fa-university faru",
    description="API wrapper for ruz.fa.ru",
    packages=["fa_api"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=["requests==2.23.0",],
)
