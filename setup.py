from setuptools import setup, find_packages

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='mortality_table',
    url='https://github.com/dixusmile/mortality_table.git',
    author='Di Xu',
    author_email='di.xu@unl.edu',
    # Needed to actually package something
    packages=find_packages(exclude=['tests*']),
    # Needed for dependencies
    install_requires=['numpy', 'pandas', 'xlrd'],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='UNL',
    description='Functions to construct mortality table',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)