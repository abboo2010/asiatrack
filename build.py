import os, html
OUT = os.path.join(os.path.dirname(__file__), 'site')

NAV = [('index.html', 'Home'), ('about.html', 'About'), ('services.html', 'Services'),
       ('products.html', 'Products'), ('portfolio.html', 'Portfolio'), ('#contact', 'Contact')]

LOGO_IMG = '<img class="logo-img" src="assets/img/logo.png" alt="Asia Track" width="131" height="52"><small class="logo-sub">(M) Sdn. Bhd.</small>'
LOGO = '''<span class="logo-mark" aria-hidden="true"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M3 8h8a3 3 0 0 1 3 3v2a3 3 0 0 0 3 3h4"/><path d="M12 3v3M21 13v6M3 5v6"/></svg></span>'''

FALLBACK_SVG = '''<svg class="fallback" viewBox="0 0 400 420" fill="none" aria-hidden="true">
<path class="pipe-line draw" d="M30 90 H190 a40 40 0 0 1 40 40 V230 a40 40 0 0 0 40 40 H370"/>
<path class="pipe-line thin draw" d="M30 90 H190 a40 40 0 0 1 40 40 V230 a40 40 0 0 0 40 40 H370"/>
<rect x="250" y="300" width="110" height="80" rx="14" fill="rgba(14,165,198,.18)" stroke="#7dd3fc" stroke-width="3"/></svg>'''

def ico(path, size=28, sw=1.8):
    return f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"><path d="{path}"/></svg>'

I_PIPE = 'M3 9h7a3 3 0 0 1 3 3v0a3 3 0 0 0 3 3h5M3 6v6M21 12v6'
I_TANK = 'M4 5h16v15H4zM4 12q4-3 8 0t8 0'
I_SHIELD = 'M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z'
I_CHECK = 'M5 12.5l4.5 4.5L19 7'
I_USERS = 'M16 20v-1a4 4 0 0 0-4-4H7a4 4 0 0 0-4 4v1M9.5 11a3.5 3.5 0 1 0 0-7 3.5 3.5 0 0 0 0 7M21 20v-1a4 4 0 0 0-3-3.9M16 4.2a3.5 3.5 0 0 1 0 6.6'
I_TARGET = 'M12 21a9 9 0 1 0 0-18 9 9 0 0 0 0 18zM12 16a4 4 0 1 0 0-8 4 4 0 0 0 0 8z'
I_CYL = 'M5 6c0-1.4 3.1-2.5 7-2.5S19 4.6 19 6v12c0 1.4-3.1 2.5-7 2.5S5 19.4 5 18zM5 6c0 1.4 3.1 2.5 7 2.5S19 7.4 19 6'
I_PUMP = 'M4 14h9a4 4 0 0 0 0-8h-1M4 14v5M13 6V4h4M8 14v-3a3 3 0 0 1 3-3'
I_GRP = 'M2 9h20v6H2zM7 9v6M17 9v6'
I_PANEL = 'M3 4h18v16H3zM3 9.3h18M3 14.7h18M9 4v16M15 4v16'

LD = """
<script type="application/ld+json">{"@context":"https://schema.org","@type":"LocalBusiness","name":"Asia Track (M) Sdn. Bhd.","description":"Pipeline fabrication, plumbing and water tank installation and refurbishment specialists in Sabah.","url":"https://asiatrack.com.my/","telephone":"+60126451885","email":"info@asiatrack.com.my","address":{"@type":"PostalAddress","streetAddress":"11, Lorong Pokok Kayu Manis 2, Luyang Commercial Centre","addressLocality":"Kota Kinabalu","postalCode":"88300","addressRegion":"Sabah","addressCountry":"MY"},"areaServed":["Sabah","Malaysia"],"sameAs":["https://web.facebook.com/asiatrackofficial/","https://www.instagram.com/asiatrackofficial/"]}</script>"""

VT_JS = r'''<script>(function(){var o=['index','about','services','products','portfolio'];function k(u){var p=new URL(u,location.href).pathname.replace(/\/+$/,'').split('/').pop().replace(/\.html$/,'');return p||'index'}function d(a,b){return o.indexOf(k(b))<o.indexOf(k(a))?'back':'fwd'}
addEventListener('pageswap',function(e){try{if(e.viewTransition&&e.activation&&e.activation.from&&e.activation.entry)document.documentElement.dataset.dir=d(e.activation.from.url,e.activation.entry.url)}catch(x){}});
addEventListener('pagereveal',function(e){try{if(e.viewTransition&&navigation.activation&&navigation.activation.from){document.documentElement.dataset.dir=d(navigation.activation.from.url,navigation.activation.entry.url);document.documentElement.classList.add('vt')}}catch(x){}});})();</script>'''

