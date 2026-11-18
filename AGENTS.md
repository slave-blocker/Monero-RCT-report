# Repository instructions

- Write in European Portuguese, using the spelling conventions preceding the 1990 Orthographic Agreement, in a style inspired by Eça de Queirós. Preserve clarity, pedagogical progression, and mathematical precision.
- Write source material as finished prose. Do not mention user prompts, requests, or instructions, and do not add meta-commentary about earlier drafts, corrections, improvements, or the process used to produce the text, unless the user explicitly requests editorial history.
- Treat the book as a cumulative exposition, not as a collection of standalone chapters. In advanced chapters, assume the terminology, notation, and elementary operations established earlier in the book; repeat them only when a genuinely new ambiguity requires it.
- Centre the exposition on the mathematics behind Monero: definitions, exact relations, derivations, and the hypotheses under which the results hold. Present the selected construction as a fixed mathematical object, with a lasting, self-contained exposition rather than a running account of software development. Do not present contingent implementation choices or conjectures as unconditional mathematical laws.
- Keep commit hashes, audit debates, implementation chronology, and incidental code details out of the chapter prose. Use primary papers and source code to establish correctness; keep source-version tracking in working notes or bibliographic metadata rather than in the exposition.
- Make understanding possible through reading alone. Work out necessary calculations in the text, explain the meaning of equations and their variables, and build memorable connections between successive ideas. Do not require a pencil, external calculations, or exercises to follow the argument.
- Explique as construções afirmativamente: apresente o que cada objecto é, como funciona e que propriedade estabelece. Elimine contrastes didácticos recorrentes da forma «não é X, mas Y» e enumerações do que uma construção não faz. Desenvolva contra-exemplos, falhas e comparações pela negativa quando forem expressamente pedidos; conserve sempre as condições matemáticas e as hipóteses necessárias à exactidão do texto.
- Use «de Monero», «por Monero» e «em Monero», conforme a construção gramatical, sem artigo antes do nome. Para designar a blockchain, use «lista de blocos»; preserve os sentidos matemáticos próprios de «cadeia» quando designem outros objectos.
- Organize as secções pela continuidade do argumento. A extensão de cada secção deve acompanhar a matéria; elimine o esquema de uma página por secção nos capítulos de divisores e FCMP++. Reserve as quebras de página explícitas para necessidades reais de composição.

## Preservação de Bulletproofs e Bulletproofs+

- Preservar a secção «Bulletproofs» (`sec:bullet_proofs`) de `translations/pt/content/commitments.tex` que começa com a epígrafe «Sou mais rápido quando me mexo», atribuída a Sundance, e «Em português: provas de bala». A referência para o seu conteúdo, incluindo todas as subsecções, é o commit `cbe02ed603ff22f9b5cfd8174f03fb2ade86f0b6`.
- Conservar a redacção, a notação, as equações, os exemplos, os diagramas e a sequência expositiva dessa versão. Está autorizada, nesta primeira intervenção, a remoção dos espaços em branco excessivos e das quebras de página que os provoquem. Os restantes aperfeiçoamentos ficam para pedidos posteriores.
- Esta preservação tem precedência sobre as directivas gerais de estilo, reescrita e uniformização deste repositório. Mesmo em revisões sucessivas ou pedidos genéricos para tornar o livro mais literal («verbatim»), conservar a secção conforme a referência fixa acima, admitindo apenas a limpeza de espaços já autorizada. Qualquer outra alteração exige um pedido que identifique expressamente esta secção; a referência permanece fixa à medida que o histórico avança.
- Conservar a secção «Bulletproofs+» (`sec:bulletproof_plus`) no estado do commit `be3da539d8b5a64faf89d97688210ce32966ac77`. A reposição da versão anterior e a limpeza de espaços incidem apenas na secção de Bulletproofs clássicas.
- O capítulo de Generalized Bulletproofs, em `translations/pt/content/generalizedBulletproofs.tex`, tem âmbito próprio.

## O segredo público gamma

- O título deve ser exactamente «O segredo público gamma», com «gamma» escrito por extenso, sem o substituir pela letra grega. Destina-se ao capítulo sobre o logaritmo discreto de \(H\) em relação a \(G\), em `translations/pt/content/dlogRelations.tex`: \(\gamma=\log_G H\), ou seja, \(H=\gamma G\).
- Preservar o jogo de palavras do título. Os pontos \(G,H\) são públicos e determinam a relação; a dificuldade computacional de encontrar \(\gamma\) sustenta a propriedade de vinculação dos compromissos. O título deve acompanhar esta distinção matemática.

