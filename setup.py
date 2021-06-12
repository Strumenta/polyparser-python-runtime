from setuptools import find_packages, setup
setup(
    name='polyparserrt',
    packages=find_packages(include=["polyparserrt"]),
    version='0.1.0',
    description='Polyparser Runtime',
    author='Strumenta S.R.L.',
    license='Apache License V2',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)
