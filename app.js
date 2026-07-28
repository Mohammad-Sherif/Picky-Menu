document.addEventListener('DOMContentLoaded', () => {
    const navContainer = document.getElementById('category-nav');
    const menuContainer = document.getElementById('menu-container');
    const langBtn = document.getElementById('lang-btn');

    // Default language
    let currentLang = 'en';

    // Make sure menuData is loaded
    if (typeof menuData === 'undefined') {
        menuContainer.innerHTML = '<p>Error loading menu data.</p>';
        return;
    }

    const { categories, items } = menuData;

    function renderMenu() {
        // Clear containers
        navContainer.innerHTML = '';
        menuContainer.innerHTML = '';

        // Set layout direction based on language
        document.body.dir = currentLang === 'ar' ? 'rtl' : 'ltr';

        // Render Categories
        categories.forEach((cat, index) => {
            const a = document.createElement('a');
            a.href = `#${cat.id}`;
            a.className = `cat-link ${index === 0 ? 'active' : ''}`;
            
            // Handle translations if available
            const name = currentLang === 'ar' && cat.name_ar ? cat.name_ar : cat.name;
            a.textContent = name;
            a.dataset.target = cat.id;
            navContainer.appendChild(a);

            // Click event for smooth scrolling and active state
            a.addEventListener('click', (e) => {
                e.preventDefault();
                document.querySelectorAll('.cat-link').forEach(link => link.classList.remove('active'));
                a.classList.add('active');
                
                const targetElement = document.getElementById(cat.id);
                if (targetElement) {
                    const headerOffset = 80;
                    const elementPosition = targetElement.getBoundingClientRect().top;
                    const offsetPosition = elementPosition + window.pageYOffset - headerOffset;
                    
                    window.scrollTo({
                        top: offsetPosition,
                        behavior: 'smooth'
                    });
                }
            });
        });

        // Render Menu Items
        categories.forEach(cat => {
            // Filter items for this category
            const catItems = items.filter(item => item.category_id === cat.id);
            if (catItems.length === 0) return;

            // Create Section
            const section = document.createElement('section');
            section.id = cat.id;
            section.className = 'category-section';

            // Add Header
            const header = document.createElement('h2');
            header.className = 'category-header';
            header.textContent = currentLang === 'ar' && cat.name_ar ? cat.name_ar : cat.name;
            section.appendChild(header);

            // Add Grid
            const grid = document.createElement('div');
            grid.className = 'items-grid';

            // Add Items
            catItems.forEach(item => {
                const card = document.createElement('div');
                card.className = 'food-box';

                const itemName = currentLang === 'ar' && item.name_ar ? item.name_ar : item.name;
                const itemDesc = currentLang === 'ar' && item.description_ar ? item.description_ar : item.description;

                card.innerHTML = `
                    <div class="food-img">
                        <img src="${item.image || 'https://via.placeholder.com/150'}" alt="${itemName}" loading="lazy">
                    </div>
                    <div class="food-detail">
                        <h3 class="food-title">${itemName}</h3>
                        ${itemDesc ? `<div class="food-desc">${itemDesc}</div>` : ''}
                        <div class="price-container">
                            <span class="price">${item.price}</span>
                        </div>
                    </div>
                `;
                grid.appendChild(card);
            });

            section.appendChild(grid);
            menuContainer.appendChild(section);
        });

        setupIntersectionObserver();
    }

    function setupIntersectionObserver() {
        const sections = document.querySelectorAll('.category-section');
        const navLinks = document.querySelectorAll('.cat-link');

        const observerOptions = {
            root: null,
            rootMargin: '-100px 0px -60% 0px',
            threshold: 0
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const id = entry.target.getAttribute('id');
                    navLinks.forEach(link => {
                        link.classList.remove('active');
                        if (link.dataset.target === id) {
                            link.classList.add('active');
                            // Optional: scroll nav container to active link
                            link.scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'center' });
                        }
                    });
                }
            });
        }, observerOptions);

        sections.forEach(section => observer.observe(section));
    }

    // Toggle Language Button
    langBtn.addEventListener('click', () => {
        if (currentLang === 'en') {
            currentLang = 'ar';
            langBtn.textContent = 'English';
        } else {
            currentLang = 'en';
            langBtn.textContent = 'عربي';
        }
        renderMenu();
    });

    // Initial render
    renderMenu();
});
