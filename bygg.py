"""Bygger webbplatsen för GitHub Pages i mappen docs/.

index.html och handritad.html är skrivna för förhandsvisning i Claude, som själv lägger till
<!doctype>, <head> och <body>. Det här skriptet lägger till dem och kopierar bilderna, så att
docs/ blir en vanlig, fristående webbplats.

Kör:  python3 bygg.py
"""
import pathlib
import shutil

ROT = pathlib.Path(__file__).parent
UT = ROT / "docs"
SIDOR = ["index.html", "handritad.html"]
# Gamla adresser som skickas vidare till huvudsidorna
OMDIRIGERA = {"karta-mork.html": "./", "index-tidigare.html": "./", "handritad-tidigare.html": "handritad.html"}

GRUND = """<style>
:root { box-sizing: border-box; padding-top: env(safe-area-inset-top, 0px); padding-bottom: env(safe-area-inset-bottom, 0px); }
body { margin: 0; }
img { max-width: 100%; }
[hidden] { display: none !important; }
</style>"""


def bygg_sida(kalla: str) -> str:
    # Allt fram till och med första </style> (titel, meta, typsnitt, stil) hör hemma i <head>.
    slut = kalla.index("</style>") + len("</style>")
    huvud, kropp = kalla[:slut], kalla[slut:]
    huvud = huvud.replace('<meta charset="utf-8">\n', "")
    return (
        "<!doctype html>\n<html lang=\"sv\">\n<head>\n"
        "<meta charset=\"utf-8\">\n"
        "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, viewport-fit=cover\">\n"
        f"{GRUND}\n{huvud}\n</head>\n<body>\n{kropp.strip()}\n</body>\n</html>\n"
    )


def main() -> None:
    if UT.exists():
        shutil.rmtree(UT)
    UT.mkdir()
    for namn in SIDOR:
        (UT / namn).write_text(bygg_sida((ROT / namn).read_text(encoding="utf-8")), encoding="utf-8")
    shutil.copytree(ROT / "bilder", UT / "bilder")
    for gammal, ny in OMDIRIGERA.items():
        (UT / gammal).write_text(
            f'<!doctype html><meta charset="utf-8"><meta http-equiv="refresh" content="0; url={ny}">'
            f'<link rel="canonical" href="{ny}"><title>Paraden</title><a href="{ny}">Paraden</a>\n', encoding="utf-8")
    (UT / ".nojekyll").write_text("")
    print("Klart:", ", ".join(str(p.relative_to(ROT)) for p in sorted(UT.rglob("*")) if p.is_file()))


if __name__ == "__main__":
    main()
