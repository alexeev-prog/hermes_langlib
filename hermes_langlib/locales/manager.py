from abc import ABC, abstractmethod

from hermes_langlib.storage.base import Config
from hermes_langlib.storage.locale_store import LocaleStorage


class AbstractLocaleInterface(ABC):
	@abstractmethod
	def _load_translations(self):
		raise NotImplementedError

	@abstractmethod
	def add_translation(self, key: str, value: str, locale: str):
		raise NotImplementedError

	@abstractmethod
	def get_string(self, key: str, language: str = None, **kwargs):
		raise NotImplementedError


class LocaleManager(AbstractLocaleInterface):
	def __init__(self, config: Config, locale_store: LocaleStorage):
		self.config = config
		self.locale_store = locale_store

	def validate_fields(self):
		default_language = self.config.default_language
		supported_locales = self.locale_store.get_supported_locales(
			dictionary_for_default=False
		)

		if default_language not in supported_locales:
			raise ValueError(f"Default language don't found in: {supported_locales}")
