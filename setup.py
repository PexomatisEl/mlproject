##Responsible for creting the package
from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''This function reads a requirements file and returns a list of packages.'''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n', '') for req in requirements]

        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements

#metadata information about the project

setup(
    name='mlproject',
    version='0.0.1',
    author='Pexomatis Lefteris',
    author_email="elpexom@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
