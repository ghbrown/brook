

import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='taylor',  
    version='0.0.0',
    scripts=['bin/taylor'] ,
    author='Gabriel H. Brown',
    author_email='gabriel.h.brown@gmail.com',
    description='Generic derivative objects (gradients, Jacobians, Hessians, and more) by finite differences',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ghbrown/taylor',
    packages=setuptools.find_packages(),
    #include_package_data = True, #include non-Python files specified in MANIFEST.in
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering',
    ],
    keywords=[
        'scientific',
        'engineering',
        'derivatives',
        'optimization',
        'rootfinding',
        'approximation',
    ],
    install_requires=[
        'numpy',
    ],
 )
