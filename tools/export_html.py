"""Export a session notebook to the styled HTML page used on the site.

Usage: python tools/export_html.py <session-folder>
"""
import sys
from pathlib import Path

import nbformat
from nbconvert import HTMLExporter

HEAD = """
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
  :root {
    --ejc-bg: #f7f7f5;
    --ejc-paper: #ffffff;
    --ejc-ink: #1a1a19;
    --ejc-ink2: #55544f;
    --ejc-line: #e3e2dd;
    --ejc-accent: #1f5fa8;
    --ejc-accent-soft: #eef3fa;
    --ejc-code-bg: #f5f5f2;
  }
  html, body { background: var(--ejc-bg) !important; }
  body { color: var(--ejc-ink); margin: 0; }

  /* Site header */
  .ejc-bar {
    position: sticky; top: 0; z-index: 10;
    background: rgba(255,255,255,.94); backdrop-filter: blur(6px);
    border-bottom: 1px solid var(--ejc-line);
    font: 500 14px/1 Inter, system-ui, sans-serif;
  }
  .ejc-bar-inner {
    max-width: 960px; margin: 0 auto; padding: 14px 24px;
    display: flex; gap: 16px; align-items: center; justify-content: space-between;
  }
  .ejc-bar a { color: var(--ejc-ink); text-decoration: none; letter-spacing: .01em; }
  .ejc-bar a:hover { color: var(--ejc-accent); }
  .ejc-bar .ejc-meta { color: var(--ejc-ink2); font-weight: 400; text-align: right; }

  /* Page frame */
  body.jp-Notebook {
    max-width: none !important; margin: 0 !important; padding: 0 !important;
    background: var(--ejc-bg) !important; overflow-x: hidden;
  }
  body.jp-Notebook > main {
    box-sizing: border-box;
    max-width: 960px; margin: 32px auto 40px; padding: 40px 48px;
    background: var(--ejc-paper); border: 1px solid var(--ejc-line); border-radius: 6px;
  }
  .jp-Cell { padding: 0 !important; margin-bottom: 14px; }
  .jp-InputPrompt, .jp-OutputPrompt { display: none !important; }
  .jp-Collapser { display: none !important; }

  main .jp-Cell, main .jp-Cell-inputWrapper, main .jp-Cell-outputWrapper,
  main .jp-InputArea, main .jp-OutputArea, main .jp-OutputArea-child,
  main .jp-RenderedHTMLCommon, main .jp-InputArea-editor, main .jp-OutputArea-output {
    min-width: 0 !important; max-width: 100% !important; box-sizing: border-box;
  }
  main .jp-InputArea-editor, main .jp-OutputArea-output, main .highlight { overflow-x: auto; }

  /* Prose */
  .jp-RenderedMarkdown, .jp-RenderedHTMLCommon {
    font-family: "Source Serif 4", Georgia, serif !important;
    font-size: 17.5px !important; line-height: 1.65 !important; color: var(--ejc-ink) !important;
    padding-right: 0 !important;
  }
  .jp-RenderedHTMLCommon h1, .jp-RenderedHTMLCommon h2,
  .jp-RenderedHTMLCommon h3, .jp-RenderedHTMLCommon h4 {
    font-family: Inter, system-ui, sans-serif !important; color: var(--ejc-ink) !important;
    letter-spacing: -0.01em;
  }
  .jp-RenderedHTMLCommon h1 {
    font-size: 1.55rem !important; font-weight: 700 !important;
    margin: 2.6rem 0 .3rem !important; padding-top: 1.6rem;
    border-top: 3px solid var(--ejc-accent);
  }
  main > .jp-Cell:first-child .jp-RenderedHTMLCommon h1 {
    font-size: 2.05rem !important; border-top: none; padding-top: 0; margin-top: 0 !important;
    line-height: 1.2;
  }
  .jp-RenderedHTMLCommon h2 {
    font-size: 1.35rem !important; font-weight: 650 !important;
    margin: 2.2rem 0 .8rem !important; padding-bottom: .4rem;
    border-bottom: 1px solid var(--ejc-line);
  }
  .jp-RenderedHTMLCommon h3 { font-size: 1.08rem !important; font-weight: 600 !important; margin: 1.6rem 0 .5rem !important; }
  .jp-RenderedHTMLCommon a.anchor-link { display: none !important; }
  .jp-RenderedHTMLCommon em { color: var(--ejc-ink2); }
  .jp-RenderedHTMLCommon hr { border: 0; border-top: 1px solid var(--ejc-line); margin: 1.5rem 0; }

  /* Callouts */
  .jp-RenderedHTMLCommon blockquote {
    margin: 1.1rem 0 !important; padding: .8rem 1.1rem !important;
    background: var(--ejc-accent-soft) !important; border-left: 3px solid var(--ejc-accent) !important;
    border-radius: 0 4px 4px 0; color: var(--ejc-ink) !important; font-style: normal;
  }
  .jp-RenderedHTMLCommon blockquote p { margin: .25rem 0 !important; }

  /* Tables */
  .jp-RenderedHTMLCommon table {
    border-collapse: collapse !important; margin: 1rem 0 !important; width: auto;
    font-family: Inter, system-ui, sans-serif !important; font-size: 14.5px !important;
    border-top: 2px solid var(--ejc-ink) !important; border-bottom: 2px solid var(--ejc-ink) !important;
  }
  .jp-RenderedHTMLCommon th {
    background: transparent !important; font-weight: 600 !important; text-align: left !important;
    border-bottom: 1px solid var(--ejc-ink) !important; padding: 8px 12px !important;
  }
  .jp-RenderedHTMLCommon td {
    border: none !important; border-bottom: 1px solid var(--ejc-line) !important;
    padding: 7px 12px !important; text-align: left !important; vertical-align: top;
  }
  .jp-RenderedHTMLCommon tbody tr:nth-child(odd) { background: transparent !important; }
  .jp-RenderedHTMLCommon tbody tr:hover { background: #fafaf8 !important; }

  /* Code and outputs */
  .jp-InputArea-editor, .jp-CodeMirrorEditor, .highlight {
    background: var(--ejc-code-bg) !important; border: 1px solid var(--ejc-line) !important;
    border-radius: 4px !important;
  }
  .jp-InputArea-editor pre, .highlight pre, .jp-OutputArea-output pre {
    font-family: "JetBrains Mono", ui-monospace, Menlo, monospace !important; font-size: 13px !important;
    line-height: 1.5 !important;
  }
  .jp-OutputArea-output pre { color: var(--ejc-ink) !important; }
  .jp-OutputArea-output img { max-width: 100%; height: auto; }
  .jp-OutputArea { margin-top: 6px; }

  /* Collapsible answers */
  details {
    border: 1px solid var(--ejc-line); border-radius: 4px; padding: .6rem 1rem; margin: 1rem 0;
  }
  summary { cursor: pointer; font-family: Inter, system-ui, sans-serif; }

  .ejc-foot {
    max-width: 960px; margin: 0 auto 48px; padding: 0 24px;
    font: 400 13px/1.5 Inter, system-ui, sans-serif; color: var(--ejc-ink2);
  }
  .ejc-foot a { color: var(--ejc-accent); }

  @media (max-width: 720px) {
    body.jp-Notebook > main { padding: 20px 16px; margin: 12px 8px 32px; }
    .jp-RenderedMarkdown, .jp-RenderedHTMLCommon { font-size: 16px !important; }
    .ejc-bar .ejc-meta { display: none; }
    .jp-RenderedHTMLCommon table { display: block; overflow-x: auto; }
  }
</style>
"""

BAR = """
<header class="ejc-bar"><div class="ejc-bar-inner">
  <a href="../">&larr; Journal Club</a>
  <span class="ejc-meta">{meta}</span>
</div></header>
"""

FOOT = """
<footer class="ejc-foot">
  Material didático do Journal Club. Todos os números foram calculados a partir das tabelas publicadas do artigo.
  <a href="notebook.ipynb">Baixar o notebook</a> · <a href="../">Todos os encontros</a>
</footer>
"""


def main(folder):
    folder = Path(folder)
    nb = nbformat.read(folder / "notebook.ipynb", 4)
    exporter = HTMLExporter(template_name="lab")
    exporter.exclude_input_prompt = True
    exporter.exclude_output_prompt = True
    html, _ = exporter.from_notebook_node(nb)

    meta = nb.metadata.get("ejc_meta", "")
    html = html.replace("</head>", HEAD + "</head>", 1)
    body_start = html.index(">", html.index("<body")) + 1
    html = html[:body_start] + BAR.format(meta=meta) + html[body_start:]
    html = html.replace("</body>", FOOT + "</body>", 1)
    (folder / "index.html").write_text(html)
    print(folder / "index.html")


if __name__ == "__main__":
    main(sys.argv[1])
