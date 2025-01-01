from hermes_langlib.locales import LocaleManager
from hermes_langlib.storage import load_config
from hermes_langlib.storage.base import Config

config = load_config("example.toml")
locale_manager = LocaleManager(config, locales=["default.json"])


def test_config():
	assert isinstance(config, Config)
	assert isinstance(locale_manager.locales, dict)


def test_en():
	assert (
		locale_manager.get("title - {version}", "default", "EN_EN", version="0.1.0")
		== "Library for internationalization - 0.1.0"
	)
	assert (
		locale_manager.get("title - {version}", "default", "EN", version="0.1.0")
		== "Library for internationalization - 0.1.0"
	)
	assert (
		locale_manager.get("mails_message.", "default", "EN_EN", count=0)
		== "You do not have any mail.."
	)
	assert (
		locale_manager.get("mails_message", "default", "EN_EN", count=0)
		== "You do not have any mail."
	)
	assert (
		locale_manager.get("mails_message", "default", "EN_EN", count=1)
		== "You have a new mail."
	)
	assert (
		locale_manager.get("mails_message", "default", "EN_EN", count=11)
		== "You have 11 new mails."
	)
	assert (
		locale_manager.get("mails_message", "default", "EN_EN", count=2)
		== "You have 2 new mails."
	)
	assert (
		locale_manager.get("mails_message", "default", "EN_EN", count=22)
		== "You have 22 new mails."
	)
	assert (
		locale_manager.get("mails_message", "default", "EN_EN", count=46)
		== "You have 46 new mails."
	)
	assert (
		locale_manager.get("mails_message", "default", "EN_EN", count=100000001)
		== "You have 100000001 new mails."
	)
	assert (
		locale_manager.translate("У вас всего три письма", "ru", "en")
		== "You only have three letters."
	)


def test_ru():
	assert (
		locale_manager.get("title - {version}", "default", "RU_RU", version="0.1.0")
		== "Библиотека для интернационализации - 0.1.0"
	)
	assert (
		locale_manager.get("title - {version}", "default", "RU", version="0.1.0")
		== "Библиотека для интернационализации - 0.1.0"
	)
	assert (
		locale_manager.get("mails_message.", "default", "RU_RU", count=0)
		== "У вас нет ни одного письма."
	)
	assert (
		locale_manager.get("mails_message", "default", "RU_RU", count=0)
		== "У вас нет ни одного письма"
	)
	assert (
		locale_manager.get("mails_message", "default", "RU_RU", count=1)
		== "У вас есть 1 письмо"
	)
	assert (
		locale_manager.get("mails_message", "default", "RU_RU", count=11)
		== "У вас есть 11 писем"
	)
	assert (
		locale_manager.get("mails_message", "default", "RU_RU", count=2)
		== "У вас есть 2 письма"
	)
	assert (
		locale_manager.get("mails_message", "default", "RU_RU", count=22)
		== "У вас есть 22 письма"
	)
	assert (
		locale_manager.get("mails_message", "default", "RU_RU", count=46)
		== "У вас есть 46 писем"
	)
	assert (
		locale_manager.get("mails_message", "default", "RU_RU", count=100000001)
		== "У вас есть 100000001 письмо"
	)
	assert (
		locale_manager.translate("You have only three mails", "en", "ru")
		== "У вас всего три письма"
	)
