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
  # - block: markdown
  #   content:
  #     title: 'Patents'
  #     subtitle: ''
  #     text: |-
  #       - 冯全源，刘家明，程简. 基于比特翻转算法加速软译码的联合译码方法及系统. 国家发明专利：202011051282.X,  授权号：CN 112350738B
  #       - 冯全源，刘家明. 一种基于码率自适应的小型化 LDPC 编码器电路. 国家发明专利：202110544262.4，授权号：CN113285724B
  #       - 冯全源，刘家明. 一种基于码率自适应的高效化 LDPC 编码器电路. 国家发明专利：202110544295.9，授权号：CN113300717B
  #   design:
  #     columns: '2'

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
