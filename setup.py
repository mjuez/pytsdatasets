import setuptools

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setuptools.setup(
    name='pytsdatasets',
    version='1.0',
    description='A python package that contains time series toy datasets',
    long_description=readme,
    author='Mario Juez-Gil',
    author_email='mariojg@ubu.es',
    url='https://github.com/mjuez/pytsdatasets',
    download_url='https://github.com/mjuez/pytsdatasets/archive/v1_0.tar.gz'
    license=license,
    install_requires=["pandas==1.1.2"],
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers ',
    'Intended Audience :: Education ',
    'Intended Audience :: Science/Research ',
    'Topic :: Scientific/Engineering',
    'Topic :: Education',
    'Topic :: Database',
    'License :: OSI Approved :: GPLv3',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8'
  ]
)