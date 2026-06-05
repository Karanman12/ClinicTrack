/**
 * Scroll-Triggered Animations Module (Optimized for Performance)
 * Uses passive event listeners, requestAnimationFrame, GPU acceleration
 */

let scrollObserver;
let scrollDirection = 'down';
let lastScrollTop = 0;
let isScrolling = false;
let scrollTimeout;

/**
 * Optimized Scroll Direction Detection with throttling
 */
function initScrollDirectionDetection() {
    let ticking = false;
    
    window.addEventListener('scroll', () => {
        if (!ticking) {
            window.requestAnimationFrame(() => {
                const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
                
                if (scrollTop > lastScrollTop) {
                    scrollDirection = 'down';
                } else if (scrollTop < lastScrollTop) {
                    scrollDirection = 'up';
                }
                
                lastScrollTop = scrollTop <= 0 ? 0 : scrollTop;
                ticking = false;
            });
            ticking = true;
        }
    }, { passive: true });
}

/**
 * Optimized Intersection Observer for Scroll Animations
 * Uses minimal configuration for max performance
 */
function createScrollObserver() {
    const observerOptions = {
        root: null,
        rootMargin: '0px 0px -50px 0px',
        threshold: 0.1
    };

    scrollObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const element = entry.target;
                const delay = parseInt(element.dataset.animationDelay) || 0;
                
                if (delay > 0) {
                    setTimeout(() => {
                        element.classList.add('in-view');
                    }, delay);
                } else {
                    element.classList.add('in-view');
                }
                
                scrollObserver.unobserve(element);
            }
        });
    }, observerOptions);
}

/**
 * Auto-apply scroll animations with GPU acceleration hints
 */
function autoApplyScrollAnimations() {
    const animationClasses = [
        'scroll-fade-in',
        'scroll-slide-left',
        'scroll-slide-right',
        'scroll-scale'
    ];

    animationClasses.forEach(className => {
        const elements = document.querySelectorAll(`.${className}`);
        elements.forEach((el, index) => {
            if (!el.dataset.animationDelay) {
                el.dataset.animationDelay = Math.min(index * 40, 200);
            }
            scrollObserver.observe(el);
        });
    });

    const tableRows = document.querySelectorAll('tbody tr:not([data-no-scroll-animation])');
    tableRows.forEach((row, index) => {
        if (!row.classList.contains('scroll-fade-in')) {
            row.classList.add('scroll-fade-in');
            row.dataset.animationDelay = Math.min(index * 20, 150);
        }
        scrollObserver.observe(row);
    });
}

/**
 * Observe new elements (for dynamic content)
 */
function observeScrollElements(elements) {
    if (!scrollObserver) createScrollObserver();
    
    const elementsArray = elements instanceof NodeList ? Array.from(elements) : [elements];
    
    elementsArray.forEach(el => {
        if (el && !el.classList.contains('in-view')) {
            scrollObserver.observe(el);
        }
    });
}

/**
 * Initialize scroll animations
 */
function initScrollAnimations() {
    if (!scrollObserver) {
        createScrollObserver();
        initScrollDirectionDetection();
        
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', autoApplyScrollAnimations);
        } else {
            autoApplyScrollAnimations();
        }
    }
}

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initScrollAnimations);
} else {
    initScrollAnimations();
}

window.scrollAnimations = {
    observe: observeScrollElements,
    init: initScrollAnimations
};
