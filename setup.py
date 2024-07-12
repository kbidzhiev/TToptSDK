from setuptools import setup, find_packages

setup(
    name='ttoptSDK',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        "ttopt==0.6.2",
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest']
)