import pathlib
from setuptools import setup
WD = pathlib.Path(__file__).parent
README = (WD / "README.md").read_text()
setup(
    name="excel_fast_load",
    version="1.0.0",
    description="Alternate, faster version of pandas.read_excel by Felix Kling",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/ScienceForChange/excel_fast_load",
    author="Felix Kling",
    author_email="felix@felix-kling.de",
    license="None",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Development Status :: 4 - Beta"
    ],
    packages=["excel_fast_load"],
    package_dir={'excel_fast_load': '.'},
    include_package_data=True,
    install_requires=["pandas", "numpy"],
)
