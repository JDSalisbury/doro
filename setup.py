from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()

setup(
    name='Pmdr',
    version='1.0.6',
    author='Jeff Salisbury',
    author_email='salisbury.jeffery@gmail.com',
    license='MIT',
    description='CLI Pomodoro Timer',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/JDSalisbury/doro',
    data_files=[
        ('pmdr', ['pmdr/endalarm.mp3', 'pmdr/sbalarm.mp3', 'pmdr/stalarm.mp3'])],
    include_package_data=True,
    py_modules=['timer', 'pmdr'],
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
