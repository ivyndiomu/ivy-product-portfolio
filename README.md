# Ivy Product Management Portfolio

A dependency-free static portfolio site designed for GitHub + Cloudflare Pages.

## Pages

- `/` Home
- `/work/` Case-study index
- `/work/tapestry-crochet-studio/` Flagship case study
- `/about/` Career narrative
- `/resume/` Web resume/profile
- `/contact/` Contact page
- `/404.html` Custom not-found page

## Why this stack

The site is plain HTML, CSS and JavaScript. There is no framework, package manager or build step. This keeps hosting simple, fast and free on Cloudflare Pages and makes the repository easy to maintain.

## Preview locally

From this folder:

```bash
python3 -m http.server 8080
```

Then open `http://localhost:8080`.

## Before public launch

Edit `assets/js/site-config.js` and add Ivy's:

- full name
- email
- LinkedIn URL
- GitHub URL
- CV URL, after the CV is uploaded

The site automatically hides missing contact links.

Also replace the placeholder resume details with Ivy's exact employers, dates, education and responsibilities before presenting the resume page as a complete CV.

## Deployment

Read `DEPLOYMENT.md` for the exact GitHub and Cloudflare Pages steps.
