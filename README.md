# Verificação de Programas - Trabalho

Este repositório contém a solução de dois problemas de verificação de programas utilizando pré-condições, pós-condições, invariantes de loop e funções variantes para identificação de falhas de correção e terminação.

---

# Problema 6 - Busca do Maior Divisor Próprio

## Especificação

- Pré-condição: `n > 0`
- Pós-condição: retornar o maior divisor próprio de `n`
- Função Variante: `V(state) = d`

## Invariante de Loop

`0 <= d < n`

## Código

```python
def largest_proper_divisor_broken(n: int):

    # 1. ASSERCAO DE PRE-CONDICAO
    assert n > 0, "Erro: Pre-condicao violada!"

    d = n - 1

    # 2. ASSERCAO DE INICIALIZACAO (CASO BASE)
    assert 0 <= d < n, \
        "Erro: Invariante falhou na inicializacao!"

    while d > 0:

        # 4. FUNCAO VARIANTE
        velha_variante = d

        assert velha_variante >= 0, \
            "Erro: Variante violou o limite inferior!"

        if n % d == 0:
            resultado = d

            # 5. POS-CONDICAO
            assert resultado < n and n % resultado == 0, \
                "Erro: A pos-condicao falhou na terminacao!"

            return resultado

        # BUG ORIGINAL:
        # d = d - 1
        # (decremento ausente)

        # 3. MANUTENCAO DO INVARIANTE
        assert 0 <= d < n, \
            "Erro: Invariante violado no corpo do loop!"

        # 4. DECREMENTO DA VARIANTE
        assert d < velha_variante, \
            "Erro: Loop em execucao infinita (sem progresso)!"

    resultado = 1

    # 5. POS-CONDICAO FINAL
    assert resultado < n and n % resultado == 0, \
        "Erro: A pos-condicao falhou na terminacao!"

    return resultado
```

## Falha Encontrada

Teste realizado com `n = 9`:

```text
AssertionError: Erro: Loop em execucao infinita (sem progresso)!
```

## Explicação

O decremento da variável `d` está ausente quando `n % d != 0`. Assim, a função variante `V(state) = d` não diminui a cada iteração do laço. A asserção

```python
assert d < velha_variante
```

detecta essa falha e interrompe a execução.

---

# Problema Alternativo - Soma dos Primeiros N Naturais (Soma de Gauss)

## Especificação

- Pré-condição: `n >= 0`
- Pós-condição: `s = n * (n + 1) / 2`
- Função Variante: `V(state) = n - i`

## Invariante de Loop

`0 <= i <= n` e `s == i * (i + 1) / 2`

## Código

```python
def sum_naturals_broken(n: int):

    # 1. ASSERCAO DE PRE-CONDICAO
    assert n >= 0, "Erro: Pre-condicao violada!"

    s = 0
    i = 0

    # 2. ASSERCAO DE INICIALIZACAO (CASO BASE)
    assert 0 <= i <= n and s == i * (i + 1) // 2, \
        "Erro: Invariante falhou na inicializacao!"

    while i < n:

        # 4. FUNCAO VARIANTE
        velha_variante = n - i

        assert velha_variante >= 0, \
            "Erro: Variante violou o limite inferior!"

        # Corpo do algoritmo (COM BUG)
        s = s + i
        i = i + 1

        # 3. MANUTENCAO DO INVARIANTE
        assert 0 <= i <= n and s == i * (i + 1) // 2, \
            "Erro: Invariante violado no corpo do loop!"

        # 4. DECREMENTO DA VARIANTE
        assert (n - i) < velha_variante, \
            "Erro: Loop em execucao infinita (sem progresso)!"

    # 5. POS-CONDICAO FINAL
    assert s == n * (n + 1) // 2, \
        "Erro: A pos-condicao falhou na terminacao!"

    return s
```

## Falha Encontrada

Teste realizado com `n = 4`:

```text
AssertionError: Erro: Invariante violado no corpo do loop!
```

## Explicação

O bug está na ordem das operações dentro do laço: a acumulação `s = s + i` utiliza o valor antigo de `i`, antes do incremento `i = i + 1`.

Com isso, o programa calcula a soma até `n - 1`, produzindo um resultado incorreto. A consequência aparece já na primeira iteração: após `i` ser incrementado para `1`, o valor de `s` ainda é `0`, fazendo com que o invariante deixe de ser satisfeito.

A asserção de manutenção do invariante detecta a falha imediatamente e interrompe a execução. A função variante continua diminuindo normalmente, portanto o problema é de correção do algoritmo, e não de terminação.
