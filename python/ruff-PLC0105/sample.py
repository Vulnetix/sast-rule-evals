from typing import TypeVar

T_co = TypeVar("T_co", contravariant=True)  # PLC0105: name says co but is contra
