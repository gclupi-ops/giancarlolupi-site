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


def font_file(family: str, style: str, fallback: str) -> str:
    """Usa il font richiesto solo se fc-match conferma davvero quella famiglia."""
    try:
        match = subprocess.check_output(
            ["fc-match", "-f", "%{family}|%{file}", f"{family}:style={style}"],
            text=True,
        ).strip()
        matched_family, found = match.split("|", 1)
        if family.lower() in matched_family.lower() and found and Path(found).exists():
            return found
    except Exception:
        pass
    return fallback


SERIF = font_file(
    "Lora", "Regular", "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
)
SERIF_BOLD = font_file(
    "Lora", "Semibold", "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
)
SANS = font_file(
    "Carlito", "Regular", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
)
SANS_BOLD = font_file(
    "Carlito", "Bold", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
)


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

    # Barra d'accento verticale, come nel visual approvato.
    draw.rectangle((0, 0, 20, height), fill=blue)

    # Monogramma GL, coerente con l'header del sito.
    cx, cy, r = 151, 154, 51
    draw.ellipse(
        (cx - r, cy - r, cx + r, cy + r),
        fill=white,
        outline="#8f989f",
        width=2,
    )
    mono_font = ImageFont.truetype(SERIF_BOLD, 31)
    box = draw.textbbox((0, 0), "GL", font=mono_font)
    tw, th = box[2] - box[0], box[3] - box[1]
    draw.text((cx - tw / 2, cy - th / 2 - 3), "GL", font=mono_font, fill=deep)

    name_font = ImageFont.truetype(SERIF, 74)
    label_font = ImageFont.truetype(SANS_BOLD, 25)
    city_font = ImageFont.truetype(SANS, 27)
    domain_font = ImageFont.truetype(SANS, 19)

    draw.text((151, 250), "Giancarlo Lupi", font=name_font, fill=white)
    draw_tracking(
        draw,
        (153, 357),
        "NEUROCHIRURGO · MD PHD",
        label_font,
        pale,
        3.2,
    )

    # Filetto editoriale sottile.
    draw.line((151, 423, 1050, 423), fill=rule, width=1)

    draw_tracking(
        draw,
        (151, 505),
        "PISA · PONSACCO · MASSA",
        city_font,
        white,
        1.8,
    )

    domain = "www.giancarlolupi.com"
    db = draw.textbbox((0, 0), domain, font=domain_font)
    dw = db[2] - db[0]
    draw.text((1050 - dw, 512), domain, font=domain_font, fill=muted)

    ASSET.parent.mkdir(parents=True, exist_ok=True)
    image.save(
        ASSET,
        "JPEG",
        quality=90,
        optimize=True,
        progressive=True,
        subsampling=2,
    )


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
        path.write_text(update_og_metadata(text), encoding="utf-8")
    print(f"Generated {ASSET.relative_to(ROOT)} and updated {len(PUBLIC_HTML)} HTML files")


if __name__ == "__main__":
    main()
