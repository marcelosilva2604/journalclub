# AAAA-MM-DD: <tema>

Copie esta pasta para `AAAA-MM-DD-tema-curto/`. Use o `build_notebook.py` do encontro anterior como ponto de partida: ele já traz as funções das caixas (`DEF`, `PRACTICE`, `PITFALL`, `CAP`), a paleta e os auxiliares de gráfico (`dot_grid`, `plain_log_x`, `br`). Siga o fluxo do `CLAUDE.md` e as regras do `STYLE.md` da raiz.

**Artigo:** <Autores>. <Título>. *<Revista>*. <Ano>;<vol>(<n>):<páginas>. [doi:<DOI>](https://doi.org/<DOI>)

**Conceitos (uma seção cada):**

**Particularidade deste artigo:**

**Arquivos:** [index.html](index.html) (página do site) · [notebook.ipynb](notebook.ipynb) (executado) · `build_notebook.py` (fonte) · `SOURCE_CHECKS.md` (verificação)

## Checklist antes de publicar

- [ ] Todo número confere com as tabelas do PDF e está registrado em `SOURCE_CHECKS.md`
- [ ] Referências verificadas (DOI, metadados) e registradas em `SOURCE_CHECKS.md`
- [ ] Notebook executado sem erro; nenhum bloco com mais de 25 linhas
- [ ] Nenhum emoji, nenhum travessão, nenhuma instrução de aula
- [ ] Objetivos com maiúscula inicial e ponto final; exatamente uma Armadilha; um Pratique por conceito; soluções em seção visível
- [ ] PDF do artigo **não** foi adicionado ao repositório
- [ ] `index.html` exportada com `tools/export_html.py` e conferida no computador e no celular
- [ ] Encontro adicionado no topo da `index.html` da raiz e na tabela do `README.md` da raiz
