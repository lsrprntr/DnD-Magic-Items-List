# D&D Magic Items List

This scrapes all magic items from the D&D Beyond Magic Items pages and outputs it into a JSON:
```
[
  {
    "id": "2188377",
    "name": "Abracadabrus",
    "rarity": "Very Rare",
    "type": "Wondrous Item"
  },
  {
    "id": "2400459",
    "name": "Absorbing Tattoo",
    "rarity": "Very Rare",
    "type": "Wondrous Item"
  },
  {
    "id": "1434250",
    "name": "Acheron Blade",
    "rarity": "Rare",
    "type": "Weapon"
  },
  {
    "id": "5370",
    "name": "Adamantine Armor",
    "rarity": "Uncommon",
    "type": "Armor"
  },
  ...
]
```

## To do / Improvements

- Add source book detail
- Make a magic_item class
- ~~Add master JSON~~
- Rewrite parsePage function to return a list of dict rather than depend on global variable
- Rewrite fetchPage function to not depend on global variable
