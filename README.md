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

### Kommande nedslag

Kommande besök får en enklare sida med kort text och en bild. Fyll i `info` (texten) och `bild`
(sökväg, t.ex. `bilder/weld.jpg`) på besöket i `PLACES`. Tomma fält ger en standardtext och en
platshållare. Gör ändringen i både `index.html` och `handritad.html`.

Just nu går kommande nedslag inte att klicka på (`KOMMANDE_KLICKBARA = false`). Sätt den till
`true` i båda filerna för att visa deras sidor igen.

## Publicering

`index.html` och `handritad.html` är källfilerna. De är skrivna för förhandsvisning i Claude och saknar
därför `<html>`/`<head>`/`<body>`.

Webbplatsen för GitHub Pages byggs i mappen `docs/`:

```
python3 bygg.py
```

Skriptet lägger till sidans skal och kopierar bilderna. Kör det efter varje ändring och committa `docs/`.

Huvudversioner (bara dessa två utvecklas vidare):

- https://olssonjoakim-hub.github.io/Paraden/ (mörk karta)
- https://olssonjoakim-hub.github.io/Paraden/handritad.html (samma sida, handskrivet typsnitt)

`handritad.html` ska vara identisk med `index.html` utom typsnitten och de handritade linjerna
(skisslinjer, ramar runt bilder, play-ikonen och ringarna på kartan). Gör ändringar i båda.

Äldre versioner ligger i `arkiv/` och byggs inte. Deras gamla adresser (karta-mork.html,
index-tidigare.html, handritad-tidigare.html) skickas vidare till huvudsidorna.
