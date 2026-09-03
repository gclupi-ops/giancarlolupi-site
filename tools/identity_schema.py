from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
PHYSICIAN_ID = "https://www.giancarlolupi.com/#physician"
SAME_AS = [
    "https://www.miodottore.it/giancarlo-lupi-2/neurochirurgo/empoli",
    "https://www.medicitalia.it/g.lupi/",
]

TARGETS = [ROOT / "index.html", ROOT / "medico.html"]


def is_identity_schema(data):
    if not isinstance(data, dict):
        return False
    if data.get("@id") == PHYSICIAN_ID:
        return True
    types = data.get("@type", [])
    if isinstance(types, str):
        types = [types]
    if "ProfilePage" in types:
        return True
    if "Physician" in types and data.get("name") == "Giancarlo Lupi":
        return True
    graph = data.get("@graph")
    return isinstance(graph, list) and any(is_identity_schema(item) for item in graph)


def strip_identity_schema(text):
    def repl(match):
        raw = match.group(1).strip()
        try:
            data = json.loads(raw)
        except json.JSONDecodeError:
            return match.group(0)
        return "" if is_identity_schema(data) else match.group(0)

    return re.sub(
        r'<script type="application/ld\+json">(.*?)</script>',
        repl,
        text,
        flags=re.I | re.S,
    )


def script_tag(data):
    return '<script type="application/ld+json">' + json.dumps(
        data, ensure_ascii=False, separators=(",", ":")
    ) + "</script>"


def physician_schema():
    return {
        "@context": "https://schema.org",
        "@type": ["Person", "Physician"],
        "@id": PHYSICIAN_ID,
        "name": "Giancarlo Lupi",
        "jobTitle": "Neurochirurgo",
        "medicalSpecialty": "Neurosurgery",
        "url": "https://www.giancarlolupi.com/",
        "image": "https://www.giancarlolupi.com/assets/giancarlo-lupi-profile.webp",
        "areaServed": ["Pisa", "Ponsacco", "Massa"],
        "sameAs": SAME_AS,
    }


def profile_page_schema():
    return {
        "@context": "https://schema.org",
        "@type": "ProfilePage",
        "@id": "https://www.giancarlolupi.com/medico.html#profile",
        "url": "https://www.giancarlolupi.com/medico.html",
        "name": "Giancarlo Lupi — profilo professionale",
        "mainEntity": {"@id": PHYSICIAN_ID},
    }


def update(path):
    text = path.read_text(encoding="utf-8")
    text = strip_identity_schema(text)
    tags = script_tag(physician_schema())
    if path.name == "medico.html":
        tags += script_tag(profile_page_schema())
    text = text.replace("</head>", tags + "</head>", 1)
    path.write_text(text, encoding="utf-8")


for target in TARGETS:
    update(target)

print("Schema identità aggiornato su index.html e medico.html")
