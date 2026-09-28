# Journal Club

Material de estudo do clube de revista de Pediatria: cada encontro parte de um artigo e desenvolve, conceito a conceito, o raciocínio metodológico necessário para lê-lo e aplicá-lo.

**Site:** https://marcelosilva2604.github.io/journalclub/

## Encontros

| Data | Artigo | Temas | Material |
|---|---|---|---|
| 28/09/2026 | Huang Y-N et al. *Pediatrics* 2026;158(3):e2025075020. [doi:10.1542/peds.2025-075020](https://doi.org/10.1542/peds.2025-075020) | RR e OR, caso-controle, desfecho raro, confundimento, E-value, NNT | [pasta](2026-09-28-antiviral-influenza-rr-or/) |

## Estrutura

```
journalclub/
├── index.html                 # home page (list of sessions)
├── CLAUDE.md                  # project guide and per-session workflow
├── STYLE.md                   # editorial line (rigid)
├── _template/                 # skeleton for the next session
└── AAAA-MM-DD-tema/
    ├── README.md              # reference, DOI, topics
    ├── build_notebook.py      # generates notebook.ipynb (source of truth)
    ├── notebook.ipynb         # executed notebook
    ├── SOURCE_CHECKS.md       # verification log (numbers and references)
    └── index.html             # HTML export shown on the site
tools/export_html.py            # styled HTML export used by every session
```

## Como gerar o material de um encontro

```bash
cd AAAA-MM-DD-tema
python build_notebook.py
jupyter nbconvert --to notebook --execute --inplace notebook.ipynb
cd .. && python tools/export_html.py AAAA-MM-DD-tema
```

O fluxo completo de um encontro está em `CLAUDE.md`, a linha editorial em `STYLE.md` e o checklist em `_template/README.md`.

Depois, adicione o encontro na `index.html` da raiz e na tabela acima.

## Regras

- **Nenhum PDF de artigo no repositório** (direito autoral): só referência e DOI.
- **Nenhum dado de paciente.** Todos os números vêm das tabelas publicadas.
- Requisitos: Python 3.12 com `numpy`, `pandas`, `matplotlib`, `nbformat`, `nbconvert`, `ipykernel`.
