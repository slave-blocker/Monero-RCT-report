# Interface de multi-assinatura na fonte fixa

Referência: Monero C++, revisão `3646f648db57f60cca86430e25a635d19fa9b92a`, de 14 de Agosto de 2026. Estas observações descrevem a cópia local, sem estabelecer o estado actual da rede ou de uma distribuição de carteira.

A carteira tem uma política plana M-de-N, limitada a 16 participantes. A funcionalidade está marcada como experimental e desactivada por omissão. A troca usa os prefixos MultisigxV2R1 e MultisigxV2Rn e rejeita V1. A assinatura termina numa CLSAG; o tipo de transacção seleccionado é RCTTypeBulletproofPlus. As políticas em árvore, o mercado, a arbitragem e a integração de uma SAL distribuída não estão implementados por este fluxo.

A fonte Rust FCMP++ `31c26d96eaadbba910ffe3613ad8b4cf9c598a93` tem as primitivas opcionais SalLegacyAlgorithm (x repartido; bases G, U e Jtilde) e SalAlgorithm (componente em T repartida), no módulo SAL, apoiadas em modular-frost. A existência dessas primitivas e dos seus testes não equivale a integração de carteira. A especificação Carrot declara a ausência de segredo mestre nas carteiras de multi-assinatura e distingue os poderes de imagem e de autorização.

A sequência operacional abaixo foi deslocada da exposição matemática para este registo de referência. Conserva-se em TeX para identificar exactamente os comandos e ressalvas da fonte consultada.

```tex
\section{Sequência mínima de comandos}
\label{sec:multisig-cli}

Os comandos seguintes não constituem um guia de instalação; fixam apenas a
correspondência entre o protocolo matemático e a interface que realmente o
executa. Cada participante começa com uma carteira nova e nunca usada. Em
cada carteira:
\begin{verbatim}
set enable-multisig-experimental 1
prepare_multisig
make_multisig <M> <R1-P1> [<R1-P2> ...]
exchange_multisig_keys <Rk-P1> [<Rk-P2> ...]
\end{verbatim}
O resultado de cada comando de troca é enviado aos restantes participantes.
Repete-se o último comando enquanto a carteira disser que falta outra ronda.
Matematicamente, esta sequência constrói \(k^v\), as parcelas \(x_S\) e
\[
 K^s=\sum_{S:\,|S|=N-M+1}x_SG.
\]
Todos confirmam que a carteira terminou com o mesmo endereço antes de esse
endereço receber fundos.

Para gastar uma saída, os signatários escolhidos actualizam primeiro as
imagens de chave e os pares públicos de valores aleatórios:
\begin{verbatim}
export_multisig_info info-Pi
import_multisig_info info-P1 [info-P2 ...]
\end{verbatim}
Os ficheiros exportados são trocados entre eles. O proponente fixa a mensagem
da transacção, os anéis, os compromissos, os destinos e a taxa:
\begin{verbatim}
transfer <endereco-destino> <montante>
\end{verbatim}
Numa carteira multi-assinatura, \texttt{transfer} escreve a proposta no
ficheiro \texttt{multisig\_monero\_tx}; não a difunde. Os co-signatários
passam a versão actualizada desse mesmo ficheiro entre si e executam
\begin{verbatim}
sign_multisig multisig_monero_tx
\end{verbatim}
até uma tentativa conter as \(M\) contribuições necessárias. Cada chamada
acrescenta as parcelas ainda ausentes à resposta CLSAG
\[
 s=\sum_i\alpha_i-c\!
   \left(\mu_P\left(d+\sum_i x_i\right)+\mu_Cz\right).
\]
Depois da última verificação, uma carteira difunde a transacção completa:
\begin{verbatim}
submit_multisig multisig_monero_tx
\end{verbatim}
Assim, a sequência operacional corresponde às equações anteriores:
trocar chaves para obter \(K^s\), trocar dados para obter \(I\) e os pontos
aleatórios, fixar o traslado, somar respostas e submeter a CLSAG resultante.
O MMS automatiza o transporte e o estado destas mensagens
\cite{mms-manual,mms-project-proposal}; não altera a matemática nem o
consenso.

Na revisão consultada aplicam-se ainda os seguintes limites:
\begin{itemize}
 \item a funcionalidade tem de ser activada explicitamente por ser
 experimental;
 \item o máximo é 16 signatários;
 \item as operações multi-assinatura indicadas não são suportadas por
 carteiras de hardware;
 \item mensagens de rondas antigas ou incompletas não devem ser forçadas;
 \item uma cópia de uma carteira já convertida não deve actuar como um novo
 participante independente.
\end{itemize}

Uma carteira clonada possui as mesmas parcelas e pode repetir material de
assinatura que a original julgava consumido. As cópias de segurança devem ser
entendidas como recuperação do mesmo participante, não como um participante
adicional no limiar.
```
