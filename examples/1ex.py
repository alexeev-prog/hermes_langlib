from hermes_langlib.storage.locale_store import LocaleStorage

ls2 = LocaleStorage("locales/default.json")
print(ls2.get_supported_locales())

ls3 = LocaleStorage("locales/default.json")
print(ls3.get_supported_locales(dictionary_for_default=True))

ls1 = LocaleStorage("locales/default2.json")
print(ls1.get_supported_locales())
