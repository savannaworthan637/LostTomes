
#### main.py

```python
#!/usr/bin/env python3
import random

tomes = [
    "The Black Codex – A book that writes itself with forgotten knowledge each full moon.",
    "The Celestial Ledger – Said to contain the names of those destined to become gods.",
    "The Ashen Grimoire – A cursed book that burns the hands of those who try to read it.",
    "The Tome of Silent Echoes – Holds whispers of the dead, but only the mad can understand them.",
    "The Veilbound Chronicle – A book that can only be read in dreams, revealing forgotten truths."
]

def get_random_tome():
    return random.choice(tomes)

def main():
    print("Welcome to Lost Tomes!")
    print("Here is a randomly generated ancient book and its legend:")
    print(get_random_tome())

if __name__ == "__main__":
    main()
