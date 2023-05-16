"""
calculator
----------

Multifunctional calculator.
Easy syntax, i.e.:
```py
from calculator import Calculator

# To execute an addition
result = Calculator(1, 2).add()

print(result) # Prints 3 (1+2)
```
"""

__title__ = "calculator"
__author__ = "Developer Anonymous"
__license__ = "Apache"
__copyright__ = "Copyright 2023-presentado Developer Anonymous"
__version__ = "1.2.0a1"

__path__ = __import__("pkgutil").extend_path(__path__, __name__)

import logging
from typing import NamedTuple, Literal

from .calculator_release import *


class VersionInfo(NamedTuple):
    major: int
    minor: int
    micro: int
    releaselevel: Literal["alpha", "beta", "candidate", "final"]
    serial: int


version_info: VersionInfo = VersionInfo(
    major=1, minor=2, micro=0, releaselevel="alpha", serial=1
)

logging.getLogger(__name__).addHandler(logging.NullHandler())

del logging, NamedTuple, Literal, VersionInfo
