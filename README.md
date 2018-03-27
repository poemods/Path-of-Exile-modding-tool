# Path of Exile modding and mods

- Search modify compare extract insert replace armour spells microtransactions in any way.
- Restrict and exclude filters to modify only some files.
- Many known mods (.aoc. .otc .epk .pet .atlas .env ...) or create yours.
- Batch process files. Create automods (.txt files with basic filters and commands) to apply all your mods in sequence (see two examples below).
- Resize textures. Textures (.DDS) are decompressed when extracted, ready to feed a DDS optimizer (DDSOpt, ...) to improve both performance and quality.
- Automatic backup. Defragment. Works on all PoE versions, does not depend on Grinding Gear Games updates : file search and file mods rely on Python.re regular expressions
- Any OS. Install [Python 3](https://www.python.org/) and as admin run `pip3 install brotli Wand`.

## TabulaRasa model change for MTX

![Tabula Rasa model change](docs/TabulaRasaMod.png)

*Automod example : Templar Tabula Rasa one-click model change for a microtransaction.*

Create a .txt file with the following commands, put it in the automods folder and it will show up in the program.
```
name "Tabula Rasa model change"
restriction "BodyArmours.*TabulaRasa/BodyTabulaRasaStrInt.sm$"
replacewith "BodyArmours/Microtransactions/DeicideArmour/DeicideArmourStrInt.sm$"
```

## Advanced PoeSmoother

![Advanced PoeSmoother](docs/Scrot.png)

*Another automod : improved Advanced PoeSmoother, does not depend on Gringind Gear Games updates.*

## Create a new mod

#### basic

1. Create a new file in the mods folder named trl_0.py
```
def execute(filename, backupfiledata, modifyggpk):
  filedata, encoding, bom = modifyggpk.stringcleanup(backupfiledata, "UTF-16-LE")
  filedatamod="0"
  return filedatamod, encoding, bom
```
`filedata` is the content of one matching file as a string.
`filedatamod` is the content of the file written back to the Content.ggpk.
This mod is replacing the content of the whole file with a 0.

2. Create a new file in the automods folder named trails.txt
```
name ".trl modification test"
restriction "\.trl$"
execute "trl_0"
```

#### With Python.re

1. Create a new file in the mods folder named aoc_nosound.py
```
import re
def execute(filename, backupfiledata, modifyggpk):
  filedata, encoding, bom = modifyggpk.stringcleanup(backupfiledata, "UTF-16-LE")
  filedatamod=re.sub(r'SoundEvents.*?\{.*?\}', r'SoundEvents\r\n{\r\n}', filedata, flags=re.DOTALL)
  return filedatamod, encoding, bom
```
This mod clears everything between the SoundEvents brackets, if any. See [Python.re documentation](https://docs.python.org/3/library/re.html).

2. Create a new file in the automods folder named removesounds.txt
```
name "remove sounds from aoc"
restriction "\.aoc$"
execute "aoc_nosound"
```

## Autmods commands

Each .txt file put in the automods folder will be shown in the application. All commands are executed in sequence.

1. __name "*xyz*"__
*will show the xyz automod in the app*
2. __title "*first checkbox*"__
*will create a checkbox to apply (or not) everything following, up to the next title (0 or more)*
3. *one or more of these filters :*
   - __restriction "*Python.re regular expression*"__
	 *files matching these filters will be modified*
   - __exclude "*Python.re regexp*"__
	 *files matching these filters will not be modified*
4. *one of these commands :*
   - __execute "*mod_filename_noext*"__
     *executes mod_filename_noext.py that should exist in the mods folder*
   - __replacewith "*Python.re regexp*"__
	 *replaces the file with another one from the game, there should be only one match to this replacewith regexp.*
   - __restore "*Python.re regexp*"__
     *restores the original files matching Python.re regexp*
   - __extract "*Python.re regexp*"__
     *extracts original matching files to the extracted folder*
   - __insert "*Python.re regexp*"__
     *inserts matching files of the extracted folder in the game*

Repeat (3. 4.) if needed. Checkboxes (2.) are optional.

You can check your regular expressions in the app's restrict/exclude filter fields, with the Search button. All of these regexp ignore case : Python.re's `flags=re.IGNORECASE` is set. Folder separator has to be `/`.
