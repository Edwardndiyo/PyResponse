from setuptools import setup, find_packages

setup(
    name="pyresponse-paradox",  
    version="0.2.0",  # Incremented version
    author="Edward Ndiyo",  
    author_email="NdiyoEdward@gmail.com",  
    description="A simple Python package for standardized API responses.",  
    long_description=open("README.md", encoding="utf-8").read(), 
    long_description_content_type="text/markdown",  
    url="https://github.com/Edwardndiyo/PyResponse",  
    packages=find_packages(),  
    install_requires=[
        "fastapi",
        "flask",
        "pydantic",
        "typing-extensions"
    ],  
    license="MIT",  # Explicitly defining the license
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
