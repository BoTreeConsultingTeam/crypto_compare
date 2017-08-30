from setuptools import setup

with open('README.md', encoding="utf-8") as f:
    readme = f.read()

setup(
        name='crypto_compare',
        version='0.0.1',
        description='Wrapper for CryptoCompare.com public API',
        long_description=readme,
        url='https://github.com/BoTreeConsultingTeam/crypto_compare',
        author='ParthBarot-BoTreeConsulting',
        keywords='crypto cryptocurrency wrapper cryptocompare crypto_compare',
        license='MIT',
        python_requires='>=2.7',
        packages=['crypto_compare'],
        classifiers=['Programming Language :: Python :: 2.7'],
        install_requires=['urllib2', 'json']
    )