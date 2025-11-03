from setuptools import setup, find_packages

setup(
    name='dockmon',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'dockmon=app.main:main',
        ],
    },
    install_requires=[
        'Flask>=2.0.0',
        'docker>=5.0.0'
    ],
    python_requires='>=3.7',
    version='1.0.0',
    author='Asrorkhodja, Akobir',
    description='A Docker container monitoring application',
    license='MIT',
)