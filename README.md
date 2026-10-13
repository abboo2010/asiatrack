# Asia Track (M) Sdn. Bhd. — website

Static 5-page website (Home, About, Services, Products, Portfolio) with a 3D hero scene (Three.js) and Motion animations.

- `site/` — the deployable website (open `site/index.html`)
- `src3d/hero.js` — source of the 3D scene, bundled to `site/assets/hero3d.js`
- `build.py` — regenerates the HTML pages (`python3 build.py`)
- `netlify.toml` — Netlify publishes the `site/` folder, no build command needed

Rebuild the 3D bundle: `npm install && npx esbuild src3d/hero.js --bundle --minify --format=iife --target=es2019 --outfile=site/assets/hero3d.js`
