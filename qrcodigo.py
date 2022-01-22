import qrcode

while True:
    link = str(input("Link do formulário: ").strip())
    nome = str(input("Nome do produto: ").strip())

    img = qrcode.make(f"{link}")
    img.save(f"{nome}.png")

    decida = str(input("Continuar cadastro? [s] para Sim ou [n] para Não.").upper())

    if decida in "N":
        break