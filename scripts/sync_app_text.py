#!/usr/bin/env python3
"""Copy 121 Scan's on-screen text (English, French, Arabic) into the guide.

Reads the `translations` dictionary from scandroid's app.py WITHOUT running the
app (it is parsed as text), and writes data/app_text.json. The guide then uses
these exact words for buttons and messages, so a renamed button in the app is
renamed in the guide automatically, in all three languages.

    python scripts/sync_app_text.py path/to/scandroid
"""

import ast
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main():
    src = Path(sys.argv[1] if len(sys.argv) > 1 else "src")
    tree = ast.parse((src / "app.py").read_text(encoding="utf-8"))
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
            isinstance(t, ast.Name) and t.id == "translations" for t in node.targets
        ):
            data = ast.literal_eval(node.value)
            break
    else:
        sys.exit("translations not found in app.py — the app's structure changed.")

    out = {lang: data[lang] for lang in ("en", "fr", "ar") if lang in data}

    # Facts the guide quotes that live in the code rather than in the text.
    m = re.search(r"const\s+MIN_PREFIX\s*=\s*(\d+)", (src / "templates" / "scan.html").read_text(encoding="utf-8"))
    if not m:
        sys.exit("MIN_PREFIX not found in templates/scan.html — the app's structure changed.")
    out["facts"] = {"min_prefix": int(m.group(1))}
    (ROOT / "data").mkdir(exist_ok=True)
    (ROOT / "data" / "app_text.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8"
    )
    print("app text:", {k: len(v) for k, v in out.items()})


if __name__ == "__main__":
    main()
