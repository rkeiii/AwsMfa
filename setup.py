from setuptools import setup

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='aws-mfa-v2',
    version='0.2.0',
    description='Manage AWS MFA Security Credentials',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    author='Ron Ellis',
    author_email='rkeiii@protonmail.com',
    packages=['awsmfav2'],
    scripts=['aws-mfa'],
    entry_points={
        'console_scripts': [
            'aws-mfa=awsmfav2:invoke',
        ],
    },
    url='https://github.com/rkeiii/aws-mfa-v2',
    install_requires=['boto3', 'configparser', 'argparse'],
    extras_require={
        'yubikey': ['yubikey-manager']
    }
)
