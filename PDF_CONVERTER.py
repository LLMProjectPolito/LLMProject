import os, glob, base64, subprocess, sys
from pathlib import Path

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang='en'>
<head>
<meta charset='UTF-8'>
<title>{title}</title>
<link rel='stylesheet' href='https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.2.0/github-markdown.min.css'>
<link rel='stylesheet' href='https://cdn.jsdelivr.net/npm/katex@0.16.4/dist/katex.min.css'>
<style>
.markdown-body {{
  box-sizing: border-box;
  min-width: 200px;
  max-width: 100%;
  margin: 0 auto;
  padding: 45px;
  font-size: 14px;
}}
table {{
    display: table !important;
    width: 100% !important;
    overflow-x: visible !important;
    font-size: 10px !important;
    table-layout: auto !important;
}}
th, td {{ padding: 4px !important; }}
@media (max-width: 767px) {{ .markdown-body {{ padding: 15px; }} }}
@media print {{ 
  .markdown-body {{ max-width: none; padding: 20px; }} 
  body {{ background-color: white; }} 
  h1, h2, h3 {{ page-break-after: avoid; }}
  pre, blockquote, table {{ page-break-inside: avoid; }}
}}
</style>
<script src='https://cdn.jsdelivr.net/npm/markdown-it@13.0.1/dist/markdown-it.min.js'></script>
<script src='https://cdn.jsdelivr.net/npm/katex@0.16.4/dist/katex.min.js'></script>
<script src='https://cdn.jsdelivr.net/npm/markdown-it-texmath@1.0.0/texmath.min.js'></script>
</head>
<body>
<article class='markdown-body' id='content'>Loading…</article>
<div id='raw-content' style='display:none;'>{b64_content}</div>
<script>
function decodeContent(str) {{
  return decodeURIComponent(atob(str).split('').map(function(c) {{
    return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
  }}).join(''));
}}
document.addEventListener('DOMContentLoaded', function() {{
  const md = window.markdownit({{ html:true, breaks:true, linkify:true }});
  if (typeof texmath !== 'undefined') {{
    md.use(texmath, {{ engine:katex, delimiters:'dollars' }});
  }}
  const raw = document.getElementById('raw-content').textContent;
  const markdown = decodeContent(raw);
  document.getElementById('content').innerHTML = md.render(markdown);
}});
</script>
</body>
</html>
"""

def find_browser():
    candidates = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    ]
    for p in candidates:
        if os.path.isfile(p): return p
    return None

def md_to_pdf(md_path, browser_path):
    print(f"📄 Converting: {md_path}")
    try:
        md_file = Path(md_path)
        md_content = md_file.read_text(encoding='utf-8')
        b64 = base64.b64encode(md_content.encode('utf-8')).decode('utf-8')
        title = md_file.stem
        html = HTML_TEMPLATE.format(title=title, b64_content=b64)
        
        temp_html = md_file.with_suffix('.temp.html')
        temp_html.write_text(html, encoding='utf-8')
        
        pdf_path = md_file.with_suffix('.pdf')
        abs_html = temp_html.absolute()
        file_uri = f"file:///{str(abs_html).replace(os.sep, '/')}"
        
        cmd = [
            browser_path, "--headless=new", "--disable-gpu",
            f"--print-to-pdf={pdf_path.absolute()}",
            "--no-pdf-header-footer", "--virtual-time-budget=10000",
            file_uri
        ]
        
        subprocess.run(cmd, check=True, capture_output=True)
        if temp_html.exists(): temp_html.unlink()
        print(f"✅ Success: {pdf_path}")
        return True
    except Exception as e:
        print(f"❌ Error converting {md_path}: {e}")
        return False

def main():
    browser = find_browser()
    if not browser:
        print("Chrome/Edge not found."); sys.exit(1)
        
    doc_dir = Path("documentation")
    if len(sys.argv) > 1:
        md_files = sys.argv[1:]
    else:
        md_files = list(doc_dir.glob("*.md")) if doc_dir.exists() else glob.glob("*.md")
    
    success_count = 0
    for md_file in md_files:
        if md_to_pdf(md_file, browser): success_count += 1
            
    print(f"\n✨ Finished! Successfully converted {success_count} files in {doc_dir}.")

if __name__ == "__main__":
    main()