def head(title, desc, active):
    nav = ''.join(
        f'<li><a href="{h}"{" aria-current=\"page\"" if h == active else ""}>{t}</a></li>' for h, t in NAV)
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#0F172A">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Asia Track (M) Sdn. Bhd.">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="assets/img/hdg-tank.jpg">
<meta property="og:locale" content="en_MY">{LD if active == 'index.html' else ''}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Lexend:wght@300;400;500;600;700&family=Source+Sans+3:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="icon" type="image/png" href="assets/img/favicon.png">
<link rel="stylesheet" href="assets/site.css">
{VT_JS}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="topbar"><div class="wrap">
  <span>11, Lorong Pokok Kayu Manis 2, Luyang Commercial Centre, Kota Kinabalu</span>
  <span><a href="tel:+60126451885">012-645 1885</a> &nbsp;·&nbsp; <a href="mailto:info@asiatrack.com.my">info@asiatrack.com.my</a></span>
</div></div>
<header class="nav"><div class="wrap">
  <a class="logo" href="index.html" aria-label="Asia Track (M) Sdn. Bhd. home">{LOGO_IMG}</a>
  <nav aria-label="Main"><ul id="menu">{nav}</ul></nav>
  <a class="btn btn-primary nav-cta" href="#contact">Get a Quote</a>
  <button class="menu-btn" aria-label="Open menu" aria-expanded="false" aria-controls="menu"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg></button>
</div></header>
<main id="main">
'''

def sec_head(eyebrow, h2, p=''):
    return f'<div class="sec-head" data-reveal><div class="eyebrow">{eyebrow}</div><h2>{h2}</h2>{"<p>"+p+"</p>" if p else ""}</div>'

def phero(crumb, h1, lead, variant):
    return f'''<div class="phero"><div class="blueprint" aria-hidden="true"></div><div class="wrap">
