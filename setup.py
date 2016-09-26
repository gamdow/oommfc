from setuptools import setup

with open('README.rst') as f:
    readme = f.read()

setup(
    name='oommfc',
    version='0.4',
    description='A Python-based OOMMF calculator.',
    long_description=readme,
    author='Computational Modelling Group',
    author_email='fangohr@soton.ac.uk',
    url = 'https://github.com/joommf/oommfc',
    download_url = 'https://github.com/joommf/oommfc/tarball/0.4',
    packages=['oommfc',
              #'oommfc.energies',           # should this be hamiltonian?
                                            # and dynamics?
              'oommfc.tests'],
    install_requires=[
        'finitedifferencefield',
        'oommffield',
        'oommfodt'
    ],
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ]
)
