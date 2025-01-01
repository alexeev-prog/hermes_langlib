# Hermes-LangLib
<a id="readme-top"></a> 

<div align="center">  
  <p align="center">
    Fast, optimized and high-performance, high-load oriented library for i18n and l10n
    <br />
    <a href="./docs/"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="#getting-started">Getting Started</a>
    ·
    <a href="#usage-examples">Basic Usage</a>
    ·
    <a href="#-key-features">Key Features</a>
    ·
    <a href="#-specifications">Specification</a>
    ·
    <a href="https://github.com/alexeev-prog/hermes_langlib/blob/main/LICENSE">License</a>
  </p>
</div>
<br>
<p align="center">
    <img src="https://img.shields.io/github/languages/top/alexeev-prog/hermes_langlib?style=for-the-badge">
    <img src="https://img.shields.io/github/languages/count/alexeev-prog/hermes_langlib?style=for-the-badge">
    <img src="https://img.shields.io/github/license/alexeev-prog/hermes_langlib?style=for-the-badge">
    <img src="https://img.shields.io/github/stars/alexeev-prog/hermes_langlib?style=for-the-badge">
    <img src="https://img.shields.io/github/issues/alexeev-prog/hermes_langlib?style=for-the-badge">
    <img src="https://img.shields.io/github/last-commit/alexeev-prog/hermes_langlib?style=for-the-badge">
    <img src="https://img.shields.io/pypi/l/babel_langlib?style=for-the-badge">
    <img src="https://img.shields.io/pypi/wheel/babel_langlib?style=for-the-badge">
    <img src="https://img.shields.io/badge/coverage-85%25-85%25?style=for-the-badge" alt="">
</p>

Hermes LangLib - a fast and productive python library for translating, localizing and internationalizing your applications. The library is aimed at high speed and stability; it can be used in highly loaded projects.