<div><div class="crumbs"><a href="index.html">Home</a> / {crumb}</div>
<h1 data-reveal>{h1}</h1><p data-reveal>{lead}</p></div>
<div class="hero-visual" data-3d="{variant}" aria-hidden="true">{FALLBACK_SVG}</div>
</div></div>
<div class="pcontent">'''

CTA = '''<div class="cta" id="contact"><div class="wrap cta-grid">
<div data-reveal>
<h2>Planning a pipeline or tank project?</h2>
<p>Tell us your requirements and we will respond with a tailored solution and quotation.</p>
<div class="btns">
<a class="btn wa" href="https://wa.me/60126451885?text=Hi%20Asia%20Track%2C%20I%20would%20like%20to%20enquire%20about%20a%20quotation." target="_blank" rel="noopener">Send Enquiry via WhatsApp</a>
<a class="btn btn-ghost" href="mailto:info@asiatrack.com.my">info@asiatrack.com.my</a>
</div></div>
<form class="quote" name="quote" method="POST" action="thank-you.html" data-netlify="true" netlify-honeypot="bot-field" data-reveal>
<h3>Request a quotation</h3>
<input type="hidden" name="form-name" value="quote">
<p class="hp" aria-hidden="true"><label>Leave this empty <input name="bot-field" tabindex="-1" autocomplete="off"></label></p>
<div class="row2"><label>Name<input name="name" required autocomplete="name"></label>
<label>Phone / WhatsApp<input name="phone" type="tel" required autocomplete="tel"></label></div>
<label>Email<input name="email" type="email" autocomplete="email"></label>
<label>I am interested in<select name="interest"><option>Pipe fabrication / pipeline</option><option>Tank installation &amp; refurbishment</option><option>Sectional panel tank</option><option>Stainless steel tank</option><option>Water pump</option><option>Plumbing</option><option>Other</option></select></label>
<label>Project details<textarea name="message" rows="4" placeholder="Location, size, material, timeline"></textarea></label>
<button class="btn btn-primary" type="submit">Send enquiry</button>
</form></div></div>
<section class="visit" aria-label="Visit our office"><div class="wrap visit-grid">
<div data-reveal><div class="eyebrow">Visit us</div><h2>Our Office, Kota Kinabalu</h2>
<p>11, Lorong Pokok Kayu Manis 2, Luyang Commercial Centre, 88300 Kota Kinabalu, Sabah</p>
<div class="btns"><a class="btn btn-primary" href="https://www.google.com/maps/dir/?api=1&amp;destination=Asia+Track+Sdn+Bhd+11+Lorong+Pokok+Kayu+Manis+2+Luyang+Commercial+Centre+88300+Kota+Kinabalu+Sabah" target="_blank" rel="noopener">Get directions</a>
<a class="btn btn-outline" href="tel:+60126451885">Call us</a></div></div>
<div class="map" data-reveal><iframe title="Map of Asia Track head office" src="https://maps.google.com/maps?q=Asia+Track+Sdn+Bhd+11+Lorong+Pokok+Kayu+Manis+2+Luyang+Commercial+Centre+88300+Kota+Kinabalu+Sabah&amp;output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe></div>
</div></section>
</div>
</main>
'''

FOOT = f'''<footer><div class="wrap">
<div class="cols">
<div><a class="logo logo-on-dark" href="index.html" aria-label="Asia Track (M) Sdn. Bhd. home">{LOGO_IMG}</a>
<p>Dependable pipeline, plumbing and water tank solutions for residential, commercial, industrial and infrastructure clients.</p></div>
<div><h4>Office</h4><p>11, Lorong Pokok Kayu Manis 2, Luyang Commercial Centre, 88300 Kota Kinabalu, Sabah</p></div>
<div><h4>Contact</h4><p><a href="tel:+60126451885">012-645 1885</a><br><a href="mailto:info@asiatrack.com.my">info@asiatrack.com.my</a></p>
<h4 style="margin-top:18px">Follow us</h4><p class="social"><a href="https://web.facebook.com/asiatrackofficial/" target="_blank" rel="noopener" aria-label="Asia Track on Facebook"><svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M13.5 21v-7.5h2.6l.4-3h-3V8.6c0-.9.3-1.5 1.5-1.5h1.6V4.4c-.3 0-1.2-.1-2.3-.1-2.3 0-3.8 1.4-3.8 3.9v2.3H8v3h2.5V21z"/></svg> Facebook</a> <a href="https://www.instagram.com/asiatrackofficial/" target="_blank" rel="noopener" aria-label="Asia Track on Instagram"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor"/></svg> Instagram</a></p>
<h4 style="margin-top:18px">Explore</h4><p><a href="about.html">About</a> · <a href="services.html">Services</a> · <a href="products.html">Products</a> · <a href="portfolio.html">Portfolio</a></p></div>
</div>
<div class="legal"><span>© Asia Track (M) Sdn. Bhd. All rights reserved.</span><span>Kota Kinabalu, Sabah</span></div>
</div></footer>
<a class="callfab" href="tel:+60126451885" aria-label="Call Asia Track"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/></svg></a>
<a class="fab" href="https://wa.me/60126451885" target="_blank" rel="noopener" aria-label="Chat on WhatsApp"><svg width="30" height="30" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm5.2 14.1c-.2.6-1.3 1.2-1.8 1.2-.5.1-1 .2-3.3-.7-2.8-1.2-4.6-4-4.7-4.2-.1-.2-1.1-1.5-1.1-2.8 0-1.3.7-1.9.9-2.2.2-.3.5-.3.7-.3h.5c.2 0 .4 0 .6.5.2.6.8 2 .8 2.1.1.1.1.3 0 .4-.1.2-.2.3-.3.5l-.5.5c-.1.1-.3.3-.1.6.2.3.8 1.3 1.7 2.1 1.2 1 2.1 1.3 2.4 1.5.3.1.5.1.6-.1.2-.2.7-.8.9-1.1.2-.3.4-.2.6-.1l2 1c.3.1.5.2.5.3.1.1.1.6-.1 1.3z"/></svg></a>
<script src="assets/motion.js"></script>
<script src="assets/hero3d.js"></script>
<script src="assets/site.js"></script>
</body></html>
'''

# ---------- data ----------
PROJECTS = [
 ('tank', 'Water Tank', 'HDG Water Retention Tank', 'THE LOGG, Luyang, Kota Kinabalu',
  'Detailed engineering, structural preparation, panel assembly, sealing work, access fittings and final commissioning of a hot-dip galvanized water retention tank for a high-density residential development.', I_PANEL),
 ('pipeline', 'Pipeline', 'MSCL Pipe Installation', 'THE LOGG, Luyang, Kota Kinabalu',
  'Planning, precision alignment, welding, joint protection and on-site installation of 300mm Mild Steel Cement Lined pipelines for a high-demand building environment.', I_PIPE),
 ('pipeline', 'Pipeline', 'Biogas Pipeline Fabrication', 'Bousted Plantation, Kota Tinggi, Johor',
  'Fabrication of biogas pipelines for a palm oil biogas plant: engineering, material selection, precision welding, protective coatings and rigorous testing for leak-proof, corrosion-resistant lines.', I_PIPE),
 ('pipeline', 'Pipeline', 'Air Pipeline Fabrication', 'Kimberly Clark, Johor',
  'Fabrication and installation of an air pipeline system supporting new blowers and filters for the production air supply, designed for efficient airflow and reliability.', I_PIPE),
 ('tank', 'Water Tank', 'Water Tank Installation', 'West Malaysia',
  'In partnership with Star Brothers Engineering Sdn. Bhd., producer of steel tank panels in hot-dip galvanized or painted finishes. Asia Track is the authorised dealer and installer for East Malaysia.', I_TANK),
 ('plant', 'Water Treatment Plant', 'Beaufort Water Treatment Plant Refurbishment', 'Beaufort, Sabah',
  'Replacement of pumps, pipelines and related accessories to improve efficiency, reliability and overall performance, ensuring a continuous and improved water supply for plant operations.', 'M3 17h18M5 17V9l7-4 7 4v8M9 17v-5h6v5'),
]

PROJ_IMG = {
 'HDG Water Retention Tank': ('hdg-tank.jpg', 'HDG sectional panel water tank on concrete supports'),
 'MSCL Pipe Installation': ('mscl-pipe.jpg', 'Cement lined MSCL pipe elbows with brass flanges ready for installation'),
 'Biogas Pipeline Fabrication': ('hdpe-pipeline.jpg', 'Black pipeline with a flanged joint on steel supports at a palm oil site'),
 'Air Pipeline Fabrication': ('air-pipeline.jpg', 'Compressed air pipework and filters beside a blue compressor'),
 'Water Tank Installation': ('tank-install.jpg', 'Inside a sectional panel tank during panel assembly'),
 'Beaufort Water Treatment Plant Refurbishment': ('pump-valves.jpg', 'Pump station with blue valves and ductile iron elbows'),
}
def photo(src, alt, cls=''):
    return f'<img class="{cls}" src="assets/img/{src}" alt="{alt}" loading="lazy" decoding="async">'

def proj_card(p, link=False):
    t, tag, title, loc, desc, ic = p
    if title in PROJ_IMG:
        media = photo(*PROJ_IMG[title])
    else:
        media = ico(ic, 56, 1.2) + '<small>Project photo placeholder</small>'
    return f'''<article class="proj" data-type="{t}" data-reveal data-tilt>
