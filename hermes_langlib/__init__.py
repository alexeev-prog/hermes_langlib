"""
Hermes is a lightweight, fast and scalable web framework for Python
Copyright (C) 2024	Alexeev Bronislav (C) 2024.

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
"""  # noqa: D205

import requests
from rich import print  # noqa: A004
from rich.traceback import install

__version__ = "0.3.0"
install(show_locals=True)


def check_for_update():
    """Check for update in pypi."""
    try:
        response = requests.get("https://pypi.org/pypi/hermes_langlib/json").json()  # noqa: S113

        latest_version = response["info"]["version"]

        latest_digits = [int(n) for n in latest_version.split(".")]
        current_digits = [int(n) for n in __version__.split(".")]

        if sum(latest_digits) > sum(current_digits):
            message = (
                f"New version of library hermes_langlib available: {latest_version}"
            )

            print(
                f"[red]{'#' * (len(message) + 4)}\n#[/red][bold yellow] {message} [/bold yellow][red]#\n{'#' * (len(message) + 4)}[/red]\n"  # noqa: E501
            )
        elif sum(latest_digits) < sum(current_digits):
            print(
                f"[yellow]You use [bold]UNSTABLE[/bold] branch of hermes_langlib. Stable version: {latest_version}, your version: {__version__}[/yellow]\n"  # noqa: E501
            )
    except (requests.RequestException, KeyError):
        print(
            f"[dim]Version updates information not available. Your version: {__version__}[/dim]"  # noqa: E501
        )

    return True


check_for_update()
