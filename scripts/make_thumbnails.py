
from pathlib import Path
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "images"
DEST = ROOT / "thumbnails"
DEST.mkdir(exist_ok=True)

EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".gif"}
EXCLUDED = {"KevinMiller.jpg"}

for path in SOURCE.iterdir():
    if not path.is_file():
        continue
    if path.suffix.lower() not in EXTENSIONS:
        continue
    if path.name in EXCLUDED:
        continue

    output = DEST / (path.name + ".webp")

    with Image.open(path) as original:
        image = ImageOps.exif_transpose(original)
        image.thumbnail((900, 900))

        if image.mode not in ("RGB", "RGBA"):
            image = image.convert("RGBA")

        image.save(output, "WEBP", quality=78, method=6)

    print(f"Created {output.name}")
