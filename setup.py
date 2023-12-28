from setuptools import setup, find_packages

setup(
  name = 'positional-embeddings-pytorch',
  packages = find_packages(),
  version = '0.0.1',
  license='MIT',
  description = 'Positional Embeddings - Pytorch',
  long_description_content_type = 'text/markdown',
  author = 'Phil Wang',
  author_email = 'kimbaang9@gmail.com',
  url = 'https://github.com/kimbaang/positional-embeddings-pytorch',
  keywords = [
    'deep learning',
    'sinusoial positional embedding',
    'rotary positional embedding',
    'transformers'
  ],
  install_requires=[
    'einops>=0.7',
    'torch>=2.0'
  ],
  classifiers=[
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.9.17',
  ],
)