# AAAA-MM-DD: <tema>

Copie esta pasta para `AAAA-MM-DD-tema-curto/`, use o `build_notebook.py` do encontro anterior como ponto de partida e preencha.

**Artigo:** <Autores>. <Título>. *<Revista>*. <Ano>;<vol>(<n>):<páginas>. [doi:<DOI>](https://doi.org/<DOI>)

**Conceitos (uma seção cada):**

**Particularidade deste artigo:**

## Arquitetura do material (fixa, nesta ordem)

1. Título, artigo em discussão e objetivos de aprendizagem (3 a 5, cada um algo que o leitor consegue fazer).
2. Introdução: o caso clínico ancorado no artigo, propostas concorrentes de colegas e as perguntas que o leitor ainda não sabe responder; parágrafo com o percurso.
3. Uma seção por conceito, com o nome do conceito, sempre nesta ordem: transição; definição em caixa cinza com citação; aplicação ao artigo; fórmula e proposição com demonstração; cálculo à mão e depois o Python que o confirma; erro comum; quadro "Pratique" apontando os exercícios.
4. De volta à decisão: reavaliar as propostas da introdução; o que se pode e o que não se pode concluir.
5. Aplicações em saúde: leitura crítica do artigo.
6. Resumo: um parágrafo por conceito, nada novo.
7. Exercícios (casos de saúde realistas) e, em seguida, uma seção visível com as soluções comentadas.
8. Leituras complementares e referências numeradas (Vancouver).

## Regras de estilo

- Registro sóbrio e preciso; sem emojis, sem travessão, sem roteiro de aula ou tempos.
- Exatamente uma caixa "Armadilha" por material.
- Figuras e tabelas numeradas, com legenda autossuficiente; figuras legíveis em escala de cinza (estilo de linha, marcador e preenchimento, não só cor).
- Blocos de código com até 25 linhas, introduzidos por uma frase e lidos de volta no texto.
- Intervalos com hífen; IC como "0,19 (IC 95% 0,14-0,27)"; vírgula decimal no texto.
- Toda referência verificada (DOI, páginas) antes de entrar no texto.

## Checklist antes de publicar

- [ ] Todo número confere com as tabelas do PDF
- [ ] PDF do artigo **não** foi adicionado ao repositório
- [ ] `python build_notebook.py` → `jupyter nbconvert --to notebook --execute --inplace notebook.ipynb` → `python ../tools/export_html.py <pasta>`
- [ ] Encontro adicionado na `index.html` da raiz e no `README.md` da raiz