<div class="img">{media}</div>
<div class="body"><span class="tag">{tag}</span><h3>{title}</h3><div class="loc">{loc}</div><p>{desc}</p></div></article>'''

def gallery(eyebrow, h2, items, cols=4):
    figs = ''.join(f'<figure class="shot" data-reveal data-tilt><img src="assets/img/{f}" alt="{a}" loading="lazy"><figcaption>{c}</figcaption></figure>' for f, a, c in items)
    return f'<section class="gallery"><div class="wrap">{sec_head(eyebrow, h2)}<div class="shots persp cols{cols}">{figs}</div></div></section>'

# ---------- pages ----------
pages = {}

# HOME
home = head('Asia Track (M) Sdn. Bhd. | Pipe Fabrication & Water Tank Solutions, Sabah',
            'Asia Track (M) Sdn. Bhd. — pipe fabrication, tank and pump supply and water tank installation, maintenance and repair for industrial, commercial and infrastructure projects in Sabah.', 'index.html')
home += f'''<div id="top" class="hero"><div class="blueprint" aria-hidden="true"></div><div class="wrap">
<div><div class="eyebrow" data-reveal>Sabah · Pipeline &amp; Water Tank Specialists</div>
<h1 data-reveal>Excellence in every drop. <em>Strength in every pipe.</em></h1>
<p class="lead" data-reveal>Pipe fabrication, water pump and stainless steel tank supply, and tank installation and refurbishment, engineered to project specifications for industrial, commercial and infrastructure clients.</p>
<div class="hero-cta" data-reveal><a class="btn btn-primary" href="#contact">Request a Quote <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
<a class="btn btn-ghost" href="portfolio.html">View Our Projects</a></div></div>
<div class="hero-visual" data-3d="home" aria-hidden="true">{FALLBACK_SVG}<span class="ph-note">Placeholder graphic</span></div>
</div></div>
<div class="pcontent">
<div class="wrap stats"><ul>
<li data-reveal><b data-count="8">0</b><span>Industries served</span></li>
<li data-reveal><b data-count="6">0</b><span>Pipe materials fabricated</span></li>
<li data-reveal><b data-count="4">0</b><span>Tank panel materials</span></li>
<li data-reveal><b data-count="2">0</b><span>Core services: pipelines &amp; tanks</span></li>
</ul></div>
<section id="services"><div class="wrap">
{sec_head('Our Services', 'Where quality comes first', 'Complete pipeline and water tank solutions, built by a skilled team with strict quality control from design support to installation readiness.')}
<div class="services persp">
<article class="svc" data-reveal data-tilt><div class="ico">{ico(I_PIPE)}</div><h3>Pipe Fabrication</h3>
<p>End-to-end pipeline fabrication: cutting, welding, jointing, surface treatment and quality inspection, in conventional and GRP materials.</p>
<ul class="chips"><li>MS</li><li>SS</li><li>MSCL</li><li>HDG</li><li>HDPE</li><li>GRP</li></ul><a class="more" href="services.html">Explore pipe fabrication <span aria-hidden="true">→</span></a></article>
<article class="svc alt" data-reveal data-tilt><div class="ico">{ico(I_TANK)}</div><h3>Tank Installation &amp; Refurbishment</h3>
<p>New tank installation, preventive maintenance, and repair and rectification: leak repairs, structural restoration and component replacement.</p>
<ul class="chips"><li>New installation</li><li>Refurbishment</li><li>Maintenance &amp; repair</li></ul><a class="more" href="services.html#tanks">Explore tank services <span aria-hidden="true">→</span></a></article>
</div></div></section>
<section id="products" class="products"><div class="wrap">
{sec_head('Our Products', 'Engineered water storage &amp; piping', 'Supplied to project specifications with consistent quality and on-time delivery.')}
<div class="grid3 persp">
<article class="prod" data-reveal data-tilt><div class="img">{photo('tank-install.jpg','Stainless steel tank panel assembly')}</div><div class="body"><h3>Stainless Steel Tank</h3><p>Hygienic, long-lasting sectional tanks, ideal for potable water storage.</p><ul><li>Corrosion resistant, easy to clean</li><li>Modular panels, flexible capacity</li><li>Residential, commercial, industrial</li></ul><a class="tag" href="products.html#ss">Learn more <span aria-hidden="true">→</span></a></div></article>
<article class="prod" data-reveal data-tilt><div class="img">{photo('pump-valves.jpg','Water pump station with valves and pipework')}</div><div class="body"><h3>Water Pumps</h3><p>Four pump types supplied, installed and serviced for water supply and treatment systems.</p><ul><li>Booster and transfer pumps</li><li>Submersible and centrifugal pumps</li><li>Supply, installation and servicing</li></ul><a class="tag" href="products.html#pumps">Learn more <span aria-hidden="true">→</span></a></div></article>
<article class="prod" data-reveal data-tilt><div class="img">{photo('hdg-tank.jpg','HDG sectional panel water tank')}</div><div class="body"><h3>Sectional Panel Tanks</h3><p>Modular panel system for flexible capacities and efficient installation, for potable and non-potable water.</p><ul><li>HDG, SS, FRP or GRP panels</li><li>Residential, commercial, industrial</li><li>Built to industry standards</li></ul><a class="tag" href="products.html#sectional">Learn more <span aria-hidden="true">→</span></a></div></article>
</div></div></section>
<div class="materials"><div class="wrap row"><h2 data-reveal>Materials we work with</h2><div class="mats">
<div class="mat" data-reveal><b>MS</b><span>Mild Steel</span></div><div class="mat" data-reveal><b>SS</b><span>Stainless Steel</span></div><div class="mat" data-reveal><b>MSCL</b><span>Cement Lined</span></div><div class="mat" data-reveal><b>HDG</b><span>Hot-Dip Galvanized</span></div><div class="mat" data-reveal><b>HDPE</b><span>High-Density PE</span></div><div class="mat" data-reveal><b>FRP/GRP</b><span>Reinforced Plastic</span></div>
</div></div></div>
<section><div class="wrap">
{sec_head('Featured Projects', 'Delivered across Sabah and Peninsular Malaysia', 'A selection of recent pipeline, tank and treatment plant work.')}
<div class="projs persp">{''.join(proj_card(PROJECTS[i]) for i in (0, 2, 5))}</div>
<p style="margin-top:32px" data-reveal><a class="btn btn-dark" href="portfolio.html">See all projects <span aria-hidden="true">→</span></a></p>
</div></section>
{gallery('On Site', 'Our work in the field', [
 ('firefighting-jetty.jpg', 'Red and blue firefighting pipework on a jetty structure', 'Firefighting pipelines'),
 ('pump-valves.jpg', 'Pump station valves and ductile iron elbows', 'Pump station valves &amp; pipework'),
 ('grp-pipe.jpg', 'GRP pipe fabrication with flanges', 'GRP pipe fabrication'),
 ('tank-install.jpg', 'Sectional tank panel assembly with scaffolding', 'Tank panel assembly')])}
