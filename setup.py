from setuptools import setup
import os

if os.environ.get('CI_COMMIT_TAG'):
    version = os.environ['CI_COMMIT_TAG']
else:
    version = os.environ['CI_JOB_ID']

with open("README.md", "r") as fh:
    long_description = fh.read()

packages = ['kb4']

requires = [
    'requests>=2.21.0',
]

test_requirements = [
    'pytest>=4.4.1',
    'pytest-cov',
    'python-dotenv>=0.10.1'
]

setup(
    name='knowbe4.py',
    version=version,
    description='A simple Python wrapper for the KnowBe4 API',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Josh Thomas',
    author_email='josh@joshuadavidthomas.com',
    url='https://github.com/elderlydoofus/knowbe4.py',
    install_requires=requires,
    tests_require=test_requirements,
    license='LICENSE.md',
    packages=packages,
    keywords=['knowbe4', 'knowbe4.py'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6'
    ],
)
