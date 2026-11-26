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

Sidan är just nu en förhandsversion som Claude Artifact. `index.html` saknar `<html>`/`<head>`/`<body>`-taggar
eftersom Artifact lägger till dem; webbläsare visar den ändå korrekt. När vi väljer host lägger vi till ett fullständigt dokumentskal.
