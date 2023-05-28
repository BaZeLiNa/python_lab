"""
Enum
"""
from enum import Enum


class EngineType(Enum):
    """Enumeration representing the type of engine."""

    UNKNOWN = 0
    ELECTRIC = 1
    GAS_TURBINE = 2
    PISTON = 3
