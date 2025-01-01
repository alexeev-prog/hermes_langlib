from enum import Enum
from deep_translator import (GoogleTranslator,
                             ChatGptTranslator,
                             MicrosoftTranslator,
                             PonsTranslator,
                             LingueeTranslator,
                             MyMemoryTranslator,
                             YandexTranslator,
                             PapagoTranslator,
                             DeeplTranslator,
                             QcriTranslator)


class TranslatorProvider:
	def __init__(self, translator):
		self.translator = translator

	def __call__(self, source: str, target: str, phrase: str):
		self.translator = self.translator(source=source, target=target)

		return self.translator.translate(phrase)


class TranslatorProviders(Enum):
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
