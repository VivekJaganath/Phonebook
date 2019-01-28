from setuptools import setup, find_packages

setup(
        name='pycontacts',
        description='Phone Book',
        author='Vivek ',
        packages=find_packages(),
        entry_points={
            'console_scripts': [
                'pycontacts = contacts.phonebook:main',
            ]
        },
        install_requires=[
            'pyyaml'
            'argparse',
        ]
      )