from dataclasses import dataclass
from enum import Enum

from hermes_langlib.translators.providers import TranslatorProviders


class FileTypes(Enum):
	"""
	This class describes file types.
	"""

	INI = "ini"
	TOML = "toml"
	XML = "xml"
	YAML = "yaml"
	JSON = "json"


@dataclass
class Config:
	"""
	This class describes a configuration.
	"""

	config_file: str
	locale_directory: str
	default_locale_file: str
	default_language: str
	translator: TranslatorProviders = None
