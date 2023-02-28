from setuptools import find_packages, setup
setup(
    name='flexy_ai',
    packages=find_packages(include=['tips']),
    version='0.1.0',
    description='Library Of Flexy AI Functions',
    author='Flexy',
    license='MIT',
    install_requires=[],
    setup_requires=['flexy_ai'],
    tests_require=['flexy_ai==0.1.0'],
    test_suite='tips',
)
