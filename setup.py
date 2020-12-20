import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="FaceFocus-aahouzi",
    version="0.0.2.1",
    author="Anas Ahouzi",
    author_email="ahouzi2000@hotmail.fr",
    description="Generates high resolution face images from low resolution ones",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # url="https://github.com/aahouzi/Simple_Document_Classification_From_Scratch.git",
    packages=setuptools.find_packages(),
    classifiers=["Programming Language :: Python :: 3",
                 "License :: OSI Approved :: MIT License",
                 "Operating System :: OS Independent"],
    python_requires='>=3.6'
)