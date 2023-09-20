from setuptools import find_packages, setup
from typing import List

hy_e = '-e .'

def get_requirements(path: str) -> List[str]:
    '''Returns a list of requirements'''
    requirement = []
    with open(path, 'r') as f: 
        requirement = f.readlines()
        requirement = [req.replace('\n', '') for req in requirement]
        if hy_e in requirement:
            requirement.remove(hy_e)
    return requirement

with open('HISTORY.rst') as history_file:
    history = history_file.read()

with open('README.rst') as readme_file:
    readme = readme_file.read()

setup(
    name='Hate_Speech_Classifier',
    version='0.0.1',
    author='noumanirshad',
    author_email='noumanirshad564@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GPL-3.0',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    description='Hate Speech Application',
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    url='https://github.com/noumanirshad/Hate_Speech_Classifier',
    packages=find_packages(include=['Hate_Speech_Classifier', 'Hate_Speech_Classifier.*']),
    install_requires=get_requirements('requirements.txt'),
    zip_safe=False,
)
