from hermes_langlib.storage.base import FileTypes
from hermes_langlib.storage.config_provider import (
	ConfigurationProvider,
	get_file_extension,
)
from hermes_langlib.storage.loader import get_translation_provider
from hermes_langlib.storage.locale_store import LocaleStorage
from hermes_langlib.translators.providers import TranslatorProviders


def test_config_provider():
	config_provider = ConfigurationProvider("example.toml")
	assert config_provider() == {
		"locale_directory": "locales",
		"default_locale_file": "default.json",
		"default_language": "RU_RU",
		"translator": "google",
	}


def test_translation_providers():
	assert get_translation_provider("google") == TranslatorProviders.google
	assert get_translation_provider("chatgpt") == TranslatorProviders.chatgpt
	assert get_translation_provider("microsoft") == TranslatorProviders.microsoft
	assert get_translation_provider("pons") == TranslatorProviders.pons
	assert get_translation_provider("linguee") == TranslatorProviders.linguee
	assert get_translation_provider("mymemory") == TranslatorProviders.mymemory
	assert get_translation_provider("yandex") == TranslatorProviders.yandex
	assert get_translation_provider("papago") == TranslatorProviders.papago
	assert get_translation_provider("deepl") == TranslatorProviders.deepl
	assert get_translation_provider("qcri") == TranslatorProviders.qcri


def test_locale_storage():
	lc = LocaleStorage("locales/default.json")

	assert lc.get_supported_locales() == ["RU", "EN", "RU_RU", "EN_EN", "EN_US"]
	assert lc.get_supported_locales(dictionary_for_default=True) == [
		{"RU": ["RU_RU"]},
		{"EN": ["EN_EN", "EN_US"]},
	]


def test_extensions():
	files = ["1.json", "2.XML", " 3.TOML ", "4.yaml", " 5.ini"]

	assert get_file_extension(files[0]) == FileTypes.JSON
	assert get_file_extension(files[1]) == FileTypes.XML
	assert get_file_extension(files[2]) == FileTypes.TOML
	assert get_file_extension(files[3]) == FileTypes.YAML
	assert get_file_extension(files[4]) == FileTypes.INI
