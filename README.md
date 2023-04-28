# GachiTyper

GachiTyper is an AutoHotkey script generator written in Python. It generates scripts with hotstrings from substitution lists (like [GachiTyperCombinedSubsList.txt](GachiTyperCombinedSubsList.txt)).

Currently there are 3 substitution lists:

- [GachiRemixerSubsList.txt](GachiRemixerSubsList.txt) - tries to natively gachi-remix anything you type.
- [GachiShortcutterSubsList.txt](GachiShortcutterSubsList.txt) - contains shortcuts for gachi phrases like ♂Do you like what you see?♂ and ♂get your ass back here♂.
- [GachiTyperCombinedSubsList.txt](GachiTyperCombinedSubsList.txt) - tries to combine gachi-remixing with shortcuts.

Generated scripts can be disabled via `!!gachi off` or `!!гачи офф` and enabled via `!!gachi on` or `!!гачи он`.

## Generated script features

- Works in most programs and even in some games (e.g. Path of Exile)
- Doesn't require administrator rights
- Can be disabled and enabled
- Doesn't require anything (if run via .exe file)

## Quickstart guide

`cd` to the repo root folder and call `src/Main.py -c` to generate and compile all scripts.

Use `-h` or `--help` for more info.

## Requirements

- Python 3 (tested on 3.11)
- [AutoHotkey script compiler](https://github.com/AutoHotkey/Ahk2Exe) (for compilation to .exe)
