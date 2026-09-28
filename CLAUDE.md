# CLAUDE.md: como trabalhar neste projeto

Este arquivo governa toda sessão que mexe no Journal Club. Leia-o, e também o `STYLE.md`, antes de criar ou editar um encontro.

## O que é

**Journal Club** é o material de estudo do clube de revista de Pediatria conduzido por Marcelo Carvalho e Silva. A cada encontro, em geral às segundas-feiras, um artigo publicado vira uma página no site, e a página desenvolve, conceito a conceito, o raciocínio metodológico necessário para ler e aplicar aquele artigo.

- **Leitor:** residentes de Pediatria que entram no site sozinhos para estudar. Sabem clínica e não sabem estatística. Não precisam saber programar.
- **Não é roteiro de aula.** A página não traz atos, tempos, votação, "em sala", instruções ao condutor nem emojis. A condução ao vivo é do Marcelo; o site é o material de estudo (decisão do Marcelo, 28/09/2026).
- **O artigo em discussão é o caso do começo ao fim.** Todo conceito é aplicado aos números do artigo; exemplos de outros cenários entram só nos exercícios ou como contraste.
- **Continuidade:** o projeto segue semana a semana enquanto houver adesão das residentes. Cada encontro novo reaproveita a estrutura, o estilo e as ferramentas do anterior.

## Onde as coisas estão

- Local: `~/project/journalclub`
- GitHub (público): https://github.com/marcelosilva2604/journalclub
- Site (GitHub Pages, branch `main`, raiz): https://marcelosilva2604.github.io/journalclub/
- `index.html` (raiz): página inicial, um cartão por encontro, o mais recente no topo.
- `AAAA-MM-DD-tema-curto/`: uma pasta por encontro, com
  - `build_notebook.py`: fonte da verdade do material (gera o notebook);
  - `notebook.ipynb`: notebook executado, com saídas;
  - `index.html`: página do site, gerada pelo export estilizado;
  - `README.md`: referência, conceitos e particularidade do artigo;
  - `SOURCE_CHECKS.md`: registro interno da verificação de números e referências.
- `_template/README.md`: esqueleto para o próximo encontro.
- `tools/export_html.py`: export do notebook para a página estilizada do site (cabeçalho, tipografia, rodapé). Todos os encontros usam o mesmo.
- `STYLE.md`: a linha editorial, rígida.

## Regras do repositório (rígidas)

- **Nenhum PDF de artigo** no repositório (direito autoral). Só referência e DOI. O `.gitignore` bloqueia `*.pdf`; nunca use `git add -f`.
- **Nenhum dado de paciente.** Os números vêm das tabelas publicadas; exemplos e exercícios usam dados sintéticos plausíveis.
- O repositório é **público**. Tudo o que entra nele é publicado.
- O nome do projeto é **Journal Club**. Não usar o nome de instituição em nenhum texto do site (decisão do Marcelo, 28/09/2026).

## Relação com o tratado

A linha editorial deriva do tratado *Data Science in Health* do Marcelo (`~/project/stats/Tratado Datascience em health/`, em especial `STYLE.md` e `templates/CHAPTER_TEMPLATE.tex`). O tratado serve de guia: a arquitetura por conceito, o rigor (proposição com demonstração) e as referências já verificadas podem ser usados aqui. Marcelo autorizou reaproveitar texto do tratado, traduzido e adaptado ao artigo do encontro (28/09/2026). Nada do tratado entra no site sem estar a serviço do artigo em discussão, e nenhum arquivo do tratado (capítulos, PDFs, figuras, bibliografia) é copiado para este repositório.

## Fluxo de cada encontro (sempre nesta ordem)

1. **Ler o artigo inteiro** (PDF fornecido pelo Marcelo, fora do repositório). Extrair o texto (`pdftotext -layout`) e registrar as tabelas e números que serão usados.
2. **Escolher os conceitos.** Quais ideias metodológicas o artigo exige para ser lido corretamente? Qual é a particularidade do artigo (um problema de desenho, de análise ou de relato) que o material precisa explicar? Uma seção por conceito, na ordem em que o caso os exige.
3. **Consultar o tratado** para os capítulos correspondentes (definições, proposições, referências verificadas em `chapters/chNN/references/chNN.bib`, `bibliography/global/global.bib` e `chapters/chNN/SOURCE_CHECKS.md`).
4. **Planejar as referências antes de escrever.** Cada definição e cada afirmação metodológica apoiada em fonte verificada (DOI, páginas). Referência do tratado já verificada pode ser reutilizada; referência nova é conferida no PubMed/Crossref antes de entrar.
5. **Criar a pasta** `AAAA-MM-DD-tema-curto/` a partir de `_template/` e escrever o `build_notebook.py`, partindo do encontro anterior e obedecendo o `STYLE.md`.
6. **Gerar e executar:**
   ```bash
   cd AAAA-MM-DD-tema-curto
   ~/.venvs/ds/bin/python build_notebook.py
   ~/.venvs/ds/bin/jupyter nbconvert --to notebook --execute --inplace notebook.ipynb
   cd .. && ~/.venvs/ds/bin/python tools/export_html.py AAAA-MM-DD-tema-curto
   ```
7. **Verificar** (e registrar em `SOURCE_CHECKS.md`):
   - todo número impresso pelo código confere com o texto e com o PDF;
   - nenhuma célula com erro; nenhum bloco de código com mais de 25 linhas;
   - nenhum emoji, nenhum travessão (—);
   - toda afirmação sobre o artigo corresponde ao que o artigo diz; inferência nossa aparece como hipótese, não como fato;
   - a página renderiza bem no computador e no celular (captura com o Chrome headless; para simular celular, abrir a página num iframe de 390 px).
8. **Atualizar** o cartão na `index.html` da raiz (novo encontro no topo) e a tabela do `README.md` da raiz.
9. **Publicar:** `git add -A`, commit, `git push`; aguardar o build do Pages (`gh api repos/marcelosilva2604/journalclub/pages/builds/latest`) e conferir que as páginas respondem 200.
10. **Entregar ao Marcelo** o link do encontro e da página inicial, com os pontos que ele precisa revisar.

## Notas de trabalho

- Conversa com o Marcelo em português; o material também em português.
- Código em Python 3 (`~/.venvs/ds`); comentários no código em inglês.
- O código fica visível na página: mostra de onde sai cada número. Não esconder as células de código.
- Marcelo revisa o material depois de publicado; correções dele têm precedência e, quando forem regra geral, entram no `STYLE.md`.
