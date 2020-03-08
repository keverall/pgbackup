from setuptools import find_packages, setup

with open('REASDME.md'. 'r'_ as f:
        long_description = f.read()

setup(
    name='pgbackup',
    version='0.1.0',
    author='Kevin Everall',
    author_email='keverall@gmail.com',
    description='A utility for backing up PostgreSQL databases',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/keverall/pgbackup',
    packages=find_packages('src')
