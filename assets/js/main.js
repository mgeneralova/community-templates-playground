// ========================================
// Zabbix Community Templates Portal
// Main JavaScript
// ========================================

document.addEventListener('DOMContentLoaded', function() {
    // Initialize features
    initNavigation();
    initCards();
    initFilters();
    initGiscus();
    initSearch();
});

/**
 * Initialize Navigation Features
 */
function initNavigation() {
    const navbar = document.querySelector('.navbar');
    
    // Scroll behavior
    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) {
            navbar?.classList.add('scrolled');
        } else {
            navbar?.classList.remove('scrolled');
        }
    });
}

/**
 * Initialize Card Animations
 */
function initCards() {
    const cards = document.querySelectorAll('.card');
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1
    });
    
    cards.forEach(card => observer.observe(card));
}

/**
 * Initialize Filter Functionality
 */
function initFilters() {
    const urlParams = new URLSearchParams(window.location.search);
    const tagFilter = urlParams.get('tag');
    const categoryFilter = urlParams.get('category');
    
    if (tagFilter) {
        filterByTag(tagFilter);
    }
    
    if (categoryFilter) {
        filterByCategory(categoryFilter);
    }
}

/**
 * Filter Cards by Tag
 */
function filterByTag(tag) {
    const cards = document.querySelectorAll('.card');
    
    cards.forEach(card => {
        const tags = card.querySelectorAll('.tag');
        const hasTag = Array.from(tags).some(t => t.textContent.trim() === tag);
        
        if (hasTag) {
            card.style.display = 'block';
            card.classList.add('fade-in');
        } else {
            card.style.display = 'none';
        }
    });
}

/**
 * Filter Cards by Category
 */
function filterByCategory(category) {
    const cards = document.querySelectorAll('.card');
    
    cards.forEach(card => {
        const categories = card.querySelectorAll('[data-category]');
        const hasCategory = Array.from(categories).some(cat => cat.dataset.category === category);
        
        if (hasCategory) {
            card.style.display = 'block';
            card.classList.add('fade-in');
        } else {
            card.style.display = 'none';
        }
    });
}

/**
 * Initialize Giscus Comments
 */
function initGiscus() {
    const giscusContainer = document.querySelector('.giscus-container');
    
    if (giscusContainer) {
        const script = document.createElement('script');
        script.src = 'https://giscus.app/client.js';
        script.setAttribute('data-repo', giscusContainer.dataset.repo);
        script.setAttribute('data-repo-id', giscusContainer.dataset.repoId);
        script.setAttribute('data-category', giscusContainer.dataset.category);
        script.setAttribute('data-category-id', giscusContainer.dataset.categoryId);
        script.setAttribute('data-mapping', giscusContainer.dataset.mapping);
        script.setAttribute('data-strict', giscusContainer.dataset.strict);
        script.setAttribute('data-reactions-enabled', giscusContainer.dataset.reactionsEnabled);
        script.setAttribute('data-emit-metadata', giscusContainer.dataset.emitMetadata);
        script.setAttribute('data-input-position', giscusContainer.dataset.inputPosition);
        script.setAttribute('data-theme', giscusContainer.dataset.theme);
        script.setAttribute('data-lang', giscusContainer.dataset.lang);
        script.setAttribute('crossorigin', 'anonymous');
        script.setAttribute('async', '');
        
        giscusContainer.appendChild(script);
    }
}

/**
 * Initialize Search Functionality
 */
function initSearch() {
    const searchInput = document.querySelector('.search-input');
    
    if (searchInput) {
        searchInput.addEventListener('input', function(e) {
            const query = e.target.value.toLowerCase();
            const cards = document.querySelectorAll('.card');
            
            cards.forEach(card => {
                const title = card.querySelector('.card-title')?.textContent.toLowerCase() || '';
                const description = card.querySelector('.card-description')?.textContent.toLowerCase() || '';
                
                if (title.includes(query) || description.includes(query)) {
                    card.style.display = 'block';
                } else {
                    card.style.display = 'none';
                }
            });
        });
    }
}

/**
 * Utility: Copy to Clipboard
 */
function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(() => {
        showNotification('Copied to clipboard!', 'success');
    }).catch(() => {
        showNotification('Failed to copy', 'error');
    });
}

/**
 * Utility: Show Notification
 */
function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.textContent = message;
    
    document.body.appendChild(notification);
    
    setTimeout(() => {
        notification.style.opacity = '0';
        setTimeout(() => notification.remove(), 300);
    }, 3000);
}

/**
 * Utility: Debounce Function
 */
function debounce(func, wait) {
    let timeout;
    return function(...args) {
        clearTimeout(timeout);
        timeout = setTimeout(() => func.apply(this, args), wait);
    };
}

// Export functions for external use
window.Templates = {
    filterByTag,
    filterByCategory,
    copyToClipboard,
    showNotification
};