<section id="industries" class="products" style="border-bottom:0"><div class="wrap">
{sec_head('Industries We Serve', 'Pipelines built for demanding sectors', 'High-quality materials, modern installation techniques and a safety-trained workforce, delivered on time and within budget.')}
<div class="ind persp" id="indgrid"></div></div></section>
<section class="why" id="why"><div class="wrap">
<div data-reveal><div class="sec-head" style="margin-bottom:0"><div class="eyebrow">Why Asia Track</div><h2>Dependable engineering that performs over time</h2><p>Quality workmanship and technical competence, with every solution engineered to project specifications, regulatory standards and operational demands.</p></div>
<div class="cert"><b>Certifications &amp; memberships</b>Product certification and Sabah Plumber Association logos go here (placeholder — send the logo files).</div></div>
<ol class="why-list">
<li data-reveal><span class="n">1</span><div><b>Skilled fabrication team</b><span>Industry experience across industrial, commercial and infrastructure projects.</span></div></li>
<li data-reveal><span class="n">2</span><div><b>Compliance with specifications</b><span>Project specifications and standards followed at every stage.</span></div></li>
<li data-reveal><span class="n">3</span><div><b>Strict quality control</b><span>High-quality workmanship, inspected before it leaves our hands.</span></div></li>
<li data-reveal><span class="n">4</span><div><b>Design to installation</b><span>From design support to fabrication and installation readiness.</span></div></li>
</ol></div></section>
<section class="reviews"><div class="wrap">
{sec_head('Customer Reviews', 'What clients say on Google')}
<div class="grid3 persp">
<figure class="rev" data-reveal data-tilt><div class="stars" aria-label="5 stars">★★★★★</div><p>“They did a great job with both the plumbing and roofing work. Everything was fixed properly and they made sure no issues were left behind. Definitely recommend them!”</p><b>Alex “Joun” Lee</b><small>Google Review</small></figure>
<figure class="rev" data-reveal data-tilt><div class="stars" aria-label="5 stars">★★★★★</div><p>“They do a thorough job in all their services. They ensure that all the problems are completely solved. Highly recommended.”</p><b>Agnes Chin</b><small>Google Review</small></figure>
<figure class="rev" data-reveal data-tilt><div class="stars" aria-label="5 stars">★★★★★</div><p>“Excellent service”</p><b>Miss Lai</b><small>Google Review</small></figure>
</div></div></section>
''' + CTA + FOOT
pages['index.html'] = home

# ABOUT
TEAM = [('SP', 'Mr. Segaran Pillai', 'Chief Executive Officer'),
        ('SJ', 'Mrs. Selvasutha Jayabalan', 'Director / Administration'), ('DM', 'Dr. Dinesh Mathavan', 'Director / Human Resources'),]
about = head('About Asia Track | Pipeline & Tank Specialists, Sabah', 'Asia Track (M) Sdn. Bhd. is an engineering-driven pipeline and tank company supporting Malaysia’s water and process industries.', 'about.html')
about += phero('About', 'Precision. Reliability. <em>Performance.</em>',
               'An engineering-driven company focused on pipeline systems and tank solutions that support essential infrastructure and industrial operations.', 'about')
about += f'''<section><div class="wrap split">
<div data-reveal>{sec_head('Our Story', 'Built to meet the demands of Malaysia’s water and process industries')}</div>
<div class="prose" data-reveal>
<p>Asia Track (M) Sdn. Bhd. was established with a clear objective: to provide dependable pipeline and tank solutions that meet the growing demands of Malaysia’s water and process industries. From our early beginnings, we have steadily grown into a trusted industry partner, recognised for quality fabrication, disciplined execution and professional service delivery.</p>
<p>As industry requirements evolved, so did our capabilities. Today, we offer end-to-end pipe fabrication, including conventional steel systems and advanced materials such as GRP and HDPE, alongside tank installation, maintenance, repair services, and the supply of sectional panel and FRP/GRP tanks.</p>
<p>Our journey is built on technical expertise, continuous improvement, and a commitment to delivering systems that are safe, efficient, and engineered to last.</p>
</div></div></section>
<section class="products"><div class="wrap">
{sec_head('Who We Are', 'Engineering solutions built on integrity', 'We work closely with clients to understand project requirements and deliver solutions that are practical, compliant and cost-effective.')}
<div class="values persp">
<div class="value" data-reveal data-tilt><div class="ico">{ico(I_SHIELD, 26)}</div><h3>Engineering with Integrity</h3><p>An engineering-driven company supporting essential infrastructure and industrial operations with practical, compliant, cost-effective solutions.</p></div>
<div class="value" data-reveal data-tilt><div class="ico">{ico(I_CHECK, 26)}</div><h3>Quality as Our Standard</h3><p>Strict quality control from material selection and fabrication to installation readiness and after-service support, by a safety-trained workforce.</p></div>
<div class="value" data-reveal data-tilt><div class="ico">{ico(I_TARGET, 26)}</div><h3>Purpose-Driven Delivery</h3><p>Precision, clear planning and respect for timelines, whether supporting new developments or upgrading existing systems.</p></div>
</div></div></section>
<section class="why"><div class="wrap">
<div data-reveal>{sec_head('Why Choose Us', 'Engineering confidence, not just products and services')}
<div class="cert"><b>Certifications &amp; memberships</b>Product certification and Sabah Plumber Association logos go here (placeholder — send the logo files).</div></div>
<ul class="check" data-reveal>
<li>Proven expertise in pipe fabrication, tank services and water-related systems</li>
<li>Experience across water, wastewater, energy, food and industrial processing</li>
<li>Strong focus on quality workmanship, safety and compliance</li>
<li>Reliable delivery within project timelines and budgets</li>
<li>Dedicated team with hands-on industry experience</li></ul></div></section>
<section id="team"><div class="wrap">
{sec_head('Our People', 'The team behind every project')}
<div class="team persp">{''.join(f'<div class="person" data-reveal data-tilt><span class="avatar">{a}</span><div><b>{n}</b><span>{r}</span></div></div>' for a, n, r in TEAM)}</div>
</div></section>
''' + CTA + FOOT
pages['about.html'] = about

# SERVICES
CONV = [('MS', 'Mild Steel — cost-effective and widely used for general piping applications'),
        ('SS', 'Stainless Steel — corrosion-resistant, suitable for hygienic and high-performance systems'),
        ('MSCL', 'Mild Steel Cement Lined — ideal for water transmission and distribution'),
        ('HDG', 'Hot-Dip Galvanized — enhanced corrosion protection for outdoor and exposed environments'),
        ('HDPE', 'High-Density Polyethylene — lightweight, flexible, resistant to chemicals and corrosion')]
services = head('Services | Pipe Fabrication & Tank Services — Asia Track', 'End-to-end pipe fabrication and tank installation, maintenance and repair for industrial, commercial and infrastructure projects.', 'services.html')
services += phero('Services', 'Where quality <em>comes first</em>',
                  'Pipeline fabrication and tank services delivered with skilled workmanship, strict quality control and compliance with project specifications.', 'services')
services += f'''<section id="pipe"><div class="wrap split">
<div class="prose" data-reveal>{sec_head('Pipe Fabrication', 'End-to-end pipeline fabrication')}
<p>We provide end-to-end pipeline fabrication solutions for a wide range of industries, delivering durable, precise and compliant piping systems tailored to your project requirements.</p>
<p>Our fabrication process includes cutting, welding, jointing, surface treatment and quality inspection to ensure strength, accuracy and long service life.</p>
<h3>GRP pipe fabrication</h3>
<p>We also specialise in GRP (Glass Reinforced Plastic) pipe fabrication: lightweight yet high-strength piping, highly resistant to corrosion and chemicals, ideal for water supply, sewage, industrial and marine applications, especially in aggressive environments.</p>
<ul class="check"><li>Skilled fabrication team with industry experience</li><li>Compliance with project specifications and standards</li><li>High-quality workmanship and strict quality control</li><li>Suitable for industrial, commercial and infrastructure projects</li></ul></div>
<div data-reveal><h3 style="font-size:22px;color:var(--primary);margin-bottom:6px">Conventional pipe fabrication</h3>
<p style="color:var(--muted-fg)">We fabricate and assemble pipelines using commonly specified materials:</p>
<ul class="pill-list">{''.join(f'<li><b>{a}</b><span>{b}</span></li>' for a, b in CONV)}</ul></div>
</div></section>
<section id="industries" class="products"><div class="wrap">
{sec_head('Industries We Serve', 'Pipelines built for demanding sectors', 'From new developments to major infrastructure upgrades, Asia Track is your trusted partner for pipeline solutions engineered to last for decades.')}
<div class="ind persp" id="indgrid"></div></div></section>
<section id="tanks"><div class="wrap">
{sec_head('Tank Services', 'Installation, maintenance &amp; repair', 'Complete tank solutions for industrial, commercial and municipal projects, with experienced personnel, proper handling procedures and strict compliance to industry standards.')}
<div class="values persp">
<div class="value" data-reveal data-tilt><div class="ico">{ico(I_TANK, 26)}</div><h3>New Tank Installation</h3><p>Professional installation including proper alignment, secure assembly and integration with supporting systems, following project specifications, safety regulations and structural requirements.</p></div>
<div class="value" data-reveal data-tilt><div class="ico">{ico(I_USERS, 26)}</div><h3>Maintenance Services</h3><p>Preventive and routine maintenance that keeps tanks in good working condition, avoids unexpected breakdowns, extends service life and reduces downtime.</p></div>
<div class="value" data-reveal data-tilt><div class="ico">{ico(I_SHIELD, 26)}</div><h3>Repair &amp; Rectification</h3><p>Leak repairs, structural restoration and component replacement for aging or damaged tanks, restoring them to safe working condition.</p></div>
</div>
<div class="cert" style="margin-top:28px;border-style:solid;background:#fff" data-reveal><b>Applications</b>Water storage tanks · Sewerage &amp; wastewater tanks · Industrial &amp; process tanks</div>
</div></section>
''' + gallery('On Site', 'Fabrication and installation in action', [
 ('plumbing.jpg', 'Plumber tightening a chrome sink trap with a wrench', 'Plumbing works'),
 ('air-pipeline.jpg', 'Compressed air pipework', 'Air pipelines'),
 ('hdpe-pipeline.jpg', 'HDPE pipeline on steel supports', 'HDPE pipelines')], 3) + CTA + FOOT
pages['services.html'] = services

# PRODUCTS
products = head('Products | Stainless Steel Tanks, Water Pumps, Sectional Panel Tanks — Asia Track', 'Stainless steel tanks, water pumps and HDG sectional panel tanks supplied to project specifications.', 'products.html')
products += phero('Products', 'Engineered water storage <em>&amp; piping</em>',
                  'Reliable supply solutions tailored to project requirements, with consistent quality, long service performance and on-time delivery.', 'products')
PD_IMG = {'Stainless Steel Tank': ('tank-install.jpg', 'Stainless steel tank panel assembly'), 'Water Pumps': ('pump-valves.jpg', 'Water pump station with valves and pipework'), 'Sectional Panel Tanks': ('hdg-tank.jpg', 'HDG sectional panel water tank')}
def pdetail(idn, flip, title, icon, intro, lists, closing):
    blocks = ''.join(f'<h4>{h}</h4><ul class="check">{"".join(f"<li>{i}</li>" for i in items)}</ul>' for h, items in lists)
    return f'''<div class="pdetail{" flip" if flip else ""}" id="{idn}">
