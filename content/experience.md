---
title: 'Experience'
date: 2023-10-24
type: landing

design:
  spacing: '5rem'

# Note: `username` refers to the user's folder name in `content/authors/`

# Page sections
sections:
  - block: resume-experience
    content:
      username: Jiaming Liu
    design:
      # Hugo date format
      date_format: 'January 2006'
      # Education or Experience section first?
      is_education_first: false

  - block: collection
    content:
      title: Awards
      text: This is where I started.
      filters:
        folders:
          - awards
      count: 10000000
    design:
      view: article-grid
      fill_image: false
      columns: 3
  # - block: resume-skills
  #   content:
  #     title: Skills & Hobbies
  #     username: Jiaming Liu
  #   design:
  #     show_skill_percentage: false
  
  # - block: resume-languages
  #   content:
  #     title: Languages
  #     username: admin
---
