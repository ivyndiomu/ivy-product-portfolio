# Deployment guide

## Recommended production setup

GitHub repository → Cloudflare Pages → free `*.pages.dev` URL

No paid domain is required.

## Step 1: create Ivy's GitHub repository

Create an empty public repository in Ivy's own GitHub account.

Recommended name:

`ivy-product-portfolio`

Do not initialise it with a README, licence or `.gitignore` if you plan to upload this complete folder with Git/GitHub Desktop. Keeping it empty avoids merge conflicts.

## Step 2: upload this site

### Easiest method: GitHub Desktop

1. Install GitHub Desktop and sign into Ivy's GitHub account.
2. Add this `portfolio-site` folder as a local repository, or create a repository from the folder.
3. Publish it to the empty `ivy-product-portfolio` repository.
4. Confirm that `index.html` is at the root of the GitHub repository.

### Alternative: command line

```bash
git init
git add .
git commit -m "Launch Ivy product portfolio"
git branch -M main
git remote add origin https://github.com/YOUR-IVY-USERNAME/ivy-product-portfolio.git
git push -u origin main
```

## Step 3: connect Cloudflare Pages

1. Sign into Cloudflare.
2. Open **Workers & Pages**.
3. Select **Create application** → **Pages** → **Connect to Git**.
4. Authorise GitHub and select Ivy's `ivy-product-portfolio` repository.
5. Production branch: `main`.
6. Framework preset: none.
7. Build command: leave blank.
8. Build output directory: `/` or leave as the repository root when Cloudflare accepts an empty output field for a static site.
9. Deploy.

Cloudflare will assign a free address such as:

`ivy-product-portfolio.pages.dev`

Every push to `main` will redeploy the site automatically.

## Step 4: verify the deployment

Open these URLs and confirm each page works:

- `/`
- `/work/`
- `/work/tapestry-crochet-studio/`
- `/about/`
- `/resume/`
- `/contact/`

Test the site on a phone and desktop.

## Step 5: add the final live URL

Once Cloudflare gives you the actual `pages.dev` address:

1. Put that URL in the public Tapestry Crochet Studio repository README.
2. Add it to LinkedIn Featured.
3. Add it to Ivy's CV.
4. Later, when a custom domain is purchased, connect it to the same Pages project. The website does not need to be rebuilt.
