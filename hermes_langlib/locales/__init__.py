import os
import re
from typing import Any, Dict, List, Optional, Union

from hermes_langlib.formatter import PluralFormatter
from hermes_langlib.storage.base import Config
from hermes_langlib.storage.locale_store import LocaleStorage


class Locale:
	"""
	This class describes a locale.
	"""

	def __init__(
		self, locale_directory: str, locale_file: str, short_name: Optional[str] = None
	):
		"""
		Constructs a new instance.

		:param		locale_directory:  The locale directory
		:type		locale_directory:  str
		:param		locale_file:	   The locale file
		:type		locale_file:	   str
		:param		short_name:		   The short name
		:type		short_name:		   Optional[str]
		"""
		self.locale_directory: str = locale_directory
		self.locale_file: str = locale_file
		self.short_name: str = short_name

		if short_name is None:
			self.short_name = "".join(str(self.locale_file).split(".")[:-1])

		self.storage: LocaleStorage = LocaleStorage(
			os.path.join(self.locale_directory, self.locale_file)
		)

	def get_supported_locales(
		self, dictionary_for_default: Optional[bool] = False
	) -> List[str]:
		"""
		Gets the supported locales.

		:param		dictionary_for_default:	 The dictionary for default
		:type		dictionary_for_default:	 bool

		:returns:	The supported locales.
		:rtype:		List[str]
		"""
		return self.storage.get_supported_locales(
			dictionary_for_default=dictionary_for_default
		)

	def get_items(self, language: str) -> Dict[str, str]:
		"""
		Gets the items.

		:param		language:  The language
		:type		language:  str

		:returns:	The items.
		:rtype:		Dict[str, str]
		"""
		for key, value in self.storage.locales.items():
			lang_items = value.get(language)

			if isinstance(lang_items, list):
				language = lang_items[0]
				continue

			if lang_items is not None:
				return lang_items

			if key == "locales":
				continue

			if isinstance(value, dict):
				if lang_items is not None:
					return lang_items


class LocaleManager:
	"""
	This class describes a locale manager.
	"""

	def __init__(self, config: Config, locales: Optional[List[str]] = []):
		"""
		Constructs a new instance.

		:param		config:	  The configuration
		:type		config:	  Config
		:param		locales:  The locales
		:type		locales:  Array
		"""
		self.config: Config = config
		self.locales: Dict[str, Locale] = self._prepare_locales(locales)
		self._validate_fields()

	def _prepare_locales(self, locales: List[str]) -> Dict[str, Locale]:
		"""
		Prepare and create locales dict

		:param		locales:  The locales
		:type		locales:  List[str]

		:returns:	locales dictionary
		:rtype:		Dict[str, Locale]
		"""
		result = {}

		default_locale = Locale(
			self.config.locale_directory, self.config.default_locale_file
		)

		result[default_locale.short_name] = default_locale

		for locale_name in locales:
			locale = Locale(self.config.locale_directory, locale_name)
			result[locale.short_name] = locale

		return result

	def _validate_fields(self):
		"""
		Validate fields for locales

		:raises		ValueError:	 Default language dont found
		"""
		default_language = self.config.default_language
		supported_locales = []

		for _, locale in self.locales.items():
			supported_locales += locale.get_supported_locales(
				dictionary_for_default=False
			)

		if default_language not in supported_locales:
			raise ValueError(f"Default language don't found in: {supported_locales}")

	def _find_language_locales(self, locale_name: str, language: str) -> Dict[str, str]:
		"""
		Finds language locales.

		:param		locale_name:  The locale name
		:type		locale_name:  str
		:param		language:	  The language
		:type		language:	  str

		:returns:	language locales
		:rtype:		Dict[str, str]
		"""

		if locale_name is None:
			language_locales = {}

			for _, locale in self.locales.items():
				items = locale.get_items(language)

				if items is not None:
					language_locales.update(items)
		else:
			locale = self.locales.get(locale_name, None)

			if locale is None:
				return None

			language_locales = locale.get_items(language)

		return language_locales

	def _prepare_key(
		self,
		word: str,
		language_locales: Union[Dict[str, str], Dict[str, Dict[str, Any]]],
		**kwargs,
	) -> str:
		"""
		Prepare key before sending

		:param		word:			   The word
		:type		word:			   str
		:param		language_locales:  The language locales
		:type		language_locales:  Union[Dict[str, str], Dict[str, Dict[str, Any]]]
		:param		kwargs:			   The keywords arguments
		:type		kwargs:			   dictionary

		:returns:	prepared word
		:rtype:		str
		"""
		pattern = re.compile(
			r"\b(" + "|".join(re.escape(k) for k in language_locales.keys()) + r")\b"
		)

		def _replace(match):
			result = PluralFormatter.format_string(
				language_locales.get(match.group(0)), **kwargs
			)

			return (
				result
				if result is not None
				else language_locales.get(match.group(0), match.group(0))
			)

		return pattern.sub(_replace, word).format(**kwargs)

	def translate(
		self,
		key: str,
		language_from: Optional[str] = "auto",
		language_to: Optional[str] = None,
		**kwargs,
	) -> str:
		"""
		Translate

		:param		key:			The key
		:type		key:			str
		:param		language_from:	The language from
		:type		language_from:	Optional[str]
		:param		language_to:	The language to
		:type		language_to:	Optional[str]
		:param		kwargs:			The keywords arguments
		:type		kwargs:			dictionary

		:returns:	translated phrase
		:rtype:		str
		"""
		if language_to is None:
			language_to = self.config.default_language

		return self.config.translator.value(language_from, language_to, key).format(
			**kwargs
		)

	def get(
		self,
		key: str,
		locale_name: Optional[str] = None,
		language: Optional[str] = None,
		**kwargs,
	) -> str:
		"""
		get value by key from locales

		:param		key:		  The key
		:type		key:		  str
		:param		locale_name:  The locale name
		:type		locale_name:  Optional[str]
		:param		language:	  The language
		:type		language:	  Optional[str]
		:param		kwargs:		  The keywords arguments
		:type		kwargs:		  dictionary

		:returns:	value
		:rtype:		str
		"""
		if language is None:
			language = self.config.default_language

		language_locales = self._find_language_locales(locale_name, language)

		if language_locales is None:
			return key

		result = self._prepare_key(key, language_locales, **kwargs)

		return result
