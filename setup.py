from setuptools import setup, find_packages

setup(
    name='MyDataAnalysisProject',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'matplotlib',
        'seaborn',
        'scipy',
        'jupyterlab'
    ],
    entry_points={
        'console_scripts': [
            'my_analysis=my_module:main',  # "my_module" should be replaced with the name of your Python module
        ],
    },
    python_requires='>=3.6',
    author='Your Name',
    author_email='your.email@example.com',
    description='An example data analysis project setup.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/mdccit/data_analysis_python_r',  # Replace with the correct URL
)
