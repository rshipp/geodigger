import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

requirements = open(os.path.join(os.path.dirname(__file__),
            'requirements.txt')).read()
requires = requirements.strip().split('\n')

setup(
    name='geodigger',
    version='0.1',
    packages=['geodigger'],
    scripts=['tools/geodigger'],
    include_package_data=True,
    install_requires=requires,
    license='BSD New',
    description='Collect and filter location information from social network services.',
    long_description=README,
    url='https://github.com/rshipp/geodigger',
    author='Ryan Shipp',
    author_email='python@rshipp.com',
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: JavaScript',
        'Programming Language :: Unix Shell',
        'Topic :: Software Development :: Libraries',
        'Topic :: Communications :: Chat',
        'Topic :: Database',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: News/Diary',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
