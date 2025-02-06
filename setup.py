from setuptools import setup, find_packages

setup(
    name="custom_logger",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pygame",
    ],
    package_data={
        'custom_logger': ['media/error.mp3'],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="A custom logging library with colored output and sound effects",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/custom_logger",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)