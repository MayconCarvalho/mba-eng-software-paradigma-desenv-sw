# Paradigma: Logico
# Base de conhecimentos de regras e fatos para a resolução de problemas lógicos.

# Fatos
pai(jose, maria).
pai(jose, joao).
mae(ana, maria).
mae(ana, joao).
pai(marcos, jose).
mae(clarice, jose).
pai(pedro, ana).
mae(renata, ana).

# Regras
eh_pai(Pai, Filho) :- 
    pai(Pai, Filho).

eh_mae(Mae, Filho) :-
    mae(Mae, Filho).

eh_irmao(Irmao1, Irmao2) :-
    pai(Pai, Irmao1),
    pai(Pai, Irmao2),
    mae(Mae, Irmao1),
    mae(Mae, Irmao2),
    Irmao1 \= Irmao2.

eh_avo(Avo, Neto) :-
    pai(Avo, Pai),
    pai(Pai, Neto).
