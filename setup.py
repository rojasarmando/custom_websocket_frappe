from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in custom_websocket_frappe/__init__.py
from custom_websocket_frappe import __version__ as version

setup(
	name="custom_websocket_frappe",
	version=version,
	description="Socket IO",
	author="Armando Rojas",
	author_email="armando.develop@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
