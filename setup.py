import setuptools

# long_desc = "https://github.com/lepotatoguy/bracu-cgpa-module"
with open("README.md", "r") as fh:
    long_desc = fh.read()

setuptools.setup(
    name="bracu_cgpa_calc",
    version="1.0.3",
    author="Joyanta J. Mondal",
    author_email="hello@joyantamondal.com",
    description="A CGPA calculator module made for BracU Students.",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    url="https://github.com/lepotatoguy/bracu-cgpa-module",
    keywords=['bracu cgpa calculator', 'cg calculator bracu', 'bracu cg'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    py_modules=['bracu_cgpa_calc'],
    install_requires=['XlsxWriter','pandas'], 
    python_requires=">=3.0",
)
