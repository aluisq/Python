premio = float(input("Digite o valor do premio: "))

inv_prim = float(input("Digite o valor investido pelo primeiro ganhador: "))

inv_seg = float(input(("Digite o valor investido pelo segundo ganhador: ")))

inv_ter = float(input("Digite o valor investido pelo terceiro ganhador: "))


inv_total = inv_prim + inv_seg + inv_ter

print(f"Foi investido a quantia de R${inv_total}")

payback = premio - inv_total


payback_prim = round((inv_prim*payback)/inv_total,2)

payback_seg = round((inv_seg*payback)/inv_total,2)

payback_ter = round((inv_ter*payback)/inv_total,2)


print(f"""
O prêmio no valor de R${premio} reais foi dividido da seguinte maneira:
[1] - O primeiro ganhador receberá: {payback_prim}
[2] - O segundo ganhador receberá: {payback_seg}
[3] - O terceiro ganhador receberá: {payback_ter}
""")
