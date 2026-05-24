from utilidadesCeV.moedas import moeda
from utilidadesCeV.dados import dado
p = dado.leiaDinheiro('Digite um valor: R$')
moeda.resumo(p, 80, 35)