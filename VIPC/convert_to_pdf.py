#!/usr/bin/env python3
"""Convert all VIPC markdown documents to styled PDF files."""

import markdown
from weasyprint import HTML
import os
import re

CSS_STYLE = """
@page {
    size: letter;
    margin: 1in;
    @bottom-center {
        content: "AUTHENTIC CONSORTIUM | VIPC VVP Launch Grant";
        font-size: 8pt;
        color: #999;
        font-family: Calibri, Arial, sans-serif;
    }
    @bottom-right {
        content: counter(page);
        font-size: 8pt;
        color: #999;
        font-family: Calibri, Arial, sans-serif;
    }
}

body {
    font-family: Calibri, Arial, Helvetica, sans-serif;
    font-size: 11pt;
    line-height: 1.5;
    color: #1a1a1a;
}

h1 {
    font-size: 20pt;
    color: #1B2A4A;
    border-bottom: 3px solid #C5960C;
    padding-bottom: 8px;
    margin-top: 0;
}

h2 {
    font-size: 16pt;
    color: #1B2A4A;
    border-bottom: 1px solid #ddd;
    padding-bottom: 4px;
    margin-top: 24px;
}

h3 {
    font-size: 13pt;
    color: #1B2A4A;
    margin-top: 18px;
}

h4 {
    font-size: 11pt;
    color: #1B2A4A;
    margin-top: 14px;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin: 12px 0;
    font-size: 10pt;
}

th {
    background-color: #1B2A4A;
    color: white;
    padding: 6px 8px;
    text-align: left;
    font-weight: bold;
}

td {
    padding: 5px 8px;
    border: 1px solid #ddd;
    vertical-align: top;
}

tr:nth-child(even) {
    background-color: #f8f8f8;
}

strong {
    color: #1B2A4A;
}

code {
    font-family: "Courier New", monospace;
    font-size: 9pt;
    background-color: #f5f5f5;
    padding: 1px 4px;
    border-radius: 3px;
}

pre {
    background-color: #f5f5f5;
    padding: 12px;
    border-left: 3px solid #C5960C;
    font-size: 8pt;
    overflow-x: auto;
    white-space: pre-wrap;
    line-height: 1.3;
}

ul, ol {
    margin-left: 16px;
}

li {
    margin-bottom: 4px;
}

hr {
    border: none;
    border-top: 1px solid #C5960C;
    margin: 20px 0;
}

blockquote {
    border-left: 3px solid #C5960C;
    margin-left: 0;
    padding-left: 16px;
    color: #555;
    font-style: italic;
}

/* Hide HTML comments */
.comment { display: none; }
"""

def md_to_pdf(md_path, pdf_path):
    """Convert a markdown file to a styled PDF."""
    with open(md_path, 'r') as f:
        md_content = f.read()

    # Remove HTML comments
    md_content = re.sub(r'<!--.*?-->', '', md_content, flags=re.DOTALL)

    html_content = markdown.markdown(
        md_content,
        extensions=['tables', 'fenced_code', 'codehilite', 'toc']
    )

    full_html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>{CSS_STYLE}</style>
</head>
<body>
{html_content}
</body>
</html>"""

    HTML(string=full_html).write_pdf(pdf_path)
    size_kb = os.path.getsize(pdf_path) / 1024
    print(f"Created: {pdf_path} ({size_kb:.0f} KB)")

# Convert all VIPC markdown documents
docs = [
    ("01_VV_Technical_Brief.md", "01_VV_Technical_Brief.pdf"),
    ("02_Implementation_Guide.md", "02_Implementation_Guide.pdf"),
]

base = "/home/user/AC/VIPC"
for md_file, pdf_file in docs:
    md_path = os.path.join(base, md_file)
    pdf_path = os.path.join(base, pdf_file)
    try:
        md_to_pdf(md_path, pdf_path)
    except Exception as e:
        print(f"ERROR converting {md_file}: {e}")

print("\nAll VIPC documents converted to PDF.")
