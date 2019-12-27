from setuptools import setup

with open("README.md", "r") as fh:
	long_description = fh.read()


setup(
	name='unrealai',
	version='0.0.4',
	description='Added Pytest',
	py_modules=["helloworld"],
	package_dir={'':'src'},
	classifiers=[
		"Programming Language :: Python :: 3",
		"Programming Language :: Python :: 3.6",
		"Programming Language :: Python :: 3.7",
		"License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
		"Operating System :: OS Independent",
		],
		long_description=long_description,
		long_description_content_type="text/markdown",
		url= "https://github.com/nishgaba-ai/unrealai",
		author="Nishchal Gaba",
		author_email="nishgaba.ai@gmail.com",
)
