import setuptools
from pathlib import Path
from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()


def get_requirements():
    """Build the requirements list for this project"""
    requirements_list = []

    with Path("requirements.txt").open() as reqs:
        for install in reqs:
            if install.startswith("#"):
                continue
            requirements_list.append(install.strip())

    return requirements_list


def get_packages_requirements():
    """Build the package & requirements list for this project"""
    reqs = get_requirements()

    exclude = ["tests*"]
    packs = find_packages(exclude=exclude)

    return packs, reqs


def get_setup_kwargs():
    packages, requirements = get_packages_requirements()

    kwargs = dict(
        name="textoria",
        version="0.0.1",
        author="lor3m",
        author_email="hiddenlorem@pm.me",
        license="MIT License",
        description="Textoria API Client for Python",
        long_description=long_description,
        long_description_content_type="text/markdown",
        project_urls={
            "Source Code": "https://github.com/textoria/textoria-python",
        },
        packages=setuptools.find_packages(),
        classifiers=[
            "Programming Language :: Python",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: 3.11",
            "Intended Audience :: Developers",
            "Operating System :: OS Independent",
            "Topic :: Software Development :: Libraries :: Python Modules",
            "Topic :: Internet"
        ],
        python_requires='>=3.8',
        py_modules=["textoria"],
        install_requires=requirements,
        include_package_data=True
    )
    return kwargs


def main():
    setup(**get_setup_kwargs())


if __name__ == "__main__":
    main()
