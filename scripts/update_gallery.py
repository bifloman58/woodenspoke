"""Keep the Work gallery in upload order, newest additions first."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IMAGES = ROOT / "images"
MANIFEST = ROOT / "gallery.json"
EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".gif", ".avif"}
EXCLUDED = {"KevinMiller.jpg"}

existing = json.loads(MANIFEST.read_text(encoding="utf-8")) if MANIFEST.exists() else []
found = {f"images/{p.name}" for p in IMAGES.iterdir() if p.is_file() and p.suffix.lower() in EXTENSIONS and p.name not in EXCLUDED}
# New filenames sort consistently within a single upload batch.
new = sorted(found - set(existing), key=str.lower)
ordered = new + [path for path in existing if path in found]
MANIFEST.write_text(json.dumps(ordered, indent=2) + "\n", encoding="utf-8")
print(f"Gallery contains {len(ordered)} photos; {len(new)} newly added.")
