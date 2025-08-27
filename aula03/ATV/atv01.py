# Faça um programa que verifique se uma letra digitada é consoante ou vogal

letra = input("Digite uma letra: ").lower()

match letra:
    case "a" | "e" | "i" | "o" | "u":
        print("Sua letra é uma vogal!")
    case _:
        print("Sua letra é uma consoante!")