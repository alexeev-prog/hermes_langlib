import os
from pathlib import Path
from typing import Any, Dict, Optional

from hermes_langlib.storage.base import Config
from hermes_langlib.storage.config_provider import ConfigurationProvider
from hermes_langlib.translators.providers import TranslatorProviders


def load_translations(
	locale_directory: str, locale_file: str, language: Optional[str] = None
) -> Dict[Any, Any]:
	"""
	Loads translations.

	:param		locale_directory:  The locale directory
	:type		locale_directory:  str
	:param		locale_file:	   The locale file
	:type		locale_file:	   str
	:param		language:		   The language
	:type		language:		   Optional[str]

	:returns:	locale data
	:rtype:		Dict[Any, Any]
	"""
	locale_provider = ConfigurationProvider(os.path.join(locale_directory, locale_file))

	locale_data = locale_provider()

	if language is None:
		return locale_data

	return locale_data.get(language, locale_data)


def get_translation_provider(provider_name: str) -> TranslatorProviders:
	if provider_name is None:
		return None

	provider_name = provider_name.lower()

	match provider_name:
		case "google":
			return TranslatorProviders.google
		case "chatgpt":
			return TranslatorProviders.chatgpt
		case "microsoft":
			return TranslatorProviders.microsoft
		case "pons":
			return TranslatorProviders.pons
		case "linguee":
			return TranslatorProviders.linguee
		case "mymemory":
			return TranslatorProviders.mymemory
		case "yandex":
			return TranslatorProviders.yandex
		case "papago":
			return TranslatorProviders.papago
		case "deepl":
			return TranslatorProviders.deepl
		case "qcri":
			return TranslatorProviders.qcri


def load_config(filename: str) -> Config:
	"""
	Loads a configuration.

	:param		filename:			The filename
	:type		filename:			str

	:returns:	config dataclass
	:rtype:		Config

	:raises		FileNotFoundError:	config don't exists
	"""
	filename = Path(filename)

	if not filename.exists():
		raise FileNotFoundError(f'Config file "{filename}" don\'t exists')

	config_provider = ConfigurationProvider(filename)

	config_data = config_provider()

	config = Config(
		config_file=filename,
		locale_directory=config_data.get("locale_directory", None),
		default_locale_file=config_data.get("default_locale_file", None),
		default_language=config_data.get("default_language", None),
		translator=get_translation_provider(config_data.get("translator", None)),
	)

	return config
