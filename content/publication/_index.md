---
# Leave the homepage title empty to use the site title
title: "Publications"
date: 2024-11-25
type: landing

design:
  # Default section spacing
  spacing: "6rem"

sections:
  - block: collection
    content:
      title: Journal & Conference
      text: ""
      filters:
        folders:
          - publication
        exclude_featured: false
      count: 100000000
    design:
      view: citation
  - block: collection
    content:
      title: Patents
      text: ""
      filters:
        folders:
          - patents
        exclude_featured: false
    design:
      view: citation

---

<!-- ---
title: Publications
cms_exclude: true

# View.
view: citation

# Optional header image (relative to `static/media/` folder).
banner:
  caption: ''
  image: ''

sections:
- block: collection
    content:
      title: Recent Patents
      text: ""
      filters:
        folders:
          - patents
        exclude_featured: false
    design:
      view: citation
      
--- -->
