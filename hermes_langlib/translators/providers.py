from enum import Enum

from deep_translator import (
	ChatGptTranslator,
	DeeplTranslator,
	GoogleTranslator,
	LingueeTranslator,
	MicrosoftTranslator,
	MyMemoryTranslator,
	PapagoTranslator,
	PonsTranslator,
	QcriTranslator,
	YandexTranslator,
)


class TranslatorProvider:
	"""
	This class describes a translator provider.
	"""

	def __init__(self, translator: object):
		"""
		Constructs a new instance.

		:param		translator:	 The translator
		:type		translator:	 object
		"""
		self.translator: object = translator

	def __call__(self, source: str, target: str, phrase: str) -> str:
		"""
		translate phrase

		:param		source:	 The source
		:type		source:	 str
		:param		target:	 The target
		:type		target:	 str
		:param		phrase:	 The phrase
		:type		phrase:	 str

		:returns:	translated phrase
		:rtype:		str
		"""
		translator = self.translator(source=source, target=target)

		return translator.translate(phrase)


class TranslatorProviders(Enum):
	"""
	This class describes translator providers.
	"""

	google = TranslatorProvider(GoogleTranslator)
	chatgpt = TranslatorProvider(ChatGptTranslator)
	microsoft = TranslatorProvider(MicrosoftTranslator)
	pons = TranslatorProvider(PonsTranslator)
	linguee = TranslatorProvider(LingueeTranslator)
	mymemory = TranslatorProvider(MyMemoryTranslator)
	yandex = TranslatorProvider(YandexTranslator)
	papago = TranslatorProvider(PapagoTranslator)
	deepl = TranslatorProvider(DeeplTranslator)
	qcri = TranslatorProvider(QcriTranslator)
