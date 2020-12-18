from setuptools import setup, find_packages
import pkg_resources

setup(
    name=pkg_resources.safe_name('blame-party'),
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['pyqt5', 'markdown', 'pytest'],
    author="Pete Smith",
    author_email="psmith at anagogical dot net",
    description='PyQt Structured Outliner and Kanban Board',
    license="Copyright 2020 P.F. Smith",
    zip_safe=False,
    entry_points={
        'gui_scripts': [
            'BlameParty=blame_party.gui:main',
        ],
    },
)
