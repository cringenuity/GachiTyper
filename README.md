# GachiTyper

GachiTyper is an AutoHotkey script generator written in Python. It generates scripts with hotstrings from substitution lists (like [GachiTyperCombined.txt](substitution_lists/GachiTyperCombined.txt)).

Currently there are 3 substitution lists:

- [GachiRemixer.txt](substitution_lists/GachiRemixer.txt) - tries to natively gachi-remix anything you type.
- [GachiShortcutter.txt](substitution_lists/GachiShortcutter.txt) - contains shortcuts for gachi phrases like ♂Do you like what you see?♂ and ♂get your ass back here♂.
- [GachiTyperCombined.txt](substitution_lists/GachiTyperCombined.txt) - tries to combine gachi-remixing with shortcuts.

Generated scripts can be disabled via `!!gachi off` or `!!гачи офф` and enabled via `!!gachi on` or `!!гачи он`.

## Generated script features

- Works in most programs and even in some games (e.g. Path of Exile)
- Doesn't require administrator rights
- Can be disabled and enabled
- Doesn't require anything (if run via .exe file)

## Quickstart guide

`cd` to the repo root folder and call `make` to generate and compile all scripts.

Use `-h` or `--help` for more info.

## Requirements

- Python 3 (tested on 3.11)
- [AutoHotkey script compiler](https://github.com/AutoHotkey/Ahk2Exe) (for compilation to .exe)
- GNU Make
