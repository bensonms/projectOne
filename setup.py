from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="projectone",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A Python project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/projectOne",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
