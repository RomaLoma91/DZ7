from setuptools import setup, find_packages
setup(
    name='clean_folder',
    version='0.1',
    description='scripts clean folder and normalize file name',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
      ],
    author='loma',
    author_email='lomachinskiy.r@gmail.com',
    license='MIT',
    packages=['clean_folder'],
    install_requires=[],
    python_requires='>=3.5',
    include_package_data=True,
    entry_points={'console_scripts':[]},
)