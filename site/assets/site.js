(function(){
var reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
var fine=matchMedia('(hover:hover) and (pointer:fine)').matches;

// Industries
var IND=[
 ["Water Industry","Domestic supply networks and vessel applications: clean, safe, reliable distribution.","M12 3c3 4.5 6 7.5 6 11a6 6 0 0 1-12 0c0-3.5 3-6.5 6-11z"],
 ["Treatment Plants","Complete pipeline installation for water and wastewater facilities.","M3 17h18M5 17V9l7-4 7 4v8M9 17v-5h6v5"],
 ["Biogas Pipelines","Safely capture, transport and utilise biogas for cleaner energy.","M12 3c1 3 5 5 5 9a5 5 0 0 1-10 0c0-2 1-3 2-4 0 2 1 3 2 3 0-3-1-5 1-8z"],
 ["Air Pipelines","Compressed air and ventilation lines with stable pressure and low energy loss.","M3 9h11a3 3 0 1 0-3-3M3 15h15a3 3 0 1 1-3 3M3 12h7"],
 ["Firefighting Pipelines","Fire protection pipework designed and installed to code.","M12 2c1 4 6 6 6 11a6 6 0 0 1-12 0c0-3 2-5 3-7 0 2 1 3 2 3 0-2 0-4 1-7z"],
 ["Food Industry","Food-grade materials and hygienic installation for contamination-free production.","M6 3v8a3 3 0 0 0 6 0V3M9 3v18M17 3c-2 2-2 8 0 9v9"],
 ["Palm Oil Industry","Durable systems for crude and refined palm oil under demanding conditions.","M12 21V9M12 9c-3 0-6-2-7-5 4 0 7 1 7 5zm0 0c3 0 6-2 7-5-4 0-7 1-7 5z"],
 ["Biochemical Pipelines","Safe handling of corrosive, volatile and high-pressure substances.","M9 3h6M10 3v6l-5 9a2 2 0 0 0 2 3h10a2 2 0 0 0 2-3l-5-9V3"]
];
var g=document.getElementById('indgrid');
if(g){g.innerHTML=IND.map(function(r){return '<article class="ind-card" data-reveal data-tilt><div class="ico"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="'+r[2]+'"/></svg></div><h3>'+r[0]+'</h3><p>'+r[1]+'</p></article>'}).join('');}

// Mobile menu
var mb=document.querySelector('.menu-btn'),menu=document.getElementById('menu');
if(mb&&menu){
  mb.addEventListener('click',function(){var o=menu.classList.toggle('open');mb.setAttribute('aria-expanded',o)});
  menu.addEventListener('click',function(e){if(e.target.tagName==='A'){menu.classList.remove('open');mb.setAttribute('aria-expanded','false')}});
}

// Portfolio filter
var fb=document.querySelectorAll('.filters button');
fb.forEach(function(b){b.addEventListener('click',function(){
  fb.forEach(function(x){x.setAttribute('aria-pressed','false')});b.setAttribute('aria-pressed','true');
  var f=b.dataset.filter;
  document.querySelectorAll('.proj').forEach(function(p){p.hidden=!(f==='all'||p.dataset.type===f)});
})});

// 3D tilt
if(fine&&!reduce){
  document.querySelectorAll('[data-tilt]').forEach(function(el){
    var max=9;
    el.addEventListener('pointermove',function(e){
      var r=el.getBoundingClientRect(),x=(e.clientX-r.left)/r.width,y=(e.clientY-r.top)/r.height;
      el.classList.add('is-tilting');
      el.style.transform='perspective(900px) rotateX('+((0.5-y)*max)+'deg) rotateY('+((x-0.5)*max*1.2)+'deg) translateZ(10px)';
      el.style.setProperty('--gx',(x*100)+'%');el.style.setProperty('--gy',(y*100)+'%');
    });
    el.addEventListener('pointerleave',function(){el.classList.remove('is-tilting');el.style.transform=''});
  });
}

// Motion
document.documentElement.classList.add('js');
var M=window.Motion;
if(M&&!reduce){
  var animate=M.animate,inView=M.inView;
  inView('[data-reveal]',function(el){
    // animate opacity + translate (not transform on tilt elements: use translate property)
    animate(el,{opacity:[0,1],translate:['0px 28px','0px 0px']},{duration:.7,ease:[.22,1,.36,1]});
  },{margin:'0px 0px -8% 0px'});
  document.querySelectorAll('.draw').forEach(function(p){
    var L=p.getTotalLength();p.style.strokeDasharray=L;
    animate(p,{strokeDashoffset:[L,0]},{duration:2.2,ease:'easeInOut',delay:.4});
  });
  document.querySelectorAll('[data-count]').forEach(function(el){
    var n=+el.dataset.count;
    inView(el,function(){animate(0,n,{duration:1.4,ease:'easeOut',onUpdate:function(v){el.textContent=Math.round(v)}})});
  });
}else{
  document.querySelectorAll('[data-count]').forEach(function(el){el.textContent=el.dataset.count});
}
})();

// Photo lightbox
(function(){
var imgs=document.querySelectorAll('.shot img,.proj img,.prod img,.pvis img');
if(!imgs.length)return;
var lb=document.createElement('div');lb.className='lb';lb.setAttribute('role','dialog');lb.setAttribute('aria-modal','true');lb.setAttribute('aria-label','Photo viewer');
lb.innerHTML='<button type="button" aria-label="Close photo">&times;</button><img alt=""><p></p>';
document.body.appendChild(lb);
var big=lb.querySelector('img'),cap=lb.querySelector('p'),x=lb.querySelector('button'),last=null;
function open(i){last=i;big.src=i.currentSrc||i.src;big.alt=i.alt;cap.textContent=i.alt;lb.classList.add('open');x.focus()}
function close(){lb.classList.remove('open');if(last)last.focus()}
imgs.forEach(function(i){i.classList.add('lb-img');i.tabIndex=0;i.setAttribute('role','button');
 i.addEventListener('click',function(){open(i)});
 i.addEventListener('keydown',function(e){if(e.key==='Enter'||e.key===' '){e.preventDefault();open(i)}})});
lb.addEventListener('click',function(e){if(e.target!==big)close()});
document.addEventListener('keydown',function(e){if(e.key==='Escape'&&lb.classList.contains('open'))close()});
})();
