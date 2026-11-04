// Image lightbox: click a screenshot to view it full size, Esc or click to close.
document.querySelectorAll('.screenshot-item img, .school-project-images img, .lightbox-img, .image-block img').forEach(img => {
    img.addEventListener('click', () => {
        const overlay = document.createElement('div');
        overlay.className = 'lightbox-overlay';
        overlay.setAttribute('role', 'dialog');
        overlay.setAttribute('aria-label', img.alt || '이미지 크게 보기');

        const big = document.createElement('img');
        big.src = img.src;
        big.alt = img.alt;

        const close = document.createElement('button');
        close.className = 'lightbox-close';
        close.setAttribute('aria-label', '닫기');
        close.textContent = '×';

        overlay.append(big, close);
        document.body.appendChild(overlay);
        document.body.style.overflow = 'hidden';
        close.focus();

        const dismiss = () => {
            overlay.remove();
            document.body.style.overflow = '';
            document.removeEventListener('keydown', onKey);
            img.focus?.();
        };
        const onKey = e => { if (e.key === 'Escape') dismiss(); };
        overlay.addEventListener('click', dismiss);
        document.addEventListener('keydown', onKey);
    });
});
