import io
import setuptools


with io.open("README.rst", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="VarCas-OFFinder",
    version="0.1.0",
    author="Abyot Melkamu",
    author_email="abyot@pusan.ac.kr",
    description="VarCas-OFFinder",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pnucolab/rgen-toolkit",
    packages=setuptools.find_packages(),
)
