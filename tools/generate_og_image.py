from pathlib import Path
import re
import subprocess

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
ASSET = ROOT / "assets" / "og-image.jpg"
SITE = "https://www.giancarlolupi.com"
OG_URL = f"{SITE}/assets/og-image.jpg"
OG_ALT = "Giancarlo Lupi, neurochirurgo — Pisa, Ponsacco, Massa"

PUBLIC_HTML = [
    ROOT / "index.html",
    ROOT / "colonna.html",
    ROOT / "neurochirurgia.html",
    ROOT / "medico.html",
    ROOT / "cv-pubblicazioni.html",
    ROOT / "seconda-opinione.html",
    ROOT / "documentazione-clinica.html",
    ROOT / "approfondimenti.html",
    ROOT / "rassegna-stampa.html",
    ROOT / "sedi.html",
    ROOT / "privacy.html",
    ROOT / "404.html",
    ROOT / "approfondimenti" / "mal-di-schiena-quando-preoccuparsi.html",
    ROOT / "approfondimenti" / "risonanza-mal-di-schiena.html",
    ROOT / "approfondimenti" / "robotica-neurochirurgia.html",
]


def font_file(pattern: str, fallback: str) -> str:
    try:
        found = subprocess.check_output(
            ["fc-match", "-f", "%{file}", pattern], text=True
        ).strip()
        if found and Path(found).exists():
            return found
    except Exception:
        pass
    return fallback


LORA = font_file("Lora:style=Regular", "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf")
LORA_BOLD = font_file("Lora:style=Semibold", "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf")
CARLITO = font_file("Carlito:style=Regular", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
CARLITO_BOLD = font_file("Carlito:style=Bold", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf")


def draw_tracking(draw, xy, text, font, fill, spacing):
    x, y = xy
    for char in text:
        draw.text((x, y), char, font=font, fill=fill)
        x += draw.textlength(char, font=font) + spacing
    return x


def generate_image():
    width, height = 1200, 630
    deep = "#0d2032"
    blue = "#0a72c7"
    white = "#ffffff"
    pale = "#d9e3ea"
    muted = "#9fb1bf"
    rule = "#456075"

    image = Image.new("RGB", (width, height), deep)
    draw = ImageDraw.Draw(image)

    # Barra d'accento, coerente con il token --blue-2 del sito.
    draw.rectangle((0, 0, 14, height), fill=blue)

    # Monogramma GL: cerchio chiaro, bordo sottile, serif come nell'header.
    cx, cy, r = 105, 105, 43
    draw.ellipse((cx-r, cy-r, cx+r, cy+r), fill=white, outline="#8f989f", width=2)
    mono_font = ImageFont.truetype(LORA_BOLD, 29)
    box = draw.textbbox((0, 0), "GL", font=mono_font)
    tw, th = box[2] - box[0], box[3] - box[1]
    draw.text((cx - tw/2, cy - th/2 - 2), "GL", font=mono_font, fill=deep)

    name_font = ImageFont.truetype(LORA, 67)
    label_font = ImageFont.truetype(CARLITO_BOLD, 22)
    city_font = ImageFont.truetype(CARLITO, 26)
    domain_font = ImageFont.truetype(CARLITO, 19)

    draw.text((182, 62), "Giancarlo Lupi", font=name_font, fill=white)
    draw_tracking(draw, (184, 154), "NEUROCHIRURGO · MD PHD", label_font, pale, 3.2)

    # Filetto editoriale.
    draw.line((76, 276, 1124, 276), fill=rule, width=1)

    draw_tracking(draw, (78, 335), "PISA · PONSACCO · MASSA", city_font, white, 2.0)

    # Firma di dominio discreta in basso a destra.
    domain = "www.giancarlolupi.com"
    db = draw.textbbox((0, 0), domain, font=domain_font)
    dw = db[2] - db[0]
    draw.text((1122 - dw, 552), domain, font=domain_font, fill=muted)

    ASSET.parent.mkdir(parents=True, exist_ok=True)
    image.save(ASSET, "JPEG", quality=88, optimize=True, progressive=True, subsampling=2)


def update_og_metadata(text: str) -> str:
    text = re.sub(
        r'<meta property="og:image" content="[^"]*">',
        f'<meta property="og:image" content="{OG_URL}">',
        text,
        count=1,
    )
    text = re.sub(
        r'<meta property="og:image:width" content="[^"]*">',
        '<meta property="og:image:width" content="1200">',
        text,
        count=1,
    )
    text = re.sub(
        r'<meta property="og:image:height" content="[^"]*">',
        '<meta property="og:image:height" content="630">',
        text,
        count=1,
    )
    text = re.sub(
        r'<meta property="og:image:alt" content="[^"]*">',
        f'<meta property="og:image:alt" content="{OG_ALT}">',
        text,
        count=1,
    )

    if 'property="og:image:type"' not in text:
        text = text.replace(
            '<meta property="og:image:height" content="630">',
            '<meta property="og:image:height" content="630"><meta property="og:image:type" content="image/jpeg">',
            1,
        )
    else:
        text = re.sub(
            r'<meta property="og:image:type" content="[^"]*">',
            '<meta property="og:image:type" content="image/jpeg">',
            text,
            count=1,
        )
    return text


def main():
    generate_image()
    for path in PUBLIC_HTML:
        text = path.read_text(encoding="utf-8")
        updated = update_og_metadata(text)
        path.write_text(updated, encoding="utf-8")
    print(f"Generated {ASSET.relative_to(ROOT)} and updated {len(PUBLIC_HTML)} HTML files")


if __name__ == "__main__":
    main()
