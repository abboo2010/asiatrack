import * as THREE from 'three';
import { RoomEnvironment } from 'three/examples/jsm/environments/RoomEnvironment.js';

function roundedPath(pts, r) {
  const path = new THREE.CurvePath();
  let prev = pts[0].clone();
  for (let i = 1; i < pts.length - 1; i++) {
    const p = pts[i], n = pts[i + 1];
    const d1 = p.clone().sub(pts[i - 1]).normalize();
    const d2 = n.clone().sub(p).normalize();
    const a = p.clone().addScaledVector(d1, -r);
    const b = p.clone().addScaledVector(d2, r);
    if (prev.distanceTo(a) > 1e-4) path.add(new THREE.LineCurve3(prev, a));
    path.add(new THREE.QuadraticBezierCurve3(a, p.clone(), b));
    prev = b;
  }
  path.add(new THREE.LineCurve3(prev, pts[pts.length - 1].clone()));
  return path;
}

function init(mount) {
  const variant = mount.dataset['3d'] || 'home';
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  let renderer;
  try {
    renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
  } catch (e) { return; }
  renderer.setPixelRatio(Math.min(devicePixelRatio || 1, 2));
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure = 1.05;
  const canvas = renderer.domElement;
  canvas.setAttribute('aria-hidden', 'true');
  canvas.style.cssText = 'position:absolute;inset:0;width:100%;height:100%;display:block';
  mount.appendChild(canvas);
  mount.classList.add('has-webgl');

  const scene = new THREE.Scene();
  const pmrem = new THREE.PMREMGenerator(renderer);
  scene.environment = pmrem.fromScene(new RoomEnvironment(), 0.04).texture;

  const camera = new THREE.PerspectiveCamera(36, 1, 0.1, 100);
  camera.position.set(0.4, 2.3, 11.5);
  camera.lookAt(0, 0.1, 0);

  scene.add(new THREE.AmbientLight(0x9fb8d6, 0.5));
  const key = new THREE.DirectionalLight(0xffffff, 2.2); key.position.set(4, 7, 6); scene.add(key);
  const rim = new THREE.PointLight(0x22d3ee, 40, 20); rim.position.set(-5, 2, -3); scene.add(rim);

  const root = new THREE.Group(); scene.add(root);

  // floor grid + shadow disc
  const grid = new THREE.GridHelper(16, 32, 0x38bdf8, 0x38bdf8);
  grid.material.transparent = true; grid.material.opacity = 0.16; grid.position.y = -2.2; root.add(grid);

  // pipe network
  const V = (x, y, z) => new THREE.Vector3(x, y, z);
  const main = roundedPath([V(-5.2, 1.7, 0), V(0.2, 1.7, 0), V(0.2, -1.2, 0), V(2.4, -1.2, 0)], 0.85);
  const branch = roundedPath([V(-5.2, -0.6, 0.8), V(-2.4, -0.6, 0.8), V(-2.4, -1.9, 0.8), V(-0.4, -1.9, 0.8)], 0.5);
  const steel = new THREE.MeshStandardMaterial({ color: 0x9ccbea, metalness: 0.85, roughness: 0.28 });
  const steel2 = new THREE.MeshStandardMaterial({ color: 0x1e5f8f, metalness: 0.8, roughness: 0.35 });
  const bolt = new THREE.MeshStandardMaterial({ color: 0xe2e8f0, metalness: 1, roughness: 0.25 });

  function addPipe(curve, radius, mat, flangeAt) {
    const tube = new THREE.Mesh(new THREE.TubeGeometry(curve, 160, radius, 28, false), mat);
    root.add(tube);
    flangeAt.forEach(t => {
      const pos = curve.getPointAt(t), tan = curve.getTangentAt(t);
      const g = new THREE.Group();
      const f = new THREE.Mesh(new THREE.CylinderGeometry(radius * 1.55, radius * 1.55, radius * 0.38, 40), steel2);
      g.add(f);
      for (let i = 0; i < 8; i++) {
        const a = (i / 8) * Math.PI * 2;
        const b = new THREE.Mesh(new THREE.CylinderGeometry(radius * 0.13, radius * 0.13, radius * 0.55, 10), bolt);
        b.position.set(Math.cos(a) * radius * 1.25, 0, Math.sin(a) * radius * 1.25);
        g.add(b);
      }
      g.position.copy(pos);
      g.quaternion.setFromUnitVectors(V(0, 1, 0), tan);
      root.add(g);
    });
  }
  addPipe(main, 0.34, steel, [0.12, 0.34, 0.62, 0.86]);
  addPipe(branch, 0.2, steel, [0.2, 0.55, 0.85]);

  // sectional panel tank
  const tankGroup = new THREE.Group(); tankGroup.position.set(3.9, -0.75, 0); root.add(tankGroup);
  const tw = 2.9, th = 2.9, td = 2.4;
  const box = new THREE.BoxGeometry(tw, th, td, 4, 4, 3);
  const glass = new THREE.MeshPhysicalMaterial({ color: 0x7dd3fc, transparent: true, opacity: 0.16, roughness: 0.1, metalness: 0.2, side: THREE.DoubleSide, depthWrite: false });
  tankGroup.add(new THREE.Mesh(box, glass));
  const wire = new THREE.LineSegments(new THREE.WireframeGeometry(box), new THREE.LineBasicMaterial({ color: 0x7dd3fc, transparent: true, opacity: 0.55 }));
  tankGroup.add(wire);
  const edges = new THREE.LineSegments(new THREE.EdgesGeometry(new THREE.BoxGeometry(tw, th, td)), new THREE.LineBasicMaterial({ color: 0xe0f2fe }));
  tankGroup.add(edges);
  const waterMat = new THREE.MeshStandardMaterial({ color: 0x0ea5c6, emissive: 0x0891b2, emissiveIntensity: 0.9, transparent: true, opacity: 0.72, roughness: 0.2 });
  const water = new THREE.Mesh(new THREE.BoxGeometry(tw - 0.14, 1, td - 0.14), waterMat);
  tankGroup.add(water);
  const legs = new THREE.Mesh(new THREE.BoxGeometry(tw + 0.3, 0.16, td + 0.3), steel2); legs.position.y = -th / 2 - 0.08; tankGroup.add(legs);

  // flow particles
  const flow = [];
  const pm = new THREE.MeshBasicMaterial({ color: 0x67e8f9 });
  for (let i = 0; i < 26; i++) {
    const m = new THREE.Mesh(new THREE.SphereGeometry(0.1, 12, 12), pm);
    root.add(m); flow.push({ m, t: Math.random(), c: i % 3 === 0 ? branch : main, s: 0.05 + Math.random() * 0.04 });
  }

  // variants
  const base = { home: [0.35, 1], about: [-0.5, 0.9], services: [0.1, 1], products: [-0.25, 1], portfolio: [0.6, 0.95] }[variant] || [0.3, 1];
  root.scale.setScalar(base[1]);

  function resize() {
    const w = mount.clientWidth || 600, h = mount.clientHeight || 500;
    renderer.setSize(w, h, false);
    camera.aspect = w / h;
    const a = w / h;
    camera.position.z = Math.min(17.5, Math.max(11.5, 11.5 + (1.95 - a) * 5.8));
    camera.updateProjectionMatrix();
  }
  resize();
  new ResizeObserver(resize).observe(mount);

  let px = 0, py = 0, tx = 0, ty = 0, running = true, scrollY = 0;
  addEventListener('pointermove', e => {
    const r = mount.getBoundingClientRect();
    tx = ((e.clientX - r.left) / r.width - 0.5) * 2;
    ty = ((e.clientY - r.top) / r.height - 0.5) * 2;
  }, { passive: true });
  addEventListener('scroll', () => { scrollY = window.scrollY; }, { passive: true });
  new IntersectionObserver(es => { running = es[0].isIntersecting; if (running && !reduce) loop(); }).observe(mount);

  const clock = new THREE.Clock();
  function frame() {
    const t = clock.getElapsedTime();
    px += (Math.max(-1, Math.min(1, tx)) - px) * 0.05;
    py += (Math.max(-1, Math.min(1, ty)) - py) * 0.05;
    root.rotation.y = base[0] + Math.sin(t * 0.25) * 0.18 + px * 0.35 + scrollY * 0.0006;
    root.rotation.x = -0.05 + py * 0.12;
    root.position.y = Math.sin(t * 0.6) * 0.08;
    const lvl = 0.55 + (Math.sin(t * 0.5) * 0.5 + 0.5) * 0.35;
    water.scale.y = lvl * (th - 0.2); water.position.y = -th / 2 + 0.07 + water.scale.y / 2;
    flow.forEach(f => {
      f.t = (f.t + f.s * 0.016) % 1;
      f.m.position.copy(f.c.getPointAt(f.t));
    });
    renderer.render(scene, camera);
  }
  let raf = 0;
  function loop() {
    cancelAnimationFrame(raf);
    const step = () => { if (!running) return; frame(); raf = requestAnimationFrame(step); };
    step();
  }
  if (reduce) { frame(); } else { loop(); }
}

document.querySelectorAll('[data-3d]').forEach(init);
