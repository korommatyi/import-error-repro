from setuptools import find_namespace_packages, setup

setup(
    name='namespace-repro',
    version='0.1.0',
    python_requires='>=3.6',
    packages=find_namespace_packages('src'),
    package_dir={'': 'src'},
    zip_safe=False,
)
