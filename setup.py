"""setup.py: setuptools control."""

import re
from setuptools import setup


version = re.search(
    r'(__version__ = "(\d\.\d(\.\d+)?)")',
    open("phdseeker/constants.py", encoding="utf8").read(),
    re.M
)[2]

setup(
    name="phdseeker",
    version=version,
    author="Amin Aghababaei, Javad Razavian",
    author_email="amin.aghababaei@outlook.com, javadr@gmail.com",
    maintainer='Javad Razavian',
    maintainer_email="javadr@gmail.com",
    packages=['phdseeker',],
    install_requires=[
        'rich',
        'http3',
        'httpx',
        'pandas',
        'docopt',
        'openpyxl',
        'brotlipy',
    ],
    python_requires=">=3.8",
    package_dir={'phdseeker': 'phdseeker'},
    description="PhD Seeker is a python web scraper to search for fully funded doctorate positions, advertised on well-known academic position websites.",
    license="GPLv3",
    keywords="Ph.D. Positions, phdseeker, Academia",
    url="https://github.com/Aghababaei/PhD-Seeker",
    entry_points={
        'console_scripts': [
            'phdseeker = phdseeker.phdseeker_cli:main',
        ],
    },
    long_description_content_type="text/markdown",
    long_description=open("README.md", encoding="utf8").read(),
)