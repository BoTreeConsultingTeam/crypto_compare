from setuptools import setup

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
        python_requires='>=2.7',
        packages=['crypto_compare'],
        classifiers=['Programming Language :: Python :: 2.7'],
        install_requires=['urllib2', 'pytest']
    )