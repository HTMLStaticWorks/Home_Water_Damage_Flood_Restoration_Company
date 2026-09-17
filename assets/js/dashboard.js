/**
 * Dashboard Logic
 */

document.addEventListener('DOMContentLoaded', () => {
    // Navigation Logic
    const navButtons = document.querySelectorAll('.nav-btn');
    const views = document.querySelectorAll('.dashboard-view');
    const pageTitle = document.getElementById('pageTitle');
    
    // Also attach to buttons with 'nav-link' class inside views
    const inlineLinks = document.querySelectorAll('.nav-link');

    const switchView = (targetId, btnElement = null) => {
        // Hide all views
        views.forEach(view => {
            view.classList.add('hidden');
            view.classList.remove('block');
        });

        // Remove active state from nav buttons
        navButtons.forEach(nav => {
            nav.classList.remove('active', 'bg-primary-50', 'text-primary-600', 'dark:bg-primary-900/30', 'dark:text-primary-400');
            nav.classList.add('text-gray-600', 'dark:text-gray-400');
        });

        // Show target view
        const targetView = document.getElementById('view-' + targetId);
        if (targetView) {
            targetView.classList.remove('hidden');
            targetView.classList.add('block');
        }

        // Set active state on corresponding nav button
        const activeNav = document.querySelector(`.nav-btn[data-target="${targetId}"]`);
        if (activeNav) {
            activeNav.classList.remove('text-gray-600', 'dark:text-gray-400');
            activeNav.classList.add('active', 'bg-primary-50', 'text-primary-600', 'dark:bg-primary-900/30', 'dark:text-primary-400');
            
            // Update Title
            if(pageTitle) {
                // simple mapping
                const titleMap = {
                    'overview': 'Dashboard Overview',
                    'request': 'Emergency Request',
                    'jobs': 'My Jobs',
                    'tracking': 'Crew Tracking',
                    'drying': 'Drying Progress',
                    'documents': 'Insurance Documents',
                    'invoices': 'Invoices',
                    'settings': 'Account Settings'
                };
                pageTitle.textContent = titleMap[targetId] || 'Dashboard';
            }
        }

        // Auto close sidebar on mobile if open
        const sidebar = document.getElementById('sidebar');
        if (window.innerWidth < 768 && !sidebar.classList.contains('hidden')) {
            sidebar.classList.add('hidden');
            sidebar.classList.remove('flex');
        }
    };

    navButtons.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const target = btn.getAttribute('data-target');
            switchView(target, btn);
        });
    });

    inlineLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            const target = link.getAttribute('data-target');
            switchView(target);
        });
    });

    // Mobile Sidebar Toggle
    const openSidebarBtn = document.getElementById('openSidebar');
    const closeSidebarBtn = document.getElementById('closeSidebar');
    const sidebar = document.getElementById('sidebar');

    if (openSidebarBtn && sidebar) {
        openSidebarBtn.addEventListener('click', () => {
            sidebar.classList.remove('hidden');
            sidebar.classList.add('flex', 'w-full', 'sm:w-64');
        });
    }

    if (closeSidebarBtn && sidebar) {
        closeSidebarBtn.addEventListener('click', () => {
            sidebar.classList.add('hidden');
            sidebar.classList.remove('flex', 'w-full', 'sm:w-64');
        });
    }

    // Theme Toggle inside dashboard
    const themeToggleBtn = document.getElementById('themeToggle');
    const htmlElement = document.documentElement;

    if (themeToggleBtn) {
        themeToggleBtn.addEventListener('click', function() {
            if (htmlElement.classList.contains('dark')) {
                htmlElement.classList.remove('dark');
                localStorage.setItem('color-theme', 'light');
            } else {
                htmlElement.classList.add('dark');
                localStorage.setItem('color-theme', 'dark');
            }
        });
    }
});
