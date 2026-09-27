#!/usr/bin/env python3
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
CONFIG = HERE / 'assets' / 'js' / 'site-config.js'

print('Ivy portfolio quick configuration')
print('Press Enter to leave any optional field blank.\n')

values = {
    'name': input('Display first name [Ivy]: ').strip() or 'Ivy',
    'fullName': input('Full professional name [Ivy]: ').strip() or 'Ivy',
    'role': input('Role [Product Manager]: ').strip() or 'Product Manager',
    'location': input('Location [Nigeria]: ').strip() or 'Nigeria',
    'email': input('Public email: ').strip(),
    'linkedin': input('LinkedIn full URL: ').strip(),
    'github': input('GitHub profile full URL: ').strip(),
    'resumeUrl': input('Public CV URL or site path, e.g. /assets/Ivy_CV.pdf: ').strip(),
    'siteUrl': input('Live site URL, once Cloudflare gives it to you: ').strip(),
}

content = 'window.IVY_SITE_CONFIG = ' + json.dumps(values, indent=2) + ';\n'
CONFIG.write_text(content, encoding='utf-8')
print(f'\nUpdated {CONFIG.relative_to(HERE)}')
print('Next: preview locally or commit/push the folder to GitHub.')
