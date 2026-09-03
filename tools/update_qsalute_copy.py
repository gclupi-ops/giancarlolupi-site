from pathlib import Path

path = Path(__file__).resolve().parents[1] / "index.html"
text = path.read_text(encoding="utf-8")

text = text.replace(
    '<span>Neurochirurgia di Pisa · non recensioni personali</span>',
    '<span>Neurochirurgia di Pisa · esperienze dei pazienti</span>'
)

text = text.replace(
    'testimonianze pubblicate sulla pagina QSalute della Neurochirurgia di Pisa, dato rilevato il 3 settembre 2026. Non sono recensioni personali del Dott. Giancarlo Lupi e non costituiscono una misura di efficacia clinica.',
    'testimonianze pubblicate sulla pagina QSalute della Neurochirurgia di Pisa, dato rilevato il 3 settembre 2026. La sintesi raccoglie i temi che ricorrono più frequentemente nei racconti dei pazienti.'
)

text = text.replace(
    '>Fonte esterna: QSalute ↗</a>',
    '>Leggi le testimonianze su QSalute ↗</a>'
)

path.write_text(text, encoding="utf-8")
print("Copy QSalute aggiornato")
