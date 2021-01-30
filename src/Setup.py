from setuptools import (setup,
                        find_packages)

setup(name='runnings',
      version='0.0.1',
      author='Antonio Felton',
      packages=find_packages(
          include=["src", "src.*", ]),
      install_requires=["pandas",
                        "Pillow",
                        "cycler",
                        "et-xmlfile",
                        "jdcal",
                        "kiwisolver",
                        "matplotlib",
                        "numpy",
                        "openpyxl",
                        "pandas",
                        "pip",
                        "pyparsing",
                        "python-dateutil",
                        "pytz",
                        "setuptools",
                        "six",
                        "xlrd"])
