from setuptools import setup
import sys

requirements = ['numpy', 'scipy', 'matplotlib']

if sys.version_info < (3, 3):
    sys.stdout.write("At least Python 3.3 is required.\n")
    sys.exit(1)
elif sys.version_info < (3, 6):
    # typing was added in 3.5, and we rely on critical features that were
    # introduced in 3.5.2+, so for versions older than 3.6 we rely on
    # a backport
    requirements.append('backports.typing')

#import versioneer

setup(
    name='earthshine',
    version="0.1",
    #cmdclass="0.9", # Is this right???
    description='Tools for earthshine calculations.',
    url='https://github.com/mattbellis/earthshine',
    download_url='https://github.com/mattbellis/earthshine/archive/refs/heads/main.zip',
    author='Matt Bellis and Josephine Swann',
    author_email='mbellis@siena.edu',
    license='MIT',
    packages = ['earthshine'],
    install_requires = ['numpy','scipy', 'matplotlib'],
    #tests_require = ['pytest', 'pytest-cov'],
    classifiers=[ # HAVE TO FIX ALL THIS
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'License :: Public Domain',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.6',
    ],
)
