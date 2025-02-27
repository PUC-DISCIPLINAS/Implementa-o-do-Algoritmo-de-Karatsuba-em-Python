def karatsuba(x, y):
    # Caso base: se os números forem pequenos, use multiplicação padrão
    if x < 10 or y < 10:
        return x * y

    # Calcula o tamanho dos números
    n = max(len(str(x)), len(str(y)))
    m = n // 2

    # Divide os números em duas partes
    high1, low1 = x // 10**m, x % 10**m
    high2, low2 = y // 10**m, y % 10**m

    # Recursivamente calcula os três produtos
    z0 = karatsuba(low1, low2)
    z1 = karatsuba((low1 + high1), (low2 + high2))
    z2 = karatsuba(high1, high2)

    # Combina os resultados usando a fórmula de Karatsuba
    return (z2 * 10**(2*m)) + ((z1 - z2 - z0) * 10**m) + z0

# Solicita ao usuário que insira dois números
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

# Calcula o produto usando o algoritmo de Karatsuba
resultado = karatsuba(num1, num2)

# Exibe o resultado
print(f"O produto de {num1} e {num2} é: {resultado}")