from ast import AST
from dataclasses import dataclass
from typing import List, Optional

from metacode.typing import Arguments


@dataclass
class ParsedComment:
    key: str
    command: str
    arguments: Arguments
