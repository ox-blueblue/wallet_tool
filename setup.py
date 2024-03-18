import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wallet_tool",
    version="0.2",
    author="embzheng",
    author_email="embzheng@qq.com",
    description="This is a web3 wallet operation tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/embzheng/wallet_tool",
    packages=setuptools.find_packages(),
    install_requires=['playwright>=1.42.0'],    
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)