# 🏷️ MARKUP Exam Prep Suite — ETE1AE

**Course:** Markup Languages & Data Formats (INFOA4)  
**Code:** ETE1AE | CZU Prague  
**Exam type:** Practical — writing real HTML/XML/CSS/XPath/XSLT code

---

## 📁 Files

| File | Description |
|------|-------------|
| `index.html` | Main dashboard — definitions matcher, code snippets, interactive tools |
| `smart_cram_cards.html` | 55 high-yield 3D flip flashcards with rating system |
| `README.md` | This file |

---

## 🚀 Quick Start

1. **Open `index.html`** in any modern browser (Chrome, Firefox, Edge)
2. **No server needed** — all files are self-contained HTML
3. Use **Cram mode** (header toggle) to hide the tools and focus on the matcher
4. Visit **Cram Cards** for flashcard study

---

## 📚 Topic Coverage

### 1. HTML5
- Semantic elements: `<header>`, `<nav>`, `<main>`, `<article>`, `<section>`, `<aside>`, `<footer>`, `<figure>`, `<time>`
- Forms: `method`, `action`, `input types`, `label`, `fieldset`
- Tables: `thead`, `tbody`, `tfoot`, `th`, `td`, `colspan`, `rowspan`
- Meta tags: `charset`, `viewport`, `name/content`
- Accessibility: `alt`, `aria-*`, `label for`, `semantic structure`
- `defer` vs `async`, `data-*` attributes, HTML entities

### 2. CSS
- Selectors: element, class, ID, attribute, descendant, child, adjacent
- Box model: content, padding, border, margin, `box-sizing`
- Flexbox: `display:flex`, `justify-content`, `align-items`, `flex-direction`, `flex-wrap`, `gap`
- Grid: `display:grid`, `grid-template-columns`, `fr`, `repeat()`, `span`, `gap`
- Specificity: `(a,b,c)` — IDs, Classes, Elements
- Pseudo-classes: `:hover`, `:focus`, `:nth-child()`, `:not()`
- Pseudo-elements: `::before`, `::after`, `::placeholder`
- Media queries: `@media`, breakpoints, responsive design
- Transitions & animations: `transition`, `@keyframes`, `animation`
- CSS variables: `--name`, `var()`

### 3. XML
- Well-formed vs Valid XML
- DTD: `<!ELEMENT>`, `<!ATTLIST>`, `<!DOCTYPE>`
- XML Schema (XSD): `xs:element`, `xs:complexType`, `xs:restriction`, data types
- Namespaces: `xmlns`, `xmlns:prefix`, qualified names
- CDATA sections: `<![CDATA[...]]>`
- Entity references: `&lt;`, `&gt;`, `&amp;`, `&apos;`, `&quot;`

### 4. XPath
- Path expressions: `/`, `//`, `.`, `..`
- Axes: `child::`, `parent::`, `ancestor::`, `descendant::`, `attribute::` (`@`)
- Predicates: `[1]`, `[last()]`, `[position()]`, `[@attr]`, `[@attr='val']`, `[expr]`
- Functions: `text()`, `count()`, `string()`, `sum()`, `not()`, `contains()`, `starts-with()`

### 5. XSLT
- `<xsl:template match="...">` — template rules
- `<xsl:apply-templates select="...">` — recursive processing
- `<xsl:for-each select="...">` — iteration
- `<xsl:value-of select="...">` — output text
- `<xsl:if test="...">` — conditional
- `<xsl:choose>`, `<xsl:when>`, `<xsl:otherwise>` — if-else
- `<xsl:sort select="...">` — sorting
- `<xsl:output method="html|xml|text">`

### 6. JSON
- Syntax: `{}` objects, `[]` arrays, data types
- JSON vs XML comparison
- `JSON.parse()` and `JSON.stringify()`
- JSON Schema basics
- `fetch()` API with JSON

### 7. CSS Specificity
- Calculation: `(a,b,c)` — IDs, Classes/Attrs/Pseudo-classes, Elements/Pseudo-elements
- `!important` override
- Inline styles
- Source order tiebreaker

---

## 🃏 Flashcard Categories (55 total)

| Category | Cards | Topics |
|----------|-------|--------|
| 🌐 HTML5 | 12 | Semantics, forms, tables, attributes, meta |
| 🎨 CSS | 12 | Box model, flexbox, grid, specificity, animations |
| 📄 XML | 10 | DTD, XSD, namespaces, CDATA, entities |
| 🔍 XPath/XSLT | 11 | Path expressions, predicates, templates, transforms |
| {} JSON | 10 | Syntax, comparison, parse/stringify, schema, fetch |

---

## ⌨️ Keyboard Shortcuts (Cram Cards)

| Key | Action |
|-----|--------|
| `Space` | Flip card |
| `→` | Next card |
| `←` | Previous card |
| `1` | Mark for review |
| `2` | Know it ✓ |

---

## 🛠️ Interactive Tools (index.html)

1. **CSS Specificity Calculator** — Enter two selectors, compare `(a,b,c)` scores
2. **JSON Formatter/Validator** — Paste JSON, validate and pretty-print
3. **HTML5 Tag Reference** — Searchable list of 40+ semantic elements
4. **XPath Expression Tester** — Test expressions against sample XML in-browser
5. **Flexbox vs Grid Guide** — Live interactive demos with controls

---

## 💡 Exam Tips

- ✅ XML must have **exactly one root element** — most common mistake
- ✅ XSLT templates use `match=` with XPath **patterns**, not expressions
- ✅ JSON keys must use **double quotes** — single quotes are invalid
- ✅ CSS specificity `(1,0,0)` (ID) always beats `(0,99,0)` (classes)
- ✅ `//book` selects from **anywhere**, `/bookstore/book` is absolute from root
- ✅ `defer` preserves script order; `async` does not
- ✅ `box-sizing: border-box` makes layouts predictable — always use it

---

*Built for CZU Prague · INFOA4 · ETE1AE — Good luck on the exam! 🎓*
