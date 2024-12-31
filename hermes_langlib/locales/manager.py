from abc import ABC, abstractmethod


class AbstractLocaleInterface(ABC):
	@abstractmethod
	def _load_translations(self):
		raise NotImplementedError

	@abstractmethod
	def get_translation(self, key: str, language: str = None, **kwargs):
		raise NotImplementedError
