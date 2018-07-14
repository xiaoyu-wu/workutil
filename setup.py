from setuptools import setup
setup(
    name = 'workutil',
    version = '0.1.0',
    packages = ['workutil'],
    entry_points = {
        'console_scripts': [
            'workutil = workutil.__main__:main'
        ]
    })
