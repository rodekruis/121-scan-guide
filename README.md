# 121 Scan help

The user guide for 121 Scan, in English and Arabic (French to follow), published with GitHub Pages at
`https://rodekruis.github.io/121-scan-guide/`.

Button names and on-screen messages are copied from the app every night, so the guide always uses the
app's current wording in each language. The instructions themselves are written by people.

## Setup (once)

1. Create the public repo `rodekruis/121-scan-guide` and upload these files.
2. **Settings → Pages → Source: GitHub Actions.**
3. **Actions → Publish help site → Run workflow.** The site is live a minute or two later.

That's all: no keys or tokens. (If `scandroid` is ever made private, the workflow will need a read-only
token to copy the app's text.)

## Everyday tasks

**Edit a page:** open the file in `content/en/` or `content/ar/` on GitHub, click the pencil, save. The site
updates within minutes. Write `{{ app.some_key }}` instead of typing a button name, so it stays in step with
the app. The keys are in `data/app_text.json`.

**Add screenshots:** `screens-needed.md` lists every picture slot still empty. Save each picture under
`assets/screens/<language>/<name>.png`. The page uses it automatically.

**Explain a new message:** add it to `data/messages.yml`. Never rename an `id`: the app's Help links point to them.

**After checking the guide against an app change:** update `checked.json` with the latest scandroid commit and
today's date. The instances page and the guide's footer both read it.

**Add French:** copy `content/en/` to `content/fr/`, translate, add the French explanations to
`data/messages.yml`, and add `fr` to `langs` in `data/pages.yml`.

## Files

- `content/<lang>/`: the page texts. `data/pages.yml`: page order and fixed addresses.
- `data/ui.yml`: the guide's own wording. `data/messages.yml`: what each message means and what to do.
- `data/app_text.json`: the app's text (refreshed nightly by `scripts/sync_app_text.py`).
- `templates/`, `assets/`: page design. `build.py`: turns all of this into the site.
- `checked.json`: the scandroid commit the guide was last checked against.

To build locally: `pip install -r requirements.txt`, then `python build.py --preview` and open `preview.html`.
