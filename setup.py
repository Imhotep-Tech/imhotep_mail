from setuptools import setup, find_packages

setup(
    name='imhotep_mail',  # Name of your library
    version='1.0.0',  # Version number
    packages=find_packages(),  # Automatically find package directories
    install_requires=[
        'Flask',
        'flask_mail',
        'dotenv'
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
    license='MIT',
    keywords='email, smtp, flask-mail, imhotep',
    entry_points={
      "console_scripts": [
          "imhotep-mail = imhotep_mail:hello",
          "imhotep-mail-cli = imhotep_mail.cli:main",
      ],
  },
)
