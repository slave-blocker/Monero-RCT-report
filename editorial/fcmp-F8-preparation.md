# Preparação de F8 — composição e tamanho

Fontes inspeccionadas em 11 de Novembro de 2026. Notas para a próxima unidade; ainda não incorporadas no capítulo. O ponto de recuperação textual e dos PDFs é `0ab541c`.

## Composição

Fonte: `/home/dollner/Public/tmp/Monero-RCT-report-research-sources/extracted/cypherstack-fcmp-review/main.tex`, sobretudo linhas 95–193 e 536–701.

- O resultado de composição (575–618) assume extracção de conhecimento (CWEE) e conhecimento zero perante verificador honesto (SHVZK) para a pertença e os componentes SAL. A relação principal extrai o registo, x,y,r_C; a abertura do compromisso C pertence às garantias das saídas admitidas e das suas provas de intervalo.
- A extracção descendente da raiz para a folha usa a abertura pública da raiz, a abertura ampliada de GBP, o certificado da máscara e a vinculação do sinal pelo inicializador. F4 já demonstra as comparações; F8 deve reunir a indução e as hipóteses, conservando os erros algébricos de F6/F7.
- F2 já demonstra a vinculação das testemunhas SAL e pertença. O resultado é O=xG+yT, I=xJ e Ctilde=C+r_CG para o mesmo registo. Duas aberturas conhecidas distintas de O dariam uma relação de logaritmo discreto; daí a mesma imagem para novo gasto da mesma saída. A validação externa compara imagens válidas e não nulas entre entradas e com o estado anterior.
- A autorização depende da mensagem de transacção vinculada ao desafio. A condição I≠O_neutro conserva uma declaração não trivial na verificação da imagem (fonte 643–652).
- A interface Rust, `monero-oxide/ringct/fcmp++/src/lib.rs:227–228`, exige que a mensagem assinável vincule prefixo, base RingCT e pseudo-compromissos. SHVZK descreve a informação acrescentada pela prova para um enunciado fixo; a privacidade da transacção inteira exige o seu próprio âmbito.
- A simulação da fonte (583–587) volta a sortear Ctilde apesar de este pertencer ao enunciado. Na exposição, conservar Ctilde e I fixos; sortear apenas Otilde,Jtilde,R,P. Com máscaras uniformes, estes quatro pontos são conjuntamente uniformes pela sequência r_O,r_J,r_R,r_P. As correlações de pseudo-compromissos impostas pelo equilíbrio devem ser conservadas. Confrontar a construção exacta dos simuladores e o domínio condicionado das testemunhas antes de apresentar a garantia para a realização concreta.
- O resultado citado não estabelece extractibilidade após simulação para toda a composição (621–623). A resistência a colisões dirigidas entre imagens de saídas diferentes, para chaves O=xG+yT, também fica fora da análise concluída (654–685). Distinguir estes âmbitos da propriedade demonstrada de imagem estável para a mesma saída.
- As observações sobre sigilo retrospectivo perante cálculo de logaritmos discretos (688–701) dependem ainda da realização da pertença e do restante contexto da transacção. Não transformar a reconstrução de SAL numa garantia pós-quântica de toda a transacção.

## Tamanho exacto da realização seleccionada

Fontes Rust: `crypto/fcmps/src/lib.rs:214–302`; `monero-oxide/ringct/fcmp++/src/lib.rs:186–220`; `monero-oxide/ringct/fcmp++/src/sal/mod.rs:410–422`, na cópia `/home/dollner/monero-oxide-fcmp` já identificada no registo de versões. Ponto ou escalar ocupa 32 bytes.

Sejam a=⌊(L−1)/2⌋, b=⌊L/2⌋ e ε=L mod2, para n,L≥1. Conservar m_S,m_H de F6. Os compromissos totais são:

    s_S = nb + ε + ceil(n(2304 + 512a) / m_S)
    s_H = n(b − 1 + ε) + 1 − ε + ceil(512nb / m_H).

As primeiras parcelas contam os compromissos dos ramos, incluindo uma só ocorrência do ramo da raiz; as últimas contam os compromissos auxiliares. Explicar a capacidade de cada K e os dados de F5 ao deduzir estas expressões.

Uma GBP transmite s pontos K, três pontos A_I,A_O,S, 3s+5 pontos T_i, três escalares τ_ξ,μ,t_hat, 2log₂m pontos das rondas IPA e dois escalares finais. Total: 4s+13+2log₂m elementos. Os 3s+5 pontos T_i resultam dos índices s+1 até 2d+2, excluindo d=2s+2.

Para as duas GBP e o único fecho de Schnorr da raiz:

    B_pertença = 32[4(s_S+s_H) + 28 + 2(log₂m_S+log₂m_H)].

SAL transmite seis pontos e seis escalares: 384 bytes por entrada. O objecto serializado FCMP++ acrescenta ainda três pontos de apresentação por entrada, 96 bytes. Ctilde já pertence ao campo pseudo-outs; as imagens de chave pertencem às entradas. Logo:

    B_blob_FCMP++ = B_pertença + 480n.

Esta quantidade não é o tamanho de toda a transacção. Conservar a separação entre provas, apresentações, pseudo-compromissos, imagens e provas de intervalo.

| n | L | m_S | m_H | s_S | s_H | Pertença (bytes) | Objecto FCMP++ (bytes) |
|---|---|---|---|---|---|---|---|
| 1 | 3 | 256 | 128 | 13 | 5 | 4160 | 4640 |
| 2 | 3 | 512 | 128 | 14 | 10 | 4992 | 5952 |
| 1 | 8 | 256 | 128 | 19 | 20 | 6848 | 7328 |
| 2 | 8 | 512 | 256 | 23 | 23 | 7872 | 8832 |
| 1 | 9 | 512 | 128 | 14 | 20 | 6272 | 6752 |
| 1 | 10 | 512 | 256 | 14 | 15 | 5696 | 6176 |

As contas foram conferidas independentemente por duas leituras e por cálculo Python. O tamanho não é monótono em L: duplicar m pode reduzir os compromissos auxiliares e os T_i, compensando a ronda adicional. Explicar esta acomodação por contagem, sem prometer monotonicidade.

## Fecho a preparar

F8 deve acrescentar cerca de seis páginas contínuas, atingindo 38 páginas de texto, e terminar com uma visão conjunta das propriedades demonstradas e das condições. O poster novo permanece uma unidade posterior de composição visual. Continuar a exposição cumulativa e afirmativa; manter historial e qualificações de fontes nestas notas, com as condições matemáticas necessárias no texto.
