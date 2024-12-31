from abc import ABC, abstractmethod
from typing import Dict, List, Optional

from hermes_langlib.storage.config_provider import ConfigurationProvider


class BaseStorage(ABC):
	@abstractmethod
	def _load_config(self) -> Dict[str, str]:
		raise NotImplementedError

	@abstractmethod
	def get_supported_locales(self) -> List[str]:
		raise NotImplementedError


class LocaleStorage(BaseStorage):
	def __init__(self, filename: str):
		self.filename = filename
		self.provider = ConfigurationProvider(self.filename)
		self.config = self._load_config()

	def _load_config(self) -> Dict[str, str]:
		return self.provider()

	def get_supported_locales(
		self, dictionary_for_default: Optional[bool] = False
	) -> List[str]:
		locales = self.config.get("locales", None)

		if locales is None:
			locales = []

			for locale_name, locale in self.config.items():
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
