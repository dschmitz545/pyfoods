from setuptools import find_packages, setup

def read(filename):
    return [
        req.strip()
        for req
        in open(filename).readlines()
    ]

setup(
    name="ElectrumFood",
    version="0.1.0",
    description="Um app de delivery",
    packages=find_packages(),
    include_package_data=True,
    author="Diego Schmitz",
    install_requires=read("requirements.txt"),
    extras_require={
        "dev": read("requirements-dev.txt")
    }
)