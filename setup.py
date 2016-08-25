from setuptools import setup
from codecs import open
import yakstack

with open('README.rst', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='yakstack',
    version=yakstack.VERSION,

    description='A command-line utility to help you stack your yaks.',
    long_description=long_description,
    keywords=['yak stack', 'yak frame', 'cli', 'tasks'],

    url='https://github.com/gilmoreorless/yakstack',

    author='Gilmore Davidson',
    author_email='gilmoreorless@gmail.com',

    license='MIT',

    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'Environment :: Console',
        'Intended Audience :: Developers',
        'Topic :: Utilities',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],

    py_modules=['yakstack'],
    entry_points={
        'console_scripts': [
            'yakstack=yakstack:main'
        ]
    }

)
