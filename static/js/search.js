document.addEventListener("DOMContentLoaded", function () {
  const searchInput = document.getElementById("searchInput");
  const modal = document.getElementById("searchModal");
  const modalInput = document.getElementById("modalSearchInput");
  const closeModal = document.getElementById("closeSearchModal");
  const resultsContainer = document.getElementById("searchResults");

  let searchData = [];

  fetch("/index.json")
    .then(res => res.json())
    .then(data => { searchData = data; })
    .catch(err => console.log("Search index error:", err));

  function openSearch(initialQuery) {
    if (!modal) return;
    modal.style.display = "flex";
    if (typeof initialQuery === 'string' && modalInput) {
      modalInput.value = initialQuery;
    }
    if (modalInput) {
      modalInput.focus();
      doSearch(modalInput.value);
    }
  }

  function closeSearch() {
    if (!modal) return;
    modal.style.display = "none";
  }

  function escapeHtml(str) {
    if (!str) return '';
    return str.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;").replace(/'/g, "&#039;");
  }

  function arrayOrStr(val) {
    if (!val) return '';
    if (Array.isArray(val)) return val.join(' ');
    return String(val);
  }

  function doSearch(rawQuery) {
    if (!resultsContainer) return;
    const q = (rawQuery || '').trim().toLowerCase();
    
    if (!q) {
      if (searchData.length > 0) {
        const defaultItems = searchData.slice(0, 5);
        resultsContainer.innerHTML = '<div style="font-size:0.85rem;color:#64748b;margin-bottom:10px;font-weight:600;">🔥 热门推荐教程：</div>' + 
          defaultItems.map(item => `
            <div class="search-result-item">
              <h4><a href="${escapeHtml(item.permalink)}">${escapeHtml(item.title)}</a></h4>
              <p>${escapeHtml((item.summary || item.description || '').substring(0, 90))}...</p>
            </div>
          `).join("");
      } else {
        resultsContainer.innerHTML = "";
      }
      return;
    }

    const scored = [];

    for (let i = 0; i < searchData.length; i++) {
      const item = searchData[i];
      const title = (item.title || "").toLowerCase();
      const summary = (item.summary || "").toLowerCase();
      const desc = (item.description || "").toLowerCase();
      const content = (item.content || "").toLowerCase();
      const keywords = arrayOrStr(item.keywords).toLowerCase();
      const synonyms = arrayOrStr(item.synonyms).toLowerCase();
      const tags = arrayOrStr(item.tags).toLowerCase();
      const category = arrayOrStr(item.category).toLowerCase();
      const provider = (item.provider || "").toLowerCase();

      let score = 0;

      if (title.includes(q)) score += 100;
      if (keywords.includes(q)) score += 50;
      if (tags.includes(q)) score += 40;
      if (provider.includes(q)) score += 40;
      if (category.includes(q)) score += 30;
      if (desc.includes(q)) score += 20;
      if (summary.includes(q)) score += 15;
      if (synonyms.includes(q)) score += 15;
      if (content.includes(q)) score += 5;

      if (score > 0) {
        scored.push({ item, score });
      }
    }

    scored.sort((a, b) => b.score - a.score);

    if (scored.length === 0) {
      resultsContainer.innerHTML = `<p style="color:#64748b;padding:16px;text-align:center;">没有找到与「<strong>${escapeHtml(rawQuery.trim())}</strong>」相关的内容</p>`;
      return;
    }

    const matches = scored.slice(0, 15).map(s => s.item);

    resultsContainer.innerHTML = matches.map(item => `
      <div class="search-result-item">
        <h4><a href="${escapeHtml(item.permalink)}">${escapeHtml(item.title)}</a></h4>
        <p>${escapeHtml((item.summary || item.description || '').substring(0, 90))}...</p>
      </div>
    `).join("");
  }

  if (searchInput) {
    searchInput.addEventListener("focus", function() {
      openSearch(this.value);
    });
    searchInput.addEventListener("input", function() {
      openSearch(this.value);
    });
  }

  if (closeModal) closeModal.addEventListener("click", closeSearch);

  document.addEventListener("keydown", function (e) {
    if ((e.ctrlKey || e.metaKey) && e.key === "k") {
      e.preventDefault();
      openSearch(searchInput ? searchInput.value : '');
    }
    if (e.key === "Escape") closeSearch();
  });

  if (modalInput) {
    modalInput.addEventListener("input", function () {
      if (searchInput) searchInput.value = this.value;
      doSearch(this.value);
    });
    modalInput.addEventListener("keyup", function () {
      doSearch(this.value);
    });
  }
});
