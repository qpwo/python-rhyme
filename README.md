## Python Rhyme

![screenshot](limericks.png)

This is a simple set of tools for grabbing words with a certain number of syllables or words that rhyme, etc.

Example program `example.py` that uses code:

```python
import rhyme

print(rhyme.makeLimerick().lower())

print("Beware of the devil.")
for word in rhyme.getRhymes("DEVIL"):
  print("He will make you " + word.lower() + '.')
```

Then of course you can run it with `python3 example.py` in a terminal.

`rhyme.py` is self-documenting.

Phonetic dictionary obtained from [here](http://www.speech.cs.cmu.edu/cgi-bin/cmudict).
