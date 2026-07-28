document.addEventListener('DOMContentLoaded', () => {
    const navContainer = document.getElementById('category-nav');
    const menuContainer = document.getElementById('menu-container');

    // Make sure menuData is loaded
    if (typeof menuData === 'undefined') {
        menuContainer.innerHTML = '<p>Error loading menu data.</p>';
        return;
    }

    const { categories, items } = menuData;

    // Render Categories
    categories.forEach((cat, index) => {
        const a = document.createElement('a');
        a.href = `#${cat.id}`;
        a.className = `cat-link ${index === 0 ? 'active' : ''}`;
        a.textContent = cat.name;
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
        header.textContent = cat.name;
        section.appendChild(header);

        // Add Grid
        const grid = document.createElement('div');
        grid.className = 'items-grid';

        // Add Items
        catItems.forEach(item => {
            const card = document.createElement('div');
            card.className = 'food-box';

            card.innerHTML = `
                <div class="food-img">
                    <img src="${item.image || 'https://via.placeholder.com/150'}" alt="${item.name}" loading="lazy">
                </div>
                <div class="food-detail">
                    <div class="star-badge"><i class="fas fa-star"></i> 0.0</div>
                    <h3 class="food-title">${item.name}</h3>
                    ${item.description ? `<div class="food-desc">${item.description}</div>` : ''}
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

    // Intersection Observer for scroll spy
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
});
