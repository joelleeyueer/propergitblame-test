from importlib.metadata import entry_points
from setuptools import setup, find_packages

setup(
    name='propergitblame',
    packages=find_packages(),
    email='chuaqiwang@gmail.com',
    author='wang',
    install_requires=[
        'click',
        'matplotlib',
        'numpy',
        'numba'
    ],
    version='0.0.1'
    entry_points='''
    [console_scripts]
    propergitblame=propergitblame:propergitblame
    '''
)