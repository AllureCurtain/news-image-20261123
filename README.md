# The World in One Day — Monday, 23 November 2026

Entry for the make.fun bounty **news-image-20261123**: sum up 23 November
2026's world news in one image.

## What the image shows

A newspaper front page, "THE WORLD IN ONE DAY — MONDAY, 23 NOVEMBER 2026",
built around an illustration of the day's biggest scenes: a cargo ship
burning at sea off a cold northern coast, the Earth, and a summit hall
lined with flags. The stories on the page, all reported on 23 November 2026:

- **COP31 collapses: no deal on climate** — talks in Antalya end without
  agreement after the final draft drops any mention of fossil fuels, and
  the EU rejects the pact.
- **War widens in the Gulf** — Iran hits a US base in Bahrain and a Houthi
  missile aimed at Saudi Arabia is intercepted as the Strait of Hormuz
  conflict spreads.
- **Ship ablaze off Finland** — a Russian cargo ship is still burning after
  an attack, and 14 are missing after a Russian drone hits a building near
  Kyiv.
- **Factory fire in Indonesia** — seven bodies recovered and 50 people
  missing after a blaze at a candy factory.
- **Mexico nabs cartel boss** — troops capture FBI most-wanted
  "El Chapo Isidro" after gunfights in Sinaloa leave 11 dead.
- **Also today** — the UN agrees to keep negotiating curbs on lethal AI
  weapons; South Korea's education minister quits over an AI exam-cheating
  scandal; Nepal's PM meets Modi in Delhi; India posts a record 720/9 in
  the Wellington Test; the Democrats clinch a House majority of at least
  258 seats.

## How it runs

`main.py` (Python 3.13, standard library only) copies the image the
repository holds to `/output/entry.png`. No network, no randomness, no
clock — both runs write the same bytes.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

The image is a PNG, 1024x1024, under 1 MiB.

## License

MIT — see `LICENSE`.
