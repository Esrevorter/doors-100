#!/usr/bin/env python3
# Generates 100 unique, hand-crafted HTML pages. Each page has its own theme,
# palette, layout and interactive gimmick. No templates are reused.
import os, random, math

OUT = os.path.join(os.path.dirname(__file__), "pages")
os.makedirs(OUT, exist_ok=True)

PAGES = []  # list of (filename, title, html)

def add(fname, title, body, head=""):
    html = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<link href="https://fonts.googleapis.com/css2?family={FONT}&display=swap" rel="stylesheet">
<style>{CSS_BASE}{head}</style></head>
<body>{body}<script>{JS}</script></body></html>"""
    PAGES.append((fname, title, html))

CSS_BASE = """*{margin:0;padding:0;box-sizing:border-box}body{font-family:'%s',sans-serif;background:#0b0e14;color:#e8e6df;overflow-x:hidden}::selection{background:#f7c948;color:#111}
"""

JS = ""  # per-page scripts get injected into body directly instead
FONT = "Syne:wght@400;700;800"

# We'll write each page fully custom below. Helper to inline script+style.
def page(fname, title, font, style, body, script=""):
    html = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><link href="https://fonts.googleapis.com/css2?family={font}&display=swap" rel="stylesheet">
<style>{style}</style></head><body>{body}<script>{script}</script></body></html>"""
    PAGES.append((fname, title, html))

R = random.Random(42)

# ---------------------------------------------------------------- 1
page("001-cosmos.html","Cosmos — A Journey Through Space","Orbitron",
"""body{background:#000;color:#fff;font-family:'Orbitron'}
.stars{position:fixed;inset:0;z-index:-1}
.hero{min-height:100vh;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center}
h1{font-size:clamp(2rem,8vw,6rem);letter-spacing:.4em;background:linear-gradient(90deg,#7b2ff7,#f107a3,#fa709a);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.planet{width:220px;height:220px;border-radius:50%;margin-top:40px;background:radial-gradient(circle at 30% 30%,#ffd56b,#ff6b35 45%,#7a1f00);box-shadow:0 0 80px #ff6b35aa;animation:spin 20s linear infinite}
@keyframes spin{to{transform:rotate(360deg)}}
section{padding:14vh 8vw;font-size:1.1rem;line-height:2}
.pulse{display:inline-block;width:14px;height:14px;border-radius:50%;background:#0ff;box-shadow:0 0 20px #0ff;animation:p 1.2s infinite}
@keyframes p{50%{transform:scale(1.8);opacity:.4}}""",
"""<canvas class="stars" id="c"></canvas>
<div class="hero"><h1>COSMOS</h1><p>light-years from ordinary</p><div class="planet"></div></div>
<section><span class="pulse"></span>&nbsp; The observable universe spans 93 billion light-years. Every atom in your left hand likely came from a different dying star than the ones in your right.</section>
<section><span class="pulse"></span>&nbsp; Neutron stars spin up to 716 times per second. A sugar-cube of their matter weighs as much as Mount Everest.</section>""",
"""const c=document.getElementById('c'),x=c.getContext('2d');let w,h,s=[];
function rs(){w=c.width=innerWidth;h=c.height=innerHeight;s=[...Array(400)].map(()=>({x:Math.random()*w,y:Math.random()*h,r:Math.random()*1.4,z:Math.random()}))}
rs();onresize=rs;
(function loop(){x.fillStyle='#000';x.fillRect(0,0,w,h);for(const st of s){st.y+=st.z*.4;if(st.y>h)st.y=0;x.globalAlpha=.3+st.z;x.fillStyle='#fff';x.beginPath();x.arc(st.x,st.y,st.r,0,7);x.fill()}requestAnimationFrame(loop)})();""")

# ---------------------------------------------------------------- 2
page("002-brutalist.html","BRUTALIST BAKERY — Bread With Opinions","Archivo Black",
"""body{background:#fff;color:#000;font-family:'Archivo Black'}
header{border-bottom:6px solid #000;padding:20px;display:flex;justify-content:space-between;align-items:center}
.logo{font-size:2rem;background:#000;color:#fff;padding:4px 12px;transform:rotate(-3deg)}
.marquee{overflow:hidden;border-bottom:6px solid #000;background:#ffeb00;padding:10px 0;white-space:nowrap}
.marquee span{display:inline-block;animation:mv 12s linear infinite;font-size:1.5rem}
@keyframes mv{to{transform:translateX(-50%)}}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:0}
.card{border:6px solid #000;border-right:0;border-bottom:0;padding:40px;transition:.15s;cursor:pointer}
.card:hover{background:#000;color:#fff;transform:scale(1.02);z-index:2}
.price{float:right;font-size:2.5rem}
.card h2{font-size:2rem;margin-bottom:12px;text-transform:uppercase}
footer{background:#000;color:#fff;text-align:center;padding:60px 20px;font-size:1.6rem}
.big{font-size:clamp(3rem,12vw,10rem);line-height:.9;padding:40px;text-transform:uppercase}""",
"""<header><div class="logo">BB//BAKERY</div><div>NO SUGAR. NO LIES.</div></header>
<div class="marquee"><span>FRESH BREAD &nbsp;★&nbsp; FIERCE OPINIONS &nbsp;★&nbsp; FRESH BREAD &nbsp;★&nbsp; FIERCE OPINIONS &nbsp;★&nbsp; FRESH BREAD &nbsp;★&nbsp; FIERCE OPINIONS &nbsp;★&nbsp;</span></div>
<div class="big">Bread.<br>Raw.<br>Honest.</div>
<div class="grid">
<div class="card"><span class="price">€4</span><h2>Sourdough Anarchy</h2><p>48-hour ferment. Zero apology. Crust that argues back.</p></div>
<div class="card"><span class="price">€3</span><h2>Rye Dictator</h2><p>Dense, dark, uncompromising. Caraway with a manifesto.</p></div>
<div class="card"><span class="price">€5</span><h2>Baguette Rebel</h2><p>Shatters on contact. Best eaten standing up, angrily.</p></div>
<div class="card"><span class="price">€6</span><h2>Croissant Chaos</h2><p>81 layers of butter and structural impossibility.</p></div>
</div><footer>OPEN WHEN WE'RE AWAKE — CLOSED ON PRINCIPLE</footer>""")

# ---------------------------------------------------------------- 3
page("003-ocean.html","Abyssal — Descent Into the Deep Ocean","Playfair Display",
"""body{font-family:'Playfair Display';color:#dff6ff;background:linear-gradient(#0a3d62,#051329 60%,#01060d)}
.wrap{max-width:760px;margin:auto;padding:12vh 24px}
h1{font-size:clamp(3rem,9vw,6rem);font-style:italic;text-shadow:0 0 40px #0ff5}
.zone{border-left:2px solid #2bb0d6;padding:24px 28px;margin:48px 0;position:relative;background:#ffffff06;border-radius:0 16px 16px 0}
.zone::before{content:attr(data-d);position:absolute;left:-70px;top:28px;color:#2bb0d6;font-size:.8rem;letter-spacing:.1em}
.bubble{position:fixed;bottom:-30px;border-radius:50%;background:#ffffff18;animation:up linear infinite}
@keyframes up{to{transform:translateY(-110vh)}}
.creature{text-align:center;font-size:4rem;filter:drop-shadow(0 0 18px #0ff)}""",
"""<div class="wrap">
<h1>The Abyssal Zone</h1><p style="opacity:.7;font-style:italic">Six hundred metres down, sunlight is a rumour.</p>
<div class="zone" data-d="200m"><h2>Twilight</h2><p>Bioluminescence replaces the sun. Ninety percent of creatures here make their own light — cold blue lanterns drifting in permanent dusk.</p></div>
<div class="zone" data-d="1000m"><h2>Midnight</h2><div class="creature">🦑</div><p>Giant squid patrol these waters. Eyes the size of dinner plates, evolved to catch the faintest glow of prey.</p></div>
<div class="zone" data-d="4000m"><h2>Abyss</h2><div class="creature">🐡</div><p>Pressure here would crush a submarine like foil. Yet life persists — ghostly pale, patient, unhurried.</p></div>
<div class="zone" data-d="11000m"><h2>Hadal</h2><div class="creature">🦴</div><p>Named for Hades. In the Mariana Trench, amphipods swim through darkness older than human civilisation.</p></div></div>""",
"""for(let i=0;i<25;i++){const b=document.createElement('div');b.className='bubble';const s=4+Math.random()*20;b.style.cssText=`width:${s}px;height:${s}px;left:${Math.random()*100}vw;animation-duration:${6+Math.random()*10}s;animation-delay:${Math.random()*8}s`;document.body.appendChild(b)}""")

# ---------------------------------------------------------------- 4
page("004-synthwave.html","NEON DRIVE — Midnight Synthwave Radio","Monoton",
"""body{font-family:'Monoton';background:#10002b;color:#fff;text-align:center}
.sun{width:300px;height:300px;border-radius:50%;margin:8vh auto 0;background:linear-gradient(#ff2975,#8c1eff);position:relative;overflow:hidden;box-shadow:0 0 120px #ff297588}
.sun::after{content:'';position:absolute;inset:0;background:repeating-linear-gradient(transparent 0 12px,#10002b 12px 20px)}
.grid{height:45vh;margin-top:6vh;background:linear-gradient(#0ff3 1px,transparent 1px),linear-gradient(90deg,#0ff3 1px,transparent 1px);background-size:44px 44px;transform:perspective(400px) rotateX(62deg);animation:mv 1.6s linear infinite}
@keyframes mv{to{background-position:0 44px,0 0}}
h1{font-size:clamp(2rem,7vw,5rem);color:#ff2975;text-shadow:0 0 30px #ff2975;margin-top:8vh}
.track{font-family:monospace;font-size:1.4rem;color:#0ff;margin:3vh;letter-spacing:.3em;text-transform:uppercase}
.eq{display:flex;gap:6px;justify-content:center;align-items:flex-end;height:60px}
.eq div{width:10px;background:linear-gradient(#0ff,#ff2975);animation:b .5s ease-in-out infinite alternate}
@keyframes b{from{height:8px}to{height:60px}}""",
"""<h1>NEON DRIVE</h1><div class="sun"></div><div class="grid"></div>
<div class="track">▶ NOW PLAYING — MIDNIGHT VELOCITY / THE LASER KINGS</div>
<div class="eq" id="eq"></div>""",
"""const eq=document.getElementById('eq');for(let i=0;i<24;i++){const b=document.createElement('div');b.style.animationDelay=(i*0.07)+'s';b.style.animationDuration=(0.3+Math.random()*0.5)+'s';eq.appendChild(b)}""")

# ---------------------------------------------------------------- 5
page("005-zen.html","枯山水 — Digital Zen Garden","Noto Serif JP",
"""body{font-family:'Noto Serif JP',serif;background:#f5f1e8;color:#3a3a3a;display:flex;flex-direction:column;min-height:100vh}
header{text-align:center;padding:60px 20px 20px}h1{font-size:3rem;letter-spacing:.5em;font-weight:400}
.sub{opacity:.55;margin-top:8px;letter-spacing:.3em}
.garden{flex:1;position:relative;margin:40px auto;width:min(92vw,900px);height:420px;background:repeating-linear-gradient(90deg,#ece5d8 0 2px,#f5f1e8 2px 26px);border-radius:8px;box-shadow:inset 0 0 60px #00000010;cursor:crosshair}
.stone{position:absolute;border-radius:50%;background:radial-gradient(circle at 35% 30%,#9a9a9a,#4b4b4b);box-shadow:0 6px 14px #0003}
.ripple{position:absolute;border:1px solid #00000030;border-radius:50%;pointer-events:none;animation:r 2.5s forwards}
@keyframes r{from{width:0;height:0;opacity:1}to{width:160px;height:160px;opacity:0;margin:-80px}}
.quote{text-align:center;padding:40px;font-style:italic;opacity:.65}""",
"""<header><h1>禅</h1><div class="sub">A GARDEN THAT LISTENS</div></header>
<div class="garden" id="g">
<div class="stone" style="width:90px;height:70px;left:12%;top:55%"></div>
<div class="stone" style="width:50px;height:44px;left:22%;top:30%"></div>
<div class="stone" style="width:120px;height:88px;left:62%;top:22%"></div>
<div class="stone" style="width:44px;height:40px;left:78%;top:64%"></div>
</div>
<div class="quote">“In this garden of the heart, moss grows thick over the stones.” — Saigyō</div>""",
"""const g=document.getElementById('g');g.addEventListener('click',e=>{const r=document.createElement('div');r.className='ripple';const b=g.getBoundingClientRect();r.style.left=(e.clientX-b.left)+'px';r.style.top=(e.clientY-b.top)+'px';g.appendChild(r);setTimeout(()=>r.remove(),2500)});""")

# ---------------------------------------------------------------- 6
page("006-terminal.html","root@nostalgia:~ — A Terminal That Remembers","Share Tech Mono",
"""body{background:#05080a;color:#33ff66;font-family:'Share Tech Mono',monospace;padding:30px;font-size:15px;line-height:1.6;text-shadow:0 0 6px #33ff6640}
.crt{position:fixed;inset:0;pointer-events:none;background:repeating-linear-gradient(transparent 0 2px,#0002 2px 4px);z-index:9}
.flicker{animation:f 4s infinite}@keyframes f{97%{opacity:.85}}
.prompt{color:#7fe7ff}.dim{opacity:.55}.warn{color:#ffb300}.pink{color:#ff5ce1}
.cursor{background:#33ff66;color:#33ff66}
.window{max-width:860px;margin:auto;border:1px solid #33ff6633;padding:24px;background:#06120aee}
pre{white-space:pre-wrap}""",
"""<div class="crt"></div><div class="window flicker">
<pre><span class="prompt">visitor@nostalgia:~$</span> cat memories.txt
<span class="dim">[loading cartridge... blowing on it out of habit... OK]</span>

<span class="warn">▸ 1998</span>  Dial-up sang its modem aria. 56k of pure patience.
<span class="warn">▸ 2001</span>  MSN Messenger pings. Green dot = someone worth waiting for.
<span class="warn">▸ 2004</span>  Burning a mix CD took 12 minutes and 3 existential crises.
<span class="warn">▸ 2007</span>  First smartphone. We ordered pizza and never looked up again.
<span class="warn">▸ TODAY</span> <span id="typed" class="pink"></span><span class="cursor">█</span>

<span class="prompt">visitor@nostalgia:~$</span> ls -la /heart
total 1
-rw-r--r-- 1 you you   ∞  keep it running
<span class="prompt">visitor@nostalgia:~$</span> <span class="dim"># press any key to continue_</span></pre></div>""",
"""const t="Still here. Still curious. Still pressing keys hoping something answers.";
let i=0;const el=document.getElementById('typed');
(function ty(){if(i<t.length){el.textContent+=t[i++];setTimeout(ty,55)}})();""")

# ---------------------------------------------------------------- 7
page("007-botanical.html","Herbarium Nocturne — Plants That Never Sleep","Cormorant Garamond",
"""body{font-family:'Cormorant Garamond',serif;background:#0d1b12;color:#e9f2e4}
.hero{min-height:100vh;display:grid;place-items:center;position:relative;background:radial-gradient(ellipse at 50% 120%,#1d3a26,#0d1b12)}
h1{font-size:clamp(3rem,10vw,7rem);font-weight:300;font-style:italic;text-align:center}
h1 em{color:#a8e6cf;font-style:normal}
.leaves{position:absolute;inset:0;overflow:hidden}
.leaf{position:absolute;font-size:2.5rem;animation:fall linear infinite;opacity:.5}
@keyframes fall{from{transform:translateY(-10vh) rotate(0)}to{transform:translateY(110vh) rotate(360deg)}}
.row{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:30px;padding:10vh 8vw}
.plant{border:1px solid #a8e6cf33;padding:30px;border-radius:2px;background:#ffffff05;transition:.4s}
.plant:hover{border-color:#a8e6cf;box-shadow:0 0 40px #a8e6cf22;transform:translateY(-6px)}
.plant h3{font-size:1.8rem;color:#a8e6cf}.latin{font-style:italic;opacity:.6}""",
"""<div class="hero"><div class="leaves" id="L"></div><h1>Herbarium<br><em>Nocturne</em></h1></div>
<div class="row">
<div class="plant"><h3>Moonflower</h3><p class="latin">Ipomoea alba</p><p>Unfurls only after dusk, chasing the moon with white satin trumpets. Farmers once read time by its opening.</p></div>
<div class="plant"><h3>Queen of the Night</h3><p class="latin">Epiphyllum oxypetalum</p><p>Blooms once a year, for a single night, then vanishes before dawn. Gardens throw parties around its schedule.</p></div>
<div class="plant"><h3>Dame's Rocket</h3><p class="latin">Hesperis matronalis</p><p>Releases its scent at twilight when day-pollinators sleep. A letter written to moths.</p></div>
</div>""",
"""const L=document.getElementById('L');
for(let i=0;i<18;i++){const d=document.createElement('div');d.className='leaf';d.textContent=['🍃','🌿','🍂'][i%3];d.style.left=Math.random()*100+'vw';d.style.animationDuration=(7+Math.random()*10)+'s';d.style.animationDelay=-Math.random()*15+'s';L.appendChild(d)}""")

# ---------------------------------------------------------------- 8
page("008-particles.html","Particle Poetry — Type Anything","Inter",
"""body{font-family:'Inter';background:#0e0e11;color:#fff;display:grid;place-items:center;min-height:100vh}
canvas{position:fixed;inset:0}
.ui{position:fixed;bottom:8vh;width:min(90vw,520px);text-align:center;z-index:2}
input{width:100%;background:#ffffff10;border:1px solid #ffffff30;color:#fff;font-size:2rem;text-align:center;padding:14px;border-radius:99px;outline:none;font-family:inherit}
input:focus{border-color:#7c5cff;box-shadow:0 0 30px #7c5cff40}
.hint{margin-top:12px;opacity:.5;font-size:.85rem;letter-spacing:.2em;text-transform:uppercase}""",
"""<canvas id="c"></canvas><div class="ui"><input id="inp" value="HELLO" maxlength="12" spellcheck="false"><div class="hint">the particles obey your words</div></div>""",
"""const c=document.getElementById('c'),ctx=c.getContext('2d');
let W,H,P=[],mouse={x:-999,y:-999};
function resize(){W=c.width=innerWidth;H=c.height=innerHeight}resize();onresize=()=>{resize();draw()}
addEventListener('mousemove',e=>{mouse.x=e.clientX;mouse.y=e.clientY});
const inp=document.getElementById('inp');
function draw(){const off=document.createElement('canvas');off.width=W;off.height=H;const o=off.getContext('2d');
o.fillStyle='#fff';o.font=`900 ${Math.min(W/ (inp.value.length*0.75), H*0.4)}px Inter,sans-serif`;o.textAlign='center';o.textBaseline='middle';o.fillText(inp.value||' ',W/2,H/2-60);
const d=o.getImageData(0,0,W,H).data;P=[];
for(let y=0;y<H;y+=4)for(let x=0;x<W;x+=4){if(d[(y*W+x)*4+3]>128)P.push({x,y,ox:x,oy:y,vx:0,vy:0})}}
draw();inp.addEventListener('input',draw);
(function loop(){ctx.fillStyle='rgba(14,14,17,.25)';ctx.fillRect(0,0,W,H);
for(const p of P){const dx=p.x-mouse.x,dy=p.y-mouse.y,d2=dx*dx+dy*dy;
if(d2<9000){const d=Math.sqrt(d2)||1;p.vx+=dx/d*4;p.vy+=dy/d*4}else{p.vx+=(p.ox-p.x)*.08;p.vy+=(p.oy-p.y)*.08}
p.vx*=.86;p.vy*=.86;p.x+=p.vx;p.y+=p.vy;
const sp=Math.hypot(p.vx,p.vy);ctx.fillStyle=`hsl(${260+sp*8},90%,${60+sp}%)`;ctx.fillRect(p.x,p.y,2,2)}
requestAnimationFrame(loop)})();""")

# ---------------------------------------------------------------- 9
page("009-vintage-passport.html","Visa Stamps — A Traveller's Passport","Special Elite",
"""body{font-family:'Special Elite',monospace;background:#d9c9a3 url('');color:#3c2f1a;padding:40px}
.book{max-width:720px;margin:auto;background:#efe3c2;border:2px solid #a08c5a;box-shadow:0 20px 60px #0004;padding:50px;position:relative}
.book::before{content:'';position:absolute;left:50%;top:0;bottom:0;width:2px;background:#a08c5a44}
h1{text-align:center;font-size:2.2rem;letter-spacing:.3em;border-bottom:3px double #3c2f1a;padding-bottom:16px}
.stamp{display:inline-block;border:4px solid;border-radius:6px;padding:12px 20px;margin:24px 10px;transform:rotate(var(--r));opacity:.85;font-size:1.1rem;box-shadow:inset 0 0 12px currentColor}
.s1{color:#b03a2e;--r:-8deg}.s2{color:#2e5aa8;--r:6deg}.s3{color:#2e7d32;--r:-3deg}.s4{color:#7b1fa2;--r:10deg}.s5{color:#c77b1f;--r:-12deg}
.entry{margin:30px 0;padding-left:20px;border-left:4px dotted #a08c5a}
.entry b{font-size:1.2rem}""",
"""<div class="book"><h1>PASSPORT · No. 88-KESTREL</h1>
<div style="text-align:center"><span class="stamp s1">ENTRY ✓ TOKYO<br>花見 SEASON</span><span class="stamp s2">VISA · REYKJAVÍK<br>AURORA CLEAR</span></div>
<div class="entry"><b>04·2019 Marrakech</b><p>Soldiers of spice towers in the souk. Followed my nose, got lost twice, ate better for it.</p></div>
<div class="entry"><b>09·2020 Lisbon</b><p>Trams climbing like they're apologising to the hills. Custard tart #6 that evening.</p></div>
<div style="text-align:center"><span class="stamp s3">CLEARANCE · CUSCO</span><span class="stamp s4">TRANSIT TBILISI</span><span class="stamp s5">OVERSTAYED ★ HANOI</span></div>
<div class="entry"><b>03·2026 Somewhere Good</b><p>Pages still filling. Ink still wet. Do not staple corner.</p></div></div>""")

# ---------------------------------------------------------------- 10
page("010-glassmorphism.html","Aurora Glass — Weather From Another Planet","Poppins",
"""body{font-family:'Poppins';min-height:100vh;background:linear-gradient(135deg,#0f2027,#2c5364,#7b4397);overflow-x:hidden;color:#fff}
.blob{position:fixed;border-radius:50%;filter:blur(90px);opacity:.55;z-index:0}
.b1{width:420px;height:420px;background:#ff6ec7;top:-100px;left:-80px;animation:fl 9s ease-in-out infinite alternate}
.b2{width:380px;height:380px;background:#00d4ff;bottom:-90px;right:-60px;animation:fl 11s ease-in-out infinite alternate-reverse}
@keyframes fl{to{transform:translate(60px,40px) scale(1.15)}}
.wrap{position:relative;z-index:1;display:grid;place-items:center;min-height:100vh;gap:30px;padding:40px}
.glass{background:#ffffff14;border:1px solid #ffffff2e;backdrop-filter:blur(18px);border-radius:28px;padding:40px 50px;box-shadow:0 30px 80px #00000045;transition:.3s}
.glass:hover{transform:translateY(-8px) rotate(-.5deg)}
.temp{font-size:5rem;font-weight:200}.city{letter-spacing:.4em;opacity:.8;text-transform:uppercase;font-size:.8rem}
.grid3{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:20px;width:min(92vw,760px)}
.mini{padding:22px;text-align:center}""",
"""<div class="blob b1"></div><div class="blob b2"></div>
<div class="wrap">
<div class="glass" style="text-align:center"><div class="city">Kepler-452b · Tomorrow</div><div class="temp">-3°</div><div>⛅ Partly meteor-showered</div></div>
<div class="grid3">
<div class="glass mini"><div class="city">Dawn</div><div style="font-size:2rem">☄️</div><div>-6°</div></div>
<div class="glass mini"><div class="city">Noon</div><div style="font-size:2rem">🌤️</div><div>-1°</div></div>
<div class="glass mini"><div class="city">Dusk</div><div style="font-size:2rem">🌕×2</div><div>-4°</div></div>
<div class="glass mini"><div class="city">Night</div><div style="font-size:2rem">🌠</div><div>-9°</div></div>
</div></div>""")

# ---------------------------------------------------------------- 11
page("011-timeline.html","The Long Now — A Timeline of Everything","Space Grotesk",
"""body{font-family:'Space Grotesk';background:#09090f;color:#ddd}
.line{position:fixed;left:50%;top:0;bottom:0;width:2px;background:linear-gradient(#ff5c7a,#7c5cff,#41ead4)}
.item{width:min(44vw,520px);margin:16vh auto;padding:26px 30px;background:#15151f;border-radius:14px;position:relative;border:1px solid #ffffff12;transition:.3s}
.item:nth-child(odd){margin-left:max(6vw,calc(50% + 40px))}
.item:nth-child(even){margin-left:max(6vw,calc(50% - 560px))}
.item:hover{border-color:#7c5cff;transform:scale(1.03)}
.item::before{content:'';position:absolute;top:34px;width:14px;height:14px;border-radius:50%;background:#41ead4;box-shadow:0 0 20px #41ead4}
.item:nth-child(odd)::before{left:-47px}.item:nth-child(even)::before{right:-47px}
.when{color:#ff5c7a;font-size:.8rem;letter-spacing:.25em;text-transform:uppercase}
h2{font-size:1.6rem;margin:8px 0}
h1{font-size:clamp(2.5rem,8vw,5rem);text-align:center;padding:24vh 20px 6vh;background:linear-gradient(#fff,#7c5cff);-webkit-background-clip:text;-webkit-text-fill-color:transparent}""",
"""<div class="line"></div><h1>The Long Now</h1>
<div class="item"><div class="when">13.8 Bya</div><h2>Everything starts</h2><p>No place, no when, then suddenly all of it.</p></div>
<div class="item"><div class="when">4.5 Bya</div><h2>Earth settles</h2><p>A molten ball cools just enough for water to have opinions.</p></div>
<div class="item"><div class="when">3.8 Bya</div><h2>Life improvises</h2><p>Chemistry learns to copy itself. It never stops.</p></div>
<div class="item"><div class="when">~300 KA</div><h2>We notice things</h2><p>Humans invent language, music, and the complaint.</p></div>
<div class="item"><div class="when">1991</div><h2>The web wakes up</h2><p>TimBL ships the first site. You are reading its great-grandchild.</p></div>
<div class="item"><div class="when">Now</div><h2>You're here</h2><p>13.8 billion years of cosmic logistics, converging on this scroll.</p></div>""")

# ---------------------------------------------------------------- 12
page("012-menu.html","Le Petit Code — A Restaurant Menu for Programmers","Playfair Display",
"""body{font-family:'Playfair Display',serif;background:#1a120b;color:#f3e5c9}
.menu{max-width:640px;margin:6vh auto;border:1px double #c9a227;padding:60px 50px;background:#120c07}
h1{text-align:center;font-size:3rem;color:#c9a227}
.tag{text-align:center;font-style:italic;opacity:.7;margin-bottom:40px}
.dish{display:flex;justify-content:space-between;gap:20px;margin:26px 0;align-items:baseline}
.dots{flex:1;border-bottom:2px dotted #c9a22755;transform:translateY(-6px)}
.dish h3{font-size:1.3rem}.dish small{display:block;opacity:.6;font-style:italic;font-family:monospace}
.price{font-family:monospace;color:#c9a227}
.sect{text-align:center;letter-spacing:.5em;margin:44px 0 10px;color:#c9a227;font-size:.9rem}
footer{text-align:center;padding:30px;opacity:.6;font-style:italic}""",
"""<div class="menu"><h1>Le Petit Code</h1><div class="tag">« cuisine served with O(1) wait times »</div>
<div class="sect">ENTRÉES</div>
<div class="dish"><div><h3>Recursive French Onion</h3><small>soup(n-1) until base case: caramelised</small></div><div class="dots"></div><div class="price">€9</div></div>
<div class="dish"><div><h3>Null Pointer Bruschetta</h3><small>tomato, basil, and nothing to reference</small></div><div class="dots"></div><div class="price">€7</div></div>
<div class="sect">PLATS</div>
<div class="dish"><div><h3>Duck à la Race Condition</h3><small>two chefs, one pan, unpredictable plating</small></div><div class="dots"></div><div class="price">€24</div></div>
<div class="dish"><div><h3>Spaghetti Deadlock</h3><small>fork left, fork right, will not resolve</small></div><div class="dots"></div><div class="price">€16</div></div>
<div class="sect">DESSERTS</div>
<div class="dish"><div><h3>Infinite Loop Soufflé</h3><small>while(true){ rise(); } — please eat quickly</small></div><div class="dots"></div><div class="price">€11</div></div>
<footer>Gratuity optional · Bugs welcome, bugs fried extra €2</footer></div>""")

# ---------------------------------------------------------------- 13
page("013-glitch.html","GLITCHCORE // Broken On Purpose","Rubik Mono One",
"""body{font-family:'Rubik Mono One';background:#0a0a0a;color:#fff;overflow-x:hidden}
.hero{min-height:100vh;display:grid;place-items:center;position:relative}
.g{font-size:clamp(2.5rem,9vw,6rem);position:relative;color:#fff}
.g::before,.g::after{content:attr(data-t);position:absolute;left:0;top:0;width:100%}
.g::before{color:#ff003c;animation:s1 2.4s infinite steps(2)}
.g::after{color:#00fff9;animation:s2 3.1s infinite steps(2)}
@keyframes s1{0%,100%{clip-path:inset(0 0 85% 0);transform:translate(-5px)}33%{clip-path:inset(40% 0 30% 0);transform:translate(5px)}66%{clip-path:inset(80% 0 0 0);transform:translate(-3px)}}
@keyframes s2{0%,100%{clip-path:inset(70% 0 10% 0);transform:translate(4px)}40%{clip-path:inset(10% 0 60% 0);transform:translate(-6px)}70%{clip-path:inset(50% 0 20% 0);transform:translate(2px)}}
.scan{position:fixed;inset:0;pointer-events:none;background:repeating-linear-gradient(#ffffff05 0 1px,transparent 1px 3px)}
.blocks{position:fixed;inset:0;pointer-events:none}
.blk{position:absolute;background:#ff003c;mix-blend-mode:screen;opacity:.7}
p.copy{font-family:monospace;font-weight:100;max-width:640px;margin:20vh auto;padding:0 24px;line-height:2;color:#9f9f9f}""",
"""<div class="scan"></div><div class="blocks" id="B"></div>
<div class="hero"><h1 class="g" data-t="ERROR 404">ERROR 404</h1></div>
<p class="copy">Perfection is a rendering bug. This page crashes beautifully on purpose. Static screams, colour bleeds, pixels defect from their posts — and somehow it loads fine on your machine and nowhere else.</p>""",
"""const B=document.getElementById('B');
setInterval(()=>{B.innerHTML='';for(let i=0;i<5;i++){const d=document.createElement('div');d.className='blk';d.style.cssText=`left:${Math.random()*100}vw;top:${Math.random()*100}vh;width:${20+Math.random()*180}px;height:${2+Math.random()*10}px;background:${['#ff003c','#00fff9','#fff'][i%3]}`;B.appendChild(d)}},900);""")

# ---------------------------------------------------------------- 14
page("014-cocktail.html","The Alchemist's Bar — Cocktails With Backstories","Abril Fatface",
"""body{font-family:'Abril Fatface',serif;background:#160b1e;color:#f5e9d0}
.bar{max-width:820px;margin:auto;padding:10vh 24px}
h1{font-size:clamp(2.5rem,8vw,4.5rem);color:#e8b64c}
.cock{display:grid;grid-template-columns:120px 1fr;gap:26px;margin:44px 0;padding-bottom:36px;border-bottom:1px solid #e8b64c33}
.glass{width:110px;height:150px;position:relative}
.liq{position:absolute;bottom:0;left:0;right:0;border-radius:0 0 40px 40px;transition:height 1.2s ease}
.stem{position:absolute;bottom:-30px;left:50%;width:3px;height:34px;background:#f5e9d088;transform:translateX(-50%)}
.base{position:absolute;bottom:-36px;left:50%;width:56px;height:5px;background:#f5e9d088;transform:translateX(-50%);border-radius:3px}
h2{color:#e8b64c;font-size:1.7rem}.story{font-family:Georgia,serif;font-weight:400;line-height:1.8;opacity:.85}
.rx{font-family:monospace;font-size:.8rem;color:#b58cff}""",
"""<div class="bar"><h1>The Alchemist's Bar</h1>
<div class="cock"><div class="glass"><div class="liq" style="background:linear-gradient(#ff7b54,#c0392b)" data-h="70%"></div><div class="stem"></div><div class="base"></div></div>
<div><h2>Phoenix Old Fashioned</h2><p class="story">Bourbon, burnt orange, and a smoke ring pulled off a cedar plank. Served to anyone who needed a second act.</p><p class="rx">45ml rye · 15 ml demerara · 2 dashes regret (angostura)</p></div></div>
<div class="cock"><div class="glass"><div class="liq" style="background:linear-gradient(#58d68d,#1e8449)" data-h="55%"></div><div class="stem"></div><div class="base"></div></div>
<div><h2>Green Flash Absinthe</h2><p class="story">Vert d'eau poured over a sugar cube slowly collapsing. Hallucinations sold separately; imagination included.</p><p class="rx">30ml absinthe · ice water cascade · one open window</p></div></div>
<div class="cock"><div class="glass"><div class="liq" style="background:linear-gradient(#a569bd,#4a235a)" data-h="85%"></div><div class="stem"></div><div class="base"></div></div>
<div><h2>Midnight Negotiation</h2><p class="story">Gin, blackberry, violet, and a brine so sharp it ends arguments. House rule: drink two, decide nothing.</p><p class="rx">50ml gin · 20ml crème de mûre · 3 drops violet · sea</p></div></div></div>""",
"""document.querySelectorAll('.liq').forEach(l=>{l.style.height='0';setTimeout(()=>l.style.height=l.dataset.h,300)});""")

# ---------------------------------------------------------------- 15
page("015-isometric.html","IsoCity — A Tiny Isometric Metropolis","Lexend",
"""body{font-family:'Lexend';background:#1b1f3b;color:#eaf0ff;display:grid;place-items:center;min-height:100vh}
.scene{perspective:1200px}
.tile{width:min(88vw,560px);aspect-ratio:1;background:#232a52;transform:rotateX(56deg) rotateZ(45deg);position:relative;box-shadow:0 60px 120px #000a;transition:transform .6s}
.tile:hover{transform:rotateX(56deg) rotateZ(45deg) scale(1.05)}
.b{position:absolute;transform-style:preserve-3d}
.roof,.side1,.side2{position:absolute}
h1{position:fixed;top:24px;left:28px;font-size:1.4rem;letter-spacing:.2em}
.legend{position:fixed;bottom:24px;right:28px;font-size:.8rem;opacity:.7;text-align:right}""",
"""<h1>ISO CITY · pop. 1,024</h1>
<div class="scene"><div class="tile" id="t"></div></div>
<div class="legend">drag-free hover to zoom district<br>all buildings code-approved</div>""",
"""const t=document.getElementById('t');const cols=['#ff6b6b','#feca57','#48dbfb','#1dd1a1','#5f27cd','#ff9ff3'];
for(let i=0;i<30;i++){const h=20+Math.random()*70,x=Math.random()*82,y=Math.random()*82,c=cols[i%cols.length];
const b=document.createElement('div');b.className='b';
b.style.cssText=`left:${x}%;top:${y}%;width:34px;height:34px;transform:translateZ(${h}px)`;
b.innerHTML=`<div style="position:absolute;inset:0;background:${c};box-shadow:0 0 12px ${c}66"></div>
<div style="position:absolute;top:100%;left:0;width:34px;height:${h}px;background:${c}88;transform-origin:top;transform:rotateX(-90deg)"></div>
<div style="position:absolute;top:0;left:100%;width:${h}px;height:34px;background:${c}55;transform-origin:left;transform:rotateY(90deg)"></div>`;
t.appendChild(b)}""")

# ---------------------------------------------------------------- 16
page("016-lofi.html","lofi radio — beats to decompress to","Quicksand",
"""body{font-family:'Quicksand';background:linear-gradient(#2b2140,#4a3055);color:#ffe6f2;min-height:100vh;display:grid;place-items:center}
.room{width:min(92vw,520px);background:#201936;border-radius:20px;padding:34px;box-shadow:0 30px 80px #0009;text-align:center}
.vinyl{width:170px;height:170px;border-radius:50%;margin:0 auto 22px;background:repeating-radial-gradient(#111 0 3px,#222 3px 6px);position:relative;animation:sp 3s linear infinite;box-shadow:0 0 0 6px #0a0a0a}
.vinyl.stop{animation-play-state:paused}
.vinyl::after{content:'';position:absolute;inset:38%;border-radius:50%;background:#ff8fb1}
@keyframes sp{to{transform:rotate(360deg)}}
.trackname{font-size:1.3rem;margin-bottom:4px}
.artist{opacity:.6;margin-bottom:20px}
button{background:#ff8fb1;border:0;color:#201936;font-family:inherit;font-weight:700;padding:12px 30px;border-radius:99px;font-size:1rem;cursor:pointer;transition:.2s}
button:hover{transform:scale(1.06)}
.rain{position:fixed;inset:0;pointer-events:none}
.drop{position:absolute;width:1px;height:14px;background:#ffffff33;animation:dr linear infinite}
@keyframes dr{to{transform:translateY(110vh)}}
.now{margin-top:18px;font-size:.8rem;letter-spacing:.2em;opacity:.7}""",
"""<div class="rain" id="r"></div>
<div class="room"><div class="vinyl" id="v"></div>
<div class="trackname" id="tn">Rainy Window Tape №4</div><div class="artist">sleepy.kettle</div>
<button id="btn">⏸ pause the rain</button>
<div class="now">♫ 12,402 people decompressing right now</div></div>""",
"""const r=document.getElementById('r');for(let i=0;i<60;i++){const d=document.createElement('div');d.className='drop';d.style.cssText=`left:${Math.random()*100}vw;top:${-Math.random()*100}vh;animation-duration:${.5+Math.random()*.7}s;animation-delay:${Math.random()*2}s`;r.appendChild(d)}
const v=document.getElementById('btn');const tracks=[['Rainy Window Tape №4','sleepy.kettle'],['Kettle & Keyboard','mono.mochi'],['3AM Study Hall','dust bunny'],['Teapot Sonata','lo fi lord fred']];let i=0,on=true;
v.onclick=()=>{on=!on;v.textContent=on?'⏸ pause the rain':'▶ resume the rain';document.getElementById('v').classList.toggle('stop',!on);if(on){i=(i+1)%tracks.length;document.getElementById('tn').textContent=tracks[i][0];document.querySelector('.artist').textContent=tracks[i][1]}};""")

# ---------------------------------------------------------------- 17
page("017-artdeco.html","THE GOLDMAN — Art Deco Grand Hotel","Poiret One",
"""body{font-family:'Poiret One';background:#0d0b08;color:#d4af37;text-align:center}
.frame{max-width:720px;margin:6vh auto;border:2px solid #d4af37;padding:70px 40px;position:relative}
.frame::before,.frame::after{content:'';position:absolute;inset:10px;border:1px solid #d4af3766}
h1{font-size:clamp(2.5rem,8vw,4.5rem);letter-spacing:.35em;margin:20px 0}
.rule{display:flex;align-items:center;gap:16px;justify-content:center;margin:26px 0}
.rule::before,.rule::after{content:'';height:1px;width:90px;background:#d4af37}
.sun{font-size:2rem}
.rooms{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:24px;padding:0 8vw 10vh}
.room{border:1px solid #d4af37;padding:30px 18px;transition:.35s;background:#151007}
.room:hover{background:#d4af37;color:#0d0b08;letter-spacing:.08em}
.room h3{font-size:1.4rem;margin-bottom:10px}
small{letter-spacing:.2em;text-transform:uppercase;font-size:.7rem;opacity:.8}""",
"""<div class="frame"><small>EST. MCMXXVII</small><div class="rule"><span class="sun">✦</span></div>
<h1>THE GOLDMAN</h1><div class="rule"><span class="sun">◆</span></div>
<p style="letter-spacing:.25em">GRANDEUR IS A DAILY AMENITY</p>
<div class="rule"><span class="sun">✦</span></div><small>Broadway & Illusion · New York</small></div>
<div class="rooms">
<div class="room"><h3>Gatsby Suite</h3><small>green light included</small><p>Chandelier views. Whisper-required balcony.</p></div>
<div class="room"><h3>Marlow Corner</h3><small>blinds stay open</small><p>Rain sounds on demand. Cigarette holder, unlit.</p></div>
<div class="room"><h3>Robie Penthouse</h3><small>lead & glass</small><p>Stained skylight projects geometry onto breakfast.</p></div></div>""")

# ---------------------------------------------------------------- 18
page("018-dinosaur.html","JURASSIC FREQUENCY — Radio From the Cretaceous","Bungee",
"""body{font-family:'Bungee';background:#0f1d0f;color:#b7ff5a}
.sky{background:radial-gradient(#1d3b1d,#0f1d0f);padding:12vh 8vw;text-align:center;position:relative;overflow:hidden}
h1{font-size:clamp(2.2rem,8vw,5rem);color:#b7ff5a;text-shadow:0 0 30px #b7ff5a55}
.trex{font-size:6rem;display:inline-block;animation:stomp 1s infinite alternate;filter:drop-shadow(0 0 20px #b7ff5a44)}
@keyframes stomp{to{transform:translateY(-14px)}}
.dust{position:absolute;bottom:0;left:0;right:0;height:40%;background:linear-gradient(transparent,#2d4a1d)}
.post{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:22px;padding:8vh 8vw}
.card{background:#15271599;border:2px solid #b7ff5a33;padding:26px;transform:rotate(var(--r));transition:.3s}
.card:hover{transform:rotate(0) scale(1.04);border-color:#b7ff5a}
.amber{color:#ffb347;font-size:.8rem;letter-spacing:.2em}""",
"""<div class="sky"><div class="trex">🦖</div><h1>JURASSIC FREQUENCY</h1><p>98.7 FM · THE ONLY STATION WITH A FOSSIL RECORD</p><div class="dust"></div></div>
<div class="post">
<div class="card" style="--r:-2deg"><div class="amber">TRANSMISSION 01</div><h3>Thunder Lizard Boogie</h3><p>Drummer spotted hitting logs. Audience of pterodactyls unimpressed but airborne.</p></div>
<div class="card" style="--r:1.5deg"><div class="amber">TRANSMISSION 02</div><h3>Brachiosaurus Ballad</h3><p>Slow song. Very slow song. Critics call it 'geological'. Charts disagree.</p></div>
<div class="card" style="--r:-1deg"><div class="amber">TRANSMISSION 03</div><h3>Asteroid Warning Banger</h3><p>One week away from release. Probably the last big thing. Encore guaranteed.</p></div></div>""")

# ---------------------------------------------------------------- 19
page("019-gradient.html","Gradient Lab — Colour Theory Without the Textbook","DM Sans",
"""body{font-family:'DM Sans';background:#101014;color:#fff}
.swatch{height:100vh;display:grid;place-items:center;position:sticky;top:0}
.name{font-size:clamp(2rem,7vw,4.5rem);font-weight:700;text-shadow:0 4px 40px #0006}
.hex{font-family:monospace;opacity:.85;background:#00000044;padding:6px 14px;border-radius:8px;margin-top:10px;display:inline-block}
.stack .swatch{position:relative;height:100vh}""",
"""<div class="stack">
<div class="swatch" style="background:linear-gradient(135deg,#667eea,#764ba2)"><div style="text-align:center"><div class="name">Velvet Dusk</div><div class="hex">#667EEA → #764BA2</div></div></div>
<div class="swatch" style="background:linear-gradient(135deg,#f093fb,#f5576c)"><div style="text-align:center"><div class="name">Bubblegum Riot</div><div class="hex">#F093FB → #F5576C</div></div></div>
<div class="swatch" style="background:linear-gradient(135deg,#4facfe,#00f2fe)"><div style="text-align:center"><div class="name">Glacier Pop</div><div class="hex">#4FACFE → #00F2FE</div></div></div>
<div class="swatch" style="background:linear-gradient(135deg,#43e97b,#38f9d7)"><div style="text-align:center"><div class="name">Electric Meadow</div><div class="hex">#43E97B → #38F9D7</div></div></div>
<div class="swatch" style="background:linear-gradient(135deg,#fa709a,#fee140)"><div style="text-align:center"><div class="name">Sunset Candy</div><div class="hex">#FA709A → #FEE140</div></div></div>
<div class="swatch" style="background:linear-gradient(135deg,#30cfd0,#330867)"><div style="text-align:center"><div class="name">Deep Reef Neon</div><div class="hex">#30CFD0 → #330867</div></div></div>
</div>""")

# ---------------------------------------------------------------- 20
page("020-clockwork.html","The Horologist — Clocks, Gears & Patience","Cinzel",
"""body{font-family:'Cinzel',serif;background:#141008;color:#e8d5a3;text-align:center;padding-bottom:14vh}
.gear{display:inline-block;font-size:5rem;animation:rot 8s linear infinite;color:#b8860b}
.gear.rev{animation-direction:reverse}
@keyframes rot{to{transform:rotate(360deg)}}
h1{font-size:clamp(2rem,6vw,3.6rem);letter-spacing:.2em;margin:20px}
.face{width:220px;height:220px;border:6px solid #b8860b;border-radius:50%;margin:40px auto;position:relative;background:#1c1508}
.hand{position:absolute;left:50%;bottom:50%;transform-origin:bottom;background:#e8d5a3;border-radius:4px}
.dot{position:absolute;width:12px;height:12px;background:#b8860b;border-radius:50%;left:50%;top:50%;transform:translate(-50%,-50%)}
.shop{max-width:640px;margin:auto;text-align:left;padding:0 24px;line-height:2}
.shop h2{text-align:center;color:#b8860b;letter-spacing:.3em;margin:60px 0 20px}""",
"""<div style="margin-top:8vh"><span class="gear">⚙</span><span class="gear rev" style="font-size:3.4rem">⚙</span><span class="gear" style="font-size:4.2rem">⚙</span></div>
<h1>THE HOROLOGIST</h1><p style="letter-spacing:.4em;font-size:.8rem">TIME, TAILORED</p>
<div class="face"><div class="hand" id="hh" style="width:6px;height:55px"></div><div class="hand" id="mh" style="width:4px;height:80px"></div><div class="hand" id="sh" style="width:2px;height:95px;background:#c0392b"></div><div class="dot"></div></div>
<div class="shop"><h2>— SERVICES —</h2>
<b>Grandfather Therapy.</b> Your 1890s clock hums tunelessly? We sing it back to pitch.<br>
<b>Mainspring Rebirth.</b> Coiled steel deserves second chances. Same for Tuesdays.<br>
<b>Escapement Tuning.</b> The tiny heartbeat between tick and tock, adjusted to your resting pulse.</div>""",
"""function tick(){const d=new Date(),s=d.getSeconds()+d.getMilliseconds()/1000,m=d.getMinutes()+s/60,h=(d.getHours()%12)+m/60;
sh.style.transform=`rotate(${s*6}deg)`;mh.style.transform=`rotate(${m*6}deg)`;hh.style.transform=`rotate(${h*30}deg)`;requestAnimationFrame(tick)}
const sh=document.getElementById('sh'),mh=document.getElementById('mh'),hh=document.getElementById('hh');tick();""")

# ---------------------------------------------------------------- 21
page("021-portfolio.html","NOVA REYES — Creative Developer Portfolio","Syne",
"""body{font-family:'Syne';background:#0b0b0d;color:#f4f4f0}
nav{display:flex;justify-content:space-between;padding:26px 6vw;position:fixed;width:100%;top:0;z-index:5;background:#0b0b0dcc;backdrop-filter:blur(8px)}
.hero{min-height:100vh;display:flex;align-items:flex-end;padding:0 6vw 12vh}
h1{font-size:clamp(3rem,11vw,9rem);line-height:.9;text-transform:uppercase}
h1 span{color:#c6f24e}
.sub{max-width:520px;margin-left:auto;font-size:1.1rem;line-height:1.8;opacity:.75}
.works{padding:6vh 6vw}
.work{display:flex;justify-content:space-between;align-items:center;padding:34px 0;border-top:1px solid #ffffff1a;cursor:pointer;transition:.3s;gap:20px}
.work:hover{padding-left:20px;background:linear-gradient(90deg,#c6f24e11,transparent)}
.work h2{font-size:clamp(1.6rem,4vw,2.6rem);text-transform:uppercase}
.tag{font-size:.8rem;letter-spacing:.2em;color:#c6f24e;white-space:nowrap}
.year{opacity:.4;font-family:monospace}
footer{padding:12vh 6vw;text-align:center;font-size:clamp(1.5rem,5vw,3rem)}
footer a{color:#c6f24e;text-decoration:none;border-bottom:2px solid}""",
"""<nav><b>NR●</b><span style="font-size:.8rem;letter-spacing:.3em">PORTFOLIO ’26</span></nav>
<div class="hero"><div><h1>Creative<br><span>Developer</span></h1></div>
<p class="sub">I build interfaces that behave like they have a pulse. Motion, type, and just enough chaos.</p></div>
<div class="works">
<div class="work"><h2>Kinetic Type Engine</h2><span class="tag">WEBGL · TYPE</span><span class="year">2026</span></div>
<div class="work"><h2>Museum of Sounds</h2><span class="tag">AUDIO · THREE.JS</span><span class="year">2025</span></div>
<div class="work"><h2>Static Dreams Hotel</h2><span class="tag">BRANDING · SHADER</span><span class="year">2025</span></div>
<div class="work"><h2>Tide Table App</h2><span class="tag">PRODUCT · MOTION</span><span class="year">2024</span></div></div>
<footer>Have an impossible idea? <a href="mailto:hi@novareyes.dev">let's argue about it →</a></footer>""")

# ---------------------------------------------------------------- 22
page("022-retro-game.html","PIXEL QUEST — An 8-Bit Adventure","Press Start 2P",
"""body{font-family:'Press Start 2P';background:#0f380f;color:#9bbc0f;display:grid;place-items:center;min-height:100vh;padding:20px}
.screen{width:min(94vw,640px);border:8px solid #306230;background:#0f380f;padding:24px;image-rendering:pixelated}
.hud{display:flex;justify-content:space-between;font-size:.65rem;margin-bottom:16px}
.world{height:260px;position:relative;background:linear-gradient(#0f380f 60%,#306230 60%);overflow:hidden}
.hero8{position:absolute;bottom:60px;left:40px;font-size:2rem;transition:left .15s linear}
.tree{position:absolute;bottom:96px;font-size:2rem}
.msg{margin-top:16px;font-size:.75rem;line-height:2;min-height:64px}
.btns{display:flex;gap:12px;margin-top:14px;flex-wrap:wrap}
button{font-family:inherit;background:#306230;color:#9bbc0f;border:4px solid #9bbc0f;padding:10px 16px;cursor:pointer;font-size:.65rem}
button:active{transform:translateY(3px)}""",
"""<div class="screen"><div class="hud"><span>HP ♥♥♥</span><span id="score">GOLD: 0</span><span>LVL 1</span></div>
<div class="world" id="w"><div class="hero8" id="p">🧙</div></div>
<div class="msg" id="m">> PRESS ▶ TO ADVENTURE. STAY HYDRATED. FLEE SPIDERS.</div>
<div class="btns"><button id="go">▶ WALK</button><button id="dig">⛏ DIG</button><button id="sing">🎵 SING</button></div></div>""",
"""const p=document.getElementById('p'),m=document.getElementById('m'),w=document.getElementById('w');let x=40,gold=0,step=0;
const lines=['> A COIN! SPECTACULAR FIND.','> THE TREE SAYS NOTHING. WISE TREE.','> YOU FOUND GOBLIN CHANGE.','> ROOT SYSTEM: DELICIOUS. LEGALLY NOT FOOD.','> SUN SETS. MOON FILES COMPLAINT.'];
document.getElementById('go').onclick=()=>{x=(x+37)%540;p.style.left=x+'px';if(Math.random()<.4){gold+=Math.floor(Math.random()*7)+1;document.getElementById('score').textContent='GOLD: '+gold;m.textContent=lines[step++%lines.length]}else m.textContent='> *determined walking noises*'};
document.getElementById('dig').onclick=()=>{m.textContent=Math.random()<.5?'> DUG UP AN ANCIENT SOCK. +2 GOLD':'> HIT BEDROCK. BEDROCK UNBOTHERED'};
document.getElementById('sing').onclick=()=>{m.textContent='> 🎶 DOODLY DOODLY DOO... 🎶\n> A DISTANT DRUM ANSWERS. Rude.'};
for(let i=0;i<5;i++){const t=document.createElement('div');t.className='tree';t.textContent=['🌲','🌳','🌵'][i%3];t.style.left=(70+i*110)+'px';w.appendChild(t)}""")

# ---------------------------------------------------------------- 23
page("023-podcast.html","STATIC & CO. — The Audio Misadventure Podcast","Sora",
"""body{font-family:'Sora';background:#0e0a1a;color:#efeaff}
.top{background:linear-gradient(160deg,#5b2be8,#e8388f);padding:12vh 8vw 10vh;clip-path:polygon(0 0,100% 0,100% 88%,0 100%)}
h1{font-size:clamp(2.6rem,9vw,5.5rem);text-transform:lowercase}
.ep{display:grid;grid-template-columns:70px 1fr auto;gap:20px;align-items:center;padding:26px 8vw;border-bottom:1px solid #ffffff14;transition:.25s;cursor:pointer}
.ep:hover{background:#5b2be818;padding-left:calc(8vw + 12px)}
.num{font-size:2rem;opacity:.35;font-weight:800}
.play{width:46px;height:46px;border-radius:50%;background:#e8388f;display:grid;place-items:center;color:#fff;font-size:.9rem;transition:.2s}
.ep:hover .play{transform:scale(1.15);box-shadow:0 0 24px #e8388f88}
.dur{opacity:.5;font-family:monospace;font-size:.85rem}
.wave{display:flex;gap:3px;align-items:flex-end;height:34px;margin-top:8px}
.wave i{width:3px;background:#8f7bff;border-radius:2px}
.host{padding:8vh 8vw;display:flex;gap:24px;align-items:center;flex-wrap:wrap}
.av{width:90px;height:90px;border-radius:50%;background:conic-gradient(#5b2be8,#e8388f,#5b2be8);display:grid;place-items:center;font-size:2rem}""",
"""<div class="top"><h1>static & co.</h1><p style="max-width:480px">Two hosts, one microphone, zero scheduled topics. Weekly-ish audio misadventures since 2023.</p></div>
<div class="ep"><div class="num">041</div><div><b>The Episode That Recorded Itself</b><div class="wave" data-n="26"></div></div><div><span class="dur">52:11</span> <div class="play">▶</div></div></div>
<div class="ep"><div class="num">040</div><div><b>Interview: A Locksmith About Trust</b><div class="wave" data-n="34"></div></div><div><span class="dur">67:03</span> <div class="play">▶</div></div></div>
<div class="ep"><div class="num">039</div><div><b>We Read Our Old Emails Aloud</b><div class="wave" data-n="20"></div></div><div><span class="dur">41:57</span> <div class="play">▶</div></div></div>
<div class="host"><div class="av">🎙️</div><div><b>Mara Vance</b> — asks the questions she'll regret<br><small style="opacity:.6">producer, apologist</small></div>
<div class="av">🎛️</div><div><b>Ilya Brandt</b> — owns too many cables<br><small style="opacity:.6">audio wizard, cable hoarder</small></div></div>""",
"""document.querySelectorAll('.wave').forEach(w=>{for(let i=0;i<+w.dataset.n;i++){const b=document.createElement('i');b.style.height=(20+Math.random()*80)+'%';w.appendChild(b)}});""")

# ---------------------------------------------------------------- 24
page("024-magazine.html","MERIDIAN — Issue 07: The Slow Issue","Lora",
"""body{font-family:'Lora',serif;background:#faf6ef;color:#1e1a14}
.cover{min-height:100vh;display:grid;grid-template-columns:1.2fr 1fr;gap:0}
.left{padding:8vh 5vw;display:flex;flex-direction:column;justify-content:space-between;border-right:1px solid #1e1a1422}
.mast{font-size:clamp(3rem,9vw,6rem);letter-spacing:-.03em;line-height:.95}
.issue{writing-mode:vertical-rl;transform:rotate(180deg);position:absolute;right:14px;top:20px;letter-spacing:.4em;font-size:.75rem}
.bigpic{background:linear-gradient(210deg,#e8a87c,#c38d9e 55%,#41b3a3);display:grid;place-items:center;font-size:7rem;position:relative}
.bigpic figcaption{position:absolute;bottom:20px;left:20px;font-size:.75rem;font-style:italic;color:#fff8}
.cols{columns:2;gap:40px;padding:8vh 6vw;font-size:1.05rem;line-height:1.9}
.cols h2{column-span:all;font-size:2.4rem;margin-bottom:20px;font-weight:600}
.dropcap::first-letter{float:left;font-size:4.6rem;line-height:.8;padding:6px 10px 0 0;color:#c38d9e}""",
"""<div class="cover"><div class="left"><div>MERIDIAN<span class="issue">ISSUE 07 · AUTUMN</span></div>
<div><h2 style="font-size:2rem">THE SLOW ISSUE</h2><p style="font-style:italic;opacity:.7;margin-top:10px">On patience, tide tables, and bread that takes three days to hate you back.</p></div>
<div style="font-size:.8rem;letter-spacing:.2em">£12 · SUBSCRIBE IN PEN-INK</div></div>
<figure class="bigpic">🌊<figcaption>“Sea, thinking about it” — cover no.7</figcaption></figure></div>
<div class="cols"><h2>Notes From the Tide Table</h2>
<p class="dropcap">There is a notebook kept in a harbour shed in which volunteers have written the sea's mood, by hand, every morning since 1962. Calm. Choppy. "Politely indifferent." It is, I have come to believe, the best newspaper in Britain.</p>
<p>Slow living is sold to us as candles and linen. But the tide table knows the truth: slowness isn't aesthetic, it's attention. You cannot rush water. You can only show up at the right hour and be grateful.</p>
<p>Turn the page for three days of bread, a profile of the last night-train conductor, and an argument with a snail.</p></div>""")

# ---------------------------------------------------------------- 25
page("025-galaxy.html","Spin Cycle — An Interactive Galaxy","Michroma",
"""body{font-family:'Michroma';background:#000;color:#cfd8ff;overflow:hidden}
canvas{display:block;cursor:grab}
.ui{position:fixed;top:20px;left:24px;z-index:2}
h1{font-size:1.2rem;letter-spacing:.4em}.hint{opacity:.5;font-size:.7rem;margin-top:8px}
.stat{position:fixed;bottom:20px;right:24px;text-align:right;font-size:.7rem;opacity:.6;z-index:2;font-family:monospace}""",
"""<div class="ui"><h1>SPIN CYCLE</h1><div class="hint">drag to rotate · scroll to zoom · stars obey gravity</div></div>
<canvas id="c"></canvas><div class="stat" id="st"></div>""",
"""const c=document.getElementById('c'),x=c.getContext('2d');let W,H;
function rs(){W=c.width=innerWidth;H=c.height=innerHeight}rs();onresize=rs;
const S=[...Array(1400)].map(()=>{const r=Math.random()**.5*420,a=Math.random()*7,cw=Math.random()*7|0;
return{r,a,cw,tilt:(cw-.5)*.5,size:Math.random()*1.6+.3,hue:[210,260,330,45][cw]}});
let rot=0,drag=null,zoom=1;
c.onmousedown=e=>drag={x:e.clientX,r:rot};onmouseup=()=>drag=null;
onmousemove=e=>{if(drag)rot=drag.r+(e.clientX-drag.x)*.005};
onwheel=e=>zoom=Math.max(.4,Math.min(2.4,zoom-e.deltaY*.001));
(function l(){x.fillStyle='#000';x.fillRect(0,0,W,H);rot+=.0016;
for(const s of S){const a=s.a+rot*(1+s.cw*.12),z=Math.sin(a)*s.tilt;
const px=Math.cos(a)*s.r*zoom,py=Math.sin(a)*s.r*zoom*.38*(1+z*.4);
x.globalAlpha=.4+.6*Math.abs(Math.cos(a));x.fillStyle=`hsl(${s.hue},80%,${60+z*25}%)`;
x.beginPath();x.arc(W/2+px,H/2+py,s.size,0,7);x.fill()}
x.globalAlpha=1;x.fillStyle='#fff8dc';x.shadowColor='#ffd56b';x.shadowBlur=40;x.beginPath();x.arc(W/2,H/2,7,0,7);x.fill();x.shadowBlur=0;
st.textContent=`ROT ${rot.toFixed(2)}rad · ZOOM ${zoom.toFixed(2)} · STARS 1400`;requestAnimationFrame(l)})();""")

# ---------------------------------------------------------------- 26
page("026-wedding.html","Amara & Theo — Save the Date","Great Vibes",
"""body{font-family:'Cormorant Garamond',serif;background:#fdf8f2;color:#4a3f35;text-align:center}
.wrap{max-width:640px;margin:auto;padding:12vh 24px}
.script{font-family:'Great Vibes';font-size:clamp(3.5rem,12vw,7rem);color:#a6414b;line-height:1.1}
.amp{font-family:'Great Vibes';font-size:3rem;color:#8a9a5b}
.flourish{color:#8a9a5b;font-size:1.6rem;margin:26px 0}
.card{border:1px solid #d9c7a7;padding:40px;margin:40px 0;background:#fffdf8;box-shadow:0 12px 40px #00000008}
.detail{display:flex;justify-content:center;gap:40px;flex-wrap:wrap;margin-top:16px;font-size:1.05rem}
.count{font-size:2.2rem;color:#a6414b;font-variant-numeric:tabular-nums}
.rsvp button{background:#a6414b;color:#fff;border:0;padding:14px 40px;font-family:inherit;font-size:1.1rem;cursor:pointer;letter-spacing:.1em;border-radius:2px}
.rsvp button:hover{background:#8a333c}""",
"""<div class="wrap"><div class="flourish">❦</div>
<div class="script">Amara</div><div class="amp">&</div><div class="script">Theo</div>
<div class="flourish">✦ ✦ ✦</div>
<p style="letter-spacing:.3em;font-size:.85rem;text-transform:uppercase">Together with their families</p>
<div class="card"><h2 style="font-size:1.6rem;letter-spacing:.2em">SATURDAY · THE 13TH OF JUNE · 2027</h2>
<p style="margin-top:10px;font-style:italic">at half past four in the afternoon</p>
<div class="detail"><span>🌿 Olive Grove Villa<br><small>Tivoli, Italy</small></span><span>🥂 Dinner beneath the pergola<br><small>Dancing until unreasonable</small></span></div></div>
<div class="card"><p>Counting down for us:</p><div class="count" id="cd"></div></div>
<div class="rsvp card"><p style="margin-bottom:16px">Kind reply requested by April 30th</p><button onclick="this.textContent='💌 Received with joy!'">RSVP — We'll be there</button></div>
<p style="opacity:.6;font-style:italic">No gifts but time; wear shoes you can lose in grass.</p></div>""",
"""const t=new Date('2027-06-13T16:30:00');setInterval(()=>{const d=t-new Date(),day=d/864e5|0,hr=d/36e5%24|0,mi=d/6e4%60|0;
document.getElementById('cd').textContent=`${day} days · ${hr} hrs · ${mi} min`},1000);""")

# ---------------------------------------------------------------- 27
page("027-cyberpunk.html","NIGHT CITY DIRECTORY 2077","Rajdhani",
"""body{font-family:'Rajdhani';background:#04060a;color:#c7f5ff;letter-spacing:.04em}
.neon{color:#f0d5ff;text-shadow:0 0 6px #b026ff,0 0 24px #b026ff88}
.cy{color:#0ff;text-shadow:0 0 6px #0ff,0 0 20px #0ff7}
header{padding:14vh 7vw 6vh}
h1{font-size:clamp(2.4rem,8vw,5rem);text-transform:uppercase}
.listing{margin:0 7vw 22vh 0;border:1px solid #b026ff44;padding:26px;position:relative;background:linear-gradient(#0a0d16,#06080e);clip-path:polygon(0 0,100% 0,100% calc(100% - 26px),calc(100% - 26px) 100%,0 100%)}
.listing::after{content:'';position:absolute;top:0;left:0;width:100%;height:2px;background:linear-gradient(90deg,#b026ff,transparent 60%)}
.row{display:flex;gap:30px;flex-wrap:wrap;margin-top:14px;font-size:.9rem;opacity:.8}
.chip{border:1px solid #0ff6;padding:2px 12px;color:#0ff;font-size:.75rem;text-transform:uppercase}
.warn{color:#ff5c5c;border:1px dashed #ff5c5c;display:inline-block;padding:2px 10px;font-size:.8rem}""",
"""<header><div class="cy">// MEGABLOCK NETWORK PRESENTS</div><h1 class="neon">Night City Directory</h1>
<div class="row"><span class="chip">netwatch verified</span><span class="chip">braindance rated</span><span class="warn">choom caution advised</span></div></header>
<div class="listing"><h2 class="cy">RIPPERDOC — “Chrome Lotus” Clinic</h2><p>Sandton Road sublevel 3. Militech-grade optics, discount because the sign's broken. Ask for Vi; she remembers your grandpa.</p><div class="row"><span>OPEN 24H</span><span>EURO | CASH | BOUNTY</span><span>★ 4.6 / 5 (glitch reviews)</span></div></div>
<div class="listing"><h2 class="cy">NOODLE BAR “MAMA SIMON”</h2><p>Best synthetic pork in Watson. The ramen broth is 40% rainwater, 100% love. Netrunners get free egg if you look tired enough.</p><div class="row"><span>18:00–04:00</span><span>NO CORPS AFTER MIDNIGHT</span><span>★ 4.9</span></div></div>
<div class="listing"><h2 class="cy">FIXER BOARD — “Whisper” Kato</h2><p>Gigs posted on the payphone at Jig-Jig Street. Ring twice, hang up, wait for the third ring. Payment in eddie, cred, or favours (favours compound).</p><div class="row"><span>REPUTATION: STREET CLEAN</span><span>DO NOT ASK ABOUT 2074</span></div></div>""")

# ---------------------------------------------------------------- 28
page("028-cheese.html","The Cheesemonger's Almanac","Fraunces",
"""body{font-family:'Fraunces',serif;background:#f8f1e2;color:#3d2c1e}
.shelf{max-width:900px;margin:auto;padding:10vh 24px}
h1{font-size:clamp(2.6rem,8vw,4.4rem);color:#7a4e28}
.wheel{display:flex;align-items:center;gap:30px;border-bottom:2px dotted #7a4e2844;padding:34px 0;flex-wrap:wrap;transition:.3s}
.wheel:hover{background:#fffdf6;transform:translateX(8px)}
.round{width:110px;height:110px;border-radius:50%;background:radial-gradient(circle at 32% 30%,#ffe9a8,#e8b64c 60%,#a06b1f);position:relative;box-shadow:0 10px 24px #0002;flex-shrink:0}
.round::after{content:attr(data-age);position:absolute;inset:0;display:grid;place-items:center;font-size:.75rem;letter-spacing:.15em;color:#3d2c1e;font-weight:700}
.wheel h2{font-size:1.7rem}.notes{opacity:.75;max-width:520px;line-height:1.7}
.pair{font-size:.85rem;color:#7a4e28;letter-spacing:.15em;text-transform:uppercase}""",
"""<div class="shelf"><h1>The Cheesemonger's Almanac</h1><p style="font-style:italic;opacity:.7;margin:10px 0 40px">Aged words for aged curds · Vol. XII</p>
<div class="wheel"><div class="round" data-age="36 MO"></div><div><h2>Comté, High Jura</h2><p class="notes">Crystalline bite, toasted hazelnut, a long savoury finish that lingers like good advice.</p><p class="pair">Pair: vin jaune · walnut bread</p></div></div>
<div class="wheel"><div class="round" data-age="60 D" style="background:radial-gradient(circle at 32% 30%,#fffdf0,#eee6cf 60%,#c9bd93)"></div><div><h2>Valençay, Ash-Rind</h2><p class="notes">Geometric as a chapel steeple. Citrus under geotrichum, chalk melting to cream.</p><p class="pair">Pair: sauvignon · strawberries</p></div></div>
<div class="wheel"><div class="round" data-age="14 D" style="background:radial-gradient(circle at 32% 30%,#fff4e3,#ffd9a0 60%,#e8a13c)"></div><div><h2>Epoisses de Bourgogne</h2><p class="notes">Brined with marc, spoonable, gloriously unruly. Banned from public transit for reasons.</p><p class="pair">Pair: pinot noir · a strong stomach</p></div></div></div>""")

# ---------------------------------------------------------------- 29
page("029-neon-typography.html","Type Is Loud — A Kinetic Type Study","Anton",
"""body{background:#0c0c0c;min-height:100vh;display:grid;place-items:center;font-family:'Anton';overflow:hidden}
.stack{text-align:center;user-select:none}
.line{font-size:clamp(3rem,13vw,10rem);line-height:.95;text-transform:uppercase;color:transparent;-webkit-text-stroke:2px #fff;transition:.4s;cursor:pointer}
.line:hover{color:#ff3d6e;-webkit-text-stroke-color:#ff3d6e;transform:skewX(-8deg) scale(1.04);text-shadow:0 0 60px #ff3d6e}
.l2{transition-delay:.05s}.l3{transition-delay:.1s}
.small{font-family:monospace;color:#777;margin-top:30px;font-size:.8rem;letter-spacing:.3em}""",
"""<div class="stack"><div class="line">TYPE</div><div class="line l2">IS</div><div class="line l3">LOUD</div>
<div class="small">▸ HOVER TO RAISE THE VOLUME ◂</div></div>""")

# ---------------------------------------------------------------- 30
page("030-tea.html","茶 — The Way of Tea","Zen Maru Gothic",
"""body{font-family:'Zen Maru Gothic',sans-serif;background:#171512;color:#e6ddcc;text-align:center}
.steam{font-size:5rem;position:relative;display:inline-block;margin-top:14vh}
.s{position:absolute;left:50%;color:#e6ddcc66;animation:st 3.4s ease-in infinite;font-size:1.6rem}
@keyframes st{from{transform:translate(-50%,0);opacity:.9}to{transform:translate(calc(-50% + var(--dx)),-90px);opacity:0}}
h1{font-size:2.4rem;letter-spacing:.6em;font-weight:300;margin:20px}
.steps{max-width:560px;margin:8vh auto;text-align:left;padding:0 24px}
.step{display:flex;gap:22px;margin:34px 0;align-items:baseline}
.n{color:#b3814f;font-size:1.6rem;font-family:serif;flex-shrink:0;width:40px}
.t{text-align:left;line-height:1.8}.t b{color:#b3814f}
footer{padding:8vh;font-style:italic;opacity:.55}""",
"""<div class="steam">🍵<span class="s" style="--dx:-14px;animation-delay:0s">〰</span><span class="s" style="--dx:10px;animation-delay:1.1s">〜</span><span class="s" style="--dx:-4px;animation-delay:2.2s">~</span></div>
<h1>THE WAY OF TEA</h1>
<div class="steps">
<div class="step"><div class="n">一</div><div class="t"><b>Warm the room, not just the cup.</b> Host and guest agree, without saying, to slow down together.</div></div>
<div class="step"><div class="n">二</div><div class="t"><b>Water at 80°, never boiling.</b> Green leaves are shy; scalding them makes them bitter about it.</div></div>
<div class="step"><div class="n">三</div><div class="t"><b>Pour in circles.</b> A steady ring, like stone skipping on water, blends each infusion evenly.</div></div>
<div class="step"><div class="n">四</div><div class="t"><b>Drink in three sips.</b> First for heat, second for taste, third for whatever the taste was trying to say.</div></div></div>
<footer>ichi-go ich-e — one time, one meeting. This cup will never be this cup again.</footer>""")

# ---------------------------------------------------------------- 31
page("031-startup.html","Fernmark — Analytics That Behave","Manrope",
"""body{font-family:'Manrope';background:#fff;color:#101322}
nav{display:flex;justify-content:space-between;align-items:center;padding:22px 7vw}
.logo{font-weight:800;font-size:1.3rem}.logo i{color:#12b76a;font-style:normal}
.hero{text-align:center;padding:12vh 7vw 8vh}
h1{font-size:clamp(2.4rem,7vw,4.6rem);font-weight:800;letter-spacing:-.03em;line-height:1.05}
h1 em{color:#12b76a;font-style:normal}
.lead{max-width:560px;margin:24px auto 0;font-size:1.2rem;color:#5b6072}
.cta{margin-top:36px;display:inline-flex;gap:14px;flex-wrap:wrap;justify-content:center}
.btn{padding:16px 32px;border-radius:12px;font-weight:700;text-decoration:none;font-size:1rem}
.b1{background:#101322;color:#fff}.b2{border:2px solid #101322;color:#101322}
.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:24px;padding:8vh 7vw;text-align:center}
.stat{padding:30px;border-radius:16px;background:#f6f8fa}
.num{font-size:2.6rem;font-weight:800;color:#12b76a}
.quote{max-width:680px;margin:auto;padding:6vh 24px;text-align:center;font-size:1.4rem;line-height:1.7;color:#3a3f52}
.quote small{display:block;margin-top:16px;color:#8a8fa3;font-size:.9rem}""",
"""<nav><div class="logo">fern<i>mark</i></div><a class="btn b2" style="padding:10px 22px;font-size:.9rem" href="#">Sign in</a></nav>
<div class="hero"><h1>Analytics that tell you<br><em>what actually happened.</em></h1>
<p class="lead">No vanity dashboards. No 400-chart graveyards. Fernmark answers three questions: who came, what they did, why they left.</p>
<div class="cta"><a class="btn b1" href="#">Start free trial</a><a class="btn b2" href="#">See a real dashboard →</a></div></div>
<div class="stats"><div class="stat"><div class="num" data-v="98">0</div><div>% signal accuracy</div></div>
<div class="stat"><div class="num" data-v="12">0</div><div>sec to first insight</div></div>
<div class="stat"><div class="num" data-v="4200">0</div><div>teams onboard</div></div></div>
<div class="quote">“We deleted three analytics tools the week we installed Fernmark. My boss thought I was joking.”<small>— Priya N., Head of Growth, Latchkey</small></div>""",
"""document.querySelectorAll('.num').forEach(el=>{const v=+el.dataset.v;let n=0;const iv=setInterval(()=>{n+=v/40;if(n>=v){n=v;clearInterval(iv)}el.textContent=Math.round(n)},24)})""")

# ---------------------------------------------------------------- 32
page("032-museum.html","Gallery of Invisible Art","Rozha One",
"""body{font-family:'Rozha One',serif;background:#111;color:#eee}
.marble{padding:14vh 8vw;text-align:center;background:radial-gradient(#1c1c1c,#111)}
h1{font-size:clamp(2.5rem,8vw,5rem);font-weight:400;letter-spacing:.05em}
.room{display:grid;place-items:center;min-height:92vh;padding:4vh 8vw;border-top:1px solid #333}
.frame{border:14px solid #caa66a;border-image:linear-gradient(#e8cf93,#8a6a2f) 1;padding:14px;background:#0b0b0b}
.canvasart{width:min(60vw,380px);height:min(40vh,320px);background:#111;display:grid;place-items:center;color:#333;font-size:.8rem;letter-spacing:.3em;cursor:pointer;transition:.6s}
.canvasart:hover{background:#151515;color:#555}
.plaque{margin-top:26px;text-align:center;font-family:Georgia;font-style:italic;color:#999}
.plaque b{color:#caa66a;font-style:normal;display:block;font-family:'Rozha One';font-size:1.3rem}""",
"""<div class="marble"><h1>Gallery of Invisible Art</h1><p style="color:#777">Esthetic restraint · East Wing · Free entry, higher exit</p></div>
<div class="room"><div class="frame"><div class="canvasart" title="squint">NOTHING №1</div></div>
<div class="plaque"><b>Untitled Void, 1962</b>Acrylic on imagination, 90×70cm. “The viewer completes what the artist refused.”</div></div>
<div class="room"><div class="frame"><div class="canvasart">COMPOSITION IN ABSENCE</div></div>
<div class="plaque"><b>Second Absence</b>Oil of nothingness on linen. Sold at auction for €4.1M; buyer returned it, saying it felt empty.</div></div>
<div class="room"><div class="frame"><div class="canvasart">SHHH</div></div>
<div class="plaque"><b>Silent Frame</b>Conceptual bronze, cast from sound. Weight: 0kg. Security guard assigned: 1.</div></div>""")

# ---------------------------------------------------------------- 33
page("033-weather-poster.html","Today's Sky — A Weather Poster","Unbounded",
"""body{font-family:'Unbounded';background:#12253d;color:#fff;display:grid;place-items:center;min-height:100vh;padding:30px}
.poster{width:min(92vw,520px);aspect-ratio:3/4;background:linear-gradient(#f7b733,#fc4a1a 32%,#2b5876 78%,#082032);border-radius:18px;padding:36px;display:flex;flex-direction:column;justify-content:space-between;box-shadow:0 40px 100px #000a;position:relative;overflow:hidden}
.sun{position:absolute;width:150px;height:150px;border-radius:50%;background:#ffe9a8;top:60px;right:-30px;box-shadow:0 0 90px #ffecb3;animation:bob 6s ease-in-out infinite}
@keyframes bob{50%{transform:translateY(14px)}}
.cloud{position:absolute;font-size:4rem;filter:drop-shadow(0 8px 20px #0004);animation:drift 14s linear infinite}
@keyframes drift{from{transform:translateX(-140px)}to{transform:translateX(560px)}}
.temp{font-size:clamp(4rem,16vw,7rem);line-height:1;font-weight:800;text-shadow:0 4px 30px #0006}
.meta{display:flex;justify-content:space-between;font-size:.8rem;letter-spacing:.15em;text-transform:uppercase}""",
"""<div class="poster"><div class="sun"></div><div class="cloud" style="top:44%">☁️</div><div class="cloud" style="top:58%;animation-delay:-7s;font-size:3rem">☁️</div>
<div><div class="meta"><span>Reykjavík</span><span>Wed · 06:41</span></div><div style="font-size:1.2rem;margin-top:8px">Sunrise in 2h 14m</div></div>
<div class="temp">-2°</div>
<div><div style="font-size:1.3rem;margin-bottom:14px">Bright cold. Wind telling stories.</div>
<div class="meta"><span>↯ UV 1</span><span>💨 24 km/h</span><span>💧 61%</span><span>🌡 feels -8°</span></div></div></div>""")

# ---------------------------------------------------------------- 34
page("034-quote-machine.html","The Quote Machine — Wisdom On Demand","Bitter",
"""body{font-family:'Bitter',serif;display:grid;place-items:center;min-height:100vh;background:#0f0f13}
.qcard{width:min(92vw,640px);padding:60px 54px;border-radius:4px;position:relative;transition:background 1s;box-shadow:0 30px 80px #0008}
.mark{font-size:5rem;line-height:0;position:relative;top:34px;opacity:.4}
blockquote{font-size:clamp(1.3rem,3.5vw,1.9rem);line-height:1.6;margin:26px 0}
cite{font-size:1rem;opacity:.75;font-style:normal;letter-spacing:.1em}
button{margin-top:34px;background:transparent;border:2px solid currentColor;color:inherit;font-family:inherit;padding:12px 28px;font-size:.9rem;cursor:pointer;letter-spacing:.2em;text-transform:uppercase;transition:.3s}
button:hover{transform:translateY(-3px)}""",
"""<div class="qcard" id="card"><div class="mark">“</div><blockquote id="q"></blockquote><cite id="a"></cite><br><button id="b">New wisdom</button></div>""",
"""const Q=[['The best way out is always through.','Robert Frost','#e74c3c'],['Simplicity is the ultimate sophistication.','Leonardo da Vinci','#16a085'],['We suffer more in imagination than in reality.','Seneca','#f39c12'],['Not all those who wander are lost.','J.R.R. Tolkien','#8e44ad'],['It is not the mountain we conquer, but ourselves.','Edmund Hillary','#2980b9'],['Talk is cheap. Show me the code.','Linus Torvalds','#27ae60'],['A ship in harbor is safe, but that is not what ships are built for.','John A. Shedd','#c0392b']];
const card=document.getElementById('card'),q=document.getElementById('q'),a=document.getElementById('a');
function nxt(){const [t,bg]=Q[Math.random()*Q.length|0];const c=bg||'#e74c3c';card.style.background=c;card.style.color=luma(c)>.5?'#111':'#fff';q.textContent='“'+pick()[0]+'”';a.textContent='— '+pick()[1]}
function pick(){return Q[Math.random()*Q.length]}
function luma(h){const n=parseInt(h.slice(1),16);return(((n>>16&255)*.299+(n>>8&255)*.587+(n&255)*.114)/255)}
document.getElementById('b').onclick=()=>{const[t,w]=pick();q.textContent='“'+t+'”';a.textContent='— '+w;const c=pick()[2];card.style.background=c;card.style.color=luma(c)>.55?'#141414':'#fff'};
q.textContent='“'+Q[0][0]+'”';a.textContent='— '+Q[0][1];card.style.background=Q[0][2];card.style.color='#fff';""")

# ---------------------------------------------------------------- 35
page("035-skincare.html","Lumen Botanica — Skincare With Sources","Josefin Sans",
"""body{font-family:'Josefin Sans';background:#fbeff2;color:#5c3a44}
.top{padding:12vh 8vw;text-align:center}
h1{font-size:clamp(2.4rem,8vw,4.2rem);letter-spacing:.12em}
.pill{display:inline-block;border:1px solid #d48a9c;border-radius:99px;padding:6px 18px;font-size:.75rem;letter-spacing:.2em;margin:6px}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:28px;padding:4vh 8vw 12vh}
.prod{background:#fff;border-radius:20px;padding:30px;box-shadow:0 18px 44px #d48a9c22;transition:.35s}
.prod:hover{transform:translateY(-10px) rotate(-1deg);box-shadow:0 30px 60px #d48a9c44}
.dropper{font-size:2.6rem}.prod h3{margin:14px 0 6px;font-size:1.3rem}
.ing{font-size:.85rem;opacity:.75;line-height:1.7}
.price{margin-top:16px;font-weight:700;color:#b0506b}""",
"""<div class="top"><h1>LUMEN BOTANICA</h1><p style="margin-top:14px">Small-batch serums. Full ingredient lists. Zero mystique.</p>
<div style="margin-top:20px"><span class="pill">VEGAN</span><span class="pill">10% NIACINAMIDE</span><span class="pill">REFILLABLE</span></div></div>
<div class="grid">
<div class="prod"><div class="dropper">🧪</div><h3>Clarity Serum 01</h3><p class="ing">Niacinamide 10% · zinc 1% · water, honestly just two things</p><p class="price">$28 · 30ml</p></div>
<div class="prod"><div class="dropper">🌹</div><h3>Rosehip Night Oil</h3><p class="ing">Cold-pressed rosehip · squalane · vitamin E · dreams optional</p><p class="price">$34 · 20ml</p></div>
<div class="prod"><div class="dropper">🫧</div><h3>Cloud Cleanser</h3><p class="ing">Coconut-derived surfactants · pH 5.5 · tightness not included</p><p class="price">$18 · 150ml</p></div></div>""")

# ---------------------------------------------------------------- 36
page("036-geocities.html","Welcome to my HOMEPAGE!!!","Comic Sans MS",
"""body{font-family:'Comic Sans MS',cursive;background:#003366;color:#ffff00;text-align:center}
.hit{background:#000;color:#0f0;font-family:monospace;display:inline-block;padding:4px 10px;border:2px ridge #888}
hr{border-color:#ff00ff}
a{color:#00ffff}
.blink{animation:bl 1s steps(2) infinite}@keyframes bl{50%{visibility:hidden}}
table{margin:20px auto;border-collapse:collapse}td{border:2px outset #c0c0c0;padding:14px;background:#000080}
.badge{display:inline-block;background:linear-gradient(#ff0,#f0f);padding:6px 12px;border:3px double #fff;font-weight:700;margin:8px}
.webring{margin:30px;font-size:.9rem;color:#fff}
h1{font-size:2.4rem;text-shadow:3px 3px #ff0000}
.stars-bg{background-image:radial-gradient(#fff 1px,transparent 1px);background-size:34px 34px}""",
"""<div class="stars-bg" style="padding:30px">
<h1>✨ Kimmy's KOOL KORNER ✨</h1>
<div class="blink" style="color:#ff9900;font-size:1.4rem">*** UNDER CONSTRUCTION FOREVER ***</div>
<div class="hit">You are visitor #000137!</div>
<hr><marquee behavior="alternate" style="color:#0f0;font-size:1.2rem">★ welcome to my homepage ★ sign my guestbook ★ tell ur friends ★</marquee><hr>
<table><tr><td><a href="#">🚀 MY HOBBIES</a></td><td><a href="#">🐹 HAMSTER PICS</a></td><td><a href="#">🎵 MIDI JUKEBOX</a></td></tr>
<tr><td><a href="#">💾 FREE WALLPAPERS</a></td><td><a href="#">📖 GUESTBOOK</a></td><td><a href="#">🔮 MY HOROSCOPE</a></td></tr></table>
<div class="badge">BEST VIEWED IN NETSCAPE 4</div><div class="badge">MADE WITH NOTEPAD™</div>
<div class="webring">[ &lt;&lt; prev | <a href="#">The Awesome Hamster WebRing</a> | next &gt;&gt; ]</div>
<p style="color:#ccc;font-size:.8rem">©1999 Kimmy · webmaster: kimmy@hotmail.com · no frames plz</p></div>""")

# ---------------------------------------------------------------- 37
page("037-coffee.html","Third Wave Theory — Coffee Notes","Cabin",
"""body{font-family:'Cabin';background:#191512;color:#efe7da}
.roast{max-width:760px;margin:auto;padding:10vh 24px}
h1{font-size:clamp(2.2rem,7vw,3.8rem);color:#d9a05b;letter-spacing:.05em}
.bean{margin:44px 0;padding:26px 30px;background:#221c17;border-left:4px solid #d9a05b;border-radius:0 12px 12px 0;transition:.3s}
.bean:hover{background:#2a221b;transform:translateX(6px)}
.origin{display:flex;justify-content:space-between;flex-wrap:wrap;gap:10px;align-items:baseline}
.origin h2{font-size:1.5rem}.price{color:#d9a05b;font-weight:700}
.notes{margin-top:10px;font-size:.95rem;opacity:.85}
.bar{height:8px;background:#3a2f26;border-radius:4px;margin-top:14px;overflow:hidden}
.fill{height:100%;background:linear-gradient(90deg,#e8c07d,#8a5a2b);width:0;transition:width 1.2s ease;border-radius:4px}
.lbl{font-size:.75rem;opacity:.6;margin-top:6px;letter-spacing:.15em;text-transform:uppercase}""",
"""<div class="roast"><h1>Third Wave Theory</h1><p style="opacity:.7;font-style:italic">Roasted Tuesday. Argued about daily.</p>
<div class="bean"><div class="origin"><h2>Yirgacheffe · Ethiopia</h2><span class="price">$22 / 250g</span></div>
<p class="notes">Jasmine, bergamot, stone fruit jam. Washed, light roast, tastes like a florist fell into a tea shop.</p>
<div class="lbl">roast level</div><div class="bar"><div class="fill" data-w="22%"></div></div></div>
<div class="bean"><div class="origin"><h2>Huéhuetenango · Guatemala</h2><span class="price">$19 / 250g</span></div>
<p class="notes">Red apple, panela, cocoa nib. The cup that convinced a latte drinker to switch sides.</p>
<div class="lbl">roast level</div><div class="bar"><div class="fill" data-w="55%"></div></div></div>
<div class="bean"><div class="origin"><h2>Mandheling · Sumatra</h2><span class="price">$21 / 250g</span></div>
<p class="notes">Cedar, dark chocolate, wet forest floor. For people whose mornings require negotiation.</p>
<div class="lbl">roast level</div><div class="bar"><div class="fill" data-w="85%"></div></div></div></div>""",
"""setTimeout(()=>document.querySelectorAll('.fill').forEach(f=>f.style.width=f.dataset.w),400);""")

# ---------------------------------------------------------------- 38
page("038-audio-wave.html","Sound Shape — Draw Your Voice","Comfortaa",
"""body{font-family:'Comfortaa';background:#0d1117;color:#e2eaf5;display:grid;place-items:center;min-height:100vh;text-align:center}
h1{font-size:1.6rem;letter-spacing:.2em;margin-bottom:6px}
p{opacity:.6;font-size:.85rem;margin-bottom:20px}
canvas{border:1px solid #2b3648;border-radius:14px;background:#090c12;cursor:crosshair;touch-action:none}
.row{display:flex;gap:14px;margin-top:18px;justify-content:center}
button{background:#1f6feb;color:#fff;border:0;padding:10px 22px;border-radius:99px;font-family:inherit;cursor:pointer}
button.alt{background:#21262d;border:1px solid #30363d}""",
"""<div><h1>SOUND SHAPE</h1><p>draw a waveform · press play · your scribble becomes sound</p>
<canvas id="c" width="760" height="260"></canvas>
<div class="row"><button id="play">▶ play</button><button class="alt" id="clr">clear</button></div></div>""",
"""const c=document.getElementById('c'),x=c.getContext('2d');let pts=new Array(190).fill(130),drawing=false;
function grid(){x.fillStyle='#090c12';x.fillRect(0,0,760,260);x.strokeStyle='#1c2532';x.beginPath();x.moveTo(0,130);x.lineTo(760,130);x.stroke()}
function render(){grid();x.strokeStyle='#58a6ff';x.lineWidth=2;x.beginPath();pts.forEach((v,i)=>{i?x.lineTo(i*4,v):x.moveTo(0,v)});x.stroke()}
function pos(e){const r=c.getBoundingClientRect();const t=e.touches?e.touches[0]:e;return[(t.clientX-r.left)/4,(t.clientY-r.top)]}
c.addEventListener('pointerdown',e=>{drawing=true;move(e)});addEventListener('pointerup',()=>drawing=false);
c.addEventListener('pointermove',move);
function move(e){if(!drawing)return;const[i,y]=pos(e);if(i>=0&&i<190)pts[i|0]=Math.max(10,Math.min(250,y))}
document.getElementById('clr').onclick=()=>{pts=new Array(190).fill(130);render()};
document.getElementById('play').onclick=async()=>{const ac=new(window.AudioContext||window.webkitAudioContext)();
const sr=ac.sampleRate,len=190*120,buf=ac.createBuffer(1,len,sr),d=buf.getChannelData(0);
for(let i=0;i<len;i++){const p=pts[(i/120)|0]/130-1;d[i]=p*Math.sin(2*Math.PI*220*i/sr)*.6}
const src=ac.createBufferSource();src.buffer=buf;src.connect(ac.destination);src.start()};
render();""")

# ---------------------------------------------------------------- 39
page("039-film-poster.html","THE LAST SIGNAL — A Film","Bebas Neue",
"""body{font-family:'Bebas Neue';background:#050505;color:#fff;display:grid;place-items:center;min-height:100vh;padding:24px}
.poster{width:min(92vw,540px);aspect-ratio:2/3;position:relative;background:linear-gradient(#0b1d33,#05070c 70%),url('');overflow:hidden;display:flex;flex-direction:column;justify-content:flex-end;padding:34px;box-shadow:0 50px 120px #000c}
.moon{position:absolute;top:10%;right:12%;width:110px;height:110px;border-radius:50%;background:radial-gradient(circle at 35% 35%,#fff,#cfd8e8);box-shadow:0 0 80px #9db8ff88}
.figure{position:absolute;bottom:31%;left:50%;transform:translateX(-50%);font-size:4.4rem;filter:brightness(.15)}
.fog{position:absolute;inset:0;background:repeating-linear-gradient(transparent 0 46px,#ffffff08 46px 48px)}
.title{font-size:clamp(3rem,12vw,5.2rem);line-height:.9;letter-spacing:.02em}
.kicker{color:#ffb627;letter-spacing:.4em;font-size:1rem}
.credits{font-family:Arial;font-size:.6rem;letter-spacing:.12em;opacity:.6;margin-top:14px;line-height:1.7}
.star{position:absolute;width:2px;height:2px;background:#fff;border-radius:50%;animation:tw 3s infinite}
@keyframes tw{50%{opacity:.2}}""",
"""<div class="poster"><div class="moon"></div><div class="fog"></div><div class="figure">📡</div>
<div class="kicker">SHE LISTENED TO THE SKY. THE SKY ANSWERED.</div>
<div class="title">THE LAST<br>SIGNAL</div>
<div class="credits">A HALCYON PICTURES FILM · “THE LAST SIGNAL” · MUSIC BY ANNA REEVES · DIRECTED BY M. OKONKWO<br>RATING PG-13 · IN THEATRES THIS NOVEMBER</div></div>""",
"""const p=document.querySelector('.poster');for(let i=0;i<50;i++){const s=document.createElement('div');s.className='star';s.style.cssText=`left:${Math.random()*100}%;top:${Math.random()*55}%;animation-delay:${Math.random()*3}s`;p.appendChild(s)}""")

# ---------------------------------------------------------------- 40
page("040-boardgame.html","Hexhome — The Board Game Cafe","Fredoka",
"""body{font-family:'Fredoka';background:#2e1e14;color:#f6ead2}
.parquet{background:repeating-conic-gradient(#3b2718 0 25%,#33220f 0 50%) 0 0/60px 60px;min-height:100vh;padding:8vh 6vw}
h1{font-size:clamp(2.4rem,8vw,4.4rem);color:#f2b134;text-shadow:0 4px 0 #7a4a12}
.meeple{font-size:3rem;display:inline-block;animation:hop 1.4s infinite}
@keyframes hop{50%{transform:translateY(-14px) rotate(6deg)}}
.games{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:22px;margin-top:40px}
.gcard{background:#fff8ea;color:#3b2718;border-radius:14px;padding:22px;transform:rotate(var(--r,0));transition:.25s;cursor:pointer;box-shadow:0 12px 30px #0006}
.gcard:hover{transform:rotate(0) translateY(-8px) scale(1.03)}
.gcard h3{font-size:1.3rem}.plex{display:flex;gap:6px;margin:10px 0;font-size:1.2rem}
.diff{font-size:.8rem;background:#f2b134;border-radius:99px;padding:3px 12px;display:inline-block}""",
"""<div class="parquet"><span class="meeple">🧑‍🎨</span><h1>HEXHOME CAFÉ</h1>
<p style="font-size:1.2rem;max-width:560px">Board games, warm soup, and friendly rivalries. 400+ titles on the shelf, none of them Monopoly (house rules).</p>
<div class="games">
<div class="gcard" style="--r:-2deg"><h3>Catan</h3><div class="plex">👨‍👩‍👧‍👦 3–4</div><span class="diff">easy to teach</span><p>Trade sheep, betray friends, hug it out after.</p></div>
<div class="gcard" style="--r:1.5deg"><h3>Wingspan</h3><div class="plex">🐦 1–5</div><span class="diff">medium thinky</span><p>Beautiful birds doing bird economics. Shockingly tense.</p></div>
<div class="gcard" style="--r:-1deg"><h3>7 Wonders</h3><div class="plex">🏛 3–7</div><span class="diff">draft dynasty</span><p>Build civilisation in 30 minutes per age.</p></div>
<div class="gcard" style="--r:2deg"><h3>Terraforming Mars</h3><div class="plex">🪐 1–5</div><span class="diff">long haul</span><p>Make Mars habitable. Bring snacks and a weekend.</p></div></div></div>""")

# ---------------------------------------------------------------- 41
page("041-minimal-photography.html","Light Leaks — A Photo Essay","Cormorant",
"""body{font-family:'Cormorant',serif;background:#0c0c0c;color:#ddd}
.head{padding:20vh 8vw 10vh}h1{font-size:clamp(2.5rem,8vw,4.5rem);font-weight:300}
.strip{display:flex;gap:2px;overflow-x:auto;padding:2px 0}
.ph{flex:0 0 min(78vw,420px);aspect-ratio:4/5;position:relative;overflow:hidden}
.ph div{position:absolute;inset:0;transition:transform 1.2s cubic-bezier(.2,.8,.2,1)}
.ph:hover div{transform:scale(1.08)}
.cap{position:absolute;bottom:0;left:0;right:0;padding:18px;background:linear-gradient(transparent,#000c);font-style:italic;font-size:1.05rem}
.note{padding:10vh 8vw;max-width:640px;font-size:1.3rem;line-height:1.9;font-weight:300}""",
"""<div class="head"><h1>Light Leaks</h1><p style="opacity:.6">Twelve frames shot on expired film, one camera held badly.</p></div>
<div class="strip">
<div class="ph"><div style="background:linear-gradient(160deg,#f7d796,#f8876f 60%,#ba4b72)"></div><div class="cap">Lisbon, golden hour, metering wrong on purpose</div></div>
<div class="ph"><div style="background:linear-gradient(200deg,#93a8c4,#3e5c76 70%,#1b263b)"></div><div class="cap">Harbour fog. The ferry arrived late and beautiful.</div></div>
<div class="ph"><div style="background:linear-gradient(140deg,#e9f5db,#b7ecc8 40%,#52ab73)"></div><div class="cap">Forest path, ISO pushed, grain like pollen</div></div>
<div class="ph"><div style="background:linear-gradient(180deg,#cdb4db,#7b5aa3 60%,#2b1b43)"></div><div class="cap">Neon alley, lens flare bleeding through the shutter</div></div></div>
<p class="note">I keep the mistakes. Every leak is proof the camera was alive, that light found a way in where it wasn't invited. Ask me nicely and I'll sell you frame four — the one where everything is overexposed except the dog.</p>""")

# ---------------------------------------------------------------- 42
page("042-space-shop.html","Orbit Outfitters — Gear for Low Gravity","Chakra Petch",
"""body{font-family:'Chakra Petch';background:#060a14;color:#d7e4ff}
.shop{max-width:1000px;margin:auto;padding:8vh 24px}
h1{font-size:clamp(2.2rem,7vw,3.6rem);color:#7fdcff}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:26px;margin-top:44px}
.item{border:1px solid #22406a;background:linear-gradient(#0b1324,#0a0f1d);padding:26px;position:relative;transition:.3s;clip-path:polygon(0 0,100% 0,100% calc(100% - 18px),calc(100% - 18px) 100%,0 100%)}
.item:hover{border-color:#7fdcff;box-shadow:0 0 40px #7fdcff22;transform:translateY(-6px)}
.stock{position:absolute;top:14px;right:14px;font-size:.7rem;color:#1dd1a1}
.out{color:#ff6b6b}
.icon{font-size:2.4rem}h3{margin:12px 0 6px;font-size:1.2rem}
.spec{font-size:.85rem;opacity:.7;line-height:1.7}
.cr{color:#fbbf24;font-size:1.1rem;margin-top:12px}
.add{margin-top:14px;background:#7fdcff;color:#060a14;border:0;padding:8px 18px;font-family:inherit;cursor:pointer;font-weight:700}
.add:hover{background:#b8efff}""",
"""<div class="shop"><h1>ORBIT OUTFITTERS</h1><p style="opacity:.7">Everything between here and LEO. Returns accepted within 3 orbits.</p>
<div class="grid">
<div class="item"><span class="stock">◉ IN STOCK</span><div class="icon">🧤</div><h3>Grip Gloves MK-IV</h3><p class="spec">Touch-capable, micrometeorite shell, keeps hands honest during EVA.</p><div class="cr">₡ 240</div><button class="add">ADD TO POD</button></div>
<div class="item"><span class="stock">◉ 3 LEFT</span><div class="icon">☕</div><h3>Zero-G Espresso Sphere</h3><p class="spec">Sealed titanium bulb. Caffeine without catastrophic droplet events.</p><div class="cr">₡ 180</div><button class="add">ADD TO POD</button></div>
<div class="item"><span class="stock out">◌ OUT OF STOCK</span><div class="icon">🥾</div><h3>Magnetic Moon Boots</h3><p class="spec">Regolith-rated soles, heel-mounted flag dispenser (decorative).</p><div class="cr">₡ 510</div><button class="add" disabled>NOTIFY ME</button></div>
<div class="item"><span class="stock">◉ IN STOCK</span><div class="icon">📻</div><h3>Longwave Radio Kit</h3><p class="spec">Ham-band transceiver tuned for Earth talk. Delay: 2.6s of awkward pauses.</p><div class="cr">₡ 760</div><button class="add">ADD TO POD</button></div></div></div>""",
"""document.querySelectorAll('.add:not([disabled])').forEach(b=>b.onclick=()=>{b.textContent='✓ IN POD';b.style.background='#1dd1a1'})""")

# ---------------------------------------------------------------- 43
page("043-poetry.html","Letters to No One — Prose Poems","EB Garamond",
"""body{font-family:'EB Garamond',serif;background:#f6f2ea;color:#2b2b2b;line-height:2}
.sheet{max-width:620px;margin:auto;padding:14vh 26px}
h1{font-size:3rem;font-weight:500;margin-bottom:6px}
.byline{font-style:italic;opacity:.6;margin-bottom:60px}
.poem{margin-bottom:70px}
.poem h2{font-size:1.4rem;font-weight:600;color:#8a5a2b;margin-bottom:14px;letter-spacing:.05em}
.poem p{font-size:1.25rem}
.poem:hover p:first-of-type::first-letter{color:#c0392b}
.end{border-top:1px solid #0002;padding-top:30px;font-style:italic;opacity:.6;text-align:center}""",
"""<div class="sheet"><h1>Letters to No One</h1><div class="byline">prose poems by the night shift</div>
<div class="poem"><h2>I. Inventory</h2><p>I keep the sounds I can't return: a screen door confessing to summer, the bus sighing like it's seen everything. My pockets are a museum of almost-goodbyes.</p></div>
<div class="poem"><h2>II. Weather Report</h2><p>Low pressure moving through the kitchen. Chance of reheated coffee, certain of staring. Somewhere a kettle commits to its ambition.</p></div>
<div class="poem"><h2>III. Instruction Manual for a Chair</h2><p>Hold still while someone decides whether to sit. Be sturdy in the ways nobody thanks you for. When they leave, keep the warmth a little longer. That's the job.</p></div>
<div class="end">more letters, when the night shift allows —</div></div>""")

# ---------------------------------------------------------------- 44
page("044-arcade-stats.html","DATA ARCADE — Stats As a High Score","VT323",
"""body{font-family:'VT323',monospace;background:#02040a;color:#0f0;font-size:20px}
.crt{position:fixed;inset:0;pointer-events:none;background:radial-gradient(#0f000000,#00000000 60%,#000a),repeating-linear-gradient(transparent 0 2px,#0003 2px 4px);z-index:3}
.wrap{max-width:900px;margin:auto;padding:6vh 20px}
h1{font-size:3.4rem;color:#ff0;text-shadow:0 0 18px #ff08;letter-spacing:.1em}
.stat{display:grid;grid-template-columns:1fr auto;gap:10px;border-bottom:1px dashed #0f04;padding:16px 0;align-items:center}
.bar{height:16px;border:2px solid #0f0;position:relative;width:min(420px,60vw)}
.bar i{position:absolute;inset:0;background:#0f0;width:0;transition:width 1.6s steps(24);box-shadow:0 0 14px #0f0}
.val{color:#0ff;font-size:1.5rem}
.insert{animation:bl 1.1s steps(2) infinite;color:#f06;text-align:center;font-size:1.8rem;margin-top:40px}
@keyframes bl{50%{opacity:0}}""",
"""<div class="crt"></div><div class="wrap"><h1>PLAYER STATS</h1>
<div class="stat"><span>COFFEE CONSUMED / WEEK</span><div class="bar"><i data-w="88%"></i></div><span class="val">14 CUPS</span></div>
<div class="stat"><span>BUGS FIXED (ALLEGEDLY)</span><div class="bar"><i data-w="62%"></i></div><span class="val">1,240</span></div>
<div class="stat"><span>TABS OPEN RIGHT NOW</span><div class="bar"><i data-w="97%"></i></div><span class="val">47 ⚠</span></div>
<div class="stat"><span>DOCS READ BEFORE CODING</span><div class="bar"><i data-w="9%"></i></div><span class="val">…oops</span></div>
<div class="stat"><span>STACKOVERFLOW KARMA</span><div class="bar"><i data-w="74%"></i></div><span class="val">12.4K</span></div>
<div class="insert">▸ INSERT COIN TO CONTINUE ◂</div></div>""",
"""setTimeout(()=>document.querySelectorAll('.bar i').forEach(b=>b.style.width=b.dataset.w),300);""")

# ---------------------------------------------------------------- 45
page("045-floral-invite.html","Bloom & Bramble — Garden Party Invitation","Marck Script",
"""body{font-family:'Cormorant Garamond',serif;background:#f2ede2;color:#3f4a33;text-align:center}
.card{max-width:560px;margin:8vh auto;background:#fffdf5;padding:70px 40px;box-shadow:0 24px 60px #00000018;position:relative;border-radius:4px}
.vine{position:absolute;font-size:2rem;opacity:.8}
.v1{top:14px;left:18px;transform:rotate(-12deg)}.v2{top:14px;right:18px;transform:rotate(12deg) scaleX(-1)}
.v3{bottom:14px;left:18px;transform:rotate(12deg) scaleY(-1)}.v4{bottom:14px;right:18px;transform:rotate(-12deg) scaleX(-1) scaleY(-1)}
.names{font-family:'Marck Script';font-size:clamp(2.6rem,9vw,4rem);color:#6b7d52;line-height:1.2}
.when{letter-spacing:.3em;text-transform:uppercase;font-size:.85rem;margin:26px 0}
.rsvp{margin-top:30px;display:inline-block;border:1px solid #6b7d52;padding:12px 34px;color:#6b7d52;text-decoration:none;transition:.3s}
.rsvp:hover{background:#6b7d52;color:#fff}
.petal{position:fixed;font-size:1.4rem;animation:ft linear infinite;opacity:.5;z-index:-1}
@keyframes ft{from{transform:translateY(-5vh) rotate(0)}to{transform:translateY(105vh) rotate(320deg)}}""",
"""<div class="card"><span class="vine v1">🌿🌸</span><span class="vine v2">🌿🌸</span><span class="vine v3">🌿🌸</span><span class="vine v4">🌿🌸</span>
<p style="font-style:italic;opacity:.7">you are cordially summoned to</p><div class="names">Bloom & Bramble</div>
<div class="when">a garden party</div><p>Saturday, the twenty-second of May<br>from four until the fireflies</p>
<p style="margin-top:20px">14 Thimble Lane · cider, seeds & songs<br><small>bring a plant you're guilty about</small></p>
<a class="rsvp" href="#" onclick="this.textContent='✓ counted among the bees';return false">RSVP</a></div>""",
"""const emo=['🌸','🍃','🌼'];for(let i=0;i<14;i++){const p=document.createElement('div');p.className='petal';p.textContent=emo[i%3];p.style.left=Math.random()*100+'vw';p.style.animationDuration=(9+Math.random()*9)+'s';p.style.animationDelay=-Math.random()*15+'s';document.body.appendChild(p)}""")

# ---------------------------------------------------------------- 46
page("046-newsprint.html","THE DAILY GRIND — Broadsheet","Old Standard TT",
"""body{font-family:'Old Standard TT',serif;background:#f4f1e8;color:#111}
.paper{max-width:960px;margin:4vh auto;padding:0 24px}
.mast{text-align:center;border-bottom:4px double #111;padding:26px 0}
.mast h1{font-size:clamp(3rem,10vw,5.5rem);letter-spacing:.05em}
.strip{display:flex;justify-content:space-between;font-size:.8rem;padding:8px 0;border-bottom:1px solid #111;letter-spacing:.1em;text-transform:uppercase}
.cols{column-count:3;column-gap:36px;margin:30px 0;font-size:.98rem;line-height:1.75}
.cols h2{font-size:1.9rem;line-height:1.1;margin-bottom:12px;column-span:all}
.byline{font-variant:small-caps;color:#555}
.side{border-left:1px solid #999;padding-left:18px}
figure{border:1px solid #111;padding:10px;margin:16px 0;break-inside:avoid;background:#fff}
.fig-art{height:120px;background:repeating-linear-gradient(45deg,#111 0 2px,transparent 2px 8px)}
@media(max-width:760px){.cols{column-count:1}}""",
"""<div class="paper"><div class="mast"><h1>THE DAILY GRIND</h1><div style="font-style:italic">All the news that fits the mug</div></div>
<div class="strip"><span>VOL. XCII · NO. 317</span><span>WEATHER: PERPETUAL OVERCAST</span><span>PRICE: ONE THOUGHT</span></div>
<div class="cols"><h2>Locals Insist Morning Coffee Improves Mood; Study Conducted Only After Second Cup</h2>
<p class="byline">By A. Sipping, Correspondent</p>
<p>The municipal caffeine board reported today that 94% of respondents felt "significantly more vertical" after regular consumption of roasted bean water. Dissenting voices — three, all decaf drinkers — were politely asked to revisit their position.</p>
<figure><div class="fig-art"></div><figcaption style="font-size:.8rem">Fig. 1: Steam rising from a civic mug, undated.</figcaption></figure>
<p class="side">Side effects announced at the press conference included dreaming in brown and an unshakeable opinion about grinders.</p>
<p>Meanwhile, the city's oldest percolator, "Old Reliable," marked its 41st anniversary in continuous service. Officials presented it with a plaque; it responded by overflowing, which witnesses described as "classic."</p>
<p>Experts advise hydration between cups. Experts also advise most things between cups.</p></div></div>""")

# ---------------------------------------------------------------- 47
page("047-vaporwave.html","A E S T H E T I C S ::: mall soft","Varela Round",
"""body{font-family:'Varela Round';background:linear-gradient(#ff71ce,#b967ff 40%,#01cdfe);color:#fff;text-align:center;overflow-x:hidden}
.wrap{padding:12vh 6vw}
h1{font-size:clamp(2.4rem,9vw,5rem);letter-spacing:.4em;text-shadow:4px 4px #05ffa1aa}
.column{display:inline-block;vertical-align:top;margin:20px;width:220px;background:#ffffff22;backdrop-filter:blur(6px);padding:24px;border-radius:4px;transition:.4s}
.column:hover{transform:translateY(-10px) rotate(2deg);background:#ffffff33}
.palm{font-size:3rem}
.jp{font-size:1.1rem;letter-spacing:.3em;opacity:.9}
.floor{height:30vh;background:linear-gradient(#00000033,transparent),repeating-linear-gradient(90deg,#fff3 0 2px,transparent 2px 60px),repeating-linear-gradient(#fff3 0 2px,transparent 2px 40px);transform:perspective(500px) rotateX(55deg);margin-top:8vh}
.cat{font-size:5rem;display:inline-block;animation:nod 3s ease-in-out infinite}
@keyframes nod{50%{transform:rotate(6deg) translateY(-8px)}}""",
"""<div class="wrap"><h1>A E S T H E T I C S</h1><p class="jp">モール・ソフト・ドリームス</p><div class="cat">🐈</div>
<div><div class="column"><div class="palm">🌴</div><h3>MALL SOFT</h3><p class="jp">ショッピング</p><p>Elevators going nowhere, beautifully lit.</p></div>
<div class="column"><div class="palm">📼</div><h3>TAPE HISS</h3><p class="jp">音楽</p><p>Every song arrives slightly melted, somehow better.</p></div>
<div class="column"><div class="palm">🌊</div><h3>POOL ROOM</h3><p class="jp">水</p><p>Tile everywhere. Water optional. Echo mandatory.</p></div></div></div>
<div class="floor"></div>""")

# ---------------------------------------------------------------- 48
page("048-resume.html","Curriculum Vitae — Iris Kalderon","IBM Plex Serif",
"""body{font-family:'IBM Plex Serif',serif;background:#e9e5dc;color:#1d1d1b}
.doc{max-width:820px;margin:5vh auto;background:#fbfaf6;box-shadow:0 30px 80px #0003;display:grid;grid-template-columns:1fr 1.6fr}
.left{padding:44px;background:#1d1d1b;color:#f2efe6}
.left h1{font-size:1.9rem;line-height:1.2}
.role{color:#c8b273;letter-spacing:.25em;font-size:.75rem;text-transform:uppercase;margin:10px 0 30px}
.block h3{font-size:.8rem;letter-spacing:.25em;text-transform:uppercase;color:#c8b273;border-bottom:1px solid #3a3a37;padding-bottom:6px;margin:26px 0 12px}
.right{padding:44px}
.right h2{font-size:.85rem;letter-spacing:.25em;text-transform:uppercase;color:#7a6a3a;margin:28px 0 14px}
.job{margin-bottom:22px}.job b{font-size:1.05rem}.job .dates{float:right;font-size:.8rem;color:#888}
.skill{display:flex;align-items:center;gap:12px;margin:8px 0;font-size:.85rem}
.dots{flex:1;height:6px;background:#3a3a37;border-radius:3px;overflow:hidden}
.dots i{display:block;height:100%;background:#c8b273}
ul{padding-left:18px;line-height:1.7;font-size:.92rem}
@media(max-width:720px){.doc{grid-template-columns:1fr}}""",
"""<div class="doc"><div class="left"><h1>Iris Kalderon</h1><div class="role">Product Designer</div>
<div class="block"><h3>Contact</h3><p style="font-size:.85rem;line-height:1.9">iris@kalderon.design<br>+30 210 ••• ••••<br>Athens, Greece · GMT+3</p></div>
<div class="block"><h3>Skills</h3><div class="skill">Systems<small class="dots"><i style="width:92%"></i></small></div>
<div class="skill">Type<small class="dots"><i style="width:85%"></i></small></div>
<div class="skill">Motion<small class="dots"><i style="width:70%"></i></small></div>
<div class="skill">Spreadsheets<small class="dots"><i style="width:44%"></i></small></div></div>
<div class="block"><h3>Languages</h3><p style="font-size:.85rem">Greek · English · TypeScript (conversational)</p></div></div>
<div class="right"><h2>Experience</h2>
<div class="job"><span class="dates">2023—now</span><b>Lead Designer · Aster Health</b><ul><li>Redesigned intake flow; abandoned forms fell 38%.</li><li>Built a design system used by six product teams and one very proud intern.</li></ul></div>
<div class="job"><span class="dates">2020—23</span><b>Designer · Courier Studio</b><ul><li>Shipped editorial platforms for three national papers.</li><li>Won an award; donated it to the office plant.</li></ul></div>
<h2>Education</h2><div class="job"><span class="dates">2016—20</span><b>AES, Athens</b><ul><li>BFA Interaction Design. Thesis: calendars people don't dread.</li></ul></div></div></div>""")

# ---------------------------------------------------------------- 49
page("049-lanterns.html","Festival of Lanterns","Noto Serif SC",
"""body{font-family:'Noto Serif SC',serif;background:linear-gradient(#090212,#1a0a2e 60%,#2b0f3a);color:#ffe9c9;min-height:100vh;overflow-x:hidden}
.sky{position:relative;min-height:100vh}
.lantern{position:absolute;font-size:2.6rem;animation:rise linear infinite;filter:drop-shadow(0 0 22px #ffb347)}
@keyframes rise{from{transform:translateY(105vh) translateX(0) rotate(-4deg)}to{transform:translateY(-15vh) translateX(var(--sway)) rotate(4deg)}}
h1{text-align:center;font-size:clamp(2.4rem,8vw,4.6rem);padding-top:22vh;letter-spacing:.3em;text-shadow:0 0 40px #ff9e4f}
.sub{text-align:center;opacity:.75;letter-spacing:.5em;font-size:.85rem}
.poem{max-width:560px;margin:24vh auto;padding:0 24px;text-align:center;font-size:1.25rem;line-height:2.2;font-style:italic}""",
"""<div class="sky" id="s"><h1>灯 火 节</h1><div class="sub">FESTIVAL OF LANTERNS</div></div>
<div class="poem">Ten thousand paper suns<br>loosen from the riverbank —<br>the night keeps receipts.</div>""",
"""const s=document.getElementById('s');
for(let i=0;i<22;i++){const l=document.createElement('div');l.className='lantern';l.textContent=['🏮','🪔','🕯️'][i%3];
l.style.left=Math.random()*96+'vw';l.style.setProperty('--sway',(Math.random()*120-60)+'px');
l.style.animationDuration=(11+Math.random()*14)+'s';l.style.animationDelay=-Math.random()*20+'s';s.appendChild(l)}""")

# ---------------------------------------------------------------- 50
page("050-dashboard.html","Mission Control — Home Dashboard","Barlow",
"""body{font-family:'Barlow';background:#0d1117;color:#dbe4ee}
.dash{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:18px;padding:24px;max-width:1100px;margin:auto}
.tile{background:#161b22;border:1px solid #21262d;border-radius:14px;padding:22px;transition:.25s;cursor:pointer}
.tile:hover{border-color:#3fb950;transform:translateY(-4px)}
.tile h3{font-size:.75rem;letter-spacing:.2em;text-transform:uppercase;color:#8b949e;margin-bottom:12px}
.big{font-size:2.4rem;font-weight:700}
.g{color:#3fb950}.y{color:#d29922}.r{color:#f85149}.b{color:#58a6ff}
.ring{width:84px;height:84px;border-radius:50%;background:conic-gradient(#3fb950 var(--p),#21262d 0);display:grid;place-items:center;margin:8px auto}
.ring i{width:64px;height:64px;border-radius:50%;background:#161b22;display:grid;place-items:center;font-style:normal;font-weight:700}
.hd{padding:26px 24px 0;max-width:1100px;margin:auto;display:flex;justify-content:space-between;flex-wrap:wrap;gap:8px}
.clock{font-size:1.4rem;font-weight:700;color:#58a6ff;font-variant-numeric:tabular-nums}""",
"""<div class="hd"><div><h2 style="font-size:1.5rem">Good evening, commander</h2><small style="color:#8b949e">Wednesday, October 28 · systems nominal-ish</small></div><div class="clock" id="clk"></div></div>
<div class="dash">
<div class="tile"><h3>Energy</h3><div class="ring" style="--p:72%"><i class="g">72%</i></div><small class="g">▲ solar surplus 4.1 kWh</small></div>
<div class="tile"><h3>Greenhouse</h3><div class="big">21.5°</div><small>humidity 48% · tomatoes thriving, basil dramatic</small></div>
<div class="tile"><h3>Water Tank</h3><div class="big y">38%</div><small class="y">▼ refill before Sunday rain fails you</small></div>
<div class="tile"><h3>Network</h3><div class="big b">412<span style="font-size:1rem"> Mbps</span></div><small>14 devices · smart fridge browsing again</small></div>
<div class="tile"><h3>Focus Timer</h3><div class="big g">25:00</div><small>next break in — press tile to start</small></div>
<div class="tile"><h3>Mood Log</h3><div class="big">🙂→😄</div><small>trend improving since coffee</small></div></div>""",
"""function clk(){const d=new Date();document.getElementById('clk').textContent=d.toLocaleTimeString([],{hour:'2-digit',minute:'2-digit',second:'2-digit'})}setInterval(clk,1000);clk();
const t=document.querySelectorAll('.tile')[4],timer=t.querySelector('.big');let sec=25*60,on=false,iv;
t.onclick=()=>{if(on){clearInterval(iv);on=false;t.querySelector('small').textContent='paused, dramatically';return}on=true;
iv=setInterval(()=>{sec--;timer.textContent=`${String(sec/60|0).padStart(2,'0')}:${String(sec%60).padStart(2,'0')}`;
if(sec<=0){clearInterval(iv);timer.textContent='DONE';t.querySelector('small').textContent='take the break you earned';on=false}},1000)};""")

# ---------------------------------------------------------------- 51
page("051-cookie.html","One Small Cookie — A Confession","Nunito",
"""body{font-family:'Nunito';background:#fff8ee;color:#5b4636;display:grid;place-items:center;min-height:100vh;text-align:center;padding:24px}
.jar{font-size:7rem;cursor:pointer;transition:.2s;display:inline-block}
.jar:active{transform:scale(.9)}
.count{font-size:3rem;font-weight:800;color:#c07c30}
p{max-width:460px;line-height:1.8}
.crumb{position:fixed;font-size:1.4rem;pointer-events:none;animation:pop .9s forwards}
@keyframes pop{to{transform:translate(var(--dx),var(--dy)) rotate(var(--r));opacity:0}}
.shop{margin-top:18px;background:#c07c30;color:#fff;border:0;padding:12px 26px;border-radius:99px;font-family:inherit;font-size:1rem;cursor:pointer}""",
"""<div><div class="jar" id="j">🍪</div><h1>You clicked the cookie.</h1><p>That's fine. They're right there. In fact, take another. Nobody's counting except the algorithm below:</p>
<div class="count" id="n">0 cookies</div>
<button class="shop" id="s">Buy more cookies (€0.00)</button>
<p style="font-size:.8rem;opacity:.6;margin-top:16px">This page stores your crimes in localStorage. It always has. It always will.</p></div>""",
"""let n=+localStorage.getItem('cookies')||0;const el=document.getElementById('n'),j=document.getElementById('j');
function upd(){el.textContent=n+' cookie'+(n===1?'':'s');localStorage.setItem('cookies',n)}upd();
j.onclick=e=>{n++;upd();for(let i=0;i<4;i++){const c=document.createElement('div');c.className='crumb';c.textContent='🍪';
c.style.cssText=`left:${e.clientX}px;top:${e.clientY}px;--dx:${Math.random()*160-80}px;--dy:${Math.random()*-120-30}px;--r:${Math.random()*360}deg`;
document.body.appendChild(c);setTimeout(()=>c.remove(),900)}};
document.getElementById('s').onclick=()=>{n+=12;upd();alert('Your self-control has been restocked.')};""")

# ---------------------------------------------------------------- 52
page("052-mountain.html","Above the Treeline — Alpine Journal","Prata",
"""body{font-family:'Prata',serif;background:#0e1621;color:#e8eef5}
.j{max-width:720px;margin:auto;padding:10vh 24px}
h1{font-size:clamp(2.4rem,8vw,4rem)}
.entry{margin:50px 0;padding-left:26px;border-left:2px solid #3d5a80}
.alt{color:#98c1d9;letter-spacing:.2em;font-size:.8rem;text-transform:uppercase}
.entry h2{font-size:1.5rem;margin:6px 0}
.entry p{line-height:1.85;opacity:.85}
.peaks{display:flex;gap:0;align-items:flex-end;height:120px;margin-top:60px}
.peaks i{flex:1;background:linear-gradient(#98c1d9,#3d5a80);transform-origin:bottom;transition:.8s;border-radius:2px 2px 0 0}""",
"""<div class="j"><h1>Above the Treeline</h1><p style="opacity:.6;font-style:italic">field notes, week nine</p>
<div class="entry"><div class="alt">Day 41 · 2,910m</div><h2>The marmots unionised</h2><p>Seven whistles before dawn, coordinated, smug. The glacier above them hasn't moved in forty years and neither, apparently, have their grievances.</p></div>
<div class="entry"><div class="alt">Day 47 · 3,340m</div><h2>Weather turned silver</h2><p>Came up blue, went away white. Ate lunch facing the tent wall like a coward. The wind practised scales on the pitons all night — mostly minor keys.</p></div>
<div class="entry"><div class="alt">Day 52 · 3,842m · SUMMIT</div><h2>Quiet, finally</h2><p>At the top, weather is underneath you. It does something to the brain. I stood eleven minutes, said nothing, meant everything.</p></div>
<div class="peaks" id="pk"></div><p style="font-size:.75rem;opacity:.5;margin-top:10px">elevation profile · hover bars for altitudes</p></div>""",
"""const pk=document.getElementById('pk');const alts=[2100,2450,2910,3120,3340,3550,3842,3400,3000,2600];
alts.forEach((a,i)=>{const b=document.createElement('i');b.style.height=(a/3842*100)+'%';b.title=a+'m';
b.onmouseenter=()=>b.style.filter='brightness(1.6)';b.onmouseleave=()=>b.style.filter='';pk.appendChild(b)});""")

# ---------------------------------------------------------------- 53
page("053-colorpicker.html","Chroma Key — Build a Palette, Steal a Mood","Rubik",
"""body{font-family:'Rubik';background:#101014;color:#fff;text-align:center;padding:8vh 4vw}
h1{font-size:2.2rem}
.swatches{display:flex;gap:14px;justify-content:center;margin:40px 0;flex-wrap:wrap}
.sw{width:110px;height:150px;border-radius:14px;cursor:pointer;position:relative;transition:.25s;box-shadow:0 14px 34px #0006}
.sw:hover{transform:translateY(-8px)}
.sw span{position:absolute;bottom:8px;left:0;right:0;font-family:monospace;font-size:.7rem;color:#fff;text-shadow:0 1px 3px #000a}
button{background:#fff;color:#101014;border:0;padding:12px 28px;border-radius:99px;font-family:inherit;font-weight:700;cursor:pointer;font-size:1rem}
.harmony{margin-top:30px;font-size:.9rem;opacity:.7}""",
"""<h1>CHROMA KEY</h1><p>press shuffle until the room feels like something</p>
<div class="swatches" id="sw"></div><button id="shuf">⟳ new palette</button>
<div class="harmony" id="hm"></div>""",
"""const names=['Golden Hour Argument','Submarine Postcard','Bruised Peach','Library Fire','Cold Bloom','Tuesday Rain','Electric Moss','Velvet Alarm'];
function hsl(h,s,l){return `hsl(${h},${s}%,${l}%)`}
function gen(){const base=Math.random()*360|0,type=['analogous','complement','triad'][Math.random()*3|0];
const offs=type==='analogous'?[-40,-15,0,15,40]:type==='complement'?[base,(base+180)%360,(base+180)%360,(base+20)%360,(base+20)%360]:[0,120,240,120,240].map(o=>(base+o)%360);
const box=document.getElementById('sw');box.innerHTML='';
offs.forEach((h,i)=>{const l=type==='analogous'?40+i*8:30+(i%3)*22;const col=hsl(typeof h==='number'?h:base,72,l);
const d=document.createElement('div');d.className='sw';d.style.background=col;
d.innerHTML=`<span>${col.match(/\\d+/g).join(' ')}° % %</span>`;
d.onclick=()=>{navigator.clipboard&&navigator.clipboard.writeText(col);d.style.outline='3px solid #fff';setTimeout(()=>d.style.outline='',600)};
box.appendChild(d)});
document.getElementById('hm').textContent=`mode: ${type} · hue ${base}° · named “${names[Math.random()*names.length|0]}”`}
gen();document.getElementById('shuf').onclick=gen;""")

# ---------------------------------------------------------------- 54
page("054-map.html","Here There Be — An Imaginary Cartograph","IM Fell English",
"""body{font-family:'IM Fell English',serif;background:#e8dcb8;color:#4a3b22}
.map{max-width:900px;margin:5vh auto;padding:26px;border:3px double #4a3b2255;position:relative;background:radial-gradient(#f0e5c4,#e3d3a8)}
h1{text-align:center;font-size:clamp(2rem,6vw,3.4rem);letter-spacing:.1em}
.terrain{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:20px;margin:34px 0}
.place{padding:20px;border:1px dashed #4a3b2266;border-radius:6px;transition:.3s;cursor:pointer}
.place:hover{background:#fffdf0;transform:rotate(-1deg) scale(1.03)}
.place h2{font-size:1.2rem}.legend-note{font-style:italic;opacity:.7;font-size:.9rem}
.compass{text-align:center;font-size:3rem;margin:20px}
.sea{background:#d8cba0;padding:20px;text-align:center;font-style:italic;border-radius:6px;margin-top:26px;letter-spacing:.2em}""",
"""<div class="map"><h1>Here There Be</h1><p style="text-align:center;font-style:italic">charted by guess and by god, 17??</p>
<div class="compass">🧭</div>
<div class="terrain">
<div class="place"><h2>Mount Petrichor</h2><p class="legend-note">smells of first rain; summit perpetually apologising for clouds</p></div>
<div class="place"><h2>The Whispering Fen</h2><p class="legend-note">reeds repeat everything said within earshot, badly</p></div>
<div class="place"><h2>Copper Bay</h2><p class="legend-note">oxidises beautifully; swim at your own patina</p></div>
<div class="place"><h2>Forest of Small Decisions</h2><p class="legend-note">enter for a shortcut, exit three hours later having chosen a cereal</p></div></div>
<div class="sea">· · · · · THE UNBORED OCEAN · · · · ·<br>here there be Wi-Fi (weak)</div></div>""")

# ---------------------------------------------------------------- 55
page("055-fitness.html","STRIDE — Run Like You Mean It","Oswald",
"""body{font-family:'Oswald';background:#0c0f0c;color:#eaffea;text-transform:uppercase}
.hero{min-height:100vh;display:flex;flex-direction:column;justify-content:center;padding:0 8vw;position:relative;overflow:hidden}
h1{font-size:clamp(3.5rem,14vw,9rem);line-height:.9;font-weight:700}
h1 .out{color:transparent;-webkit-text-stroke:2px #7fff6e}
.track{position:absolute;bottom:0;left:0;right:0;height:6px;background:#1c241c}
.runner{position:absolute;bottom:0;width:16px;height:6px;background:#7fff6e;animation:lap 4s linear infinite;box-shadow:0 0 16px #7fff6e}
@keyframes lap{to{transform:translateX(100vw)}}
.split{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:2px;background:#0c0f0c;padding:0 8vw 8vh}
.cell{background:#141a14;padding:30px 20px;text-align:center}
.cell b{font-size:2.4rem;color:#7fff6e;display:block}
.plan{padding:6vh 8vw;font-size:1rem;line-height:2.4;opacity:.85}""",
"""<div class="hero"><h1>Run the<br><span class="out">boring miles</span><br>loudly.</h1>
<div class="track"><div class="runner"></div></div></div>
<div class="split"><div class="cell"><b>4:52</b>km pace</div><div class="cell"><b>21.1</b>best half</div><div class="cell"><b>148</b>weekly k's</div><div class="cell"><b>0</b>excuses</div></div>
<div class="plan">Week plan — Tue: tempo 6×90s · Thu: easy 8km, conversations mandatory · Sat: long run 18km through the reservoir · Sun: rest, or the lie that is stretching.</div>""")

# ---------------------------------------------------------------- 56
page("056-mixtape.html","Mixtape for a Rainy Thursday","Permanent Marker",
"""body{font-family:'Permanent Marker';background:#1b1b23;color:#ffd93d}
.tape{width:min(92vw,560px);margin:10vh auto;background:#2a2a35;border-radius:16px;padding:34px;box-shadow:0 24px 60px #000a;position:relative}
.reels{display:flex;justify-content:space-around;align-items:center;margin:20px 0}
.reel{width:90px;height:90px;border-radius:50%;border:10px solid #ffd93d;background:#111;animation:sp 4s linear infinite}
.reel.s2{animation-duration:5.5s}
@keyframes sp{to{transform:rotate(360deg)}}
.label{background:#f5f1e6;color:#333;padding:12px 20px;border-radius:4px;font-family:'Permanent Marker';margin-bottom:20px}
.tracks{list-style:none;font-size:1.05rem;line-height:2.2;color:#e8e8f0}
.tracks li::before{content:'▸ ';color:#ffd93d}
.side{font-size:1.6rem;color:#ff6b6b}""",
"""<div class="tape"><div class="label">SIDE A — mixtape for a rainy thursday<br><small>recorded off the radio, 11:42pm, do not skip track 3</small></div>
<div class="reels"><div class="reel"></div><div style="font-size:2rem">〰〰〰</div><div class="reel s2"></div></div>
<ul class="tracks"><li>Let It Rain On Me (Live in Kitchen)</li><li>Braids & Thunderstorms — The Umbrellas</li><li>Window Fog Sonata</li><li>Half a Song for the Bus</li><li>Thursday's Child (Extended Rainbreak)</li></ul>
<div class="side">SIDE B: for the drive home · 47 min</div></div>""")

# ---------------------------------------------------------------- 57
page("057-changelog.html","Patch Notes for Being Human","JetBrains Mono",
"""body{font-family:'JetBrains Mono',monospace;background:#0d1117;color:#c9d1d9;line-height:1.8}
.wrap{max-width:720px;margin:auto;padding:10vh 24px}
h1{color:#58a6ff;font-size:1.8rem}
.rel{border:1px solid #30363d;border-radius:10px;padding:24px;margin:26px 0;background:#161b22;transition:.3s}
.rel:hover{border-color:#58a6ff}
.ver{color:#3fb950;font-weight:700}
.fix{color:#d29922}.new{color:#58a6ff}.dep{color:#f85149}
code{background:#21262d;padding:2px 8px;border-radius:4px}""",
"""<div class="wrap"><h1>PATCH NOTES — being human, v3.26.10</h1>
<div class="rel"><span class="ver">v3.26.10</span> “Autumn Release”<br>
<span class="new">NEW:</span> sweater weather module enabled globally.<br>
<span class="fix">FIX:</span> daylight savings now affects clocks, not souls (known issue persists).<br>
<span class="dep">DEPRECATED:</span> resolving family dinners in one conversation.</div>
<div class="rel"><span class="ver">v3.26.09</span><br>
<span class="new">NEW:</span> <code>gratitude()</code> runs silently in background; logs improve sleep quality 12%.<br>
<span class="fix">FIX:</span> song stuck in head loops reduced from ∞ to 3 days.</div>
<div class="rel"><span class="ver">v3.26.08</span><br>
<span class="new">NEW:</span> friendship API supports async catch-ups ("we should—").<br>
<span class="fix">FIX:</span> knee sounds now load-bearing. Please update your posture.</div>
<p style="opacity:.5">Next release: winter. Expect hibernation bugs and candle-based lighting.</p></div>""")

# ---------------------------------------------------------------- 58
page("058-market.html","Saturday Market — Fresh From the Van","Lilita One",
"""body{font-family:'Lilita One';background:#fef8e7;color:#2d3436}
.banner{background:#ff7675;color:#fff;padding:16px 0;overflow:hidden;white-space:nowrap}
.banner span{display:inline-block;animation:mv 16s linear infinite;font-size:1.3rem;letter-spacing:.1em}
@keyframes mv{to{transform:translateX(-50%)}}
.stalls{display:grid;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:22px;padding:8vh 6vw}
.stall{border-radius:18px;padding:26px;color:#fff;transition:.3s;cursor:pointer;position:relative;overflow:hidden}
.stall::before{content:'';position:absolute;top:0;left:0;right:0;height:14px;background:repeating-linear-gradient(90deg,#fff 0 22px,#00000022 22px 44px)}
.stall:hover{transform:translateY(-8px) rotate(-1.5deg)}
.stall h3{font-size:1.5rem;margin:14px 0 6px}
.stall .emoji{font-size:2.6rem}
.price-tag{background:#fff;color:#2d3436;border-radius:99px;padding:4px 14px;display:inline-block;margin-top:10px;font-size:.9rem}""",
"""<div class="banner"><span>★ SATURDAY MARKET · 8AM–2PM · BRING BAGS, BE NICE TO TOM · ★ SATURDAY MARKET · 8AM–2PM · BRING BAGS, BE NICE TO TOM · ★ SATURDAY MARKET · 8AM–2PM · BRING BAGS, BE NICE TO TOM · ★&nbsp;</span></div>
<div class="stalls">
<div class="stall" style="background:#00b894"><span class="emoji">🥬</span><h3>Greensmouth Farm</h3><p>kale with attitude</p><span class="price-tag">€3/bunch</span></div>
<div class="stall" style="background:#fdcb6e;color:#2d3436"><span class="emoji">🧀</span><h3>Wheel & Rind</h3><p>speak softly, carry cheddar</p><span class="price-tag">taste first</span></div>
<div class="stall" style="background:#e17055"><span class="emoji">🥐</span><h3>Butter Riot</h3><p>sells out by 10:15, yes again</p><span class="price-tag">€2.50</span></div>
<div class="stall" style="background:#6c5ce7"><span class="emoji">🫐</span><h3>Blueberry Bin</h3><p>staining guaranteed</p><span class="price-tag">€5 punnet</span></div>
<div class="stall" style="background:#0984e3"><span class="emoji">🐟</span><h3>Salty Dog Fish</h3><p>today's catch: opinions</p><span class="price-tag">market rate</span></div>
<div class="stall" style="background:#d63031"><span class="emoji">🌶️</span><h3>Heat Index</h3><p>sign waiver first</p><span class="price-tag">€1–∞</span></div></div>""")

# ---------------------------------------------------------------- 59
page("059-orbit-tracker.html","Orbit Tracker — Live Satellite Sketch","Space Mono",
"""body{font-family:'Space Mono',monospace;background:#04070d;color:#9fd3ff}
.hd{padding:22px 24px;border-bottom:1px solid #123}
h1{font-size:1.1rem;letter-spacing:.2em}
canvas{display:block;margin:0 auto;border:1px solid #123;max-width:100%}
.feed{max-width:760px;margin:20px auto;padding:0 24px;font-size:.85rem;line-height:2}
.sat{color:#9fd3ff}.ok{color:#3fb950}.warn{color:#d29922}""",
"""<div class="hd"><h1>◉ ORBIT TRACKER · ground station 04</h1><small style="opacity:.6">simulated pass predictions, refreshed with vibes</small></div>
<canvas id="c" width="760" height="380"></canvas>
<div class="feed"><div><span class="sat">ISS (ZARYA)</span> — overhead window 21:47 · magnitude -3.1 <span class="ok">[VISIBLE]</span></div>
<div><span class="sat">STARLINK-8842</span> — train forming over Nevada <span class="ok">[PRETTY]</span></div>
<div><span class="sat">TIANGONG</span> — passive tumbling <span class="warn">[ATTITUDE]</span></div>
<div><span class="sat">NOAA-19</span> — APT downlink on 137 MHz, sounds like a fax machine confessing</div></div>""",
"""const c=document.getElementById('c'),x=c.getContext('2d');let t=0;
const sats=[{r:120,s:.011,col:'#9fd3ff'},{r:150,s:-.007,col:'#3fb950'},{r:80,s:.019,col:'#d29922'},{r:170,s:.004,col:'#f778ba'}];
(function l(){x.fillStyle='#04070d';x.fillRect(0,0,760,380);
x.strokeStyle='#123';for(let r=40;r<=180;r+=35){x.beginPath();x.arc(380,190,r,0,7);x.stroke()}
x.fillStyle='#1c3a5f';x.beginPath();x.arc(380,190,26,0,7);x.fill();
x.fillStyle='#9fd3ff';x.font='10px Space Mono';x.fillText('EARTH (allegedly)',348,230);
for(const s of sats){t;const a=t*s.s*60;const px=380+Math.cos(a)*s.r,py=190+Math.sin(a)*s.r*.55;
x.strokeStyle=s.col+'44';x.beginPath();x.ellipse(380,190,s.r,s.r*.55,0,0,7);x.stroke();
x.fillStyle=s.col;x.fillRect(px-3,py-3,6,6);x.shadowColor=s.col;x.shadowBlur=10;x.fillRect(px-3,py-3,6,6);x.shadowBlur=0}
t+=1;requestAnimationFrame(l)})();""")

# ---------------------------------------------------------------- 60
page("060-patisserie.html","Maison Doré — Patisserie","Cormorant Garamond",
"""body{font-family:'Cormorant Garamond',serif;background:#f9f2e7;color:#4b3621;text-align:center}
.maison{padding:10vh 6vw}
h1{font-size:clamp(2.8rem,9vw,4.6rem);letter-spacing:.15em;color:#a67c52}
.thin{font-weight:300;font-style:italic}
.case{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:30px;padding:6vh 8vw 12vh}
.treat{background:#fff;border:1px solid #e2d3bc;padding:34px 22px;border-radius:2px;transition:.35s;box-shadow:0 10px 30px #00000008}
.treat:hover{transform:translateY(-10px);box-shadow:0 24px 50px #a67c5233}
.treat .glyph{font-size:3rem}
.treat h3{font-size:1.5rem;margin:10px 0 4px;font-weight:600}
.gold{color:#a67c52;letter-spacing:.2em;font-size:.8rem;text-transform:uppercase}""",
"""<div class="maison"><div class="gold">est. 1987 · rue de la faim</div><h1>MAISON DORÉ</h1><p class="thin" style="font-size:1.4rem">Pastry, pressed gently into submission by butter.</p></div>
<div class="case">
<div class="treat"><div class="glyph">🍰</div><h3>Fraisier Classique</h3><p class="thin">Genoise, crème mousseline, strawberries arranged like a thesis defence.</p><p class="gold">€8</p></div>
<div class="treat"><div class="glyph">🥧</div><h3>Tarte au Citron Meringuée</h3><p class="thin">Torched peaks, sour enough to forgive the sugar.</p><p class="gold">€7</p></div>
<div class="treat"><div class="glyph">🍫</div><h3>Fondant 70%</h3><p class="thin">Molten centre, structural integrity revoked at the oven.</p><p class="gold">€9</p></div>
<div class="treat"><div class="glyph">🥐</div><h3>Galette des Rois</h3><p class="thin">Puff pastry king. Find the fève, wear the crown, owe everyone cake.</p><p class="gold">seasonal</p></div></div>""")

# ---------------------------------------------------------------- 61
page("061-tarot.html","The Midnight Deck — Three Cards","Marcellus",
"""body{font-family:'Marcellus',serif;background:radial-gradient(#241b3a,#0e0a18 70%);color:#e8ddff;text-align:center;padding:8vh 4vw}
h1{font-size:clamp(2rem,7vw,3.4rem);letter-spacing:.15em}
.deck{display:flex;gap:26px;justify-content:center;margin:60px 0;flex-wrap:wrap}
.card{width:170px;height:290px;border:2px solid #c9a227;border-radius:12px;background:#161028;display:grid;place-items:center;font-size:4rem;cursor:pointer;transition:.5s;position:relative;transform-style:preserve-3d}
.card:hover{transform:rotateY(12deg) translateY(-10px);box-shadow:0 24px 50px #c9a22733}
.card span{position:absolute;bottom:12px;left:0;right:0;font-size:.75rem;letter-spacing:.2em;opacity:0;transition:.4s}
.card.open span{opacity:1}
.reading{max-width:560px;margin:auto;min-height:120px;font-style:italic;line-height:1.9;font-size:1.15rem;color:#d9b8ff}""",
"""<h1>THE MIDNIGHT DECK</h1><p style="opacity:.7">tap three cards · the universe will paraphrase</p>
<div class="deck" id="deck"></div><div class="reading" id="out">…</div>""",
"""const CARDS=[['🌙','THE MOON','Intuition over itinerary. Trust the tide you can't see.'],['☀️','THE SUN','Unironic joy available today. Coupon attached.'],['🗝','THE KEY','A door you called "someday" is actually a hinge.'],['🌊','THE TIDE','Feelings are weather, not geography. Walk through.'],['🦉','THE OWL','Ask the embarrassing question. It's the only useful one.'],['⚡','THE SPARK','Start messy. Momentum forgives form.'],['🪞','THE MIRROR','You already know who to text. Do it.'],['🕰','THE HOUR','Not late — precisely on your schedule.']];
const deck=document.getElementById('deck'),out=document.getElementById('out');let chosen=[],pool=[...CARDS].sort(()=>Math.random()-.5);
for(let i=0;i<8;i++){const c=document.createElement('div');c.className='card';c.innerHTML=`${pool[i][0]}<span>${pool[i][1]}</span>`;
c.onclick=()=>{if(c.classList.contains('open'))return;c.classList.add('open');chosen.push(pool[i]);
if(chosen.length===3){out.textContent=`${chosen.map((x,j)=>`${['PAST','PRESENT','PATH'][j]}: ${x[2]}`).join(' · ')} — shuffled by the midnight desk.`}};
deck.appendChild(c)}""")

# ---------------------------------------------------------------- 62
page("062-bike-repair.html","Spoke & Wrench — Bike Repair, No Judgment","Barlow Condensed",
"""body{font-family:'Barlow Condensed';background:#101418;color:#eef3f7}
.shop{padding:10vh 8vw}
h1{font-size:clamp(2.6rem,9vw,5rem);text-transform:uppercase;letter-spacing:.03em;color:#ffb454}
.chain{display:flex;align-items:center;gap:0;margin:40px 0;flex-wrap:wrap}
.link{width:34px;height:18px;border:3px solid #6b7a88;border-radius:6px}
.link.hot{border-color:#ffb454;animation:sh .8s infinite alternate}
@keyframes sh{to{transform:translateY(-6px)}}
.svc{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:2px;background:#222}
.s{background:#151a20;padding:28px;transition:.25s}
.s:hover{background:#1c242d}
.s h3{text-transform:uppercase;font-size:1.4rem}.price{color:#ffb454;font-size:1.6rem;font-weight:700}
.s p{opacity:.7;line-height:1.6;font-family:Barlow,sans-serif;font-weight:300}
.queue{margin-top:40px;font-family:monospace;font-size:.9rem;color:#7fd1ae}""",
"""<div class="shop"><h1>SPOKE & WRENCH</h1>
<p style="font-size:1.4rem;max-width:640px">Your bike isn't broken, it's buffering. We fix brakes, gears, and the one squeak you've learned to live with (you haven't).</p>
<div class="chain"><div class="link"></div><div class="link hot"></div><div class="link"></div><div class="link hot"></div><div class="link"></div><div class="link hot"></div><div class="link"></div></div>
<div class="svc">
<div class="s"><h3>Tune-Up Deluxe</h3><div class="price">€55</div><p>Full drivetrain clean, brake bleed check, 42-point sanity audit.</p></div>
<div class="s"><h3>Flat No More</h3><div class="price">€12</div><p>Patch or tube swap while you wait and explain why it's "weird this time."</p></div>
<div class="s"><h3>Wheel Truth</h3><div class="price">€30</div><p>Truing session. Your rim will admit what it's been hiding.</p></div>
<div class="s"><h3>Squeak Exorcism</h3><div class="price">€20</div><p>We find it. We always find it. You'll hear silence and distrust us.</p></div></div>
<div class="queue">TODAY'S QUEUE: [✓ fixed: emily's commuter] [🔧 bench 2: cargo trike] [⏳ waiting: you — ~40 min]</div></div>""")

# ---------------------------------------------------------------- 63
page("063-firefly.html","Firefly Field — Catch One","Comfortaa",
"""body{font-family:'Comfortaa';background:linear-gradient(#050b1e,#0a1530 60%,#0d1f1a);color:#cdeffd;min-height:100vh;overflow:hidden;position:relative}
.h1{position:fixed;top:24px;left:0;right:0;text-align:center;letter-spacing:.3em;z-index:2;font-size:1rem}
.count{position:fixed;top:52px;text-align:center;width:100%;opacity:.7;z-index:2;font-size:.8rem}
.fly{position:fixed;width:10px;height:10px;border-radius:50%;background:#ffe680;box-shadow:0 0 18px 6px #ffe68088;cursor:pointer;transition:transform .2s}
.grass{position:fixed;bottom:0;left:0;right:0;height:18vh;background:linear-gradient(transparent,#04140a);z-index:1}
.msg{position:fixed;bottom:6vh;width:100%;text-align:center;font-size:1.1rem;z-index:2;opacity:.85}""",
"""<div class="h1">FIREFLY FIELD</div><div class="count" id="cnt">caught: 0 / 7 · tap gently, release with double-click</div>
<div class="grass"></div><div class="msg" id="m">the field is waking up…</div>""",
"""let n=0;const flies=[];
for(let i=0;i<7;i++){const f=document.createElement('div');f.className='fly';f.style.left=Math.random()*90+'vw';f.style.top=30+Math.random()*55+'vh';
flies.push({el:f,x:parseFloat(f.style.left),y:parseFloat(f.style.top),vx:(Math.random()-.5)*.15,vy:(Math.random()-.5)*.1});
f.onclick=()=>{if(!f.caught){n++;f.caught=true;f.style.transform='scale(1.8)';document.getElementById('cnt').textContent=`caught: ${n} / 7`;
document.getElementById('m').textContent=n===7?'all seven glow in your jar tonight ✨':'one more! they move slower near the grass'}
else{f.caught=false;f.style.transform='';n--;document.getElementById('cnt').textContent=`caught: ${n} / 7`}};
document.body.appendChild(f)}
setInterval(()=>{for(const fl of flies){fl.x+=fl.vx;fl.y+=fl.vy;
if(fl.x<2||fl.x>92)fl.vx*=-1;if(fl.y<28||fl.y>86)fl.vy*=-1;
if(Math.random()<.05){fl.vx+=(Math.random()-.5)*.1;fl.vy+=(Math.random()-.5)*.1}
if(!fl.el.caught){fl.el.style.left=fl.x+'vw';fl.el.style.top=fl.y+'vh';fl.el.style.opacity=.5+Math.random()*.5}}},50);""")

# ---------------------------------------------------------------- 64
page("064-cheatsheet.html","CSS Grid Cheatsheet — For People Who Code at 2AM","Fira Code",
"""body{font-family:'Fira Code',monospace;background:#0d1117;color:#e6edf3;padding-bottom:14vh}
.wrap{max-width:880px;margin:auto;padding:8vh 22px}
h1{color:#79c0ff;font-size:1.8rem}
.tip{color:#d29922;font-size:.9rem;font-style:italic}
.block{margin:34px 0;border:1px solid #30363d;border-radius:10px;overflow:hidden}
.block h2{background:#161b22;padding:12px 18px;font-size:1rem;color:#7ee787}
pre{padding:18px;overflow-x:auto;font-size:.85rem;line-height:1.7;background:#0d1117;margin:0}
.demo{display:grid;gap:6px;padding:14px;background:#161b22;border-top:1px solid #30363d}
.demo div{background:#1f6feb66;border:1px solid #58a6ff;padding:10px;text-align:center;font-size:.75rem;border-radius:4px}
.kw{color:#ff7b72}.st{color:#a5d6ff}.cm{color:#8b949e}""",
"""<div class="wrap"><h1>▸ CSS GRID CHEATSHEET</h1><p class="tip">// for people who code at 2am and forget everything by 2:15</p>
<div class="block"><h2>auto-fit + minmax = responsive without media queries</h2>
<pre><span class="kw">.grid</span>{ display:grid;
  grid-template-columns: <span class="st">repeat(auto-fit, minmax(240px, 1fr))</span>; gap:1rem }</pre>
<div class="demo" style="grid-template-columns:repeat(auto-fit,minmax(140px,1fr))"><div>1fr</div><div>1fr</div><div>1fr</div></div></div>
<div class="block"><h2>named areas beat nth-child therapy</h2>
<pre><span class="kw">.layout</span>{ grid-template:<span class="st">"head head" auto "side main" 1fr / 200px 1fr</span> }</pre>
<div class="demo" style="grid-template-areas:'h h' 's m';grid-template-columns:120px 1fr;grid-template-rows:40px 80px">
<div style="grid-area:h">head head</div><div style="grid-area:s">side</div><div style="grid-area:m">main</div></div></div>
<div class="block"><h2>subgrid keeps nested things honest</h2><pre><span class="kw">.card</span>{ display:grid; grid-row:<span class="st">span 3</span>; grid-template-rows:<span class="st">subgrid</span> }</pre>
<div class="demo" style="grid-template-columns:repeat(3,1fr)"><div>a</div><div>b</div><div>c</div></div></div>
<p class="cm">// if this saved you: close a tab. any tab. we're even.</p></div>""")

# ---------------------------------------------------------------- 65
page("065-vinyl-record.html","Crate Digger — Vinyl of the Month","Anton",
"""body{font-family:'Anton';background:#191410;color:#f5efe0;text-transform:uppercase}
.crate{max-width:900px;margin:auto;padding:8vh 24px}
h1{font-size:clamp(2.6rem,9vw,5rem);color:#e07a3f;letter-spacing:.02em}
.turntable{display:flex;gap:40px;align-items:center;flex-wrap:wrap;margin:40px 0}
.disc{width:230px;height:230px;border-radius:50%;background:repeating-radial-gradient(#0c0c0c 0 4px,#181818 4px 8px);position:relative;animation:sp 2.2s linear infinite;box-shadow:0 0 0 8px #0c0c0c,0 20px 50px #000c}
.disc::after{content:'';position:absolute;inset:36%;border-radius:50%;background:conic-gradient(#e07a3f,#f2b134,#e07a3f)}
.disc::before{content:'';position:absolute;inset:48.5%;border-radius:50%;background:#191410;z-index:2}
@keyframes sp{to{transform:rotate(360deg)}}
.tonearm{width:130px;height:6px;background:#bbb;border-radius:4px;transform-origin:right;transform:rotate(-24deg);position:relative;margin-left:-70px}
.info h2{font-size:2rem;color:#f2b134}.info p{font-family:Georgia;text-transform:none;line-height:1.8;opacity:.85;max-width:420px}
.other{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:18px;margin-top:50px}
.rec{border:1px solid #3a2f26;padding:20px;transition:.3s;cursor:pointer}
.rec:hover{border-color:#e07a3f;background:#221b15}""",
"""<div class="crate"><h1>Crate Digger</h1><p style="opacity:.6;font-family:Georgia;text-transform:none">this month's pressings, judged before they hit the shelf</p>
<div class="turntable"><div class="disc"></div><div class="tonearm"></div>
<div class="info"><h2>“Riverbed Sessions”<br>Mala Webb · 180g</h2><p>Recorded live to tape beside actual water, which you can faintly hear under track 4. The crackle is marketing; the singing is not.</p></div></div>
<div class="other"><div class="rec"><b>Night Bus Jazz Octet</b><br><small style="opacity:.6">repress · €26</small></div>
<div class="rec"><b>Kiln & Chorus — Ceramic Pop</b><br><small style="opacity:.6">first press · €31</small></div>
<div class="rec"><b>B-Sides From A Lighthouse</b><br><small style="opacity:.6">extremely limited · €44</small></div></div></div>""")

# ---------------------------------------------------------------- 66
page("066-mood-tracker.html","Weather Report: Internal — Mood Tracker","Baloo 2",
"""body{font-family:'Baloo 2';background:#f4f1ff;color:#33304a;padding:8vh 6vw;text-align:center}
h1{font-size:2.2rem}
.sub{opacity:.6;margin-bottom:34px}
.moods{display:flex;gap:18px;justify-content:center;flex-wrap:wrap}
.m{width:92px;height:92px;border-radius:24px;font-size:2.6rem;display:grid;place-items:center;cursor:pointer;transition:.25s;background:#fff;box-shadow:0 8px 24px #4c3f8a1a}
.m:hover{transform:translateY(-8px) scale(1.06)}
.m.sel{outline:4px solid #7c5cff;transform:scale(1.12)}
.log{max-width:520px;margin:40px auto;background:#fff;border-radius:18px;padding:24px;box-shadow:0 10px 30px #4c3f8a14;text-align:left}
.day{display:flex;justify-content:space-between;padding:8px 0;border-bottom:1px dashed #ddd;font-size:.95rem}
.note{font-size:.9rem;opacity:.7;margin-top:10px;min-height:1.2em}""",
"""<h1>Weather Report: Internal</h1><p class="sub">how's the climate in there? tap one, add a note if brave</p>
<div class="moods"><div class="m" data-l="sunny">☀️</div><div class="m" data-l="cloudy">⛅</div><div class="m" data-l="rainy">🌧️</div><div class="m" data-l="stormy">⛈️</div><div class="m" data-l="foggy">🌫️</div><div class="m" data-l="calm">🌙</div></div>
<div class="note" id="note"></div>
<div class="log"><b>this week's forecast log</b>
<div class="day"><span>Mon</span><span>⛅ cloudy → cleared by 4pm</span></div>
<div class="day"><span>Tue</span><span>⛈️ stormy · umbrella day</span></div>
<div class="day"><span>Wed</span><span id="today">— awaiting report —</span></div></div>""",
"""const notes={sunny:'highs near unstoppable, light breeze of humility',cloudy:'mostly brilliant with patches of meeting',rainy:'productive grey. things grow in this.',stormy:'proceed with caution and tea',foggy:'ideas present, visibility optional',calm:'clear skies within. low wind, high wisdom'};
document.querySelectorAll('.m').forEach(m=>m.onclick=()=>{document.querySelectorAll('.m').forEach(x=>x.classList.remove('sel'));
m.classList.add('sel');const l=m.dataset.l;document.getElementById('note').textContent=notes[l];
document.getElementById('today').textContent=m.textContent+' '+l+' · logged'})""")

# ---------------------------------------------------------------- 67
page("067-jazzclub.html","Blue Note Cellar — Live Jazz Since 1959","Yeseva One",
"""body{font-family:'Yeseva One',serif;background:#080a12;color:#e8d9b0;text-align:center}
.spot{background:radial-gradient(ellipse 60% 40% at 50% 30%,#1a2340,#080a12 70%);padding:14vh 6vw}
h1{font-size:clamp(2.6rem,9vw,4.6rem);color:#7fb4ff;text-shadow:0 0 40px #7fb4ff44}
.smoke{height:100px;background:linear-gradient(transparent,#ffffff06);position:relative;overflow:hidden}
.puff{position:absolute;bottom:0;width:120px;height:120px;border-radius:50%;background:#ffffff08;filter:blur(24px);animation:puff 9s ease-out infinite}
@keyframes puff{to{transform:translate(var(--dx),-160px) scale(2.4);opacity:0}}
.gig{max-width:620px;margin:40px auto;text-align:left;padding:0 24px}
.slot{display:grid;grid-template-columns:90px 1fr auto;gap:18px;padding:20px 0;border-bottom:1px solid #e8d9b022;align-items:center}
.time{color:#7fb4ff;font-size:1.2rem}.band{font-size:1.3rem}.fee{opacity:.7}
.book{background:#7fb4ff;color:#081020;border:0;font-family:inherit;font-size:1.1rem;padding:14px 40px;border-radius:2px;cursor:pointer;margin:30px 0}
.book:hover{background:#a8cdff}""",
"""<div class="spot"><h1>BLUE NOTE CELLAR</h1><p style="letter-spacing:.4em;font-size:.8rem">DOWN THE STAIRS · PAST THE BAR · SINCE 1959</p></div>
<div class="smoke"><div class="puff" style="left:20%;--dx:60px"></div><div class="puff" style="left:60%;--dx:-40px;animation-delay:3s"></div><div class="puff" style="left:40%;--dx:20px;animation-delay:6s"></div></div>
<div class="gig">
<div class="slot"><span class="time">THU 21:00</span><span class="band">The Ellington Six</span><span class="fee">€15</span></div>
<div class="slot"><span class="time">FRI 22:00</span><span class="band">Nadia Fierro Trio · bossa noir</span><span class="fee">€18</span></div>
<div class="slot"><span class="time">SAT 20:00</span><span class="band">Late Set: improvise until closing</span><span class="fee">free-ish</span></div>
<div class="slot"><span class="time">SUN 18:00</span><span class="band">Sunday LP Club — records only, humans optional</span><span class="fee">€5</span></div></div>
<button class="book" onclick="this.textContent='✓ table by the pillar'">Reserve a table</button>
<p style="opacity:.5;font-size:.85rem;padding-bottom:60px">Cellar temp: 16°C · Dress code: comfortable mystery</p>""")

# ---------------------------------------------------------------- 68
page("068-emoji-orchestra.html","Emoji Orchestra — Conduct Yourself","Kalam",
"""body{font-family:'Kalam';background:#fffbe6;color:#333;text-align:center}
.stage{max-width:760px;margin:auto;padding:8vh 20px}
h1{font-size:2.4rem}
.row{display:flex;justify-content:center;gap:14px;margin:22px 0;font-size:3rem;flex-wrap:wrap}
.seat{cursor:pointer;transition:.2s;display:inline-block;filter:grayscale(.7)}
.seat:hover{transform:scale(1.3) rotate(-6deg);filter:none}
.seat.play{animation:bounce .5s;filter:none}
@keyframes bounce{50%{transform:translateY(-20px) scale(1.4)}}
.conductor{font-size:4rem;margin:20px;cursor:pointer;display:inline-block}
.caption{font-size:1.1rem;opacity:.7;min-height:1.6em}""",
"""<div class="stage"><h1>🎼 Emoji Orchestra 🎼</h1>
<p>sectionals below · click an instrument to solo, baton for the full symphony</p>
<div class="row" data-snd="strings"><span class="seat">🎻</span><span class="seat">🎻</span><span class="seat">🎺</span><span class="seat">🎻</span></div>
<div class="row" data-snd="wind"><span class="seat">🎷</span><span class="seat">🪕</span><span class="seat">🪈</span><span class="seat">🎹</span></div>
<div class="row" data-snd="perc"><span class="seat">🥁</span><span class="seat">🪘</span><span class="seat">🔔</span><span class="seat">🪇</span></div>
<div class="conductor" id="baton">🪄</div>
<div class="caption" id="cap">the orchestra warms up politely…</div></div>""",
"""function blip(freq,dur,type='triangle'){try{const ac=blip.ac||(blip.ac=new(window.AudioContext||window.webkitAudioContext)());
const o=ac.createOscillator(),g=ac.createGain();o.type=type;o.frequency.value=freq;g.gain.value=.12;
o.connect(g).connect(ac.destination);o.start();g.gain.exponentialRampToValueAtTime(.001,ac.currentTime+dur);o.stop(ac.currentTime+dur)}catch(e){}}
const caps=['🎻 aching in minor sevenths','🎷 smooth as velvet furniture','🥁 keeping time like it owes money','🎹 eighty-eight opinions, all correct'];
document.querySelectorAll('.seat').forEach(s=>s.onclick=e=>{s.classList.remove('play');void s.offsetWidth;s.classList.add('play');
const row=s.parentElement.dataset.snd;blip(row==='strings'?440:row==='wind'?330:220,.3,row==='perc'?'square':'triangle');
document.getElementById('cap').textContent=caps[Math.random()*caps.length|0]});
document.getElementById('baton').onclick=()=>{document.querySelectorAll('.seat').forEach((s,i)=>setTimeout(()=>s.click(),i*110));
document.getElementById('cap').textContent='🌟 FULL ORCHESTRA: chaos, but metered chaos 🌟'};""")

# ---------------------------------------------------------------- 69
page("069-rust-belt.html","Rust Belt Radio — Analog Rock Archive","Oswald",
"""body{font-family:'Oswald';background:#201512;color:#f0e2d0}
.mill{background:linear-gradient(#3a241a,#201512);padding:12vh 7vw;border-bottom:6px solid #e8590c}
h1{font-size:clamp(2.6rem,9vw,5rem);text-transform:uppercase}
h1 b{color:#e8590c}
.racks{padding:6vh 7vw;display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:20px}
.reel{border:2px solid #6b4a35;padding:22px;background:#2a1c15;transition:.3s;cursor:pointer;position:relative}
.reel:hover{border-color:#e8590c;transform:skewX(-2deg)}
.reel::before{content:'◉ ◉';letter-spacing:14px;color:#e8590c88;font-size:.8rem}
.reel h3{font-size:1.25rem;text-transform:uppercase}
.meta{font-size:.8rem;opacity:.6;margin-top:8px;font-family:monospace}
.dust{position:fixed;inset:0;pointer-events:none;background:radial-gradient(transparent 60%,#00000055)}""",
"""<div class="dust"></div>
<div class="mill"><h1>RUST <b>BELT</b> RADIO</h1><p>field recordings from factories that stopped humming but never stopped echoing · 900 hours archived</p></div>
<div class="racks">
<div class="reel"><h3>Press Shop №7</h3><p>Hydraulic sighs in B♭, shift whistle, one foreman whistling back.</p><div class="meta">1978 · quarter-inch · 47 min</div></div>
<div class="reel"><h3>Foundry Rain</h3><p>Molten iron meets sand quarry. Sounds worse than it is. Much worse.</p><div class="meta">1981 · reel-to-reel · 22 min</div></div>
<div class="reel"><h3>Last Shift, Milldale Looms</h3><p>Machines powered down one by one, like an audience leaving.</p><div class="meta">1994 · cassette · 68 min</div></div>
<div class="reel"><h3>Bridge Grinders, 3AM</h3><p>Repair crew on the Ironway. Sparks audible as percussion.</p><div class="meta">2019 · digital · 31 min</div></div></div>""")

# ---------------------------------------------------------------- 70
page("070-star-chart.html","Northern Sky — Tonight's Star Chart","Spectral",
"""body{font-family:'Spectral',serif;background:#050810;color:#dbe6ff}
.chart{max-width:760px;margin:auto;padding:8vh 22px;text-align:center}
h1{font-size:2.4rem}
.dom{width:min(92vw,520px);aspect-ratio:1;margin:30px auto;border-radius:50%;position:relative;background:radial-gradient(#0a1226,#050810 75%);border:1px solid #22355c;cursor:crosshair}
.star{position:absolute;width:3px;height:3px;background:#fff;border-radius:50%;box-shadow:0 0 6px #fff;transition:.3s}
.star:hover{transform:scale(2.6);box-shadow:0 0 14px #ffd}
.star b{position:absolute;left:8px;top:-4px;font-size:.7rem;color:#ffd93d;opacity:0;transition:.3s;white-space:nowrap;font-weight:400}
.star:hover b{opacity:1}
.constellation{position:absolute;inset:0}
.legend{font-size:.9rem;opacity:.7;line-height:2}""",
"""<div class="chart"><h1>Northern Sky · 22:00 tonight</h1><p style="opacity:.7;font-style:italic">hover the bright ones — they remember their names</p>
<div class="dom" id="d"><svg class="constellation" viewBox="0 0 100 100" preserveAspectRatio="none"><polyline points="22,30 30,22 40,26 46,18 55,24" fill="none" stroke="#3d5a99" stroke-width=".4"/><text x="38" y="14" fill="#5f7db8" font-size="3">Big Dipper ↑ Polaris</text></svg></div>
<div class="legend">★ magnitude ≤2 visible · ☾ moon 61% waxing gibbous · ISS pass 21:47<br>seeing: good · transparency: fair · light pollution: your streetlamp, again</div></div>""",
"""const d=document.getElementById('d');
const named=[['Polaris',50,12],['Vega',74,30],['Deneb',82,52],['Altair',66,66],['Arcturus',26,62],['Aldebaran',34,44],['Sirius',58,82]];
for(let i=0;i<130;i++){const s=document.createElement('div');s.className='star';
s.style.left=Math.sqrt(Math.random())*48+2+'%';s.style.top=Math.sqrt(Math.random())*48+2+'%';
if(i%9===0){s.style.width=s.style.height='5px'}d.appendChild(s)}
named.forEach(([n,x,y])=>{const s=document.createElement('div');s.className='star';s.style.cssText=`left:${x}%;top:${y}%;width:6px;height:6px`;
s.innerHTML=`<b>${n}</b>`;d.appendChild(s)})""")

# ---------------------------------------------------------------- 71
page("071-dinner-party.html","Six for Dinner — Seating Chaos Planner","Shrikhand",
"""body{font-family:'Shrikhand';background:#ffeed6;color:#3d2b1f}
.room{max-width:860px;margin:auto;padding:8vh 22px;text-align:center}
.table{width:min(92vw,560px);height:280px;margin:50px auto;background:#e8b98a;border-radius:160px/120px;position:relative;box-shadow:inset 0 -14px 0 #c98d55,0 24px 50px #00000022}
.guest{position:absolute;width:74px;height:74px;border-radius:50%;background:#fff;border:3px solid #3d2b1f;display:grid;place-items:center;font-size:.62rem;cursor:grab;transition:.2s;box-shadow:0 8px 18px #0002;text-align:center;line-height:1.2;padding:4px}
.guest:hover{transform:scale(1.15) rotate(-4deg);background:#ffd93d}
h1{font-size:clamp(2rem,7vw,3.4rem)}
.shuffle{background:#3d2b1f;color:#ffeed6;border:0;padding:14px 34px;border-radius:99px;font-family:inherit;cursor:pointer;font-size:1rem}
.shuffle:hover{background:#7a4e28}""",
"""<div class="room"><h1>Six for Dinner</h1><p style="font-family:cursive;font-size:1.2rem">drag nobody, hover everyone, seat the feudals apart… good luck</p>
<div class="table" id="t"></div><button class="shuffle" id="sh">⟳ reshuffle the disaster</button></div>""",
"""const G=['Aunt Bea (loud)','Theo (ex)','Priya (new partner)','Dad (grill)','Sam (knows everything)','Mim (homemade wine)','You (host)','Cousin Lin'] ;
const t=document.getElementById('t');
function place(){t.querySelectorAll('.guest').forEach(e=>e.remove());
G.forEach((n,i)=>{const a=i/G.length*Math.PI*2,r=1.0;const el=document.createElement('div');el.className='guest';el.textContent=n;
const cx=50+Math.cos(a)*44,cy=50+Math.sin(a)*38;el.style.left=cx+'%';el.style.top=cy+'%';el.style.margin='-37px';
el.onclick=()=>{el.style.background='#ff6b6b';setTimeout(()=>el.style.background='',500)};t.appendChild(el)})}
place();document.getElementById('sh').onclick=place;""")

# ---------------------------------------------------------------- 72
page("072-darkmode-toggle.html","Lights Out — A Page That Sleeps","Quicksand",
"""body{font-family:'Quicksand';transition:background 1.4s,color 1.4s;background:#fdfbf3;color:#2b2b2b;min-height:100vh;padding:10vh 8vw}
body.night{background:#070b14;color:#c8d3e8}
h1{font-size:clamp(2rem,6vw,3.4rem)}
.switch{position:fixed;top:26px;right:26px;width:86px;height:42px;border-radius:99px;background:#ffd93d;cursor:pointer;transition:.6s;border:0;overflow:hidden}
.knob{position:absolute;top:4px;left:4px;width:34px;height:34px;border-radius:50%;background:#fff;transition:.6s;display:grid;place-items:center;font-size:1.1rem}
body.night .switch{background:#274060}
body.night .knob{left:48px;background:#c8d3e8}
.stars-fade{opacity:0;transition:1.4s}body.night .stars-fade{opacity:1}
p{max-width:560px;line-height:1.9;margin-top:20px}
.scene{margin-top:40px;font-size:3rem;filter:drop-shadow(0 8px 20px #0002)}""",
"""<button class="switch" id="sw" aria-label="toggle lights"><span class="knob" id="kb">☀️</span></button>
<h1>Lights Out</h1><p>This page has a bedtime. Flip the switch and watch the sun clock out, the stars fade in, and your eyes quietly thank you.</p>
<div class="scene" id="sc">🏔️🌞</div>
<p class="stars-fade">✦ ✧ ✦ &nbsp; night mode engaged. crickets loading… 🦗</p>""",
"""const sw=document.getElementById('sw'),kb=document.getElementById('kb'),sc=document.getElementById('sc');
sw.onclick=()=>{document.body.classList.toggle('night');const n=document.body.classList.contains('night');
kb.textContent=n?'🌙':'☀️';sc.textContent=n?'🏔️🌙 ✨':'🏔️🌞'};""")

# ---------------------------------------------------------------- 73
page("073-radio-theatre.html","CBS Parlor — Radio Drama Night","Cabin Sketch",
"""body{font-family:'Cabin Sketch';background:#141009;color:#e8dcc0;text-align:center}
.set{max-width:720px;margin:auto;padding:10vh 24px}
h1{font-size:clamp(2.4rem,8vw,4rem);color:#f5c542}
.oldradio{width:220px;height:150px;margin:30px auto;background:#3a2a18;border-radius:70px 70px 14px 14px;border:4px solid #6b4a2a;position:relative;box-shadow:0 16px 40px #000a}
.oldradio::before{content:'';position:absolute;inset:18px 60px 40px;border-radius:50%;background:repeating-radial-gradient(#241a0e 0 3px,#4a3420 3px 6px)}
.oldradio::after{content:'◉';position:absolute;bottom:12px;right:22px;color:#f5c542}
.sfx{font-size:1.6rem;color:#c0392b;letter-spacing:.2em;animation:wob 2s infinite}
@keyframes wob{50%{transform:skewX(-4deg)}}
.script{max-width:560px;margin:30px auto;text-align:left;font-size:1.15rem;line-height:2}
.script .who{color:#f5c542}""",
"""<div class="set"><h1>CBS PARLOR</h1><p>thursday nights · drama read live by people whose microphones predate drama</p>
<div class="oldradio"></div><div class="sfx">♪ theme sting ♪</div>
<div class="script"><span class="who">NARRATOR:</span> The warehouse smelled of rust and bad decisions.<br>
<span class="who">VELMA:</span> "You said the door would be unlocked."<br>
<span class="who">[SFX]:</span> *thunder, closer than promised*<br>
<span class="who">VELMA:</span> "…you also said 'warehouse.'"</div>
<p style="opacity:.6">next week: “The Lighthouse That Filed Taxes.” Don't miss it. It won't.</p></div>""")

# ---------------------------------------------------------------- 74
page("074-pixel-art-studio.html","Pixel Press — Draw With Your Mouse","DotGothic16",
"""body{font-family:'DotGothic16';background:#1c1f26;color:#eee;text-align:center;padding:6vh 4vw}
h1{font-size:1.6rem;letter-spacing:.2em}
.grid{display:grid;grid-template-columns:repeat(16,1fr);gap:1px;background:#333;padding:4px;width:min(92vw,480px);margin:24px auto;border-radius:6px}
.px{aspect-ratio:1;background:#11141a;cursor:pointer;transition:.1s}
.px:hover{outline:1px solid #fff;z-index:2}
.palette{display:flex;gap:10px;justify-content:center;margin:14px;flex-wrap:wrap}
.col{width:34px;height:34px;border-radius:6px;cursor:pointer;border:3px solid transparent}
.col.on{border-color:#fff;transform:scale(1.15)}
button{background:#444;color:#fff;border:0;padding:8px 20px;font-family:inherit;cursor:pointer;border-radius:6px;margin-top:8px}""",
"""<h1>PIXEL PRESS</h1><p style="opacity:.6">pick ink, drag across canvas · 16×16, no pressure, no mistakes</p>
<div class="palette" id="pal"></div><div class="grid" id="g"></div><button id="clr">🗑 clear</button>""",
"""const cols=['#ff595e','#ffca3a','#8ac926','#1982c4','#6a4c93','#ffffff','#ff9f1c','#06d6a0'];
let cur='#ffca3a';const pal=document.getElementById('pal');
cols.forEach((c,i)=>{const d=document.createElement('div');d.className='col'+(i===1?' on':'');d.style.background=c;
d.onclick=()=>{cur=c;document.querySelectorAll('.col').forEach(x=>x.classList.remove('on'));d.classList.add('on')};pal.appendChild(d)});
const g=document.getElementById('g');let down=false;
addEventListener('mouseup',()=>down=false);
for(let i=0;i<256;i++){const p=document.createElement('div');p.className='px';
const paint=()=>p.style.background=cur;p.onmousedown=e=>{down=true;paint()};p.onmouseenter=()=>{if(down)paint()};
p.ontouchstart=e=>{e.preventDefault();paint()};g.appendChild(p)}
document.getElementById('clr').onclick=()=>document.querySelectorAll('.px').forEach(p=>p.style.background='')""")

# ---------------------------------------------------------------- 75
page("075-observatory.html","Dome 7 — An Observatory Newsletter","IBM Plex Mono",
"""body{font-family:'IBM Plex Mono',monospace;background:#060913;color:#b7c5e0}
.log{max-width:720px;margin:auto;padding:9vh 24px}
h1{color:#eaf2ff;font-size:1.6rem;letter-spacing:.2em}
.entry{border-left:3px solid #233a63;padding:16px 22px;margin:26px 0;background:#0a0f1d;transition:.3s}
.entry:hover{border-color:#7fb4ff;background:#0d1426}
.stamp{color:#7fb4ff;font-size:.8rem}
.sig{color:#3fb950}.noise{color:#d29922}
footer{margin-top:60px;opacity:.5;font-size:.8rem}""",
"""<div class="log"><h1>◉ DOME 7 · NIGHT LOG</h1><p style="opacity:.6">automated dispatches from a telescope with strong opinions</p>
<div class="entry"><span class="stamp">2026-10-27 23:14 UTC</span><br>Tracking <b>NGC 7000</b>. Seeing excellent, dome smells of cold metal and coffee. Wall of America glows like a neon sign for gas that died 5,000 years ago.
</div>
<div class="entry"><span class="stamp">01:02 UTC</span><br><span class="sig">SIGNAL:</span> hydrogen line spike, 1420.4 MHz, 11 seconds. Probably satellite. Probably. Logged anyway; "probably" deserves witnesses.</div>
<div class="entry"><span class="stamp">02:47 UTC</span><br><span class="noise">NOISE:</span> mount stepper motor complaining about bearing 3. Re-greased Tuesday; it holds grudges like an astronomer.</div>
<div class="entry"><span class="stamp">04:30 UTC</span><br>Dawn protocol. Dome slit closing like an eyelid. One last exposure of M31 — our neighbour, still not answering. Good night from 51°N.</div>
<footer>reply with your own sky observations · stamp collection now accepting claims</footer></div>""")

# ---------------------------------------------------------------- 76
page("076-carnival.html","Le Carnival des Ombres","Alfa Slab One",
"""body{font-family:'Alfa Slab One',serif;background:#16060f;color:#ffe6f0;overflow-x:hidden}
.big{background:repeating-conic-gradient(from 0deg,#b3123f 0 12deg,#7a0c2c 12deg 24deg);height:100vh;display:grid;place-items:center;position:relative}
.big::after{content:'';position:absolute;inset:0;background:radial-gradient(circle,transparent 30%,#16060fee 75%)}
h1{font-size:clamp(2.6rem,10vw,6rem);color:#ffd166;transform:rotate(-4deg);text-shadow:4px 4px #b3123f;z-index:2}
.tents{display:flex;gap:26px;justify-content:center;flex-wrap:wrap;padding:8vh 6vw}
.tent{width:230px;background:#2a0d1c;border:2px solid #ffd16644;padding-bottom:24px;transition:.3s;cursor:pointer;clip-path:polygon(0 18%,50% 0,100% 18%,100% 100%,0 100%)}
.tent:hover{transform:translateY(-10px) rotate(-1deg);border-color:#ffd166}
.tent .glyph{font-size:3rem;padding-top:34px}
.tent h3{color:#ffd166;margin:10px 0 4px}
.tent p{font-family:Georgia;padding:0 18px;font-size:.9rem;line-height:1.6}
.mask{position:fixed;font-size:2rem;opacity:.14;animation:float 12s ease-in-out infinite alternate}
@keyframes float{to{transform:translateY(-40px) rotate(20deg)}}""",
"""<div class="big"><h1>CARNIVAL OF SHADOWS</h1></div>
<div class="tents">
<div class="tent"><div class="glyph">🎭</div><h3>Theory Booth</h3><p>Trade one secret for one fortune. Inflation ongoing.</p></div>
<div class="tent"><div class="glyph">🎠</div><h3>Carousel Backwards</h3><p>Horses go counter-clockwise, regrets clockwise.</p></div>
<div class="tent"><div class="glyph">🔮</div><h3>Mirror Maze</h3><p>Meet eleven versions of you. Only two pay.</p></div>
<div class="tent"><div class="glyph">🎪</div><h3>Midnight Parade</h3><p>Lanterns, tubas, one very serious llama. 00:00 sharp.</p></div></div>""",
"""const emo=['🎭','🃏','🪅','🎪'];for(let i=0;i<10;i++){const m=document.createElement('div');m.className='mask';m.textContent=emo[i%4];
m.style.left=Math.random()*95+'vw';m.style.top=Math.random()*95+'vh';m.style.animationDelay=(-Math.random()*10)+'s';document.body.appendChild(m)}""")

# ---------------------------------------------------------------- 77
page("077-readinglist.html","Shelf Life — Books Read & Regretted","Karla",
"""body{font-family:'Karla';background:#0f1115;color:#e7e3da}
.shelf{max-width:800px;margin:auto;padding:9vh 24px}
h1{font-size:2.4rem}
.spine{display:flex;align-items:center;gap:18px;margin:16px 0;padding:14px 18px;border-radius:8px;cursor:pointer;transition:.25s;border:1px solid transparent}
.spine:hover{border-color:#e7e3da33;transform:translateX(8px)}
.book{width:16px;height:64px;border-radius:3px;box-shadow:inset -3px 0 0 #0003}
.info{flex:1}.info b{font-size:1.1rem}.info small{display:block;opacity:.6}
.rate{font-size:1.1rem;letter-spacing:2px;color:#ffb703}
.status{font-size:.75rem;padding:4px 12px;border-radius:99px;border:1px solid #555}
.done{color:#8ecf81}.mid{color:#ffb703}.dnf{color:#ff6b6b}""",
"""<div class="shelf"><h1>Shelf Life</h1><p style="opacity:.6;margin-bottom:30px">what I read, half-read, and heroically abandoned</p>
<div class="spine"><div class="book" style="background:#264653"></div><div class="info"><b>Piranesi</b><small>Susanne Clarke</small></div><div class="rate">★★★★★</div><span class="status done">finished, changed</span></div>
<div class="spine"><div class="book" style="background:#e76f51"></div><div class="info"><b>The Secret History</b><small>Donna Tartt</small></div><div class="rate">★★★★☆</div><span class="status done">murderers, riveting</span></div>
<div class="spine"><div class="book" style="background:#2a9d8f"></div><div class="info"><b>Infinite Jest</b><small>DFW</small></div><div class="rate">★★☆☆☆</div><span class="status mid">pg 412, footnotes winning</span></div>
<div class="spine"><div class="book" style="background:#9b5de5"></div><div class="info"><b>Pride & Prejudice</b><small>Austen</small></div><div class="rate">★★★★★</div><span class="status done">Darcy apologist now</span></div>
<div class="spine"><div class="book" style="background:#f4a261"></div><div class="info"><b>Pale Fire</b><small>Nabokov</small></div><div class="rate">—</div><span class="status dnf">DNF · poem better than plot?</span></div></div>""")

# ---------------------------------------------------------------- 78
page("078-sound-of-city.html","The Sound of Cities — Ambient Map","Rubik",
"""body{font-family:'Rubik';background:#0b0f14;color:#e8eef2}
.hd{padding:9vh 8vw 4vh}h1{font-size:clamp(2rem,6vw,3.2rem)}
.city{display:grid;place-items:center;padding:26px;margin:14px 8vw;border-radius:16px;cursor:pointer;transition:.3s;position:relative;overflow:hidden}
.city:hover{transform:scale(1.015)}
.city b{font-size:1.6rem;position:relative;z-index:2;text-align:center}
.city small{position:relative;z-index:2;opacity:.85}
.tokyo{background:linear-gradient(135deg,#bc00dd,#390099)}.rio{background:linear-gradient(135deg,#f77f00,#d62828)}
.oslo{background:linear-gradient(135deg,#2193b0,#6dd5ed)}.lagos{background:linear-gradient(135deg,#ee9ca7,#bd0026)}
.bars{display:flex;gap:4px;align-items:flex-end;height:34px;margin-top:12px;position:relative;z-index:2}
.bars i{width:6px;background:#ffffffbb;animation:eq .7s infinite alternate ease-in-out;border-radius:2px}
@keyframes eq{to{height:100%!important}}
.now{margin:0 8vw 8vh;font-family:monospace;color:#7fd1ae}""",
"""<div class="hd"><h1>The Sound of Cities</h1><p style="opacity:.7">tap a city to listen to its mix — headphones recommended, empathy required</p></div>
<div class="city tokyo"><b>東京 · Tokyo Shibuya 07:40</b><small>crossing hum × train chimes × vending machine jingle</small><div class="bars" data-n="12"></div></div>
<div class="city rio"><b>Rio · Copacabana 16:00</b><small>drums under surf under frisbee under argument</small><div class="bars" data-n="16"></div></div>
<div class="city oslo"><b>Oslo · Grünerløkka 22:00</b><small>snow on tram wires, one bicycle, distant hygge</small><div class="bars" data-n="8"></div></div>
<div class="city lagos"><b>Lagos · Balwa Market 12:00</b><small>danfo horns, generator choir, laughter at full volume</small><div class="bars" data-n="20"></div></div>
<div class="now" id="now">▶ nothing playing — pick a city</div>""",
"""document.querySelectorAll('.bars').forEach(b=>{for(let i=0;i<+b.dataset.n;i++){const x=document.createElement('i');x.style.height=(20+Math.random()*60)+'%';b.appendChild(x)}});
const mixes={'tokyo':'🎧 train melody (official but soulful)… crossing white noise… a robot saying please mind the gap','rio':'🥁 surdo at 92bpm blended with waves, gulls negotiating ownership','oslo':'❄️ almost silence, then a single tram bell, extremely polite','lagos':'📢 horns in clusters, generator bassline, someone selling something brilliantly'};
document.querySelectorAll('.city').forEach(c=>c.onclick=()=>{document.getElementById('now').textContent=c.querySelector('b').textContent.split('·')[0]+' — '+mixes[c.classList[1]]})""")

# ---------------------------------------------------------------- 79
page("079-botanical-print.html","Plate XI — Ferns, Engraved","Libre Caslon Text",
"""body{font-family:'Libre Caslon Text',serif;background:#f2ead8;color:#2e2a20}
.plate{max-width:680px;margin:8vh auto;background:#faf4e4;border:1px solid #d8caa8;padding:56px 48px;box-shadow:0 20px 60px #00000012}
h1{font-size:1.6rem;text-align:center;letter-spacing:.3em;text-transform:uppercase}
.fig{text-align:center;font-size:9rem;line-height:1;margin:30px 0;filter:sepia(1) contrast(1.1);transition:transform 1s}
.fig:hover{transform:rotate(6deg) scale(1.1)}
.desc{columns:2;gap:30px;font-size:1rem;line-height:1.9;margin-top:20px}
.desc h2{column-span:all;font-size:1.2rem;font-style:italic;font-weight:400;margin-bottom:10px}
.roman{display:block;text-align:center;margin-top:30px;font-size:.85rem;letter-spacing:.2em;color:#8a7c58}""",
"""<div class="plate"><h1>Plate XI</h1>
<div class="fig">🌿</div>
<div class="desc"><h2>Polystichum setiferum — Soft Shield Fern</h2>
<p>In the damp hollows behind the mill, the soft shield fern unfurls its fronds like letters no one rushed to send. Each pinna finely serrated; each crozier coiled with the patience of a question.</p>
<p>Collectors prize it, deer ignore it, poets exaggerate it. Spores mature by August; dispersal occurs entirely on the whims of air.</p></div>
<span class="roman"> drawn from life · engraved by hand · printed on rag paper </span></div>""")

# ---------------------------------------------------------------- 80
page("080-game-of-life.html","Cellular Automata — Conway's Garden","Ubuntu Mono",
"""body{font-family:'Ubuntu Mono',monospace;background:#05070a;color:#8be25a;text-align:center}
.hd{padding:6vh 4vw 2vh}h1{font-size:1.6rem}
canvas{border:1px solid #1c2a1c;cursor:crosshair;image-rendering:pixelated;max-width:94vw}
.row{display:flex;gap:12px;justify-content:center;margin:16px;flex-wrap:wrap}
button{background:#0b120b;color:#8be25a;border:1px solid #2c4a2c;padding:8px 18px;font-family:inherit;cursor:pointer}
button:hover{background:#142214}
.stat{font-size:.85rem;opacity:.7}""",
"""<div class="hd"><h1>CONWAY'S GAME OF LIFE</h1><p class="stat">rules: 3 neighbours → born · 2–3 → survive · else die. draw cells while paused.</p></div>
<div class="row"><button id="play">▶ run</button><button id="rnd">🎲 randomize</button><button id="gld">🪐 glider gun</button><button id="clr">✕ clear</button></div>
<canvas id="c" width="640" height="400"></canvas>
<p class="stat" id="gen">generation 0 · population 0</p>""",
"""const c=document.getElementById('c'),x=c.getContext('2d'),S=10,W=64,h=40;
let g=Array.from({length:h},()=>Array(W).fill(0)),run=false,n=0;
function draw(){x.fillStyle='#05070a';x.fillRect(0,0,640,400);x.fillStyle='#8be25a';let p=0;
for(let y=0;y<h;y++)for(let xx=0;xx<W;xx++)if(g[y][xx]){x.fillRect(xx*S+1,y*S+1,S-2,S-2);p++}
gen.textContent=`generation ${n} · population ${p}`}
function step(){const ng=Array.from({length:h},()=>Array(W).fill(0));
for(let y=0;y<h;y++)for(let xx=0;xx<W;xx++){let a=0;
for(let dy=-1;dy<=1;dy++)for(let dx=-1;dx<=1;dx++){if(dx||dy)a+=g[(y+dy+h)%h][(xx+dx+W)%W]}
ng[y][xx]=a===3||a===2&&g[y][xx]?1:0}g=ng;n++}
function loop(){if(run){step();draw()}requestAnimationFrame(loop)}loop();
play.onclick=()=>{run=!run;play.textContent=run?'⏸ pause':'▶ run'};
rnd.onclick=()=>{for(let y=0;y<h;y++)for(let xx=0;xx<W;xx++)g[y][xx]=Math.random()<.28?1:0;draw()};
clr.onclick=()=>{g=g.map(r=>r.fill(0));n=0;draw()};
gld.onclick=()=>{g=g.map(r=>r.fill(0));const cells=[[1,5],[1,6],[1,7],[2,5],[2,6],[2,7],[3,4],[3,8],[4,4],[4,8],[5,3],[5,9],[6,2],[6,10],[7,2],[7,10],[8,2],[8,10],[9,3],[9,9],[10,4],[10,8],[11,5],[11,6],[11,7],[12,5],[12,6],[12,7],[13,4],[13,8],[14,4],[14,8],[15,3],[15,9],[16,2],[16,10],[17,2],[17,10],[18,2],[18,10],[19,3],[19,9],[20,4],[20,8],[21,5],[21,6],[21,7],[22,5],[22,6],[22,7]];
cells.forEach(([yy,xx])=>g[yy][xx]=1);n=0;draw()};
let dr=false;c.onmousedown=e=>{dr=true;paint(e)};onmouseup=()=>dr=false;
c.onmousemove=e=>{if(dr)paint(e)};
function paint(e){const r=c.getBoundingClientRect();const px=((e.clientX-r.left)/r.width*W)|0,py=((e.clientY-r.top)/r.height*h)|0;
if(g[py])g[py][px]^=1;draw()}draw();""")

# ---------------------------------------------------------------- 81
page("081-sourdough.html","The Levain Log — Bread Diary","Bodoni Moda",
"""body{font-family:'Bodoni Moda',serif;background:#efe6d5;color:#33291c}
.log{max-width:680px;margin:auto;padding:10vh 24px}
h1{font-size:clamp(2.4rem,8vw,3.8rem);text-align:center}
.week{display:grid;grid-template-columns:120px 1fr;gap:24px;margin:36px 0;padding-bottom:30px;border-bottom:1px solid #33291c33}
.temp{font-size:2.6rem;text-align:center;color:#a05c2a;font-variant-numeric:tabular-nums}
.week h2{font-size:1.3rem}.obs{font-family:Georgia,serif;font-weight:400;line-height:1.8;opacity:.85}
.tagline{text-align:center;font-style:italic;opacity:.6;margin-bottom:40px}
.crumb{display:flex;justify-content:center;gap:14px;font-size:2rem;margin-top:40px}""",
"""<div class="log"><h1>The Levain Log</h1><p class="tagline">batch journal of a kitchen learning patience from yeast</p>
<div class="week"><div class="temp">78°</div><div><h2>Week 12 — “The Comeback”</h2><p class="obs">Starter doubled in four hours, aggressive, joyful. Bulk went long (my phone, my fault). Crust sang during cooling — literally, crackling like tiny applause. Ear opened perfectly. Not bragging. Bragging slightly.</p></div></div>
<div class="week"><div class="temp">71°</div><div><h2>Week 11 — “Cold Proof, Cold Heart”</h2><p class="obs">Fridge at 4°C, dough unimpressed, proofed like it owed money somewhere. Dense crumb. Tasted of lesson learned: the fridge is a pause button, not a friend.</p></div></div>
<div class="week"><div class="temp">80°</div><div><h2>Week 10 — “Overproof Autopsy”</h2><p class="obs">Left it ninety minutes too long. Slack, blobby, dignified no more. Baked anyway; ate anyway; forgiveness is a flatbread.</p></div></div>
<div class="crumb">🍞 🥖 🫓 🥐</div></div>""")

# ---------------------------------------------------------------- 82
page("082-neon-sign-maker.html","Sign Spinner — Make Your Neon","Pacifico",
"""body{font-family:'Pacifico';background:#0b0b0b;color:#fff;text-align:center;padding:10vh 5vw}
.sign{display:inline-block;border:6px solid #333;border-radius:18px;padding:40px 60px;background:#101010;margin:30px auto;box-shadow:0 0 40px #00000088,inset 0 0 30px #000}
.txt{font-size:clamp(2rem,8vw,4.4rem);color:var(--nc,#0ff);text-shadow:0 0 8px var(--nc,#0ff),0 0 30px var(--nc,#0ff),0 0 60px var(--nc,#0ff);animation:flick 5s infinite;outline:none}
@keyframes flick{0%,92%,94%,100%{opacity:1}93%{opacity:.4}96%{opacity:.75}}
input[type=text]{background:#1a1a1a;border:1px solid #333;color:#fff;padding:12px 18px;font-family:'Pacifico';font-size:1.2rem;border-radius:8px;width:min(90vw,360px);text-align:center}
.colors{display:flex;gap:14px;justify-content:center;margin-top:20px}
.dot{width:30px;height:30px;border-radius:50%;cursor:pointer;border:2px solid #444;transition:.2s}
.dot:hover{transform:scale(1.25)}
label{font-family:sans-serif;font-size:.8rem;color:#888;letter-spacing:.2em;text-transform:uppercase}""",
"""<h1 style="font-size:2.6rem">Sign Spinner</h1><label>type your sign</label><br><input id="inp" value="Open Late" maxlength="18"><br>
<div class="sign"><div class="txt" id="t">Open Late</div></div><br><label>choose gas tube colour</label>
<div class="colors"><div class="dot" style="background:#0ff" data-c="#0ff"></div><div class="dot" style="background:#f0f" data-c="#f0f"></div>
<div class="dot" style="background:#ff0" data-c="#ff0"></div><div class="dot" style="background:#0f0" data-c="#0f0"></div><div class="dot" style="background:#f60" data-c="#f60"></div></div>""",
"""const inp=document.getElementById('inp'),t=document.getElementById('t');
inp.oninput=()=>t.textContent=inp.value||'…';
document.querySelectorAll('.dot').forEach(d=>d.onclick=()=>t.style.setProperty('--nc',d.dataset.c));""")

# ---------------------------------------------------------------- 83
page("083-field-museum.html","Field Museum of Small Things","Asap",
"""body{font-family:'Asap';background:#f4f4f0;color:#22242a}
.case{max-width:860px;margin:auto;padding:9vh 24px}
h1{font-size:clamp(2rem,6vw,3.2rem);font-weight:800}
.specimens{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:18px;margin-top:40px}
.sp{background:#fff;border:1px solid #dcdcd2;border-radius:10px;padding:22px;transition:.3s;cursor:zoom-in;position:relative}
.sp:hover{box-shadow:0 16px 40px #00000014;transform:translateY(-6px)}
.sp .art{font-size:2.6rem}
.sp b{display:block;margin-top:10px}
.sp small{color:#7a7d88;line-height:1.5;display:block;margin-top:6px}
.pin{position:absolute;top:10px;right:10px;width:10px;height:10px;border-radius:50%;background:#e63946;box-shadow:0 2px 4px #0004}
.acc{font-family:monospace;font-size:.7rem;color:#aab}""",
"""<div class="case"><h1>Field Museum of Small Things</h1><p style="color:#666">permanent collection · admission: one interesting glance</p>
<div class="specimens">
<div class="sp"><span class="pin"></span><div class="art">🔑</div><b>Key To Unknown Door</b><small>Brass, worn cheerful by use. Teeth pattern suggests optimism.</small><span class="acc">ACC.1987.04</span></div>
<div class="sp"><span class="pin"></span><div class="art">🪨</div><b>Pocket River Stone</b><small>Perfectly held-shaped. Collected twice, returned once, kept eventually.</small><span class="acc">ACC.2003.11</span></div>
<div class="sp"><span class="pin"></span><div class="art">🧵</div><b>Thread, Still Tied</b><small>Ends unknown, knot intact. Possibly holding something together spiritually.</small><span class="acc">ACC.1999.01</span></div>
<div class="sp"><span class="pin"></span><div class="art">🎞️</div><b>Frame Without Film</b><small>One strip of vacation, unnumbered. Sea suspected; faces cropped.</small><span class="acc">ACC.1974.30</span></div>
<div class="sp"><span class="pin"></span><div class="art">🍂</div><b>Leaf Caught Mid-Fall</b><small>Acquired at waist height on October 12. Maple. Zero regrets observed.</small><span class="acc">ACC.2021.10</span></div>
<div class="sp"><span class="pin"></span><div class="art">📻</div><b>Radio Stuck On One Station</b><small>Receives only Thursday mornings. Plays kettle sounds. Popular exhibit.</small><span class="acc">ACC.1968.02</span></div></div></div>""")

# ---------------------------------------------------------------- 84
page("084-nightbus.html","Night Bus 27 — Window Seat","Work Sans",
"""body{font-family:'Work Sans';background:#0a0d12;color:#dfe6ee}
.bus{max-width:760px;margin:auto;padding:8vh 22px}
.window{height:300px;border-radius:14px;position:relative;overflow:hidden;background:linear-gradient(#0d1420,#0a0d12);border:6px solid #1c2430;margin:30px 0}
.streetlight{position:absolute;width:60px;height:60px;border-radius:50%;background:radial-gradient(#ffd93d88,transparent 70%);animation:pass 3s linear infinite}
@keyframes pass{from{transform:translateX(800px)}to{transform:translateX(-120px)}}
.rain-line{position:absolute;width:1px;height:26px;background:#ffffff22;animation:fall .5s linear infinite}
@keyframes fall{to{transform:translateY(320px)}}
.stop{display:flex;gap:18px;padding:16px 0;border-bottom:1px dashed #2a3442;align-items:center}
.time{font-family:monospace;color:#7fd1ae;width:64px}
.next{color:#ffd93d}
h1{font-size:2.2rem}h1 span{background:#ffd93d;color:#111;padding:2px 12px;border-radius:6px;font-size:1.4rem}""",
"""<div class="bus"><h1>Night Bus <span>27</span></h1><p style="opacity:.7">23:41 · heading east · driver knows shortcuts, refuses to explain them</p>
<div class="window" id="win"></div>
<div class="stop next"><span class="time">23:52</span><b>Alder Street</b><small style="opacity:.6">one passenger boards carrying a cake box, no occasion disclosed</small></div>
<div class="stop"><span class="time">00:06</span>Ferry Terminal<small style="opacity:.6">closed, lit, philosophical</small></div>
<div class="stop"><span class="time">00:19</span>Museum Gate<small style="opacity:.6">the lions are definitely judging</small></div>
<div class="stop"><span class="time">00:33</span>Terminus — East Depot<small style="opacity:.6">last stop. decide if that's sad or free</small></div></div>""",
"""const w=document.getElementById('win');
for(let i=0;i<4;i++){const l=document.createElement('div');l.className='streetlight';l.style.top=(30+i*55)+'px';l.style.animationDelay=(i*.8)+'s';w.appendChild(l)}
for(let i=0;i<40;i++){const r=document.createElement('div');r.className='rain-line';r.style.left=Math.random()*100+'%';r.style.top=-30+'px';r.style.animationDelay=Math.random()*.5+'s';w.appendChild(r)}""")

# ---------------------------------------------------------------- 85
page("085-type-specimen.html","Grotesque Nº 12 — Type Specimen","Archivo",
"""body{font-family:'Archivo',sans-serif;background:#ece9df;color:#111;padding-bottom:12vh}
.sheet{max-width:820px;margin:auto;padding:8vh 26px}
.waterfall p{font-size:clamp(1rem,4vw,2.6rem);line-height:1.5;border-bottom:1px solid #0001;padding:10px 0;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.weights{display:flex;gap:30px;flex-wrap:wrap;margin:40px 0;font-size:2rem}
.w1{font-weight:100}.w3{font-weight:300}.w5{font-weight:500}.w7{font-weight:700}.w9{font-weight:900}
.chars{font-size:2rem;letter-spacing:.1em;line-height:1.6;word-break:break-all;border:2px solid #111;padding:20px;margin:30px 0}
h1{font-size:clamp(3rem,10vw,6rem);font-weight:900;letter-spacing:-.04em}
.meta{font-size:.8rem;letter-spacing:.2em;text-transform:uppercase;color:#777}""",
"""<div class="sheet"><div class="meta">specimen sheet · grotesque nº 12 · 1962 revival</div>
<h1>Handgloves</h1>
<div class="weights"><span class="w1">Thin</span><span class="w3">Light</span><span class="w5">Regular</span><span class="w7">Bold</span><span class="w9">Black</span></div>
<div class="chars">ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz 0123456789 &amp;?!@#$%*()[]{}&lt;&gt;</div>
<div class="waterfall">
<p>The quick brown fox jumps over the lazy dog — 09</p><p style="font-size:2rem">The quick brown fox jumps — 16</p>
<p style="font-size:1.6rem">The quick brown fox — 24</p><p style="font-size:1.3rem">The quick brown — 36</p>
<p style="font-size:1.1rem;letter-spacing:.3em">SPACED CAPS FOR MUSEUMS — 48</p></div>
<p class="meta" style="margin-top:40px">cut by H. Grotesk · licensed freely · use it loudly</p></div>""")

# ---------------------------------------------------------------- 86
page("086-compost.html","Worm Bin Weekly — Compost Report","Nunito Sans",
"""body{font-family:'Nunito Sans';background:#1d2618;color:#e4efd8}
.bin{max-width:700px;margin:auto;padding:9vh 22px}
h1{font-size:2.2rem;color:#b7d98f}
.layer{border-radius:12px;padding:20px 26px;margin:12px 0;display:flex;justify-content:space-between;align-items:center;transition:.3s;cursor:default}
.layer:hover{transform:scale(1.02)}
.l1{background:#3a2f1e}.l2{background:#4a5d23}.l3{background:#2d3a1a}.l4{background:#5c4a2e}
.temp{font-size:1.6rem;font-weight:800;color:#e8c547}
.news{margin-top:34px;line-height:1.9;font-size:1.05rem}
.news b{color:#b7d98f}
.stats{display:flex;gap:26px;margin-top:26px;flex-wrap:wrap}
.st{background:#243020;padding:16px 22px;border-radius:10px;text-align:center}
.st b{font-size:1.6rem;display:block;color:#e8c547}""",
"""<div class="bin"><h1>🪱 Worm Bin Weekly</h1><p style="opacity:.7">issue 34 · reported honestly by the bin itself</p>
<div class="layer l1"><span>Top — newspaper hats, melon rind</span><span class="temp">☀︎ warm</span></div>
<div class="layer l2"><span>Middle — active munching zone (coffee grounds)</span><span class="temp">38°C</span></div>
<div class="layer l3"><span>Deep — dark & humid, casting occurring</span><span class="temp">31°C</span></div>
<div class="layer l4"><span>Base — finished black gold, ready for tomatoes</span><span class="temp">ambient</span></div>
<div class="news"><b>Bin news:</b> Citrus overload on Tuesday caused diplomatic incident with colony leadership. Resolved with extra cardboard and an apology written in frass. Avocado pit accepted after 3 weeks of negotiation. Melon season: thriving.</div>
<div class="stats"><div class="st"><b>1,240</b>worms counted (approx.)</div><div class="st"><b>6.2 kg</b>diverted this month</div><div class="st"><b>0</b>fruit fly victories claimed</div></div></div>""")

# ---------------------------------------------------------------- 87
page("087-time-capsule.html","Capsule Nº 8 — Open In 2046","Courier Prime",
"""body{font-family:'Courier Prime',monospace;background:#111;color:#d9d2b8;text-align:center;padding:8vh 4vw}
.metal{width:min(92vw,560px);margin:auto;background:linear-gradient(#3a3f45,#23272b);border:3px solid #566;padding:44px;border-radius:8px;box-shadow:0 30px 80px #000a,inset 0 2px 0 #ffffff22}
h1{letter-spacing:.3em;font-size:1.4rem;color:#9db4c4}
.items{text-align:left;margin:30px 0;line-height:2.2;font-size:.95rem}
.items li{list-style:none}
.seal{border:2px dashed #9db4c4;display:inline-block;padding:14px 26px;margin-top:20px;letter-spacing:.2em;cursor:pointer;transition:.4s}
.seal:hover{background:#9db4c4;color:#111}
.counter{margin-top:26px;font-size:.85rem;color:#e8c547}""",
"""<div class="metal"><h1>TIME CAPSULE Nº 8</h1><p>SEALED 2026-10-28 · TO BE OPENED 2046-10-28</p>
<ul class="items"><li>▸ one smartphone, dead, as ritual object</li><li>▸ printout of "most popular song," disputed</li><li>▸ sourdough starter (desiccated), label: "Feed me first"</li><li>▸ letter to future self, mostly apologies about posture</li><li>▸ USB drive containing 4,000 photos of other people's lunches</li><li>▸ question: do you still say "that's crazy" unironically?</li></ul>
<div class="seal" id="seal">✕ DO NOT OPEN ✕</div>
<div class="counter" id="cnt"></div></div>""",
"""const target=new Date('2046-10-28');
setInterval(()=>{const ms=target-new Date();document.getElementById('cnt').textContent=
`${(ms/864e5|0).toLocaleString()} days, ${(ms/36e5%24)|0} hrs until history reads this`},1000);
document.getElementById('seal').onclick=function(){this.textContent='…temptation noted. seal remains.';this.style.borderColor='#e8c547'};""")

# ---------------------------------------------------------------- 88
page("088-aurora.html","Chasing Aurora — Live-ish Forecast","Exo 2",
"""body{font-family:'Exo 2';background:#01040a;color:#dff6ff;min-height:100vh;overflow-x:hidden}
.sky{position:fixed;inset:0;z-index:-1;background:linear-gradient(#01040a,#020a18)}
.band{position:fixed;top:-10vh;left:-20vw;width:140vw;height:60vh;filter:blur(50px);opacity:.5;
background:linear-gradient(100deg,transparent,#2bff8844 20%,#00d4ff55 45%,#b026ff44 70%,transparent);
animation:wave 12s ease-in-out infinite alternate;transform-origin:center}
@keyframes wave{to{transform:skewY(8deg) translateX(6%) scaleY(1.2)}}
.content{max-width:720px;margin:auto;padding:26vh 24px 12vh;position:relative}
h1{font-size:clamp(2.4rem,8vw,4rem);letter-spacing:.05em}
.kp{display:flex;gap:10px;align-items:center;margin:30px 0}
.kp b{font-size:3rem;color:#2bff88}
.odds{height:14px;flex:1;background:#0a1420;border-radius:8px;overflow:hidden}
.odds i{display:block;height:100%;width:0;background:linear-gradient(90deg,#2bff88,#00d4ff);transition:2s}
.tips{line-height:2;opacity:.85}""",
"""<div class="sky"></div><div class="band"></div><div class="band" style="animation-delay:-6s;opacity:.35;top:5vh"></div>
<div class="content"><h1>Chasing Aurora</h1><p style="opacity:.7">Tromsø station · Kp index climbing, clouds behaving</p>
<div class="kp"><b>Kp 5.7</b><div class="odds"><i id="o"></i></div><span>82% chance overhead</span></div>
<div class="tips">▸ best window: 22:40 – 01:15<br>▸ camera: 15s exposures, ISO 800, steady hands or rocks<br>▸ dress: wool, anger, thermos of soup<br>▸ if it starts green then purple, do not scream at your companion — it's rude</div></div>""",
"""setTimeout(()=>document.getElementById('o').style.width='82%',400);""")

# ---------------------------------------------------------------- 89
page("089-board-manifesto.html","Manifesto of the Small Table","Spline Sans",
"""body{font-family:'Spline Sans';background:#f2efe9;color:#1c1c1c;line-height:1.9}
.pamph{max-width:640px;margin:auto;padding:12vh 26px}
h1{font-size:2.4rem;font-weight:800;letter-spacing:-.02em}
.rule{height:4px;width:60px;background:#e63946;margin:20px 0 40px}
ol{padding-left:22px}
ol li{margin:22px 0;font-size:1.1rem}
ol li b{display:block;font-size:.8rem;letter-spacing:.25em;color:#e63946;text-transform:uppercase}
.pull{font-size:1.6rem;font-weight:700;margin:50px 0;padding-left:26px;border-left:4px solid #1c1c1c}
.sig{font-size:.85rem;opacity:.6}""",
"""<div class="pamph"><h1>Manifesto of the Small Table</h1><div class="rule"></div>
<ol><li><b>Article I</b>Every gathering deserves a table too small for its ambitions.</li>
<li><b>Article II</b>Candles are mandatory; competence is optional. Wax in the pasta is seasoning.</li>
<li><b>Article III</b>No phones above the bread plate. The bread plate is sacred.</li>
<li><b>Article IV</b>Someone must cook, someone must wash, one person may dramatically peel garlic and call it contribution.</li>
<li><b>Article V</b>Dessert happens regardless of dinner quality. Solidarity sugar.</li></ol>
<div class="pull">“We do not gather to be impressive. We gather because impressive people eat alone and own nice dishes nobody sees.”</div>
<p class="sig">ratified unanimously by six friends, one partner's colleague, and a cat with veto power.</p></div>""")

# ---------------------------------------------------------------- 90
page("090-hologram.html","HoloDeck Beta — Wireframe Projection","Orbitron",
"""body{font-family:'Orbitron';background:#000;color:#0ff;text-align:center;overflow:hidden}
.stage{perspective:800px;margin:6vh auto;width:min(92vw,420px)}
.holo{width:100%;aspect-ratio:1;position:relative;transform-style:preserve-3d;animation:spin 14s linear infinite}
@keyframes spin{to{transform:rotateY(360deg) rotateX(12deg)}}
.face{position:absolute;inset:0;border:1px solid #0ff6;background:linear-gradient(#0ff08,transparent 60%),repeating-linear-gradient(#0ff2 0 1px,transparent 1px 24px),repeating-linear-gradient(90deg,#0ff2 0 1px,transparent 1px 24px);transform-style:preserve-3d}
.f2{transform:rotateY(90deg) translateZ(210px)}.f1{transform:translateZ(210px)}
.f3{transform:rotateY(180deg) translateZ(210px)}.f4{transform:rotateY(270deg) translateZ(210px)}
.base{width:120%;height:30px;margin:-15px auto 0;border-radius:50%;background:radial-gradient(#0ff6,transparent 70%);box-shadow:0 0 60px #0ff4}
h1{letter-spacing:.5em;font-size:1.2rem;margin-top:30px}
.glitchy{animation:jig 4s infinite}
@keyframes jig{0%,100%{filter:none}92%{filter:hue-rotate(90deg) brightness(1.6)}94%{filter:none}}
.status{opacity:.6;font-size:.75rem;margin-top:14px;letter-spacing:.3em}""",
"""<h1 class="glitchy">H O L O D E C K</h1><div class="status">beta build · projection stable-ish</div>
<div class="stage"><div class="holo"><div class="face f1"></div><div class="face f2"></div><div class="face f3"></div><div class="face f4"></div></div><div class="base"></div></div>
<p style="max-width:480px;margin:30px auto;opacity:.75;font-size:.85rem;line-height:2">PROJECTED ARTIFACT: “Cube (Study in Confidence)” — a wireframe so certain of itself it rotates without being asked.</p>""")

# ---------------------------------------------------------------- 91
page("091-seed-library.html","Heirloom Seed Library — Borrow a Future","Gaegu",
"""body{font-family:'Gaegu',cursive;background:#f2f7e4;color:#2f4a1e;text-align:center;padding:8vh 5vw}
h1{font-size:clamp(2.4rem,8vw,3.6rem)}
.jars{display:flex;gap:26px;justify-content:center;flex-wrap:wrap;margin-top:50px}
.jar{background:#fffdf5;border:3px solid #2f4a1e;border-radius:14px;padding:26px 20px;width:190px;transition:.3s;cursor:pointer;position:relative}
.jar:hover{transform:rotate(-2deg) translateY(-8px);box-shadow:0 16px 34px #2f4a1e33}
.jar::before{content:'';position:absolute;top:-14px;left:50%;transform:translateX(-50%);width:110px;height:16px;background:#2f4a1e;border-radius:8px}
.seed{font-size:2.6rem}.jar b{display:block;font-size:1.25rem;margin:8px 0}
.jar small{line-height:1.5;display:block}
.qty{margin-top:10px;font-size:.85rem;color:#7a9a5a}
.borrowed{background:#dcedc8}
p.foot{margin-top:50px;font-size:1.2rem;opacity:.8}""",
"""<h1>🌱 Heirloom Seed Library</h1><p style="font-size:1.3rem">borrow seeds like books · grow them · return next year's pages</p>
<div class="jars">
<div class="jar" onclick="this.classList.toggle('borrowed')"><div class="seed">🍅</div><b>Brandywine Tomato</b><small>1885 · beefsteak giant, terrible storage, worth it</small><div class="qty">34 packets left</div></div>
<div class="jar" onclick="this.classList.toggle('borrowed')"><div class="seed">🌶️</div><b>Shishito</b><small>one in ten spicy, like people</small><div class="qty">51 packets left</div></div>
<div class="jar" onclick="this.classList.toggle('borrowed')"><div class="seed">🎃</div><b>Jarrahdale Pumpkin</b><small>blue-grey, floury, dramatic at markets</small><div class="qty">12 packets left</div></div>
<div class="jar" onclick="this.classList.toggle('borrowed')"><div class="seed">🌻</div><b>Mammoth Sunflower</b><small>grow taller than your fence feelings</small><div class="qty">77 packets left</div></div></div>
<p class="foot">click a jar to borrow — honesty-based returns policy 🌾</p>""")

# ---------------------------------------------------------------- 92
page("092-elevator.html","Floor 13 — Elevator Panel","Rajdhani",
"""body{font-family:'Rajdhani';background:#14161a;color:#e8e8e8;display:grid;place-items:center;min-height:100vh}
.panel{background:linear-gradient(#2a2d33,#1c1f24);border:3px solid #3a3f46;border-radius:18px;padding:34px;display:grid;grid-template-columns:repeat(4,1fr);gap:16px;width:min(92vw,340px)}
.floor-btn{aspect-ratio:1;border-radius:50%;border:2px solid #555;background:#22262c;color:#ccc;font-size:1.1rem;font-family:inherit;cursor:pointer;transition:.2s}
.floor-btn:hover{border-color:#ffd166}
.floor-btn.on{background:#ffd166;color:#111;border-color:#ffd166;box-shadow:0 0 24px #ffd16688}
.display{grid-column:1/-1;background:#0a0a0a;color:#ff4d4d;font-family:monospace;font-size:2rem;text-align:center;padding:12px;border-radius:8px;letter-spacing:.3em}
.door{grid-column:1/-1;height:14px;background:linear-gradient(90deg,#3a3f46 50%,#222 50%);border-radius:6px;animation:doors 3s infinite}
@keyframes doors{0%,100%{background-size:200% 100%;background-position:0}50%{background-position:100%}}
h1{margin-bottom:20px;letter-spacing:.4em;font-weight:500}""",
"""<div><h1>ELEVATOR · TRUST US</h1><div class="panel"><div class="display" id="dsp">— —</div>
<button class="floor-btn">1</button><button class="floor-btn">2</button><button class="floor-btn">3</button><button class="floor-btn">4</button>
<button class="floor-btn">5</button><button class="floor-btn">6</button><button class="floor-btn">7</button><button class="floor-btn">8</button>
<button class="floor-btn">9</button><button class="floor-btn">10</button><button class="floor-btn">11</button><button class="floor-btn">12</button>
<button class="floor-btn" id="q13">13</button><button class="floor-btn">R</button><button class="floor-btn">P</button><button class="floor-btn">✳</button>
<div class="door"></div></div><p style="text-align:center;opacity:.5;margin-top:16px;font-size:.85rem">capacity 8 persons · or one grand piano · physics TBD</p></div>""",
"""const dsp=document.getElementById('dsp');
document.querySelectorAll('.floor-btn').forEach(b=>b.onclick=()=>{document.querySelectorAll('.floor-btn').forEach(x=>x.classList.remove('on'));b.classList.add('on');
let f=b.textContent,i=0;const iv=setInterval(()=>{dsp.textContent=('0'+(1+Math.floor(Math.random()*12))).slice(-2);if(++i>7){clearInterval(iv);dsp.textContent=f.padStart(2,'0')}},220)});
document.getElementById('q13').onclick=()=>{dsp.textContent='∞';setTimeout(()=>dsp.textContent='13',1200)};""")

# ---------------------------------------------------------------- 93
page("093-birdsong.html","Morning Chorus — Identify by Ear","Noto Serif",
"""body{font-family:'Noto Serif',serif;background:#eef3ea;color:#2b3a2b}
.field-guide{max-width:760px;margin:auto;padding:9vh 24px}
h1{font-size:clamp(2rem,6vw,3rem)}
.bird{display:grid;grid-template-columns:70px 1fr auto;gap:22px;align-items:center;padding:22px 0;border-bottom:1px solid #2b3a2b22;cursor:pointer;transition:.25s}
.bird:hover{padding-left:10px}
.bird .glyph{font-size:2.6rem}
.bird b{font-size:1.2rem}.bird small{display:block;opacity:.65;font-style:italic}
.song{font-family:monospace;color:#5a7a5a;font-size:.9rem}
.play{background:#5a7a5a;color:#fff;border:0;border-radius:99px;padding:8px 18px;font-size:.8rem;cursor:pointer}
.play:hover{background:#3f5a3f}
.dawn{background:linear-gradient(#f6e7b2,#eef3ea);border-radius:14px;padding:22px;margin:30px 0;font-style:italic}""",
"""<div class="field-guide"><h1>Morning Chorus</h1><div class="dawn">Today's dawn chorus peaked at 05:42. Territory density: ambitious. One robin arguing with traffic again.</div>
<div class="bird"><span class="glyph">🐦</span><div><b>European Robin</b><small>territorial tinkle, garden-sized ego</small></div><span><span class="song">tweet-chew-chew-TRILL</span><br><button class="play" data-f="2600">listen</button></span></div>
<div class="bird"><span class="glyph">🕊️</span><div><b>Common Wood Pigeon</b><small>coo-ing like a foghorn with manners</small></div><span><span class="song">coo-HOO-hoo-hoo</span><br><button class="play" data-f="420">listen</button></span></div>
<div class="bird"><span class="glyph">🪶</span><div><b>Eurasian Wren</b><small>tiny bird, absurdly loud opinion</small></div><span><span class="song">brrrr-BRRR-brrr</span><br><button class="play" data-f="4200">listen</button></span></div>
<div class="bird"><span class="glyph">🦜</span><div><b>Blackbird</b><small>flute solo at dusk, takes requests, gives none</small></div><span><span class="song">lee-ooo AAA-ooo</span><br><button class="play" data-f="1100">listen</button></span></div></div>""",
"""document.querySelectorAll('.play').forEach(b=>b.onclick=()=>{try{const ac=b._ac||(b._ac=new(window.AudioContext||window.webkitAudioContext)());
const f=+b.dataset.f,o=ac.createOscillator(),g=ac.createGain();o.frequency.value=f;g.gain.value=.12;o.connect(g).connect(ac.destination);
o.start();const t=ac.currentTime;for(let i=0;i<4;i++){o.frequency.setValueAtTime(f*(1+(i%2)*.12),t+i*.22);g.gain.setValueAtTime(.12,t+i*.22);g.gain.exponentialRampToValueAtTime(.001,t+i*.22+.2)}
o.stop(t+1);b.textContent='♪ playing'}catch(e){}});""")

# ---------------------------------------------------------------- 94
page("094-micro-brand.html","Fable & Filament — Brand One-Pager","Outfit",
"""body{font-family:'Outfit';background:#f7f5f0;color:#161616}
.page{max-width:900px;margin:auto;padding:9vh 26px}
.logo{display:flex;align-items:center;gap:14px;font-weight:800;font-size:1.6rem}
.bulb{width:44px;height:44px;border-radius:50%;background:#ffc857;box-shadow:0 0 0 6px #ffc85733,0 0 40px #ffc85788;animation:glow 2.6s infinite alternate}
@keyframes glow{to{box-shadow:0 0 0 10px #ffc85722,0 0 70px #ffc857}}
h1{font-size:clamp(2.4rem,8vw,4.4rem);font-weight:800;letter-spacing:-.03em;line-height:1.05;margin:50px 0 20px}
h1 span{color:#e5533c}
.cols{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:26px;margin-top:60px}
.val{border-top:3px solid #161616;padding-top:16px}
.val h3{font-size:1.1rem;margin-bottom:8px}.val p{opacity:.7;line-height:1.7;font-size:.95rem}
.swatches{display:flex;gap:12px;margin-top:60px}
.sw{width:64px;height:64px;border-radius:14px;display:grid;place-items:center;font-size:.6rem;color:#fff;font-family:monospace}
.cta{margin-top:60px;display:inline-block;background:#161616;color:#fff;padding:16px 36px;border-radius:99px;text-decoration:none;font-weight:700}""",
"""<div class="page"><div class="logo"><div class="bulb"></div>fable & filament</div>
<h1>Stories told in<br>warm light, <span>short sentences,</span><br>and honest wiring.</h1>
<p style="max-width:520px;font-size:1.2rem;opacity:.75">We're a two-person studio making brands feel like lamps: specific, glowing, easy to sit near.</p>
<div class="cols"><div class="val"><h3>Identity</h3><p>Marks that age like wood, not plastic.</p></div>
<div class="val"><h3>Editorial</h3><p>Words cut to length, never to size.</p></div>
<div class="val"><h3>Motion</h3><p>Animation with a resting heart rate.</p></div></div>
<div class="swatches"><div class="sw" style="background:#161616">#161616</div><div class="sw" style="background:#e5533c">#E5533C</div><div class="sw" style="background:#ffc857;color:#161616">#FFC857</div><div class="sw" style="background:#3a6b5a">#3A6B5A</div></div>
<a class="cta" href="#">Start a project →</a></div>""")

# ---------------------------------------------------------------- 95
page("095-deepsea-sub.html","DSV Erebus — Submersible Status Board","Space Mono",
"""body{font-family:'Space Mono',monospace;background:#03080c;color:#7fd1ae}
.board{max-width:820px;margin:auto;padding:8vh 22px}
h1{color:#e0f4ff;letter-spacing:.2em;font-size:1.3rem}
.depth{font-size:clamp(2.4rem,8vw,4rem);color:#4cc9f0;font-variant-numeric:tabular-nums;margin:20px 0}
.gauges{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:16px;margin:30px 0}
.g{border:1px solid #1c3a2e;padding:16px;background:#06131a}
.g small{color:#5a8a7a;letter-spacing:.2em;font-size:.7rem}
.g b{display:block;font-size:1.4rem;margin-top:6px}
.ok{color:#7fd1ae}.warn{color:#f4a261}.bad{color:#e76f51}
.sonar{width:min(92vw,300px);height:min(92vw,300px);border-radius:50%;border:1px solid #1c3a2e;margin:30px auto;position:relative;background:radial-gradient(#0a1f26,#03080c)}
.sweep{position:absolute;inset:0;border-radius:50%;background:conic-gradient(#4cc9f033,transparent 25%);animation:sw 3s linear infinite}
@keyframes sw{to{transform:rotate(360deg)}}
.blip{position:absolute;width:8px;height:8px;background:#f4a261;border-radius:50%;box-shadow:0 0 12px #f4a261}
.log{font-size:.8rem;line-height:2;opacity:.8}""",
"""<div class="board"><h1>DSV EREBUS · STATUS BOARD</h1>
<div class="depth" id="dep">-4,212 m</div><small style="color:#5a8a7a">descending · hull nominal · coffee operational</small>
<div class="gauges"><div class="g"><small>O₂ MIX</small><b class="ok">20.9%</b></div><div class="g"><small>HULL PRESSURE</small><b class="warn">42.3 MPa</b></div>
<div class="g"><small>BATTERY</small><b class="ok">78%</b></div><div class="g"><small>EXT. TEMP</small><b class="ok">1.8°C</b></div>
<div class="g"><small>BALLAST</small><b class="ok">-2.1%</b></div><div class="g"><small>SCARE LEVEL</small><b class="bad">elevated</b></div></div>
<div class="sonar"><div class="sweep"></div><div class="blip" style="left:30%;top:44%"></div><div class="blip" style="left:62%;top:28%"></div><div class="blip" style="left:55%;top:70%"></div></div>
<div class="log">22:41 hydrophone: rhythmic knocking, unidentified, politeness assumed<br>22:44 lights caught something vast and then it wasn't<br>22:47 crew vote: continue, obviously</div></div>""",
"""let d=4212;setInterval(()=>{d-=Math.floor(Math.random()*9);document.getElementById('dep').textContent='-'+d.toLocaleString()+' m'},800);""")

# ---------------------------------------------------------------- 96
page("096-quilt.html","The Quilt Archive — Patchwork Histories","Kalam",
"""body{font-family:'Kalam',cursive;background:#efe9dc;color:#3a3226;text-align:center}
.box{max-width:760px;margin:auto;padding:9vh 22px}
h1{font-size:2.2rem}
.quilt{display:grid;grid-template-columns:repeat(6,1fr);gap:6px;margin:40px auto;max-width:600px}
.patch{aspect-ratio:1;border-radius:6px;display:grid;place-items:center;font-size:1.6rem;cursor:pointer;transition:.3s;box-shadow:0 4px 10px #0001}
.patch:hover{transform:scale(1.15) rotate(4deg);z-index:2}
.story{max-width:520px;margin:20px auto;font-size:1.15rem;min-height:3.4em;line-height:1.7}
.legend{font-size:.85rem;opacity:.6}""",
"""<div class="box"><h1>The Quilt Archive</h1><p style="opacity:.7">every square was a person, a place, or a stubborn idea · tap to hear the stitching</p>
<div class="quilt" id="q"></div><div class="story" id="s">pick a patch…</div>
<p class="legend">machine-pieced 1974 · hand-bound by aunties · washed exactly once, carefully</p></div>""",
"""const P=[['#c94f4f','🌊','Grandmother Ada sailed this square across the Atlantic in her coat lining. Salt stains remain; she insisted they were seasoning.'],
['#e8a13c','🐝','The bee block commemorates the summer the orchard finally produced. Six jars, zero complaints, one stung eyebrow.'],
['#5a8a5a','🌙','Midnight fabric from a curtain Ada hated. "Good enough for quilts," she said, about curtains.'],
['#4f7fc9','🚂','Printed cotton from the railway hotel where the quilt pattern was first sketched on a napkin.'],
['#9a5ac9','🧵','The purple came from dye experimentation. The sofa never recovered. Worth it.'],
['#c9c94f','🌻','Sunflower square stitched by the children, ages 6–11, contributions legally binding.']];
const q=document.getElementById('q');
for(let i=0;i<24;i++){const [c,e,t]=P[i%6];const d=document.createElement('div');d.className='patch';
d.style.background=c+(i%3===0?'':i%3===1?'ee':'dd');d.textContent=e;
d.onclick=()=>document.getElementById('s').textContent=t;q.appendChild(d)}""")

# ---------------------------------------------------------------- 97
page("097-speed-dial.html","Rotary — One Number From 1962","Limelight",
"""body{font-family:'Limelight';background:#1a1512;color:#e8dcc0;display:grid;place-items:center;min-height:100vh;padding:20px}
.phone{width:min(92vw,420px);aspect-ratio:1;background:#241d18;border-radius:50%;position:relative;border:10px solid #382c22;box-shadow:0 30px 80px #000a,inset 0 0 60px #0008}
.hole{position:absolute;width:52px;height:52px;border-radius:50%;background:#0d0a08;display:grid;place-items:center;color:#e8dcc0;font-size:1.2rem;cursor:pointer;transition:.2s;top:50%;left:50%}
.hole:hover{background:#c94f4f;transform:scale(1.15)}
.center{position:absolute;inset:34%;border-radius:50%;background:radial-gradient(#3a2e24,#241d18);display:grid;place-items:center;text-align:center;padding:10px}
.center small{font-size:.55rem;letter-spacing:.2em}
.dial{animation:shake .4s}
@keyframes shake{25%{transform:rotate(8deg)}75%{transform:rotate(-8deg)}}
.readout{margin-top:30px;font-size:1.6rem;color:#c9a228;min-height:1.4em}
.instruct{opacity:.6;margin-top:10px;font-size:.9rem}""",
"""<div style="text-align:center"><div class="phone" id="ph"><div class="center"><div>LONG<br>DISTANCE<br><small>EST. 1962</small></div></div></div>
<div class="readout" id="num">— — —</div><div class="instruct">poke holes to dial · old number: GRanite 7-4243</div></div>""",
"""const ph=document.getElementById('ph');const digits=['1','2 ABC','3 DEF','4 GHI','5 JKL','6 MNO','7 PRS','8 TUV','9 WXY','0 OPER','•','✱'];
digits.forEach((d,i)=>{const a=i/digits.length*Math.PI*2-Math.PI/2;const h=document.createElement('div');h.className='hole';
h.textContent=d[0];h.title=d;const r=38;h.style.transform=`translate(calc(-50% + ${Math.cos(a)*r}%), calc(-50% + ${Math.sin(a)*r}%))`;
h.onclick=()=>{ph.classList.add('dial');setTimeout(()=>ph.classList.remove('dial'),400);
const n=document.getElementById('num');n.textContent=(n.textContent.replace(/[^0-9A-Z]/gi,'')+' '+d[0]).slice(-14);
if(n.textContent.replace(/[^0-9]/g,'').length>=7)setTimeout(()=>n.textContent='GRanite 7-4243 rings…',700)};ph.appendChild(h)});""")

# ---------------------------------------------------------------- 98
page("098-recipe-fold.html","The Recipe Fold — Sunday Ragù","Caveat",
"""body{font-family:'Caveat',cursive;background:#fbf7ec;color:#2e2a24;line-height:1.7}
.card{max-width:680px;margin:8vh auto;background:#fffdf4;padding:50px 44px;box-shadow:0 20px 60px #00000018;transform:rotate(-.6deg);position:relative}
.card::before{content:'';position:absolute;top:-12px;left:50%;transform:translateX(-50%) rotate(2deg);width:120px;height:30px;background:#f2c6a0cc;opacity:.8}
h1{font-size:3rem}
.ing{columns:2;gap:30px;font-size:1.35rem}
.ing li{list-style:none;padding:2px 0}
.ing li::before{content:'○ ';color:#b08968}
.method{font-size:1.4rem;margin-top:30px}
.step{margin:18px 0;padding-left:16px;border-left:3px solid #b08968}
.note{background:#f5ecd8;padding:14px 18px;font-size:1.2rem;margin-top:30px;transform:rotate(.4deg)}
.splash{color:#a34e2b;font-size:1.1rem}""",
"""<div class="card"><h1>Sunday Ragù ⭐</h1><p style="font-size:1.3rem;opacity:.7">Nonna's card, stained twice, corrected never</p>
<ul class="ing"><li>1kg beef chuck, cubed angry</li><li>2 carrots, 1 onion, celery shrug</li><li>tomato passata, whole tin + splash</li><li>red wine "the cooking kind" (lie)</li><li>milk, small glug — trust me</li><li>bay leaves 2, patience 4 hrs</li></ul>
<div class="method"><div class="step">1. Brown meat properly. Loud pan, quiet TV.</div>
<div class="step">2. Veg soft, wine in, scrape the fond (fond = flavour, don't skip).</div>
<div class="step">3. Passata, milk, bay. Barely bubbling. Nap time for the pot.</div>
<div class="step">4. Pasta separately, tossed with a ladle of ragù, no ceremony.</div></div>
<p class="splash">✗ crossed out: "2 hrs" — replaced with "4, minimum, I'm not raising lies"</p>
<div class="note">Note: tastes better Tuesday. This is not negotiable. — M.K. ’61</div></div>""")

# ---------------------------------------------------------------- 99
page("099-constellation.html","Draw Your Constellation","Syncopate",
"""body{font-family:'Syncopate';background:#020308;color:#cdd6f4;min-height:100vh;overflow:hidden;text-align:center}
h1{padding-top:6vh;font-size:1.1rem;letter-spacing:.4em}
p{opacity:.5;font-size:.75rem;margin-top:10px}
canvas{display:block;cursor:crosshair}
.name{position:fixed;bottom:6vh;width:100%;font-size:.9rem;letter-spacing:.3em;color:#ffd93d}""",
"""<h1>NAME THE STARS BETWEEN YOU</h1><p>click stars to connect · double-click to clear</p>
<canvas id="c"></canvas><div class="name" id="nm">your constellation awaits its myth</div>""",
"""const c=document.getElementById('c'),x=c.getContext('2d');let W,H,stars=[],links=[],hover=null;
function rs(){W=c.width=innerWidth;H=c.height=innerHeight;stars=[...Array(14)].map(()=>({x:60+Math.random()*(W-120),y:100+Math.random()*(H-220),tw:Math.random()*6}))}rs();onresize=rs;
addEventListener('mousemove',e=>{hover=null;let best=60;for(const s of stars){const d=Math.hypot(s.x-e.clientX,s.y-e.clientY);if(d<best){best=d;hover=s}}});
c.addEventListener('click',()=>{if(hover){const last=links[links.length-1];if(last!==hover){if(links.length&&links[links.length-1]!==hover)links.push(hover);links.push(hover)}}});
c.addEventListener('dblclick',()=>{links=[];document.getElementById('nm').textContent='fresh sky, fresh myth'});
const myths=['The Late Lantern','Two Bears Arguing','Her Unsent Letter','The Ferry That Waited','Small Crown, Heavy Head','The Third Well'];
(function l(){x.fillStyle='#020308';x.fillRect(0,0,W,H);
x.strokeStyle='#ffd93d88';x.lineWidth=1.4;x.beginPath();links.forEach((s,i)=>i?x.lineTo(s.x,s.y):x.moveTo(s.x,s.y));if(links.length)x.stroke();
for(const s of stars){const tw=.6+.4*Math.sin(Date.now()/700+s.tw);
x.fillStyle=`rgba(220,230,255,${tw})`;x.beginPath();x.arc(s.x,s.y,s===hover?7:3,0,7);x.fill();
if(s===hover){x.strokeStyle='#fff3';x.beginPath();x.arc(s.x,s.y,12,0,7);x.stroke()}}
if(links.length>1&&!document.getElementById('nm').dataset.set){document.getElementById('nm').textContent='“'+myths[Math.random()*myths.length|0]+'” — recorded in the almanac';document.getElementById('nm').dataset.set=1}
if(!links.length)delete document.getElementById('nm').dataset.set;
requestAnimationFrame(l)})()""")

# ---------------------------------------------------------------- 100
page("100-thankyou.html","Page 100 — The End Of The Beginning","Caveat",
"""body{font-family:'Caveat',cursive;background:radial-gradient(#1c2333,#0a0d16);color:#fff;display:grid;place-items:center;min-height:100vh;text-align:center;overflow:hidden}
.thanks{position:relative;z-index:2;padding:24px}
h1{font-size:clamp(3rem,10vw,6rem);line-height:1.1}
h1 span{color:#ffd93d}
p{font-size:1.6rem;opacity:.8;max-width:520px;margin:20px auto}
.confetti{position:fixed;top:-20px;font-size:1.6rem;animation:drop linear forwards}
@keyframes drop{to{transform:translateY(110vh) rotate(720deg);opacity:.1}}
button{background:#ffd93d;color:#1c2333;border:0;font-family:inherit;font-size:1.4rem;padding:12px 36px;border-radius:99px;cursor:pointer;transition:.2s}
button:hover{transform:scale(1.08) rotate(-2deg)}
.pages{margin-top:26px;font-size:1rem;opacity:.5}""",
"""<div class="thanks"><h1>You made it to <span>page 100.</span></h1>
<p>One hundred worlds, one hundred fonts, zero templates reused. Somewhere in here a galaxy spins, a worm reports weekly, and a cookie counts your clicks.</p>
<button id="pop">throw confetti 🎉</button>
<div class="pages">pages 001–100 · built by hand, generated with love</div></div>""",
"""document.getElementById('pop').onclick=()=>{for(let i=0;i<80;i++){const c=document.createElement('div');c.className='confetti';
c.textContent=['🎉','✨','🎊','⭐','💛'][i%5];c.style.left=Math.random()*100+'vw';c.style.animationDuration=(2+Math.random()*3)+'s';
document.body.appendChild(c);setTimeout(()=>c.remove(),5000)}};""")

print(f"All pages defined: {len(PAGES)}")
assert len(PAGES)==100, f"expected 100, got {len(PAGES)}"

# Write files
seen=set()
for fname,title,html in PAGES:
    assert fname not in seen, "duplicate filename "+fname
    seen.add(fname)
    with open(os.path.join(OUT,fname),"w",encoding="utf-8") as f:
        f.write(html)
print(f"Wrote {len(PAGES)} files to {OUT}")