## FCMP++ rewriting scope

- Rebuild the FCMP++ chapter from primary sources. Do not reuse the existing chapter's prose, structure, examples, figures, or sequence of exposition. The old chapter remains recoverable through Git history only.
- The replacement FCMP++ chapter is to occupy 38 text pages, including three additional pages explaining the need for divisor certificates and their computational costs. The former chapter occupied 27 text pages, excluding its following one-page poster.
- Use the preceding chapter on divisors as established mathematical background, consistent with the cumulative exposition of the book.

## Local primary sources

These paths were checked on 3 October 2026. Inspect the relevant files directly; directory names and bibliography entries alone do not establish their contents. Local copies are fixed source material, not evidence of the current network's deployment status. Do not update or alter these source repositories as part of writing the book.

- Monero C++ repository: `/home/dollner/monero`.
- Additional fixed Monero source snapshot, including Curve Trees integration: `/home/dollner/Public/tmp/Monero-RCT-report-research-sources/extracted/monero-master-3d3920d7-src`; relevant code in `src/fcmp_pp/`.
- FCMP++ specification by Luke Parker, including `fcmp++.tex` and `fcmp++.pdf`: `/home/dollner/Public/tmp/Monero-RCT-report-research-sources/extracted/fcmp-plus-plus-paper-develop`.
- Monero-oxide FCMP++ Rust implementation: `/home/dollner/monero-oxide-fcmp`.
  - Membership circuit, tree, and branch masks: `crypto/fcmps/`, especially `src/circuit.rs`, `src/tree.rs`, and `src/prover/blinds.rs`.
  - Spend authorization and linkability (SAL): `monero-oxide/ringct/fcmp++/src/sal/`.
  - Generalized Bulletproofs: `crypto/generalized-bulletproofs/`.
  - Scalar-multiplication gadgets: `crypto/fcmps/ec-gadgets/`.
  - Divisor witness construction: `crypto/divisors/`.
  - Helios-Selene curve cycle: `crypto/helioselene/`.
- Curve Trees reference/benchmark implementation: `/home/dollner/curve-trees`; relevant material in `relations/`, `readme.md`, and `bulletproofs/generalized-bulletproofs.md`. A local modification was found in `relations/tests/curve_tree.rs`; distinguish it from upstream material.
- Cypher Stack FCMP++ composition/security proofs, with LaTeX source: `/home/dollner/Public/tmp/Monero-RCT-report-research-sources/extracted/cypherstack-fcmp-review`.
- Composition review PDF: `/home/dollner/monero-oxide-fcmp/audits/fcmp++/Review.pdf`.
- Generalized Bulletproofs mathematical/security reports: `/home/dollner/monero-oxide-fcmp/audits/generalized-bulletproofs/`, including `Fixed Protocol.pdf`, `Security Proofs.pdf`, and `Updated Security Proofs.pdf`.
- Helios-Selene security assessment: `/home/dollner/monero-oxide-fcmp/audits/helioselene/`.
- Liam Eagen's principal-divisor and Weil-reciprocity paper: `/home/dollner/Public/tmp/Monero-RCT-report-research-sources/archives/eagen-2022-596.pdf`; extracted text in `/home/dollner/Public/tmp/Monero-RCT-report-research-sources/extracted/eagen-2022-596-text/eagen.txt`.
- Bulletproofs++ paper (a complementary source, distinct from FCMP++ and Generalized Bulletproofs): `/home/dollner/Downloads/2022-510.pdf`.
- Central archive of source snapshots and extracted repositories: `/home/dollner/Public/tmp/Monero-RCT-report-research-sources/`, with `archives/` and `extracted/` subdirectories. A duplicate of the FCMP++ Rust snapshot is in `extracted/monero-oxide-31c26d96-src/`.
- Older FCMP++ implementation for historical comparison only: `/home/dollner/fcmp-plus-plus`.

The original Curve Trees paper, SLVer Bullet, zkSecurity divisor notes, the complete Veridise FCMP audit, and the Trail of Bits FCMP audit were not located as local standalone documents during this search. Some source READMEs link to them; a link is not a local copy.
