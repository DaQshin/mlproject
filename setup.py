from setuptools import find_packages, setup

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path:str) -> list[str]:
    '''

    This function will return list of requirements.

    '''
    with open(file_path) as file:
        requirements=file.readlines()
        requirements=[req.replace("\n", "") for req in requirements]

        if(HYPHEN_E_DOT in requirements):
            requirements.remove(HYPHEN_E_DOT)
        
    return requirements


setup(
    name='mlproject',
    version='1.0.0',
    author='Dakshin',
    author_email='dakshin.official@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)