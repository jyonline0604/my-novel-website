document.addEventListener('DOMContentLoaded', () => {
    // --- 全局設定與主題邏輯 ---
    const savedSettings = JSON.parse(localStorage.getItem('novel-settings')) || {};
    let currentTheme = savedSettings.theme || 'light-mode';
    const currentFontSize = savedSettings.fontSize || 'medium';

    function applyTheme(theme) {
        document.body.className = theme;
        const giscusFrame = document.querySelector('iframe.giscus-frame');
        if (giscusFrame) {
            const giscusThemeMap = { 'light-mode': 'light', 'dark-mode': 'dark', 'sepia-mode': 'light_tritanopia', 'sky-blue-mode': 'light', 'light-green-mode': 'light' };
            giscusFrame.contentWindow.postMessage({ giscus: { setConfig: { theme: giscusThemeMap[theme] || 'light' } } }, 'https://giscus.app');
        }
    }
    
    function applyFontSize(size) {
        const article = document.getElementById('reader-article');
        if (article) {
            article.className = `reader-article font-size-${size}`;
        }
    }

    applyTheme(currentTheme);
    applyFontSize(currentFontSize);

    // --- 主頁 (index.html) 專屬邏輯 ---
    const continueReadingBtn = document.getElementById('continue-reading-btn');
    if (continueReadingBtn) {
        const lastReadChapter = localStorage.getItem('novel-last-read');
        if (lastReadChapter) {
            continueReadingBtn.style.display = 'inline-flex';
            continueReadingBtn.href = lastReadChapter;
            
            const chapterLinks = document.querySelectorAll('.chapter-link');
            chapterLinks.forEach(link => {
                if (lastReadChapter.endsWith(link.getAttribute('href'))) {
                    link.parentElement.classList.add('is-last-read');
                }
            });
        }
    }

    const backToTopBtn = document.getElementById('back-to-top-btn');
    if (backToTopBtn) {
        window.addEventListener('scroll', () => {
            backToTopBtn.classList.toggle('show', window.scrollY > 300);
        });
        backToTopBtn.addEventListener('click', () => {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }

    const indexThemeBtn = document.querySelector('.main-header #theme-toggle-btn');
    if (indexThemeBtn) {
        const themeIcon = indexThemeBtn.querySelector('i');
        function updateIcon(theme) {
            themeIcon.className = theme === 'dark-mode' ? 'fas fa-sun' : 'fas fa-moon';
        }
        updateIcon(currentTheme);
        indexThemeBtn.addEventListener('click', () => {
            currentTheme = document.body.classList.contains('light-mode') ? 'dark-mode' : 'light-mode';
            savedSettings.theme = currentTheme;
            localStorage.setItem('novel-settings', JSON.stringify(savedSettings));
            applyTheme(currentTheme);
            updateIcon(currentTheme);
        });
    }

    // --- 章節頁面 (chapter-*.html) 專屬邏輯 ---
    const settingsPanel = document.getElementById('settings-panel');
    if (settingsPanel) {
        localStorage.setItem('novel-last-read', window.location.href);

        const settingsBtn = document.getElementById('settings-btn');
        const fontSizeOptions = document.getElementById('font-size-options');
        const themeOptions = document.getElementById('theme-options');

        function updateSettingsUI(theme, size) {
            document.querySelector('#theme-options .active')?.classList.remove('active');
            document.querySelector('#font-size-options .active')?.classList.remove('active');
            document.querySelector(`#theme-options button[data-theme="${theme}"]`)?.classList.add('active');
            document.querySelector(`#font-size-options button[data-size="${size}"]`)?.classList.add('active');
        }
        updateSettingsUI(currentTheme, currentFontSize);

        settingsBtn.addEventListener('click', (e) => { e.stopPropagation(); settingsPanel.classList.toggle('show'); });
        document.addEventListener('click', (e) => { if (!settingsPanel.contains(e.target) && !settingsBtn.contains(e.target)) { settingsPanel.classList.remove('show'); } });

        fontSizeOptions.addEventListener('click', (e) => {
            if (e.target.tagName === 'BUTTON') {
                const newSize = e.target.dataset.size;
                savedSettings.fontSize = newSize;
                localStorage.setItem('novel-settings', JSON.stringify(savedSettings));
                applyFontSize(newSize);
                updateSettingsUI(currentTheme, newSize);
            }
        });

        themeOptions.addEventListener('click', (e) => {
            if (e.target.tagName === 'BUTTON') {
                const newTheme = e.target.dataset.theme;
                currentTheme = newTheme;
                savedSettings.theme = newTheme;
                localStorage.setItem('novel-settings', JSON.stringify(savedSettings));
                applyTheme(newTheme);
                updateSettingsUI(newTheme, savedSettings.fontSize || 'medium');
            }
        });

        const prevBtn = document.getElementById('prev-chapter-btn');
        const nextBtn = document.getElementById('next-chapter-btn');
        document.addEventListener('keydown', (e) => {
            if (e.key === 'ArrowLeft' && !prevBtn.classList.contains('disabled')) window.location.href = prevBtn.href;
            if (e.key === 'ArrowRight' && !nextBtn.classList.contains('disabled')) window.location.href = nextBtn.href;
        });

        const pageUrl = window.location.href;
        const pageTitle = document.title;
        document.getElementById('share-facebook').addEventListener('click', (e) => { e.preventDefault(); window.open(`https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(pageUrl)}`, 'facebook-share', 'width=580,height=296'); });
        document.getElementById('share-twitter').addEventListener('click', (e) => { e.preventDefault(); window.open(`https://twitter.com/intent/tweet?url=${encodeURIComponent(pageUrl)}&text=${encodeURIComponent(pageTitle)}`, 'twitter-share', 'width=550,height=420'); });
        document.getElementById('share-line').addEventListener('click', (e) => { e.preventDefault(); window.open(`https://social-plugins.line.me/lineit/share?url=${encodeURIComponent(pageUrl)}`, 'line-share', 'width=500,height=500'); });
        document.getElementById('copy-link-btn').addEventListener('click', (e) => {
            const btn = e.currentTarget; const icon = btn.querySelector('i'); const originalIconClass = icon.className;
            navigator.clipboard.writeText(pageUrl).then(() => {
                icon.className = 'fas fa-check'; btn.style.backgroundColor = '#2ecc71';
                setTimeout(() => { icon.className = originalIconClass; btn.style.backgroundColor = ''; }, 2000);
            }).catch(err => { console.error('無法複製連結: ', err); });
        });

        const giscusScript = document.createElement('script');
        const giscusAttributes = {
            "src": "https://giscus.app/client.js",
            "data-repo": "jyonline0604/my-novel-website",
            "data-repo-id": "R_kgDOPHnJng",
            "data-category": "Announcements",
            "data-category-id": "DIC_kwDOPHnJns4Csik6",
            "data-mapping": "pathname",
            "data-strict": "0",
            "data-reactions-enabled": "1",
            "data-emit-metadata": "0",
            "data-input-position": "bottom",
            "data-theme": currentTheme === 'dark-mode' ? 'dark' : (currentTheme === 'sepia-mode' ? 'light_tritanopia' : 'light'),
            "data-lang": "zh-TW",
            "crossorigin": "anonymous",
            "async": ""
        };
        Object.entries(giscusAttributes).forEach(([key, value]) => {
            giscusScript.setAttribute(key, value);
        });
        document.querySelector('.comment-section').appendChild(giscusScript);
    }
});
