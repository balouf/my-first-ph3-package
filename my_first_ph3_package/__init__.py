"""Top-level package for My First PH3 Package."""

from importlib.metadata import metadata

from my_first_ph3_package.sub_package_1.my_class_1 import MyClass1 as MyClass1
from my_first_ph3_package.sub_package_2.my_class_2 import MyClass2 as MyClass2
from my_first_ph3_package.sub_package_2.my_class_3 import MyClass3 as MyClass3


infos = metadata(__name__)
__version__ = infos["Version"]
__author__ = "Fabien Mathieu"
__email__ = "fabien.mathieu@normalesup.org"
