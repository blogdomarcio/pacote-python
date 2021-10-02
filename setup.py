from setuptools import setup

with open("README.md", "r") as fh:
    readme = fh.read()

setup(name='blogdomarcio-firstpackage',
      version='0.0.3',
      url='https://github.com/blogdomarcio/pacote-python',
      license='MIT License',
      author='Claudio Marcio',
      long_description=readme,
      long_description_content_type="text/markdown",
      author_email='blogdomarcio@live.com',
      keywords='Pacote',
      description=u'Exemplo de pacote PyPI',
      packages=['blogdomarcio_pacote_python'],
      install_requires=['numpy'],)
