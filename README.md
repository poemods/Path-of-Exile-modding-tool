# Path of Exile modding and mods

- Search modify compare extract insert replace armour spells microtransactions in any way.
- Restrict and exclude filters to modify only some files.
- Many known mods (.aoc. .otc .epk .pet .atlas .env ...) or create yours.
- Batch process files. Create automods (.txt files with basic filters and commands) to apply all your mods in sequence (see two examples below).
- Resize textures. Textures (.DDS) are decompressed when extracted, ready to feed a DDS optimizer (DDSOpt, ...) to improve both performance and quality.
- Automatic backup. Defragment. Any OS (Python 3). Works on all PoE versions, does not depend on GGG updates.

## TabulaRasa model change for MTX
![Tabula Rasa model change](docs/TabulaRasaMod.png)

*Automod example : Templar Tabula Rasa one-click model change for a microtransaction.*

Create a .txt file with the following commands, put it in the automods folder and it will show up in the program.
```
name "Tabula Rasa model change"
restriction "BodyArmours.*TabulaRasa/BodyTabulaRasaStrInt.sm"
replacewith "BodyArmours/Microtransactions/DeicideArmour/DeicideArmourStrInt.sm"
```

## Advanced PoeSmoother
![Advanced PoeSmoother](docs/Scrot.png)

*Another automod : improved Advanced PoeSmoother, does not depend on Gringind Gear Games updates (file search and file mods rely on Python.re regular expressions).*
