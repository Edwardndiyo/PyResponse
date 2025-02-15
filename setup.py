from setuptools import setup, find_packages

setup(
    name="pyresponse",  
    version="0.1.0",  
    author="Edward Ndiyo",  
    author_email="NdiyoEdward@gmail.com",  
    description="A simple Python package for standardized API responses.",  
    long_description=open("README.md").read(),  
    long_description_content_type="text/markdown",  
    url="https://github.com/Edwardndiyo/PyResponse",  
    packages=find_packages(),  
    install_requires=[
        "fastapi",
        "flask",
        "pydantic",
        "typing-extensions"
    ],  
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
