from setuptools import setup, find_packages

setup(
    name='imhotep_mail',  # Name of your library
    version='0.0.1',  # Version number
    packages=find_packages(),  # Automatically find package directories
    install_requires=[
        'Flask',
        'flask_mail',
    ],
    description='A python library to send mails easily',
    long_description=open('README.md').read(),  # Read long description from README
    long_description_content_type='text/markdown',
    author='Karim Bassem',
    author_email='imhoteptech@outlook.com',
    url='https://github.com/Imhotep-Tech/imhotep_mail',  # URL of your project
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Minimum Python version
    entry_points={
      "console_scripts": [
          "imhotep-mail = imhotep_mail:hello",
      ],
  },
)
