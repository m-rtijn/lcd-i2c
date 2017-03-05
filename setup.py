from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='lcd_i2c_raspberrypi',
    version='1.1',
    description='A module to easily use a simple LCD with an i2c backpack with a raspberry pi',
    classifiers=[
        'Topic :: Software Development :: Libraries',
    ],
    keywords='raspberry pi raspberrypi LCD i2c',
    url='https://github.com/Tijndagamer/lcd-i2c',
    author='MrTijn/Tijndagamer',
    author_email='mrtijn@riseup.net',
    license='GPLv3',
    packages=['lcd_i2c'],
    install_requires=[
        'smbus',
    ],
    scripts=['bin/lcd-i2c-example'],
    zip_safe=False)
