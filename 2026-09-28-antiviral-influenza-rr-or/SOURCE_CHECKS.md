# SOURCE_CHECKS: 28/09/2026, risco relativo e odds ratio

Registro interno da verificação. Não é publicado como conteúdo do encontro.

## Artigo (referência 1)

Huang Y-N et al. Pediatrics. 2026;158(3):e2025075020. doi:10.1542/peds.2025-075020. PDF lido na íntegra (fora do repositório), texto extraído com `pdftotext -layout`.

| Número usado no material | Onde está no artigo | Conferido |
|---|---|---|
| 354 internados, 1.138 não internados, 1.492 no total | Resultados, Figura 1 | sim |
| 1.539 com influenza confirmada, 1.531 elegíveis | legenda da Figura 1 | sim |
| Antiviral precoce: 194 internados, 1.012 não internados | Tabela 1 | sim |
| Tardio: 156 e 113; nenhum: 4 e 13 | Tabela 1 (continuação) | sim |
| OR bruto 0,15 (0,11-0,20); aOR 0,19 (0,14-0,27) | Tabela 2 | sim; OR bruto recalculado bate |
| Vacina: OR bruto 1,56 (1,20-2,03); aOR 0,62 (0,42-0,90) | Tabela 2 | sim |
| Antibiótico 10,87/7,23; corticoide 4,71/1,99; comorbidade 2,42/2,29; coinfecção 9,86/3,95 | Tabela 2 | sim |
| Vacinação pública: 55,6% dos internados, 30,0% dos não internados | Tabela 1 | sim |
| Vacina paga ausente do registro nacional, imputada | Métodos e Discussão (limitações) | sim |
| Peramivir IV 28,8% vs 3,9%; terapia combinada 20,1% vs 1,7% | Tabela 1 (continuação) | sim |
| Mediana de 1,5 dia entre início do tratamento e internação | Resultados | sim |
| Sensibilidade sem peramivir: efetividade 80%-82% | Resultados, análises de sensibilidade | sim |
| E-value 10,0 | Abstract e Resultados | sim; reproduzido tratando OR como RR |
| "All eligible cases were matched to all eligible controls" | Métodos | sim, citação literal |
| Antibiótico precoce como possível marcador de gravidade | Discussão | sim |
| Hospitais como grandes prestadores de atenção primária, população razoavelmente representativa | Discussão (limitações) | sim |

**Inferências nossas, marcadas como tal no texto:** a amostra funciona como coorte hospitalar (deduzido do fluxograma e da frase dos Métodos); a vacinação pública alcançaria mais crianças de maior risco (hipótese, não testada no artigo); a direção do confundimento por indicação não é evidente (argumento nosso, apresentado depois do argumento dos autores).

## Referências 2-13

Reutilizadas das entradas já verificadas do tratado (`bibliography/global/global.bib`, `chapters/ch07/references/ch07.bib`, `chapters/ch22/references/ch22.bib`), com metadados e DOI conferidos lá. Knol 2008: números usados (150 relatos, 125 com casos incidentes, 105 compatíveis com razão de taxas) conforme `chapters/ch07/SOURCE_CHECKS.md` do tratado. VanderWeele e Ding 2017: recomendação de RR ≈ √OR para desfecho comum (acima de 15%). McNutt 2003: viés da correção de Zhang e Yu com OR ajustado e recomendação de log-binomial ou Poisson robusto.

## Código

Notebook executado do início ao fim sem erro em 28/09/2026. Todos os números impressos conferem com o texto: RR 0,29 (0,24-0,34); OR 0,15 (0,11-0,20); fator 0,53; RR de Zhang e Yu 0,35 (0,27-0,46); E-values 10,0, 4,0 e 5,2; NNT 154, 52, 16 e 6; soluções dos exercícios 1-9.
