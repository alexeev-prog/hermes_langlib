from abc import ABC, abstractmethod
from typing import Dict, List, Optional

from hermes_langlib.storage.config_provider import ConfigurationProvider


class BaseStorage(ABC):
	"""
	This class describes a base storage.
	"""

	@abstractmethod
	def _load_locales(self) -> Dict[str, str]:
		"""
		Loads locales.

		:returns:	locales
		:rtype:		Dict[str, str]
		"""
		raise NotImplementedError

	@abstractmethod
	def get_supported_locales(self) -> List[str]:
		"""
		Gets the supported locales.

		:returns:	The supported locales.
		:rtype:		List[str]
		"""
		raise NotImplementedError


class LocaleStorage(BaseStorage):
	"""
	This class describes a locale storage.
	"""

	def __init__(self, filename: str):
		"""
		Constructs a new instance.

		:param		filename:  The filename
		:type		filename:  str
		"""
		self.filename: str = filename
		self.provider: ConfigurationProvider = ConfigurationProvider(self.filename)
		self.locales: Dict[str, str] = self._load_locales()

	def _load_locales(self) -> Dict[str, str]:
		"""
		Loads locales.

		:returns:	locales
		:rtype:		Dict[str, str]
		"""
		return self.provider()

	def get_supported_locales(
		self, dictionary_for_default: Optional[bool] = False
	) -> List[str]:
		"""
		Gets the supported locales.

		:param		dictionary_for_default:	 The dictionary for default
		:type		dictionary_for_default:	 Optional[bool]

		:returns:	The supported locales.
		:rtype:		List[str]
		"""
		locales = self.locales.get("locales", None)

		if locales is None:
			locales = []

			for locale_name, locale in self.locales.items():
				locales.append(locale_name)
				if isinstance(locale, dict):
					for sublocale_name, sublocale in locale.items():
						locales.append(sublocale_name)
		else:
			locales_list = []

			if not dictionary_for_default:
				locales_list = list(locales.keys())
				for _, locale in locales.items():
					locales_list += [locale_name for locale_name in locale]
			else:
				for locale_name, locale in locales.items():
					sublocales = [sublocale_name for sublocale_name in locale]
					locales_list.append({locale_name: sublocales})

			locales = locales_list

		return locales
