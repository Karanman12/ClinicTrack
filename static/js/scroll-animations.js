/**
 * Scroll-Triggered Animations Module
 * Professional implementation using Intersection Observer API
 * Handles scroll-down content loading and smooth upward content appearance
 */

let scrollObserver;
let scrollDirection = 'down';
let lastScrollTop = 0;

/**
 * Initialize Scroll Direction Detection
 */
function initScrollDirectionDetection() {
    window.addEventListener('scroll', () => {
        const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        
        if (scrollTop > lastScrollTop) {
            scrollDirection = 'down';
        } else if (scrollTop < lastScrollTop) {
            scrollDirection = 'up';
        }
        
        lastScrollTop = scrollTop <= 0 ? 0 : scrollTop;
    }, { passive: true });
}

/**
 * Create Intersection Observer for Scroll Animations
 * Detects when elements enter/leave viewport and triggers animations
 */
function createScrollObserver() {
    const observerOptions = {
        root: null,
        rootMargin: '0px 0px -100px 0px', // Trigger slightly before element fully enters viewport
        threshold: [0, 0.25, 0.5, 0.75, 1]
    };

    scrollObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const element = entry.target;
                
                // Get animation delay from data attribute (for staggered animations)
                const delay = element.dataset.animationDelay || 0;
                
                // Apply animation based on scroll direction
                if (scrollDirection === 'down') {
                    // Downward scroll: fade in from bottom
                    setTimeout(() => {
                        element.classList.add('in-view');
                    }, parseInt(delay));
                } else if (scrollDirection === 'up') {
                    // Upward scroll: smooth appearance with easing
                    setTimeout(() => {
                        element.classList.add('in-view');
                    }, parseInt(delay));
                }
                
                // Unobserve after animation to save performance
                scrollObserver.unobserve(element);
            }
        });
    }, observerOptions);
}

/**
 * Auto-assign scroll animations to common content elements
 * Classes: scroll-fade-in, scroll-slide-left, scroll-slide-right, scroll-scale
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
            // Add staggered animation delay for lists/grids
            if (!el.dataset.animationDelay) {
                el.dataset.animationDelay = index * 50; // 50ms between each element
            }
            scrollObserver.observe(el);
        });
    });

    // Auto-apply to table rows for smooth content loading
    const tableRows = document.querySelectorAll('tbody tr:not([data-no-scroll-animation])');
    tableRows.forEach((row, index) => {
        if (!row.classList.contains('scroll-fade-in')) {
            row.classList.add('scroll-fade-in');
            row.dataset.animationDelay = index * 30; // 30ms stagger for rows
        }
        scrollObserver.observe(row);
    });

    // Auto-apply to cards/containers
    const cards = document.querySelectorAll('[data-card]:not([data-no-scroll-animation])');
    cards.forEach((card, index) => {
        if (!card.classList.contains('scroll-fade-in') && !card.classList.contains('scroll-scale')) {
            card.classList.add('scroll-fade-in');
            card.dataset.animationDelay = index * 50;
        }
        scrollObserver.observe(card);
    });
}

/**
 * Manually observe elements with scroll animations
 * Usage: Call this after dynamically adding content
 */
function observeScrollElements(elements) {
    if (!scrollObserver) createScrollObserver();
    
    elements = elements instanceof NodeList ? Array.from(elements) : [elements];
    
    elements.forEach(el => {
        if (el && !el.classList.contains('in-view')) {
            scrollObserver.observe(el);
        }
    });
}

/**
 * Initialize all scroll animation features
 */
function initScrollAnimations() {
    if (!scrollObserver) {
        createScrollObserver();
        initScrollDirectionDetection();
        
        // Apply animations when DOM is ready
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', autoApplyScrollAnimations);
        } else {
            autoApplyScrollAnimations();
        }
    }
}

// Auto-initialize on script load
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initScrollAnimations);
} else {
    initScrollAnimations();
}

// Expose for manual usage
window.scrollAnimations = {
    observe: observeScrollElements,
    init: initScrollAnimations
};
