import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="todo_database",
    version="0.0.1",
    author="Roman Esin",
    author_email="esinromanswift@gmail.com",
    description="A todo database wrapper for DPL course",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/romanesin/todo_database",
    project_urls={},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
)
