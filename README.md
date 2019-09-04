# TraceryCounter
Count the number of possible traces of Tracery grammars.

This script runs over all children and expands all their variables in order to count them.

## Usage
### Simplest:

```
python tracerycounter.py yourGrammarFile.json
```

### More 'advanced':

Optionally, run it with the`-o` parameter to use a starting node different from the default `origin`.

```
python tracerycounter.py yourGrammarFile.json -o someOtherOrigin
```