## Check Other My Projects

 + [SQLSymphony](https://github.com/alexeev-prog/SQLSymphony) - simple and fast ORM in sqlite (and you can add other DBMS)
 + [Burn-Build](https://github.com/alexeev-prog/burn-build) - simple and fast build system written in python for C/C++ and other projects. With multiprocessing, project creation and caches!
 + [OptiArch](https://github.com/alexeev-prog/optiarch) - shell script for fast optimization of Arch Linux
 + [libnumerixpp](https://github.com/alexeev-prog/libnumerixpp) - a Powerful C++ Library for High-Performance Numerical Computing
 + [pycolor-palette](https://github.com/alexeev-prog/pycolor-palette) - display beautiful log messages, logging, debugging.
 + [shegang](https://github.com/alexeev-prog/shegang) - powerful command interpreter (shell) for linux written in C
 + [pyEchoNext](https://github.com/alexeev-prog/pyEchoNext) - EchoNext is a lightweight, fast and scalable web framework for Python.

 <p align="right">(<a href="#readme-top">back to top</a>)</p>

## 📚 Key Features

- Intuitive API: Pythonic, object-oriented interface for interacting with routes and views.
- Comprehensive Documentation: Detailed usage examples and API reference to help you get started.
- Modular Design: Clean, maintainable codebase that follows best software engineering practices.
- Extensive Test Coverage: Robust test suite to ensure the library's reliability and stability.
- Various types of localization storage: you can store localization in JSON, TOML, YAML and INI formats or in RAM.
- Automatic translation: you can enable automatic translation of your localization if the required word is not found.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 🚀 Getting Started

HermesLangLib is available on [PyPI](https://pypi.org/project/hermes_langlib). Simply install the package into your project environment with PIP:

```bash
pip install hermes_langlib
```

Once installed, you can start using the library in your Python projects.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 💻 Usage Examples

### Main Example
Directory tree:

```
├── example.toml
└── locales
    └── default.json
```

Example config-file `example.toml`:

```toml
locale_directory="locales"
default_locale_file="default.json"
default_language="RU_RU"
translator="google"
```

Example locale file `locales/default.json`:

```
{
  "locales": {
    "RU": ["RU_RU"],
    "EN": ["EN_EN", "EN_US"]
  },
  "RU": {
    "RU_RU": {
      "title": "Библиотека для интернационализации",
      "description": "Библиотека, которая позволит переводить ваши приложения",
      "mails_message": {
        "plural": "count",
        "^0$": "У вас нет ни одного письма",
        "11": "У вас есть {count} писем",
        "1$|1$": "У вас есть {count} письмо",
        "^(2|3|4)$|(2|3|4)$": "У вас есть {count} письма",
        "other": "У вас есть {count} писем"
      }
    }
  },
  "EN": {
    "EN_EN": {
      "title": "Library for internationalization",
      "description": "A library that will allow you to translate your applications",
      "mails_message": {
        "plural": "count",
        "^0$": "You do not have any mail.",
        "^1$": "You have a new mail.",
        "other": "You have {count} new mails."
      }
    },
    "EN_US": {
      "title": "Library for internationalization",
      "description": "A library that will allow you to translate your applications",
      "mails_message": {
        "plural": "count",
        "^0$": "You do not have any mail.",
        "^1$": "You have a new mail.",
        "other": "You have {count} new mails."
      }
    }
  }
}
```

Example usage:

```python
from hermes_langlib.locales import LocaleManager
from hermes_langlib.storage import load_config

config = load_config('example.toml')

locale_manager = LocaleManager(config)
print(locale_manager.get('title - {version}', 'default', 'RU_RU', version="0.1.0"))
print(locale_manager.get('title - {version}', 'default', 'RU', version="0.1.0"))
print(locale_manager.get('mails_message.', 'default', 'RU_RU', count=0))
print(locale_manager.get('mails_message', 'default', 'RU_RU', count=1))
print(locale_manager.get('mails_message', 'default', 'RU_RU', count=11))
print(locale_manager.get('mails_message', 'default', 'RU_RU', count=2))
print(locale_manager.get('mails_message', 'default', 'RU_RU', count=22))
print(locale_manager.get('mails_message', 'default', 'RU_RU', count=46))
print(locale_manager.get('mails_message', 'default', 'RU_RU', count=100000001))
print(locale_manager.translate("You have only three mails", "en", 'ru'))
print(locale_manager.translate("У вас всего три письма", "ru", 'en'))
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 🔧 Specifications
The core of your project is the configuration. It can be loaded via a file (TOML, JSON, YAML, INI are supported) or created directly in code.

Loaded via a file:

```python
from hermes_langlib.storage import load_config

config = load_config('example.toml')
```

Or created in code:

```python
from hermes_langlib.storage.base import Config
from hermes_langlib.translators.providers import TranslatorProviders

config = Config(
  config_file = None,
  locale_directory = "locales",
  default_locale_file = "default.json",
  default_language = "RU_RU",
  translator = TranslatorProviders.google
)
```

TranslatorProviders is an enum class with translator providers. To do this, used [deep-translator](https://pypi.org/project/deep-translator):

```python
class TranslatorProvider:
  def __init__(self, translator):
    self.translator = translator

  def __call__(self, source: str, target: str, phrase: str):
    translator = self.translator(source=source, target=target)

    return translator.translate(phrase)
    

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
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 💬 Support
If you encounter any issues or have questions about hermes_langlib, please:

- Check the [documentation](https://alexeev-prog.github.io/hermes_langlib) for answers
- Open an [issue on GitHub](https://github.com/alexeev-prog/hermes_langlib/issues/new)
- Reach out to the project maintainers via the [mailing list](mailto:alexeev.dev@mail.ru)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 🤝 Contributing
We welcome contributions from the community! If you'd like to help improve hermes_langlib, please check out the [contributing guidelines](https://github.com/alexeev-prog/hermes_langlib/blob/main/CONTRIBUTING.md) to get started.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## License
Distributed under the GNU LGPL 2.1 License. See [LICENSE](https://github.com/alexeev-prog/hermes_langlib/blob/main/LICENSE) for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

HermesLangLib is a lightweight, fast and scalable web framework for Python
Copyright (C) 2024  Alexeev Bronislav (C) 2024

This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2.1 of the License, or (at your option) any later version.

This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public
License along with this library; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301
USA
