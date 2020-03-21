from setuptools import setup, find_packages

setup(
    name='pydevd-odoo',
    version='0.1',
    description='PyDev.Debugger plugin for Odoo',
    url='https://github.com/trinhanhngoc/pydevd-odoo',
    author='Trinh Anh Ngoc',
    author_email='atw1990@gmail.com',
    packages=find_packages(),
    license='MIT',
    long_description=open('README.md').read(),
)