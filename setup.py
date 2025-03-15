from setuptools import setup, find_packages

setup(
    name="custom_logger",
    version="0.1.0",
    packages=find_packages(exclude=['tests*']),
    install_requires=[
        "pygame",
		"python-dotenv",
    ],
    package_data={
        'custom_logger': ['media/error.mp3'],
    },
    author="Jebin Einstein",
    description="A custom logging library with colored output and sound effects",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/jebin2/custom_logger",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",  # Specify minimum Python version
)