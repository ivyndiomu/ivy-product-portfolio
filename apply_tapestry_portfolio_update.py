#!/usr/bin/env python3
from pathlib import Path
import shutil
import sys
import re

PORTFOLIO = Path.cwd()
SOURCE = None

if len(sys.argv) > 1:
    SOURCE = Path(sys.argv[1]).expanduser().resolve()
else:
    candidates = [
        PORTFOLIO.parent / "tapestry-crochet-studio",
        PORTFOLIO.parent / "Tapestry Crochet Studio",
        PORTFOLIO.parent / "tapestry-crochet-studio-public-repo",
    ]
    for candidate in candidates:
        if (candidate / "screenshots").exists():
            SOURCE = candidate
            break

if SOURCE is None or not (SOURCE / "screenshots").exists():
    print("Could not find the Tapestry Crochet Studio screenshots folder.")
    print("Run the script again and pass the repository path, for example:")
    print('python3 apply_tapestry_portfolio_update.py "../tapestry-crochet-studio"')
    sys.exit(1)

home_file = PORTFOLIO / "index.html"
case_file = PORTFOLIO / "work" / "tapestry-crochet-studio" / "index.html"
if not home_file.exists() or not case_file.exists():
    print("Run this script from the root of the ivy-product-portfolio repository.")
    sys.exit(1)

img_dir = PORTFOLIO / "assets" / "img" / "tapestry"
img_dir.mkdir(parents=True, exist_ok=True)

selected = {
    "Home screen.png": "home-screen.png",
    "Imported artwork.png": "imported-artwork.png",
    "Image-to-grid conversion.png": "image-to-grid-conversion.png",
    "Background removal controls.png": "background-removal-controls.png",
    "Garment designer.png": "garment-designer.png",
    "Front panel.png": "front-panel.png",
    "Back panel.png": "back-panel.png",
    "Left sleeve.png": "left-sleeve.png",
    "Right sleeve.png": "right-sleeve.png",
    "Production mode_row focus.png": "production-row-focus.png",
    "Written instructions.png": "written-instructions.png",
    "Yarn intelligence.png": "yarn-intelligence.png",
    "Export page 1.png": "export-page.png",
}

missing = []
for source_name, dest_name in selected.items():
    src = SOURCE / "screenshots" / source_name
    dst = img_dir / dest_name
    if src.exists():
        shutil.copy2(src, dst)
    else:
        missing.append(source_name)

css_file = PORTFOLIO / "assets" / "css" / "tapestry-media.css"
css_file.write_text(r'''
/* Tapestry Crochet Studio product evidence */
.case-media {
  margin: 30px 0 34px;
}
.case-media img,
.project-art-image img,
.hero-product-shot {
  width: 100%;
  display: block;
}
.case-media img {
  border: 1px solid var(--line);
  border-radius: 18px;
  background: var(--white);
  box-shadow: 0 14px 42px rgba(24,35,30,.07);
}
.case-media figcaption {
  margin-top: 10px;
  color: var(--muted);
  font-size: .86rem;
  line-height: 1.5;
}
.media-grid-2,
.media-grid-4 {
  display: grid;
  gap: 14px;
  margin: 30px 0 34px;
}
.media-grid-2 { grid-template-columns: repeat(2, minmax(0, 1fr)); }
.media-grid-4 { grid-template-columns: repeat(4, minmax(0, 1fr)); }
.media-grid-2 figure,
.media-grid-4 figure {
  margin: 0;
}
.media-grid-2 img,
.media-grid-4 img {
  width: 100%;
  height: 100%;
  min-height: 210px;
  max-height: 440px;
  object-fit: cover;
  object-position: top left;
  border: 1px solid var(--line);
  border-radius: 16px;
  background: var(--white);
  box-shadow: 0 12px 34px rgba(24,35,30,.055);
}
.media-grid-2 figcaption,
.media-grid-4 figcaption {
  margin-top: 8px;
  color: var(--muted);
  font-size: .82rem;
}
.hero-visual.product-evidence {
  background: var(--white);
  padding: 0;
}
.hero-product-shot {
  height: 100%;
  min-height: 480px;
  object-fit: cover;
  object-position: top left;
}
.hero-visual.product-evidence::before,
.hero-visual.product-evidence::after {
  display: none;
}
.hero-visual.product-evidence .visual-label {
  left: 18px;
  right: 18px;
  bottom: 18px;
  padding: 10px 12px;
  color: var(--ink);
  background: rgba(245,242,234,.92);
  border: 1px solid var(--line);
  border-radius: 12px;
  backdrop-filter: blur(10px);
}
.project-art-image {
  min-height: 360px;
  background: var(--white);
}
.project-art-image::before,
.project-art-image::after {
  display: none;
}
.project-art-image img {
  height: 100%;
  min-height: 360px;
  object-fit: cover;
  object-position: top left;
}
.media-note {
  margin: 30px 0;
  padding: 24px 26px;
  border: 1px solid var(--line);
  border-radius: 18px;
  background: var(--white);
}
.media-note h3 { margin-bottom: 8px; }

@media (max-width: 760px) {
  .media-grid-2,
  .media-grid-4 {
    grid-template-columns: 1fr;
  }
  .hero-product-shot {
    min-height: 360px;
  }
}
'''.strip() + "\n", encoding="utf-8")

