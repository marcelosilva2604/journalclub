# STYLE.md: linha editorial do Journal Club

Rígida. Nenhum encontro é publicado violando este arquivo. Quando uma regra e um rascunho conflitam, vale a regra. Deriva do `STYLE.md` do tratado *Data Science in Health*, adaptado para material de estudo em português.

## A. Voz e registro

- **Português do Brasil.** Termos consagrados em inglês ficam em inglês quando é assim que aparecem nos artigos (odds, odds ratio, E-value), explicados na primeira ocorrência.
- **Registro sóbrio e preciso.** Frases declarativas, afirmações na força que a evidência sustenta, limites e suposições ditos com clareza. Sem entusiasmo, sem metáforas estendidas, sem frases de efeito.
- **Material de estudo, não roteiro de aula.** Sem atos, tempos, votação, "em sala", "pergunta para a turma", instruções ao condutor.
- **Sem emojis.** Nenhum, em lugar nenhum.
- **Motivação antes da mecânica.** Cada conceito entra porque o caso precisa dele.
- **Fidelidade ao artigo.** O que o artigo diz é citado como dito; o que é inferência nossa aparece como hipótese ("uma explicação plausível, não testada no artigo, é..."). Quando criticamos o artigo, apresentamos antes o argumento dos autores.
- **Ensinar vem antes de ser breve.** O leitor não sabe estatística. Defina cada termo, dê um exemplo concreto, um passo de cada vez. Cortar enchimento, nunca a explicação.

## B. Arquitetura (fixa, nesta ordem)

1. **Título** do encontro, linha "Journal Club · Pediatria" e o artigo em discussão com link do DOI.
2. **Objetivos de aprendizagem**: "Ao final deste material, você será capaz de:" seguido de 3 a 5 itens. Cada item nomeia algo que o leitor consegue fazer, **começa com maiúscula e termina com ponto**, e é cumprido por uma seção.
3. **1. Introdução**: o caso clínico ancorado no artigo, a frase central do abstract, propostas concorrentes de colegas (uma leitura ingênua e uma objeção), as perguntas que o leitor ainda não sabe responder e um parágrafo com o percurso. O caso é retomado e resolvido em "De volta à decisão".
4. **Uma seção por conceito**, com o nome do conceito como título, na ordem em que o caso exige. Dentro de cada seção, sempre nesta ordem (pule um passo só quando não se aplica):
   a. uma ou duas frases de transição: por que a pergunta surge agora no caso;
   b. a **definição** em caixa cinza (só a definição, uma ou duas frases, com citação);
   c. a aplicação aos números do artigo;
   d. notação, fórmula e, quando há resultado derivado, **Proposição N** seguida de *Demonstração* terminada em ∎;
   e. o cálculo à mão e, **logo depois**, o bloco de Python que confirma o mesmo número;
   f. o erro comum, quando houver;
   g. o quadro **Pratique**: "Antes de continuar, resolva o Exercício N (seção X)." com uma linha sobre o que observar.
5. **De volta à decisão**: reavaliar as propostas da introdução; dizer o que se pode e o que não se pode concluir; quando couber, uma frase de comunicação à família.
6. **Aplicações em saúde: leitura crítica deste estudo**: desenho, exposição, confundimento, seleção, relato. Curta.
7. **Resumo**: um parágrafo por conceito, na ordem das seções, abrindo com o nome do conceito em negrito. Nada novo.
8. **Exercícios**: casos de saúde realistas, conceituais e de código misturados; em geral um por conceito.
9. **Soluções dos exercícios**: seção visível (não recolhida), com a solução comentada de cada exercício.
10. **Leituras complementares** (3 a 5) e **Referências** numeradas.

## C. Caixas e aparato

- **Definição**: caixa cinza, nome do conceito em negrito na primeira linha, definição e citação. Sem história, ressalvas ou aplicação dentro da caixa.
- **Armadilha**: exatamente uma por encontro, dentro da seção cujo erro descreve.
- **Pratique**: uma por conceito, no fim da seção do conceito.
- **Proposições** numeradas em sequência no encontro; toda proposição tem demonstração (esboço permitido quando longa, dizendo "esboço").
- **Figuras e tabelas** numeradas, com legenda autossuficiente logo abaixo; a figura é interpretada no parágrafo seguinte.
- As funções auxiliares `DEF`, `PRACTICE`, `PITFALL` e `CAP` do `build_notebook.py` geram essas caixas com estilo embutido; reutilize-as.

## D. Números, pontuação e tipografia

- **Vírgula decimal** no texto: 0,19; 16,1%. O código pode imprimir com vírgula usando a função `br()`.
- **Percentual** sem espaço: 46,9%.
- **Intervalo de confiança**: "0,19 (IC 95% 0,14-0,27)". Sempre reportar a incerteza junto da estimativa.
- **Intervalos** com hífen e sem espaço: 2020-2023, 0,27-0,46.
- **Milhar** com ponto no texto: 1.492.
- **Travessão (—) proibido.** Use vírgula, dois-pontos ou parênteses.
- **Títulos de seção** com inicial maiúscula só na primeira palavra e em nomes próprios.
- **Negrito** só para o termo definido na primeira definição, rótulos de caixa e rótulos de proposição, exercício e resumo. Itálico com parcimônia (títulos de periódico, *Demonstração*).
- Siglas por extenso na primeira ocorrência: risco relativo (RR), odds ratio (OR).

## E. Figuras, tabelas e código

- **Legível em escala de cinza.** A cor é uma camada extra; séries e grupos se distinguem por estilo de linha, marcador e preenchimento (ex.: evento = ponto cheio, não evento = ponto vazado; OR = quadrado, RR = círculo).
- Paleta fixa: azul `#2a78d6`, laranja `#eb6834`, verde-água `#1baf7a`, cinza `#9a9993`. Não inventar cores novas.
- Eixos em escala logarítmica para razões (OR, RR), com rótulos em vírgula decimal (`plain_log_x`).
- **Python 3 apenas** (numpy, pandas, matplotlib). Comentários no código em inglês.
- **Nenhum bloco com mais de 25 linhas.** Cada bloco é introduzido por uma frase dizendo o que calcula, e o resultado é lido de volta no parágrafo seguinte.
- O código fica visível na página.

## F. Referências

- **Vancouver numerado**, lista única ao final do encontro, em ordem de primeira citação. No texto, só o número entre colchetes: [3], [5-7].
- **Nenhuma referência sem verificação**: DOI e metadados conferidos no PubMed/Crossref, ou reutilizados de uma entrada já verificada do tratado. Registrar em `SOURCE_CHECKS.md`.
- **Referência forte**: o assunto dela é a própria afirmação que ela apoia. Não citar por palavra-chave.
- O artigo do encontro é sempre a referência 1.

## G. Exercícios

- Casos de saúde realistas e plausíveis (dados sintéticos), de preferência pediátricos.
- Um exercício por conceito, no mínimo; cada quadro Pratique aponta exercícios que só exigem conceitos já apresentados.
- Toda solução mostra a conta e interpreta o resultado.
