# Informe um valor e veja quanto de desconto você terá em R$, receba a % do desconto que quer receber;
reias = float(input("digite seu valor em R$:"))
desconto = float(input("digite seu desconto em porcetagem %:"))
porcentagem= desconto/100
x = reias *porcentagem
economia = reias - x
print(f"você  vai economizar {economia} R$")
