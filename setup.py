from setuptools import setup,find_packages
from typing import List

# Define the constant for -e .
HYPEN_E_DOT = '-e .'

# Get all the required file from requirements.txt
def get_requirements(file_path:str) -> List[str]:
    '''
    This Function will return the list of requirements.
    '''
    # Define empty list for requirements
    requirements = []

    # open the requirements.txt file and read all lines
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n','') for req in requirements]

        # We don't want '-e .'
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


# Setup for the build the project as the package
setup(
    name='studentperformance',
    version='0.0.1',
    author='Dhairy',
    author_email='dhairy.tilva26@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)