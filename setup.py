from setuptools import setup

# reading long description from file
with open('DESCRIPTION.txt') as file:
    long_description = file.read()


# specify requirements of your package here
REQUIREMENTS = []

# some more details
CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Internet',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    ]

# calling the setup function 
setup(name='algo',
      version='1.0.0',
      description='Built-In algos in Python for Competitive Programming',
      long_description=long_description,
      url='https://github.com/vishuvish/algo',
      author='Vishal Agrawal',
      author_email='vishvishu14@gmail.com',
      license='MIT',
      packages=['algo'],
      classifiers=CLASSIFIERS,
      install_requires=REQUIREMENTS,
      keywords='algos built-in competitive programming'
      )
