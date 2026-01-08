// ===== Navbar Scroll Effect =====
const navbar = document.querySelector('.navbar');

window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
});

// ===== Smooth Scroll for Anchor Links =====
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// ===== Scroll Reveal Animation =====
const revealElements = document.querySelectorAll('.reveal');

const revealOnScroll = () => {
    const windowHeight = window.innerHeight;
    const revealPoint = 150;

    revealElements.forEach(element => {
        const elementTop = element.getBoundingClientRect().top;

        if (elementTop < windowHeight - revealPoint) {
            element.classList.add('active');
        }
    });
};

window.addEventListener('scroll', revealOnScroll);
window.addEventListener('load', revealOnScroll);

// ===== Skill Cards Stagger Animation =====
const skillCards = document.querySelectorAll('.skill-card');

const animateSkillCards = () => {
    skillCards.forEach((card, index) => {
        const cardTop = card.getBoundingClientRect().top;
        const windowHeight = window.innerHeight;

        if (cardTop < windowHeight - 100) {
            setTimeout(() => {
                card.style.opacity = '1';
                card.style.transform = 'translateY(0)';
            }, index * 100);
        }
    });
};

// Initialize skill cards
skillCards.forEach(card => {
    card.style.opacity = '0';
    card.style.transform = 'translateY(30px)';
    card.style.transition = 'all 0.5s ease';
});

window.addEventListener('scroll', animateSkillCards);
window.addEventListener('load', animateSkillCards);

// ===== Project Cards Hover Effect =====
const projectCards = document.querySelectorAll('.project-card');

projectCards.forEach(card => {
    card.addEventListener('mouseenter', function() {
        this.style.transform = 'translateY(-10px)';
    });

    card.addEventListener('mouseleave', function() {
        this.style.transform = 'translateY(0)';
    });
});

// ===== Typing Effect for Hero (Optional) =====
const heroTitle = document.querySelector('.hero-title');

if (heroTitle && heroTitle.dataset.typed) {
    const text = heroTitle.dataset.typed;
    heroTitle.textContent = '';
    let i = 0;

    const typeWriter = () => {
        if (i < text.length) {
            heroTitle.textContent += text.charAt(i);
            i++;
            setTimeout(typeWriter, 100);
        }
    };

    typeWriter();
}

// ===== Stats Counter Animation =====
const statNumbers = document.querySelectorAll('.stat-number');

const animateStats = () => {
    statNumbers.forEach(stat => {
        const statTop = stat.getBoundingClientRect().top;
        const windowHeight = window.innerHeight;

        if (statTop < windowHeight - 100 && !stat.classList.contains('animated')) {
            stat.classList.add('animated');
            const target = stat.textContent;

            // Check if it's a number
            if (!isNaN(parseInt(target))) {
                const targetNum = parseInt(target);
                let current = 0;
                const increment = targetNum / 50;
                const suffix = target.replace(/[0-9]/g, '');

                const counter = setInterval(() => {
                    current += increment;
                    if (current >= targetNum) {
                        stat.textContent = targetNum + suffix;
                        clearInterval(counter);
                    } else {
                        stat.textContent = Math.floor(current) + suffix;
                    }
                }, 30);
            }
        }
    });
};

window.addEventListener('scroll', animateStats);
window.addEventListener('load', animateStats);

// ===== Image Gallery Lightbox =====
const lightboxImages = document.querySelectorAll('.gallery-item img, .screenshot-item img, .school-project-images img, .lightbox-img, .image-block img');

lightboxImages.forEach(img => {
    img.style.cursor = 'zoom-in';

    img.addEventListener('click', function() {
        const overlay = document.createElement('div');
        overlay.className = 'lightbox-overlay';
        overlay.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.95);
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 9999;
            cursor: zoom-out;
            padding: 2rem;
            opacity: 0;
            transition: opacity 0.3s ease;
        `;

        const enlargedImg = document.createElement('img');
        enlargedImg.src = this.src;
        enlargedImg.alt = this.alt;
        enlargedImg.style.cssText = `
            max-width: 95%;
            max-height: 95%;
            border-radius: 8px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5);
            transform: scale(0.9);
            transition: transform 0.3s ease;
        `;

        // Close button
        const closeBtn = document.createElement('button');
        closeBtn.innerHTML = '&times;';
        closeBtn.style.cssText = `
            position: absolute;
            top: 20px;
            right: 30px;
            font-size: 40px;
            color: white;
            background: none;
            border: none;
            cursor: pointer;
            opacity: 0.7;
            transition: opacity 0.2s;
        `;
        closeBtn.onmouseover = () => closeBtn.style.opacity = '1';
        closeBtn.onmouseout = () => closeBtn.style.opacity = '0.7';

        overlay.appendChild(enlargedImg);
        overlay.appendChild(closeBtn);
        document.body.appendChild(overlay);

        // Animate in
        requestAnimationFrame(() => {
            overlay.style.opacity = '1';
            enlargedImg.style.transform = 'scale(1)';
        });

        // Prevent body scroll
        document.body.style.overflow = 'hidden';

        const closeOverlay = () => {
            overlay.style.opacity = '0';
            enlargedImg.style.transform = 'scale(0.9)';
            setTimeout(() => {
                overlay.remove();
                document.body.style.overflow = '';
            }, 300);
        };

        overlay.addEventListener('click', closeOverlay);
        closeBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            closeOverlay();
        });

        // Close on ESC key
        const closeOnEsc = (e) => {
            if (e.key === 'Escape') {
                closeOverlay();
                document.removeEventListener('keydown', closeOnEsc);
            }
        };
        document.addEventListener('keydown', closeOnEsc);
    });
});

// ===== Table Row Highlight =====
const tableRows = document.querySelectorAll('.results-table tbody tr');

tableRows.forEach(row => {
    row.addEventListener('mouseenter', function() {
        if (!this.classList.contains('highlight-row')) {
            this.style.background = 'rgba(37, 99, 235, 0.05)';
        }
    });

    row.addEventListener('mouseleave', function() {
        if (!this.classList.contains('highlight-row')) {
            this.style.background = '';
        }
    });
});

// ===== Intersection Observer for Better Performance =====
const observerOptions = {
    root: null,
    rootMargin: '0px',
    threshold: 0.1
};

const observerCallback = (entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('active');
        }
    });
};

const observer = new IntersectionObserver(observerCallback, observerOptions);

document.querySelectorAll('.reveal, .skill-card, .project-card').forEach(el => {
    observer.observe(el);
});

// ===== Console Easter Egg =====
console.log('%c Welcome to my Portfolio!', 'color: #667eea; font-size: 20px; font-weight: bold;');
console.log('%c Built with passion for AI & NLP', 'color: #764ba2; font-size: 14px;');
