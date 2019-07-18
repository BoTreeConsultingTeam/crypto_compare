from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

setup(
        name='crypto_compare',
        version='0.0.1',
        description='Wrapper for CryptoCompare.com public API',
        long_description=readme,
        url='https://github.com/BoTreeConsultingTeam/crypto_compare',
        author='Parth Barot',
        author_email='parth.barot@botreetechnologies.com',
        keywords='crypto cryptocurrency wrapper cryptocompare crypto_compare',
        license='MIT',
        python_requires='>=3.6',
        packages=find_packages(),
        classifiers=['Programming Language :: Python :: 3.6'],
        install_requires=['urllib3', 'pytest']
    )
