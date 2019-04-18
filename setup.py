from setuptools import setup
import os

if os.environ.get('CI_COMMIT_TAG'):
    version = os.environ['CI_COMMIT_TAG']
else:
    version = os.environ['CI_JOB_ID']

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='knowbe4.py',
    version=version,
    description='A simple Python wrapper for the KnowBe4 API',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Josh Thomas',
    author_email='josh@joshuadavidthomas.com',
    url='https://github.com/elderlydoofus/knowbe4.py',
    install_requires=[
        'requests>=2.21.0',
        'python-dotenv>=0.10.1',
    ],
    tests_require=[
        'pytest',
        'vcrpy',
    ],
    license='LICENSE.md',
    packages=['kb4'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
