import setuptools

setuptools.setup(
    name="melodia_py",
    version="0.1.2",
    url="https://github.com/rwmontalvao/Melodia_py",
    author="Rinaldo Wander Montalvão, PhD",
    author_email="rwmontalvao@gmail.com",
    description="Differential Geometry of Proteins Backbones",
    long_description=open('README.md').read(),
    packages=setuptools.find_packages(),
    install_requires=['biopython', 'pandas', 'typing-extensions'],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.12',
    ],
    include_package_data=True,
    package_data={'': ['data/*.dat']},
)