<div class="pvis" data-reveal>{photo(*PD_IMG[title]) if title in PD_IMG else ico(icon, 120, 1) + '<small>Product photo placeholder</small>'}</div>
<div data-reveal><h2>{title}</h2>{intro}{blocks}<p style="margin-top:20px;color:var(--muted-fg)">{closing}</p>
<p style="margin-top:20px"><a class="btn btn-primary" href="https://wa.me/60126451885?text=Hi%20Asia%20Track%2C%20I%20would%20like%20to%20enquire%20about%20{title.replace(' ','%20')}." target="_blank" rel="noopener">Enquire about {title} on WhatsApp</a> <a class="btn btn-outline" href="#contact">Request a quote</a></p></div></div>'''
products += '<section><div class="wrap">' + \
 pdetail('ss', False, 'Stainless Steel Tank', I_CYL,
  '<p>Stainless steel sectional tanks for hygienic, long-lasting water storage. The modular panel system allows flexible sizing and efficient installation for residential, commercial and industrial sites.</p>',
  [('Key features', ['Hygienic and easy to clean, ideal for potable water', 'Excellent corrosion resistance and long service life', 'Modular design for flexible tank capacities', 'Built to industry standards and project specifications']),
   ('Applications', ['Potable water storage', 'Commercial and industrial buildings', 'Process and utility water'])],
  'Supplied with installation, refurbishment and after-sales support.') + \
 pdetail('pumps', True, 'Water Pumps', I_PUMP,
  '<p>Water pumps for supply, boosting and transfer, selected to match your flow and pressure requirements, with installation and servicing by our team.</p>',
  [('Applications', ['Building water supply and pressure boosting', 'Water treatment plants and pump stations', 'Industrial and process systems'])],
  'Supply, installation and servicing available.') + \
 '<div class="pumpgrid" id="pump-range">' + ''.join(f'<article class="pump" data-reveal><div class="pimg"><img src="assets/img/pump-placeholder.svg" alt="Pump {n} photo coming soon" loading="lazy" width="400" height="300"><span class="soon">Coming soon</span></div><div class="pbody"><h3>Pump {n}</h3><p>Details and photo coming soon.</p></div></article>' for n in range(1, 5)) + '</div>' + \
 pdetail('sectional', False, 'Sectional Panel Tanks', I_PANEL,
  '<p>High-quality sectional panel tanks for reliable water storage in residential, commercial and industrial applications. A modular panel system allows flexible sizing and efficient installation to suit various site requirements, while maintaining compliance with project specifications and water industry standards.</p>',
  [('Available materials', ['HDG (Hot-Dip Galvanized Steel) — durable and corrosion-resistant, suited to outdoor and utility installations', 'FRP (Fibre Reinforced Plastic) — lightweight, corrosion-resistant, low maintenance', 'GRP (Glass Reinforced Plastic) — high strength and chemical resistance for harsh environments']),
   ('Key features', ['Modular design for flexible tank capacities', 'Strong and durable construction', 'Suitable for potable and non-potable water storage', 'Designed to meet industry standards and project specifications'])],
  'Authorised dealer and installer for East Malaysia in partnership with Star Brothers Engineering Sdn. Bhd., with supply, installation and after-sales support.') + \
 '</div></section>' + CTA + FOOT
pages['products.html'] = products

# PORTFOLIO
portfolio = head('Portfolio | Pipeline, Tank & Treatment Plant Projects — Asia Track', 'Selected Asia Track projects: HDG water tanks, MSCL pipelines, biogas and air pipelines, and water treatment plant refurbishment.', 'portfolio.html')
portfolio += phero('Portfolio', 'Projects built to <em>last</em>',
                   'Complete plumbing installations, infrastructure pipeline systems, and the supply and installation of HDG and FRP tanks, with strict adherence to quality, safety and industry standards.', 'portfolio')
portfolio += f'''<section><div class="wrap">
<div class="filters" role="group" aria-label="Filter projects">
<button data-filter="all" aria-pressed="true">All projects</button><button data-filter="tank" aria-pressed="false">Water tanks</button>
<button data-filter="pipeline" aria-pressed="false">Pipelines</button><button data-filter="plant" aria-pressed="false">Treatment plants</button></div>
<div class="projs persp">{''.join(proj_card(p) for p in PROJECTS)}</div>
</div></section>
''' + CTA + FOOT
pages['portfolio.html'] = portfolio

pages['thank-you.html'] = head('Thank you | Asia Track', 'Thank you for your enquiry.', 'thank-you.html').replace('<meta charset="utf-8">','<meta charset="utf-8">\n<meta name="robots" content="noindex">') + '<section><div class="wrap" style="text-align:center;padding:60px 0"><img src="assets/img/logo.png" alt="Asia Track (M) Sdn. Bhd." width="220" height="87" style="margin:0 auto 28px;height:auto;max-width:220px"><div class="eyebrow" style="justify-content:center">Enquiry received</div><h1 style="font-size:clamp(32px,4vw,48px);color:var(--primary);margin-bottom:16px">Thank you!</h1><p style="color:var(--muted-fg);max-width:520px;margin:0 auto 28px">We have received your request and will get back to you shortly. For urgent matters, message us on WhatsApp.</p><a class="btn btn-primary" href="index.html">Back to home</a></div></section></main>' + FOOT
for name, content in pages.items():
    with open(os.path.join(OUT, name), 'w', encoding='utf-8') as f:
        f.write(content)
BASE='https://asiatrack.com.my/'
with open(os.path.join(OUT,'sitemap.xml'),'w') as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(f'<url><loc>{BASE}{"" if n=="index.html" else n}</loc></url>\n' for n in pages if n!='thank-you.html')+'</urlset>\n')
with open(os.path.join(OUT,'robots.txt'),'w') as f:
    f.write('User-agent: *\nAllow: /\nSitemap: '+BASE+'sitemap.xml\n')
with open(os.path.join(OUT,'_redirects'),'w') as f:
    f.write('# Old Joomla links -> new pages (add more once old URLs are known)\n/index.php  /  301\n/index.php/*  /  301\n')
print('built', list(pages))
