from dataclasses import dataclass
from enum import Enum


class FileTypes(Enum):
	INI = 'ini'
	TOML = 'toml'
	XML = 'xml'
	YAML = 'yaml'
	JSON = 'json'


@dataclass
class Config:
	config_file: str
	locale_directory: str
	default_locale_file: str
	default_language: str
	use_translator: bool = True
