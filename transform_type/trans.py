import os
import re
from datetime import datetime

def convert_bib_to_yaml(bib_entry):
    # 定义正则表达式模式以匹配bib条目的各个部分
    patterns = {
        'type': r'@(\w+){',
        'id': r'@(\w+){(\w+),',
        'title': r'title\s*=\s*{(.*?)}(?=,\s*(?:author|journal|booktitle|volume|number|pages|year|doi|note|keywords|url|}|$))',
        'authors': r'author\s*=\s*{(.*?)}',
        'journal': r'journal\s*=\s*{(.*?)}',
        'booktitle': r'booktitle\s*=\s*{(.*?)}',
        'volume': r'volume\s*=\s*{(\d+)}',
        'number': r'number\s*=\s*{(\d+)}',
        'pages': r'pages\s*=\s*{(\d+)-(\d+)}',
        'year': r'year\s*=\s*{(\d{4})}',
        'doi': r'doi\s*=\s*{(.*?)}',
        'note': r'note\s*=\s*{(.*?)}',
        'keywords': r'keywords\s*=\s*{(.*?)}',
        'url': r'url\s*=\s*{(.*?)}'
    }
    
    # 使用字典来存储匹配的结果
    matches = {key: re.search(pattern, bib_entry) for key, pattern in patterns.items()}

    current_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    
    # 构建输出字符串
    output = f'''---
title: "{matches['title'].group(1)}"
authors:
'''
    # 处理作者列表，假设作者之间用and分隔
    authors = matches['authors'].group(1).split(' and ')
    for author in authors:
        # 假设作者名字格式为 Lastname, Firstname
        parts = author.split(',')
        if len(parts) == 2:
            first_name = parts[1].strip()
            last_name = parts[0].strip()
            author_str = f'{first_name} {last_name}'
        else:
            author_str = author.strip()
        output += f'- {author_str}\n'
    
    # 继续添加其他字段
    output += f'''date: "{current_time}"
doi: "{matches['doi'].group(1) if matches['doi'] else ''}"

# Schedule page publish date (NOT publication's date).
publishDate: "{current_time}"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: [{get_publication_type(matches['type'].group(1))}]
'''
    
    if matches['type'].group(1) == 'ARTICLE':
        output += f'''# Publication name and optional abbreviated publication name.
publication: "*{matches['journal'].group(1)}, {matches['volume'].group(1) if matches['volume'] != None else ''}*({matches['number'].group(1) if matches['number'] != None else 'Early Access'})"
publication_short: ""

abstract: Detailed information is not available

# Summary. An optional shortened abstract.
summary: Detailed information is not available

tags:
- Source Themes
featured: false

url_pdf: {matches['url'].group(1) if matches['url'] else ''}
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
image:
  caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/jdD8gXaTZsc)'
  focal_point: ""
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: []

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: example
'''
    elif matches['type'].group(1) == 'INPROCEEDINGS':
        output += f'''# Publication name and optional abbreviated publication name.
publication: "*{matches['booktitle'].group(1)}*"
publication_short: ""

abstract: Detailed information is not available

# Summary. An optional shortened abstract.
summary: Detailed information is not available

tags:
- Source Themes
featured: false

url_pdf: {matches['url'].group(1) if matches['url'] else ''}
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
image:
  caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/jdD8gXaTZsc)'
  focal_point: ""
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: []

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: example
'''
    elif matches['type'].group(1) == 'PATENTS':
        output += f'''# Publication name and optional abbreviated publication name.
publication: "{matches['note'].group(1)}"
publication_short: ""

abstract: Detailed information is not available

# Summary. An optional shortened abstract.
summary: Detailed information is not available

tags:
- Source Themes
featured: false

url_pdf: {matches['url'].group(1) if matches['url'] else ''}
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
image:
  caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/jdD8gXaTZsc)'
  focal_point: ""
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: []

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: example

'''
    
    output += '''

---

{{% callout note %}}
Click the *Cite* button above to demo the feature to enable visitors to import publication metadata into their reference management software.
{{% /callout %}}

{{% callout note %}}
Create your slides in Markdown - click the *Slides* button to check out the example.
{{% /callout %}}

Add the publication's **full text** or **supplementary notes** here. You can use rich formatting such as including [code, math, and images](https://docs.hugoblox.com/content/writing-markdown-latex/).
'''

    return output

def get_publication_type(pub_type):
    if pub_type == 'ARTICLE':
        return '"article-journal"'
    elif pub_type == 'INPROCEEDINGS':
        return '"conference-paper"'
    elif pub_type == 'PATENTS':
        return '"patent"'
    else:
        return '""'

def process_directory(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.bib'):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as file:
                bib_content = file.read()
            
            # Split the bib file into individual entries
            entries = re.split(r'\n@', bib_content)
            converted_entries = []
            for entry in entries:
                if entry.strip():
                    converted_entries.append(convert_bib_to_yaml('@' + entry))
            
            # Save the converted entries to a new file
            output_filename = f"index.md"
            output_filepath = os.path.join(directory, output_filename)
            with open(output_filepath, 'w', encoding='utf-8') as output_file:
                for converted_entry in converted_entries:
                    output_file.write(converted_entry + '\n\n')

# 指定目录路径
directory_path = 'H:\github_code\home_page\content\publication\\2024-Biocas-Low-Light'

# 处理目录中的所有bib文件
process_directory(directory_path)