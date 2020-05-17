from distutils.core import setup

setup(
    name='row2plot',
    version='1.0',
    packages=['pandas','matplotlib','seaborn','tqdm'],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.txt').read(),
    author="Ashish Patel"
)

setup(
    name = 'row2plot',
    install_requires=['pandas','matplotlib','seaborn','tqdm']
    version = 'version number',  # Ideally should be same as your GitHub release tag varsion
    description = 'description',
    author = '',
    author_email = '',
    url = 'github package source url',
    download_url = 'download link you saved',
    keywords = ['tag1', 'tag2'],
    classifiers = [],
)