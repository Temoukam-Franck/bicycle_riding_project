from setuptools import setup, find_packages

setup(
    name="bicycle_riding",
    version="0.0.1",
    author="Franck Temoukam",
    packages=find_packages(where="./src"),
    package_dir={"","./src"},
    install_requires=["setuptools"]
)
