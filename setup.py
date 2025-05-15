from setuptools import setup, find_packages


setup(
    name='taskcli',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'tabulate',
    ],
    entry_points={
        'console_scripts':[
            'taskcli = taskcli.main:main',
        ],
    },
)