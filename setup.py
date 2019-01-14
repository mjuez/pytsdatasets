import setuptools

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setuptools.setup(
    name='pytsdatasets',
    version='0.1',
    description='A python package that contains time series toy datasets',
    long_description=readme,
    author='Mario Juez-Gil',
    author_email='mariojg@ubu.es',
    url='https://github.com/mjuez/pytsdatasets',
    license=license,
    install_requires=["pandas"],
    packages=setuptools.find_packages(),
)