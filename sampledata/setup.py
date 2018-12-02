import os
from setuptools import setup, find_packages


def get_long_description():
    this_directory = os.path.abspath(os.path.dirname(__file__))

    with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as file_:
        long_description = file_.read()

    return long_description


def parse_requirements(file):
    return sorted(set(
        line.partition('#')[0].strip()
        for line in open(os.path.join(os.path.dirname(__file__), file))
    ) - set(''))


def get_version():
    for line in open(os.path.join(os.path.dirname(__file__), 'eobox', 'sampledata', '__init__.py')):
        if line.find("__version__") >= 0:
            version = line.split("=")[1].strip()
            version = version.strip('"').strip("'")
    return version


setup(name='eo-box-sampledata',
      python_requires='>=3.5',
      version=get_version(),
      description='Small earth observation sampledata to play with.',
      long_description=get_long_description(),
      long_description_content_type='text/markdown',
      url='https://github.com/benmack/eo-box',
      author='Benjamin Mack',
      author_email='ben8mack@gmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires=parse_requirements("requirements.txt"),
      include_package_data=True,
      package_data={'eobox/sampledata/data': ['s2l1c/**/*jp2', 's2l1c/s2l1c_ref.gpkg']},
      zip_safe=False)