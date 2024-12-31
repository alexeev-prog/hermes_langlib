import os
from pathlib import Path
from typing import Optional, Dict, Any
from hermes_langlib.storage.config_provider import ConfigurationProvider
from hermes_langlib.storage.base import Config


def load_translations(locale_directory: str, locale_file: str, language: Optional[str] = None) -> Dict[Any, Any]:
	"""
	Loads translations.

	:param      locale_directory:  The locale directory
	:type       locale_directory:  str
	:param      locale_file:       The locale file
	:type       locale_file:       str
	:param      language:          The language
	:type       language:          Optional[str]

	:returns:   locale data
	:rtype:     Dict[Any, Any]
	"""
	locale_provider = ConfigurationProvider(os.path.join(locale_directory, locale_file))

	locale_data = locale_provider()

	if language is None:
		return locale_data

	return locale_data.get(language, locale_data)


def load_config(filename: str) -> Config:
	"""
	Loads a configuration.

	:param      filename:           The filename
	:type       filename:           str

	:returns:   config dataclass
	:rtype:     Config

	:raises     FileNotFoundError:  config don't exists
	"""
	filename = Path(filename)

	if not filename.exists():
		raise FileNotFoundError(f'Config file "{filename}" don\'t exists')

	config_provider = ConfigurationProvider(filename)

	config_data = config_provider()

	config = Config(
		config_file=filename,
		locale_directory=config_data.get('locale_directory', None),
		default_locale_file=config_data.get('default_locale_file', None),
		default_language=config_data.get('default_language', None),
		use_translator=config_data.get('use_translator', True)
	)

	return config
