from importlib.metadata import entry_points
from setuptools import setup, find_packages

setup(
    name='propergitblame',
    packages=find_packages(),
    email='chuaqiwang@gmail.com',
    author='chua qi wang',
    install_requires=[
        'click',
        'matplotlib',
        'numpy',
        'numba'
    ],
    version='0.0.1',
    description='a better git blame',
    long_description=README,
    long_description_content_type='text/markdown',
    entry_points='''
    [console_scripts]
    propergitblame=propergitblame:propergitblame
    '''

)