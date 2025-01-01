from abc import ABC, abstractmethod
from configparser import ConfigParser
from typing import Any, Dict, Union

import orjson as json
import toml
import yaml

from hermes_langlib.storage.base import FileTypes


def get_file_extension(filename: str) -> Union[None, FileTypes]:
	"""
	Gets the file extension.

	:param		filename:  The filename
	:type		filename:  str

	:returns:	The file extension.
	:rtype:		Union[None, FileTypes]
	"""
	filename = str(filename).lower().strip()

	ext = filename.split(".")[-1]

	match ext:
		case "json":
			return FileTypes.JSON
		case "xml":
			return FileTypes.XML
		case "toml":
			return FileTypes.TOML
		case "yaml":
			return FileTypes.YAML
		case "ini":
			return FileTypes.INI
		case _:
			return None


class AbstractConfig(ABC):
	"""
	This class describes an abstract configuration.
	"""

	@abstractmethod
	def get_loaded_config(self) -> Dict[Any, Any]:
		"""
		Gets the loaded configuration.

		:returns:	The loaded configuration.
		:rtype:		{ return_type_description }
		"""
		raise NotImplementedError


class AbstractConfigFactory(ABC):
	"""
	Front-end to create abstract configuration objects.
	"""

	def create_config(self) -> AbstractConfig:
		"""
		Creates a configuration.

		:returns:	The abstract configuration.
		:rtype:		AbstractConfig
		"""
		raise NotImplementedError


class JSONConfig(AbstractConfig):
	"""
	This class describes a json configuration.
	"""

	def __init__(self, config_path: str):
		"""
		Constructs a new instance.

		:param		config_path:  The configuration path
		:type		config_path:  str
		"""
		self.config_path = config_path
		self.config: Dict[Any, Any] = {}

	def get_loaded_config(self) -> Dict[Any, Any]:
		"""
		Gets the loaded configuration.

		:returns:	The loaded configuration.
		:rtype:		Dict[Any, Any]
		"""
		with open(self.config_path, "r") as f:
			self.config = json.loads(f.read())

		return self.config


class TOMLConfig(AbstractConfig):
	"""
	This class describes a toml configuration.
	"""

	def __init__(self, config_path: str):
		"""
		Constructs a new instance.

		:param		config_path:  The configuration path
		:type		config_path:  str
		"""
		self.config_path = config_path
		self.config: Dict[Any, Any] = {}

	def get_loaded_config(self) -> Dict[Any, Any]:
		"""
		Gets the loaded configuration.

		:returns:	The loaded configuration.
		:rtype:		Dict[Any, Any]
		"""
		with open(self.config_path) as f:
			self.config = toml.load(f)

		return self.config


class INIConfig(AbstractConfig):
	"""
	This class describes an INI configuration.
	"""

	def __init__(self, config_path: str):
		"""
		Constructs a new instance.

		:param		config_path:  The configuration path
		:type		config_path:  str
		"""
		self.config_path = config_path
		self.config: Dict[Any, Any] = {}

	def get_loaded_config(self) -> Dict[Any, Any]:
		"""
		Gets the loaded configuration.

		:returns:	The loaded configuration.
		:rtype:		Dict[Any, Any]
		"""
		config = ConfigParser()
		config.read(self.config_path)

		return config


class YAMLConfig(AbstractConfig):
	"""
	This class describes an yaml configuration.
	"""

	def __init__(self, config_path: str):
		"""
		Constructs a new instance.

		:param		config_path:  The configuration path
		:type		config_path:  str
		"""
		self.config_path = config_path
		self.config: Dict[Any, Any] = {}

	def get_loaded_config(self) -> Dict[Any, Any]:
		"""
		Gets the loaded configuration.

		:returns:	The loaded configuration.
		:rtype:		Dict[Any, Any]
		"""
		with open(self.config_path) as f:
			self.config = yaml.load(f, Loader=yaml.FullLoader)

		return self.config


class ConfigFactory(AbstractConfigFactory):
	"""
	Front-end to create configuration objects.
	"""

	def __init__(self, config_path: str):
		"""
		Constructs a new instance.

		:param		config_path:  The configuration path
		:type		config_path:  str
		"""
		self.ext = get_file_extension(config_path)
		self.config_path = config_path

	def create_config(self) -> Union[JSONConfig, TOMLConfig, YAMLConfig, INIConfig]:
		"""
		Creates a configuration.

		:returns:	config dict
		:rtype:		Dict[Any, Any]
		"""
		match self.ext:
			case FileTypes.JSON:
				return JSONConfig(self.config_path)
			case FileTypes.TOML:
				return TOMLConfig(self.config_path)
			case FileTypes.YAML:
				return YAMLConfig(self.config_path)
			case FileTypes.INI:
				return INIConfig(self.config_path)
			case _:
				return None


class ConfigurationProvider:
	"""
	This class describes a configuration provider.
	"""

	def __init__(self, config_path: str):
		"""
		Constructs a new instance.

		:param		config_path:  The configuration path
		:type		config_path:  str
		"""
		self.factory = ConfigFactory(config_path)
		self.config = self.factory.create_config()

	def __call__(self) -> AbstractConfig:
		"""
		Gets the instance.

		:returns:	The instance.
		:rtype:		AbstractConfig
		"""

		return self.config.get_loaded_config()
