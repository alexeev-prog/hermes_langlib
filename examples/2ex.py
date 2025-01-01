from hermes_langlib.locales import LocaleManager
from hermes_langlib.storage import load_config

config = load_config("example.toml")

locale_manager = LocaleManager(config)
print(locale_manager.get("title - {version}", "default", "RU_RU", version="0.1.0"))
print(locale_manager.get("title - {version}", "default", "RU", version="0.1.0"))
print(locale_manager.get("mails_message.", "default", "RU_RU", count=0))
print(locale_manager.get("mails_message", "default", "RU_RU", count=1))
print(locale_manager.get("mails_message", "default", "RU_RU", count=11))
print(locale_manager.get("mails_message", "default", "RU_RU", count=2))
print(locale_manager.get("mails_message", "default", "RU_RU", count=22))
print(locale_manager.get("mails_message", "default", "RU_RU", count=46))
print(locale_manager.get("mails_message", "default", "RU_RU", count=100000001))
print(locale_manager.translate("You have only three mails", "en", "ru"))
print(locale_manager.translate("У вас всего три письма", "ru", "en"))
