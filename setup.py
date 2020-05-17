from distutils.core import setup

setup(
    name = 'row2plot',
    install_requires=['pandas','matplotlib','seaborn','tqdm'],
    version = '1.0',  # Ideally should be same as your GitHub release tag varsion
    description = 'This package is use for convert your row to histogram and kdeplot',
    author = 'Ashish Patel',
    author_email = 'ashishpatel26',
    url = 'https://github.com/ashishpatel26/row2plot',
    download_url = 'download link you saved',
    keywords = ['pandas', 'dataset','matplotlib','seaborn','row2plot'],
    classifiers = [],
    long_description=open('README.txt').read(),
)