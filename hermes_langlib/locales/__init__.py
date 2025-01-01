from typing import Optional, List, Dict, Union, Any
import os
import re
from hermes_langlib.storage.locale_store import LocaleStorage
from hermes_langlib.storage.base import Config


class Locale:
	def __init__(self, locale_directory: str, locale_file: str, short_name: Optional[str] = None):
		self.locale_directory = locale_directory
		self.locale_file = locale_file
		self.short_name = short_name

		if short_name is None:
			self.short_name = "".join(str(self.locale_file).split('.')[:-1])

		self.storage = LocaleStorage(os.path.join(self.locale_directory, self.locale_file))

	def get_supported_locales(
		self, dictionary_for_default: Optional[bool] = False
	) -> List[str]:
		return self.storage.get_supported_locales(dictionary_for_default=dictionary_for_default)

	def get_items(self, language: str) -> Dict[str, str]:
		for key, value in self.storage.locales.items():
			lang_name = value.get(language)
			# print(language, lang_name, key, value)

			if isinstance(lang_name, list):
				language = lang_name[0]
				continue

			if lang_name is not None:
				return lang_name

			if key == 'locales':
				continue

			if isinstance(value, dict):
				if lang_name is not None:
					return lang_name


class LocaleManager:
	def __init__(self, config: Config, locales: List[str]):
		self.config = config
		self.locales: Dict[str, Locale] = self._prepare_locales(locales)
		self._validate_fields()

	def _prepare_locales(self, locales: List[str]):
		result = {}

		for locale_name in locales:
			locale = Locale(self.config.locale_directory, locale_name)
			result[locale.short_name] = locale

		return result

	def _validate_fields(self):
		default_language = self.config.default_language
		supported_locales = []

		for _, locale in self.locales.items():
			supported_locales += locale.get_supported_locales(
				dictionary_for_default=False
			)

		if default_language not in supported_locales:
			raise ValueError(f"Default language don't found in: {supported_locales}")

	def _find_language_locales(self, locale_name: str, language: str):
		locale = self.locales.get(locale_name, None)

		if locale is None:
			return None

		language_locales = locale.get_items(language)

		return language_locales

	def _prepare_key(self, word: str, language_locales: Union[Dict[str, str], Dict[str, Dict[str, Any]]], **kwargs):
		# locales = language_locales.get(word, word)
		pattern = re.compile(r'\b(' + '|'.join(re.escape(k) for k in language_locales.keys()) + r')\b')

		def _replace(match):
			locales = language_locales.get(match.group(0))

			if isinstance(locales, dict):
				plural = locales.get('plural', False)

				plural_param = str(kwargs.get(plural))

				if plural_param is None:
					raise ValueError(f'Missing required plural parameter: {plural_param}')

				if plural:
					for pattern, plural_locale in locales.items():
						if pattern == 'plural':
							continue
						elif pattern == 'other':
							return plural_locale.format(**kwargs)
						elif re.match(pattern, plural_param) or re.search(pattern, plural_param):
							return plural_locale.format(**kwargs)

			return language_locales.get(match.group(0), match.group(0))
		
		return pattern.sub(_replace, word).format(**kwargs)

	def get_string(self, key: str, locale_name: str, language: Optional[str] = None, **kwargs) -> str:
		if language is None:
			language = self.config.default_language

		language_locales = self._find_language_locales(locale_name, language)

		if language_locales is None:
			return key

		result = self._prepare_key(key, language_locales, **kwargs)

		return result

