from setuptools import setup

setup(
  name='knowbe4.py',
  version='0.0.1',
  description='A simple Python wrapper for the KnowBe4 API',
  author='Josh Thomas',
  author_email='josh@joshuadavidthomas.com',
  install_requires=[
    'requests>=2.21.0',
  ],
  tests_require=[
    'pytest',
    'python-dotenv',
    'vcrpy',
  ],
  license='LICENSE.md',
  packages=['kb4']
)