# Paraden

Hemsida för konstverket PARADEN: ett deltagarbaserat konstverk i mötet mellan kropp, skulptur och koreografi.

## Filer

- `index.html`: hela sidan (stil, innehåll och skript i en fil).
- `bilder/`: bilder. Bilderna i galleriet är exempelbilder tills riktiga finns.

## Ändra platser, film och bilder

Platserna ligger i listan `PLACES` i skriptet längst ner i `index.html`. För varje plats finns:

- `ort`, `lokal`, `lat`/`lon` (position på kartan) och `besok` (datum).
- `video`: sökväg till en `.mp4`-fil, eller `null` för en platshållare.
- `rum`: bilder på rummet.
- `portratt`: porträtt av deltagarna.

## Publicering

`index.html` och `handritad.html` är källfilerna. De är skrivna för förhandsvisning i Claude och saknar
därför `<html>`/`<head>`/`<body>`.

Webbplatsen för GitHub Pages byggs i mappen `docs/`:

```
python3 bygg.py
```

Skriptet lägger till sidans skal och kopierar bilderna. Kör det efter varje ändring och committa `docs/`.

Adresser när GitHub Pages är påslaget (källa: grenen med koden, mappen `/docs`):

- https://olssonjoakim-hub.github.io/Paraden/
- https://olssonjoakim-hub.github.io/Paraden/handritad.html
