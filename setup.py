from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()

setup(
    name='Pmdr',
    version='0.0.8',
    author='Jeff Salisbury',
    author_email='salisbury.jeffery@gmail.com',
    license='MIT',
    description='CLI Pomodoro Timer',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/JDSalisbury/doro',
    py_modules=['timer', 'app'],
    packages=find_packages(),
    install_requires=[requirements],
    python_requires='>=3.7',
    classifiers=["Programming Language :: Python :: 3.8",
                 "Operating System :: OS Independent"],
    entry_points='''
        [console_scripts]
        pmdr=timer:cli
    '''
)
