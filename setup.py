from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()

setup(
    name='Doro',
    version='0.0.1',
    author='Jeff Salisbury',
    author_email='salisbury.jeffery@gmail.com',
    license='MIT',
    description='Pomodoro Timer for programming dope shit.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/JDSalisbury/doro',
    py_modules=['my_tool', 'app'],
    packages=find_packages(),
    install_requires=[requirements],
    python_requires='>=3.7',
    classifiers=[
        'Programing Language :: Python :: 3.8',
        "Operating System :: OS independent",
    ],
    entry_points='''
        [console_scripts]
        doro=timer:cli
    '''
)
