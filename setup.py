from setuptools import setup

setup(
    name='yakstack',
    version='0.1.0',

    description='A command-line utility to help you stack your yaks.',
    keywords='yak stack frame cli tasks',

    url='https://github.com/gilmoreorless/yakstack',

    author='Gilmore Davidson',
    author_email='gilmoreorless@gmail.com',

    license='MIT',

    classifiers=[
        # 'Development Status :: 5 - Production/Stable',
        'Development Status :: 4 - Beta',

        'Environment :: Console',
        'Intended Audience :: Developers',
        'Topic :: Utilities',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],

    py_modules=['yakstack'],
    entry_points={
        'console_scripts': [
            'yakstack=yakstack:main'
        ]
    }

)
