import os.path
import setuptools


with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as f:
    readme = f.read()


setuptools.setup(
    name='pep567',
    version="0.1.0",
    description='PEP 567 Backport',
    long_description=readme,
    author='MagicStack Inc',
    author_email='hello@magic.io',
    packages=['pep567'],
    provides=['pep567'],
    license='Apache License, Version 2.0',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Operating System :: POSIX',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'License :: OSI Approved :: Apache Software License',
        'Intended Audience :: Developers',
    ],
    include_package_data=True,
    test_suite='tests.suite',
)
