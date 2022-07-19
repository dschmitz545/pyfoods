from setuptools import find_packages, setup


def read(filename):
    return [req.strip() for req in open(filename).readlines()]


setup(
    name="pyfoods",
    version="0.2.0",
    packages=find_packages(),
    include_package_data=True,
    author="Diego Schmitz",
    author_email="diego@dschmitz.dev",
    install_requires=read("requirements.txt"),
    description="A delivery food app",
    long_description=read("README.md"),
    extras_require={"dev": read("requirements-dev.txt")},
    python_requires=">=3.7",
    classifiers=[
        "Framework :: Flask",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ]
)
