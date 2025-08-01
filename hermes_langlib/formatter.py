import re
from abc import ABC, abstractmethod
from typing import Any, Union


class BaseFormatter(ABC):
    """This class describes a base formatter."""

    @abstractmethod
    def format_string(self) -> Any:
        """
        Format string.

        :returns:	formatted string
        :rtype:		Any
        """
        raise NotImplementedError


class PluralFormatter(BaseFormatter):  # noqa: D101
    @staticmethod
    def format_string(
        locales: Union[dict[str, str], dict[str, dict[str, Any]]], **kwargs
    ) -> Union[str, None]:
        """
        Format string.

        :param		locales:	 The locales
        :type		locales:	 nion[Dict[str, str], Dict[str, Dict[str, Any]]]
        :param		kwargs:		 The keywords arguments
        :type		kwargs:		 dictionary

        :returns:	localized string
        :rtype:		Union[str, None]

        :raises		ValueError:	 missing plural parameter
        """
        if isinstance(locales, dict):
            plural = locales.get("plural", False)

            plural_param = str(kwargs.get(plural))

            if plural_param is None:
                raise ValueError(f"Missing required plural parameter: {plural_param}")

            if plural:
                for plural_pattern, plural_locale in locales.items():
                    if plural_pattern == "plural":
                        continue
                    if (
                        plural_pattern == "other"
                        or re.match(plural_pattern, plural_param)
                        or re.search(plural_pattern, plural_param)
                    ):
                        return plural_locale.format(**kwargs)

        return None
