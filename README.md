# Projeto KaratsubaMultiply

O **KaratsubaMultiply** é um projeto desenvolvido para explorar e demonstrar o funcionamento do **Algoritmo de Karatsuba**, uma técnica eficiente para realizar a multiplicação de números inteiros grandes. Este projeto utiliza uma implementação personalizada do algoritmo, com foco em aprendizado e análise da eficiência computacional em comparação com a multiplicação tradicional.

---

## O Algoritmo de Karatsuba

O **Algoritmo de Karatsuba** é uma abordagem de **divisão e conquista** para multiplicar números grandes, reduzindo o número total de multiplicações necessárias. Ao invés de realizar as tradicionais 4 multiplicações, como no método ingênuo, o Karatsuba utiliza apenas 3 multiplicações e algumas somas e subtrações, melhorando a eficiência para grandes entradas.

---

## Complexidade Computacional

O algoritmo de Karatsuba possui uma complexidade assintótica de:

\[
O(n^{\log_2 3}) \approx O(n^{1.585})
\]

Essa complexidade é significativamente melhor do que a multiplicação ingênua de:

\[
O(n^2)
\]

Essa melhora faz com que o algoritmo de Karatsuba seja muito utilizado em bibliotecas de cálculo numérico e aplicações que lidam com números extremamente grandes.

---

## Diferença entre Karatsuba e Multiplicação Tradicional

| Método | Complexidade |
|---|---|
| Multiplicação Tradicional | O(n²) |
| Karatsuba | O(n¹⁾µ⁸⁵) |

Enquanto a multiplicação tradicional realiza multiplicações diretas dígito a dígito, o Karatsuba divide os números, resolve subproblemas menores e combina os resultados com uma fórmula otimizada. Isso reduz drasticamente o tempo de execução para números grandes.

---

## Dependências

Nenhuma dependência externa é necessária para rodar este projeto, apenas o Python padrão.

---

## Ambiente Virtual

### Passo 1: Criar e ativar o ambiente virtual

É recomendável utilizar um ambiente virtual para isolar o projeto:

```bash
python3 -m venv .venv
```

Ativação:

- No macOS e Linux:
    ```bash
    source .venv/bin/activate
    ```
- No Windows:
    ```bash
    .venv\Scripts\activate
    ```

---

## Passo 2: Executar o script

Com o ambiente virtual ativado (ou mesmo sem ele), basta executar o script principal:

```bash
python karatsuba.py
```

---

## Versão do Python

Este projeto foi desenvolvido e testado na versão 3.13.0 do Python, mas deve funcionar em versões 3.8+.

---

## Explicação das Funções

### 🗄 Arquivo: karatsuba.py

**Objetivo:** Este arquivo implementa o algoritmo de Karatsuba e executa testes com diferentes números.

### Função principal: `karatsuba(x, y)`

**Descrição:**  
Executa a multiplicação de dois números inteiros grandes usando o algoritmo de Karatsuba.

**Parâmetros:**
- `x`: Primeiro número inteiro.
- `y`: Segundo número inteiro.

**Retorno:**  
- O resultado da multiplicação de `x` e `y`.

---

## Estrutura do Arquivo

- Importa módulos padrão (se necessário).
- Define a função recursiva `karatsuba`.
- Contém casos de teste direto no `if __name__ == "__main__"`.

### Exemplo de função:

```python
def karatsuba(x, y):
    if x < 10 or y < 10:  # Casos base
        return x * y

    n = max(len(str(x)), len(str(y)))
    m = n // 2

    x1, x0 = divmod(x, 10**m)
    y1, y0 = divmod(y, 10**m)

    p1 = karatsuba(x1, y1)
    p2 = karatsuba(x0, y0)
    p3 = karatsuba(x1 + x0, y1 + y0)

    return p1 * 10**(2*m) + (p3 - p1 - p2) * 10**m + p2
```

---

## Saída da Execução

### Exemplo de saída ao executar:

```bash
Multiplicando 1234 por 5678
Resultado: 7006652
```

---

## Documentação e Links Úteis

- [Artigo sobre o Algoritmo de Karatsuba - Wikipedia](https://pt.wikipedia.org/wiki/Algoritmo_de_Karatsuba)
- [Introdução a Algoritmos - Cormen et al.](https://www.amazon.com.br/Introduction-Algorithms-Thomas-H-Cormen/dp/026204630X)

---

## Licença

Este projeto está licenciado sob a Licença MIT. Sinta-se à vontade para usar, modificar e distribuir.

