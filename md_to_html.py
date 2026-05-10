"""
Convert paper_full.md and blog_note_full.md into self-contained HTML
files (with MathJax for equations, embedded CSS, image inlining).

User can then 'Print → Save as PDF' from their browser to get a
publication-ready PDF.
"""
import os
import sys
import base64
import markdown
import re

ROOT = r'C:\Users\TeradaMunehiro\quantum_gravity_info'
RELEASE = os.path.join(ROOT, 'release')
os.makedirs(RELEASE, exist_ok=True)

CSS = r"""
<style>
@page { size: A4; margin: 18mm 16mm 18mm 16mm; }
body {
    font-family: "Noto Serif CJK JP", "Yu Mincho", "Hiragino Mincho ProN",
                 "MS Mincho", serif;
    font-size: 10.5pt;
    line-height: 1.55;
    max-width: 780px;
    margin: 0 auto;
    padding: 24px;
    color: #111;
}
h1 { font-size: 18pt; border-bottom: 2px solid #444; padding-bottom: 6px;
     margin-top: 16px; }
h2 { font-size: 14pt; border-bottom: 1px solid #888; padding-bottom: 3px;
     margin-top: 22px; page-break-after: avoid; }
h3 { font-size: 12pt; margin-top: 16px; page-break-after: avoid; }
h4 { font-size: 11pt; margin-top: 12px; }
p { margin: 0.45em 0; text-align: justify; }
code {
    background: #f4f4f4;
    padding: 1px 4px;
    border-radius: 3px;
    font-family: "Consolas", "Menlo", monospace;
    font-size: 9.5pt;
}
pre {
    background: #f4f4f4;
    padding: 8px 10px;
    border-radius: 4px;
    overflow-x: auto;
    font-size: 9pt;
    page-break-inside: avoid;
}
table {
    border-collapse: collapse;
    margin: 8px 0;
    font-size: 9.5pt;
    page-break-inside: avoid;
}
th, td {
    border: 1px solid #aaa;
    padding: 4px 7px;
    text-align: left;
}
th { background: #eee; font-weight: 600; }
img { max-width: 100%; height: auto; page-break-inside: avoid;
      display: block; margin: 8px auto; }
blockquote {
    border-left: 3px solid #888;
    padding-left: 12px;
    color: #444;
    margin: 8px 0;
}
hr { border: none; border-top: 1px solid #ccc; margin: 18px 0; }
.author { text-align: center; font-size: 11pt; margin-bottom: 18px; }
.abstract {
    background: #fafafa; padding: 8px 14px;
    border-left: 3px solid #444;
}
</style>
"""

MATHJAX = r"""
<script>
MathJax = {
    tex: {
        inlineMath: [['$', '$'], ['\\(', '\\)']],
        displayMath: [['$$', '$$'], ['\\[', '\\]']],
        processEscapes: true,
    },
    options: { skipHtmlTags: ['script','noscript','style','textarea','pre','code'] }
};
</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>
"""


def embed_image(match):
    """Inline images as base64 data URIs so the HTML is self-contained."""
    alt, src = match.group(1), match.group(2)
    candidates = [
        os.path.join(ROOT, src),
        os.path.join(RELEASE, src),
        os.path.abspath(src),
    ]
    if src.startswith('quantum_gravity_info/'):
        candidates.append(os.path.join(os.path.dirname(ROOT),
                                        src))
    for path in candidates:
        if os.path.exists(path):
            ext = os.path.splitext(path)[1][1:].lower()
            mime = {'png': 'image/png', 'jpg': 'image/jpeg',
                    'jpeg': 'image/jpeg', 'svg': 'image/svg+xml'}.get(ext, 'image/png')
            with open(path, 'rb') as f:
                data = base64.b64encode(f.read()).decode('ascii')
            return f'<img src="data:{mime};base64,{data}" alt="{alt}" />'
    return f'<img src="{src}" alt="{alt}" />'


def md_to_html(md_path, out_path, title):
    with open(md_path, 'r', encoding='utf-8') as f:
        text = f.read()
    # Strip image basenames so embed_image can find them in ROOT
    text = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)',
                  lambda m: f'![{m.group(1)}]({os.path.basename(m.group(2))})',
                  text)
    html_body = markdown.markdown(
        text,
        extensions=['tables', 'fenced_code', 'toc', 'attr_list', 'sane_lists'],
        extension_configs={'toc': {'baselevel': 2}},
    )
    # Inline images as base64
    html_body = re.sub(r'<img\s+alt="([^"]*)"\s+src="([^"]+)"\s*/?>',
                       embed_image, html_body)
    html_body = re.sub(r'<img\s+src="([^"]+)"\s+alt="([^"]*)"\s*/?>',
                       lambda m: embed_image(
                           type('M', (), {'group': lambda self, i: [m.group(0), m.group(2), m.group(1)][i]})()),
                       html_body)
    # Final HTML
    html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="utf-8">
<title>{title}</title>
{CSS}
{MATHJAX}
</head>
<body>
{html_body}
</body>
</html>
"""
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Generated: {out_path}  ({os.path.getsize(out_path)/1024:.1f} KB)")


if __name__ == '__main__':
    # Japanese versions (originals at ROOT)
    md_to_html(
        os.path.join(ROOT, 'paper_full.md'),
        os.path.join(RELEASE, 'paper_full.html'),
        '情報理論的統一理論 (Information-Theoretic Unification of GR + QM + SM)'
    )
    md_to_html(
        os.path.join(ROOT, 'blog_note_full.md'),
        os.path.join(RELEASE, 'blog_note_full.html'),
        '重力と量子力学を統一する単一の方程式'
    )
    # English versions (in RELEASE)
    md_to_html(
        os.path.join(RELEASE, 'paper_full_en.md'),
        os.path.join(RELEASE, 'paper_full_en.html'),
        'Information-Theoretic Unification of GR and QM (Phases 1–16)'
    )
    md_to_html(
        os.path.join(RELEASE, 'blog_note_full_en.md'),
        os.path.join(RELEASE, 'blog_note_full_en.html'),
        'A Single Equation Unifying Gravity and Quantum Mechanics'
    )
