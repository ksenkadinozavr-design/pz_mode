const canvas = document.getElementById("particles");
const ctx = canvas.getContext("2d");
let width;
let height;
let particles = [];

const resize = () => {
  width = canvas.width = window.innerWidth;
  height = canvas.height = window.innerHeight;
};

const createParticles = () => {
  particles = Array.from({ length: 80 }).map(() => ({
    x: Math.random() * width,
    y: Math.random() * height,
    radius: Math.random() * 2 + 0.5,
    speed: Math.random() * 0.3 + 0.2,
    drift: Math.random() * 0.4 - 0.2,
    opacity: Math.random() * 0.6 + 0.2,
  }));
};

const animate = () => {
  ctx.clearRect(0, 0, width, height);
  ctx.fillStyle = "rgba(190, 200, 220, 0.6)";
  particles.forEach((p) => {
    ctx.globalAlpha = p.opacity;
    ctx.beginPath();
    ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
    ctx.fill();
    p.y -= p.speed;
    p.x += p.drift;
    if (p.y < -10) {
      p.y = height + 10;
      p.x = Math.random() * width;
    }
    if (p.x < -10 || p.x > width + 10) {
      p.x = Math.random() * width;
    }
  });
  requestAnimationFrame(animate);
};

const parallaxLayers = document.querySelectorAll(".hero-layer");

const handleScroll = () => {
  const scrollTop = window.scrollY;
  parallaxLayers.forEach((layer, index) => {
    const depth = Number(layer.dataset.depth) || (index + 1) * 0.12;
    layer.style.transform = `translateY(${scrollTop * depth}px)`;
  });
};

window.addEventListener("resize", () => {
  resize();
  createParticles();
});

window.addEventListener("scroll", handleScroll);

resize();
createParticles();
animate();
handleScroll();

const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("in-view");
      }
    });
  },
  { threshold: 0.2 }
);

document.querySelectorAll("section").forEach((section) => {
  section.classList.add("reveal");
  observer.observe(section);
});