def add_stylesheet(html):
    line = '  <link rel="stylesheet" href="/assets/css/tapestry-media.css">'
    if line not in html:
        html = html.replace(
            '  <link rel="stylesheet" href="/assets/css/styles.css">',
            '  <link rel="stylesheet" href="/assets/css/styles.css">\n' + line
        )
    return html

for f in [home_file, case_file]:
    bak = f.with_suffix(f.suffix + ".before-screenshots")
    if not bak.exists():
        shutil.copy2(f, bak)

home = home_file.read_text(encoding="utf-8")
home = add_stylesheet(home)

home_hero_pattern = re.compile(
    r'<div class="hero-visual" aria-label="Abstract crochet grid product illustration">.*?'
    r'<div class="visual-label"><span>Physical constraints</span><span>Product systems</span></div>\s*</div>',
    re.S
)
home_hero_replacement = '''<div class="hero-visual product-evidence" aria-label="Tapestry Crochet Studio garment designer interface">
      <img class="hero-product-shot" src="/assets/img/tapestry/garment-designer.png" alt="Tapestry Crochet Studio garment designer showing a crochet garment panel and design controls">
      <div class="visual-label"><span>Tapestry Crochet Studio</span><span>Real product evidence</span></div>
    </div>'''
home = home_hero_pattern.sub(home_hero_replacement, home, count=1)

home = home.replace(
    '<div class="project-art" aria-hidden="true"></div>',
    '<div class="project-art project-art-image"><img src="/assets/img/tapestry/image-to-grid-conversion.png" alt="Tapestry Crochet Studio image-to-grid conversion interface"></div>'
)

if 'property="og:image"' not in home:
    home = home.replace(
        '  <meta property="og:description" content="Product management portfolio for Ivy, focused on construction technology, technical product management and products that connect software to physical work.">',
        '  <meta property="og:description" content="Product management portfolio for Ivy, focused on construction technology, technical product management and products that connect software to physical work.">\n'
        '  <meta property="og:image" content="https://ivy-portfolio.ivyndiomu.workers.dev/assets/img/tapestry/garment-designer.png">'
    )

home_file.write_text(home, encoding="utf-8")

case = case_file.read_text(encoding="utf-8")
case = add_stylesheet(case)

if 'property="og:image"' not in case:
    case = case.replace(
        '  <meta property="og:description" content="A product management case study about Tapestry Crochet Studio, a local-first crochet production application spanning gauge, garment design, automation, production and business workflow.">',
        '  <meta property="og:description" content="A product management case study about Tapestry Crochet Studio, a local-first crochet production application spanning gauge, garment design, automation, production and business workflow.">\n'
        '  <meta property="og:image" content="https://ivy-portfolio.ivyndiomu.workers.dev/assets/img/tapestry/garment-designer.png">'
    )

context_media = '''<figure class="case-media">
  <img src="/assets/img/tapestry/home-screen.png" alt="Tapestry Crochet Studio home screen showing the project workspace">
  <figcaption>The product home screen makes the project, rather than an isolated chart, the primary unit of work.</figcaption>
</figure>'''
if context_media not in case:
    case = case.replace(
        '<div class="callout"><strong>Product opportunity</strong>',
        context_media + '<div class="callout"><strong>Product opportunity</strong>',
        1
    )

problem_media = '''<div class="media-grid-2">
  <figure><img src="/assets/img/tapestry/imported-artwork.png" alt="Imported artwork inside Tapestry Crochet Studio"><figcaption>Source artwork before crochet-specific transformation.</figcaption></figure>
  <figure><img src="/assets/img/tapestry/image-to-grid-conversion.png" alt="Artwork converted into a crochet grid"><figcaption>The same workflow after conversion into an editable stitch grid.</figcaption></figure>
</div>'''
if problem_media not in case:
    case = case.replace('<div class="flow">', problem_media + '<div class="flow">', 1)

