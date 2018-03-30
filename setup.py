from setuptools import setup

setup(name='pma-python',
      version='2.0.0.4',
      description='Universal viewing of whole slide imaging and microscopy data',
      url='http://github.com/pathomation/pma-python',
      author='Pathomation',
	  author_email='info@pathomation.com',
      license='http://free.pathomation.com/eula/',
      packages=['pma-python'],
	  classifiers = [
		'Development Status :: 3 - Alpha', 
		'Programming Language :: Python :: 3'],
	  keywords='wsi whole slide imaging gigapixel microscopy histology pathology',
	  install_requires=['pillow', 'requests'],
	  python_requires='~=3',	# assume this only works in Python 3
      zip_safe=False)
