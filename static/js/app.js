document.addEventListener('DOMContentLoaded', () => {
    // Initialize Feather Icons
    if (typeof feather !== 'undefined') {
        feather.replace();
    }

    // 1. Mobile Sidebar Toggle
    initMobileSidebar();

    // 2. Confirm Delete Modals
    initDeleteConfirmations();

    // 3. Client-Side Patient Search
    initPatientSearch();

    // 4. Form Validation and Loading Indicators
    initFormInteractions();

    // 5. Scroll-Triggered Animations
    if (window.scrollAnimations) {
        window.scrollAnimations.init();
    }
});

/**
 * Mobile Sidebar Toggle Logic
 */
function initMobileSidebar() {
    const mobileMenuBtn = document.getElementById('mobile-sidebar-toggle');
    const sidebar = document.getElementById('sidebar');
    const backdrop = document.getElementById('mobile-sidebar-backdrop');

    if (mobileMenuBtn && sidebar && backdrop) {
        const toggleMenu = () => {
            const isOpen = !sidebar.classList.contains('-translate-x-full');
            if (isOpen) {
                sidebar.classList.add('-translate-x-full');
                sidebar.classList.remove('translate-x-0');
                backdrop.classList.add('hidden');
            } else {
                sidebar.classList.remove('-translate-x-full');
                sidebar.classList.add('translate-x-0');
                backdrop.classList.remove('hidden');
            }
        };

        mobileMenuBtn.addEventListener('click', toggleMenu);
        backdrop.addEventListener('click', toggleMenu);
    }
}

/**
 * Confirm Delete Interception
 */
function initDeleteConfirmations() {
    const deleteForms = document.querySelectorAll('form[action*="delete"]');
    deleteForms.forEach(form => {
        form.addEventListener('submit', (e) => {
            if (!confirm("Are you sure you want to delete this record? This action is permanent and cannot be undone.")) {
                e.preventDefault();
            }
        });
    });
}

/**
 * Client-Side Patient Search
 * Filters table rows immediately based on user input
 */
function initPatientSearch() {
    const searchInput = document.querySelector('input[name="search"]');
    if (searchInput) {
        searchInput.addEventListener('input', (e) => {
            const query = e.target.value.toLowerCase();
            const rows = document.querySelectorAll('table tbody tr');
            
            let visibleCount = 0;
            rows.forEach(row => {
                // Skip the "No patients found" row
                if (row.querySelector('td[colspan]')) return;
                
                const text = row.textContent.toLowerCase();
                if (text.includes(query)) {
                    row.style.display = '';
                    visibleCount++;
                } else {
                    row.style.display = 'none';
                }
            });

            // Handle Empty State dynamically
            let emptyStateRow = document.querySelector('#empty-state-row');
            if (visibleCount === 0 && query !== '') {
                if (!emptyStateRow) {
                    const tbody = document.querySelector('table tbody');
                    const colcount = document.querySelectorAll('table thead th').length;
                    emptyStateRow = document.createElement('tr');
                    emptyStateRow.id = 'empty-state-row';
                    emptyStateRow.innerHTML = `
                        <td colspan="${colcount}" class="px-6 py-12 text-center text-slate-500 text-sm">
                            No matching results found for "${query}"
                        </td>
                    `;
                    tbody.appendChild(emptyStateRow);
                } else {
                    emptyStateRow.style.display = '';
                    emptyStateRow.querySelector('td').innerText = `No matching results found for "${query}"`;
                }
            } else if (emptyStateRow) {
                emptyStateRow.style.display = 'none';
            }
        });
    }
}

/**
 * Form Validation and Submit Loading States
 */
function initFormInteractions() {
    const forms = document.querySelectorAll('form:not([action*="delete"])');
    forms.forEach(form => {
        form.addEventListener('submit', (e) => {
            // HTML5 validation
            if (!form.checkValidity()) {
                e.preventDefault();
                showToast('Please fill out all required fields properly.', 'error');
                return;
            }
            
            // Set loading state on submit button
            const submitBtn = form.querySelector('button[type="submit"]');
            if (submitBtn) {
                const originalContent = submitBtn.innerHTML;
                const originalWidth = submitBtn.offsetWidth;
                
                // Keep dimensions to prevent layout shift
                submitBtn.style.width = `${originalWidth}px`;
                submitBtn.disabled = true;
                submitBtn.classList.add('opacity-80', 'cursor-not-allowed');
                
                submitBtn.innerHTML = `
                    <svg class="animate-spin h-4 w-4 text-white mx-auto" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                        <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                        <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z"></path>
                    </svg>
                `;

                // Timeout fallback in case response takes too long or fails
                setTimeout(() => {
                    submitBtn.disabled = false;
                    submitBtn.classList.remove('opacity-80', 'cursor-not-allowed');
                    submitBtn.innerHTML = originalContent;
                    submitBtn.style.width = '';
                }, 8000);
            }
        });
    });
}

/**
 * Toast Notification System
 * Example usage: showToast('Patient saved successfully', 'success')
 */
function showToast(message, type = 'info') {
    let container = document.getElementById('toast-container');
    if (!container) {
        container = document.createElement('div');
        container.id = 'toast-container';
        container.className = 'fixed bottom-6 right-6 z-50 flex flex-col gap-3 pointer-events-none';
        document.body.appendChild(container);
    }

    const toast = document.createElement('div');
    
    // Style configurations based on type
    const colors = {
        error: 'bg-white border-red-200 text-red-800 border-l-4 border-l-red-500',
        success: 'bg-white border-emerald-200 text-emerald-800 border-l-4 border-l-emerald-500',
        info: 'bg-white border-blue-200 text-blue-800 border-l-4 border-l-blue-500'
    };
    
    const icons = {
        error: 'alert-circle',
        success: 'check-circle',
        info: 'info'
    };

    const bgClass = colors[type] || colors.info;
    const icon = icons[type] || icons.info;

    toast.className = `p-4 rounded-xl shadow-lg border w-80 pointer-events-auto flex items-start gap-3 toast-enter ${bgClass}`;
    toast.innerHTML = `
        <div class="mt-0.5">
            <i data-feather="${icon}" class="w-5 h-5 ${type === 'error' ? 'text-red-500' : type === 'success' ? 'text-emerald-500' : 'text-blue-500'}"></i>
        </div>
        <div class="flex-1 text-sm font-medium text-slate-700">${message}</div>
        <button onclick="this.parentElement.remove()" class="text-slate-400 hover:text-slate-600 focus:outline-none shrink-0 transition-colors">
            <i data-feather="x" class="w-4 h-4"></i>
        </button>
    `;

    container.appendChild(toast);
    if (typeof feather !== 'undefined') feather.replace();

    // Auto remove after 4 seconds
    setTimeout(() => {
        toast.style.animation = 'fadeIn 0.3s cubic-bezier(0.16, 1, 0.3, 1) reverse forwards';
        setTimeout(() => toast.remove(), 300);
    }, 4000);
}