garment_media = '''<figure class="case-media">
  <img src="/assets/img/tapestry/garment-designer.png" alt="Garment designer interface in Tapestry Crochet Studio">
  <figcaption>The garment designer moved the product from a single abstract chart toward physical panel-aware production.</figcaption>
</figure>
<div class="media-grid-4">
  <figure><img src="/assets/img/tapestry/front-panel.png" alt="Front garment panel in Tapestry Crochet Studio"><figcaption>Front panel</figcaption></figure>
  <figure><img src="/assets/img/tapestry/back-panel.png" alt="Back garment panel in Tapestry Crochet Studio"><figcaption>Back panel</figcaption></figure>
  <figure><img src="/assets/img/tapestry/left-sleeve.png" alt="Left sleeve panel in Tapestry Crochet Studio"><figcaption>Left sleeve</figcaption></figure>
  <figure><img src="/assets/img/tapestry/right-sleeve.png" alt="Right sleeve panel in Tapestry Crochet Studio"><figcaption>Right sleeve</figcaption></figure>
</div>'''
if garment_media not in case:
    case = case.replace('<div class="evidence-grid">', garment_media + '<div class="evidence-grid">', 1)

automation_media = '''<figure class="case-media">
  <img src="/assets/img/tapestry/background-removal-controls.png" alt="Background removal and subject protection controls in Tapestry Crochet Studio">
  <figcaption>Background removal evolved into a controlled, recoverable workflow rather than a one-click promise.</figcaption>
</figure>'''
if automation_media not in case:
    marker = '<p>The same pattern appears in candidate generation. Simplified, balanced and detailed recommendations can trade visual retention against crochet complexity, but the user can still edit the final grid.</p>'
    case = case.replace(marker, marker + automation_media, 1)

quality_media = '''<div class="media-grid-2">
  <figure><img src="/assets/img/tapestry/production-row-focus.png" alt="Production mode focused on the current crochet row"><figcaption>Row-focused production mode keeps the active instruction visible during physical work.</figcaption></figure>
  <figure><img src="/assets/img/tapestry/written-instructions.png" alt="Bottom-up written crochet instructions generated by Tapestry Crochet Studio"><figcaption>Written instructions follow the construction order rather than screen-reading order.</figcaption></figure>
</div>'''
if quality_media not in case:
    marker = '<div class="grid-2"><div class="card"><h3>Regression coverage</h3>'
    case = case.replace(marker, quality_media + marker, 1)

yarn_media = '''<div class="media-note">
  <h3>Yarn became part of the product model.</h3>
  <p>Once a grid had to become a physical object, colour choices also had to connect to available yarn rather than exist only as screen colours.</p>
</div>
<figure class="case-media">
  <img src="/assets/img/tapestry/yarn-intelligence.png" alt="Yarn intelligence interface in Tapestry Crochet Studio">
  <figcaption>Yarn intelligence connects pattern colours to the materials required to produce the design.</figcaption>
</figure>'''
if yarn_media not in case:
    marker = '<section id="decisions"'
    case = case.replace(marker, yarn_media + marker, 1)

export_media = '''<figure class="case-media">
  <img src="/assets/img/tapestry/export-page.png" alt="Professional export options in Tapestry Crochet Studio">
  <figcaption>Export is treated as part of the production workflow, not an afterthought after editing.</figcaption>
</figure>'''
if export_media not in case:
    marker = '<div class="callout"><strong>Product boundary</strong>'
    case = case.replace(marker, export_media + marker, 1)

case = case.replace(
    '<a class="button secondary js-github-link" hidden target="_blank" rel="noreferrer">View GitHub</a>',
    '<a class="button secondary" href="https://github.com/ivyndiomu/tapestry-crochet-studio" target="_blank" rel="noreferrer">View project repository</a>'
)

case_file.write_text(case, encoding="utf-8")

print("Portfolio screenshot update applied.")
print(f"Copied images to: {img_dir}")
print(f"Updated: {home_file}")
print(f"Updated: {case_file}")
print(f"Added: {css_file}")
if missing:
    print("\nThese expected screenshots were not found and were skipped:")
    for name in missing:
        print(" -", name)
print("\nNext: review the changes, then commit them in GitHub Desktop.")
