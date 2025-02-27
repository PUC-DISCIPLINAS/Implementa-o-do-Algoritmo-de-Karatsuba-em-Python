# Projeto KaratsubaMultiply

## Descrição do Projeto

O projeto **KaratsubaMultiply** implementa o algoritmo de Karatsuba em Python para realizar a multiplicação eficiente de dois números inteiros. Este algoritmo, criado por Anatolii Karatsuba em 1960, é amplamente utilizado para multiplicar números grandes de forma mais eficiente do que a abordagem tradicional.

---

## Sobre o Algoritmo de Karatsuba

O algoritmo de Karatsuba utiliza uma abordagem de divisão e conquista para reduzir a quantidade de multiplicações necessárias. Ele divide cada número em duas partes e utiliza três multiplicações menores, combinadas de forma estratégica, para calcular o produto final. Isso resulta em uma complexidade assintótica de:

- **Complexidade Temporal:** O(n^log2(3)), aproximadamente O(n^1.585)
- **Complexidade Espacial:** O(n)

---

## Como Executar o Projeto

### 1. Ambiente Virtual (Opcional, mas recomendado)

Criar e ativar um ambiente virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate    # Windows
```

### 2. Executar o Script

Para executar o algoritmo, basta rodar o arquivo `main.py`:

```bash
python Karatsuba.py
```

O programa solicitará que o usuário insira dois números inteiros e exibirá o produto calculado pelo algoritmo de Karatsuba.

---

## Explicação do Código (Linha a Linha)

Arquivo: **main.py**

```python
def karatsuba(x, y):
    # Caso base: para números pequenos, usamos a multiplicação direta
    if x < 10 or y < 10:
        return x * y

    # Determina o tamanho dos números
    n = max(len(str(x)), len(str(y)))
    m = n // 2

    # Divide os números em partes alta e baixa
    high1, low1 = x // 10**m, x % 10**m
    high2, low2 = y // 10**m, y % 10**m

    # Calcula recursivamente os produtos parciais
    z0 = karatsuba(low1, low2)
    z1 = karatsuba((low1 + high1), (low2 + high2))
    z2 = karatsuba(high1, high2)

    # Combina os resultados conforme a fórmula de Karatsuba
    return (z2 * 10**(2*m)) + ((z1 - z2 - z0) * 10**m) + z0

# Entrada e saída do programa
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
resultado = karatsuba(num1, num2)
print(f"O produto de {num1} e {num2} é: {resultado}")
```

---

## Relatório Técnico

### Complexidade Assintótica

- Melhor caso: O(n^log2(3))
- Caso médio: O(n^log2(3))
- Pior caso: O(n^log2(3))

Essa complexidade é mais eficiente do que a multiplicação tradicional (O(n²)), especialmente para números muito grandes.

### Complexidade Ciclomática

#### Fluxo de Controle (Grafo de Fluxo)

- Nós (N): 7
- Arestas (E): 8
- Componentes Conexos (P): 1

Fórmula: M = E - N + 2P
M = 8 - 7 + 2(1) = 3

A complexidade ciclomática do algoritmo é **3**, indicando que há 3 caminhos independentes no fluxo de controle da função `karatsuba`.

### Visualização do Grafo de Fluxo

![image](https://github.com/user-attachments/assets/2246f900-4ce4-4a5d-964d-21938d94b73f)


---

## Conclusão

O algoritmo de Karatsuba oferece uma solução eficiente para multiplicação de números inteiros grandes, sendo amplamente utilizado em áreas como criptografia e manipulação de big integers. Este projeto cumpre os requisitos solicitados e inclui toda a documentação necessária para entendimento e execução.

---

## Licença

Este projeto está licenciado sob a Licença MIT.



