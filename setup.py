import setuptools

# Read the long description:
with open("README.md", mode="r") as FILE_HANDLER:
    LONG_DESCRIPTION = FILE_HANDLER.read()

# Keywords:
TAGS = [
    "utilities",
    "enhancements",
    "lowercase",
    "booleans",
    "keywords",
    "values",
    "errors"
]

# Classifiers:
CLASSIFIERS = [
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: Implementation :: PyPy",
    "License :: OSI Approved :: MIT License",
    "Operating System :: Microsoft",
    "Operating System :: Microsoft :: Windows :: Windows 10",
    "Operating System :: Microsoft :: Windows :: Windows 8",
    "Operating System :: Microsoft :: Windows :: Windows 8.1",
    "Operating System :: Microsoft :: Windows :: Windows 7",
    "Operating System :: MacOS",
    "Operating System :: MacOS :: MacOS X",
    "Operating System :: POSIX :: Linux",
    "Operating System :: Other OS",
    "Operating System :: OS Independent",
    "Intended Audience :: Developers",
    "Intended Audience :: End Users/Desktop",
    "Topic :: Software Development :: Libraries",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Utilities",
    "Topic :: System",
    "Topic :: Terminals",
    "Development Status :: 5 - Production/Stable",
    "Framework :: IDLE",
    "Natural Language :: English"
]

# GitHub URL:
MainURL = "https://github.com/RDIL/lcpy"

# Other Project URLs:
URLs = \
    {
        "Bug Tracker": "https://github.com/RDIL/lcpy/issues",
        "Source Code": "https://github.com/RDIL/lcpy/",
        "License": "https://github.com/RDIL/lcpy/blob/master/LICENSE",
        "Documentation": "https://docs.rdil.rocks/lcpy"
    }


setuptools.setup(
    name="lc-py",
    version="2.0.0",
    author="Reece Dunham",
    author_email="me@rdil.rocks",
    description="Lowercase values for Python!",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url=MainURL,
    license="MIT",
    packages=setuptools.find_packages(),
    classifiers=CLASSIFIERS,
    project_urls=URLs,
    keywords=TAGS,
    include_package_data=True,
    zip_safe=False
)
