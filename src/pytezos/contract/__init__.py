from contextlib import suppress
from datetime import datetime, timezone
from typing import Any, Type

import dateutil.parser
from cattr import Converter


def structure_datetime(obj: Any, cls: Type) -> datetime:
    with suppress(ValueError, TypeError):
        return datetime.utcfromtimestamp(float(obj)).replace(tzinfo=timezone.utc)
    with suppress(dateutil.parser.ParserError):
        return dateutil.parser.parse(obj)
    raise ValueError


def unstructure_datetime(obj: datetime) -> float:
    return obj.timestamp()


converter = Converter()
converter.register_structure_hook(datetime, structure_datetime)
converter.register_unstructure_hook(datetime, unstructure_datetime)
