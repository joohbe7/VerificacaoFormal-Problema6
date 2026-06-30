# Problema Alternativo - Soma dos Primeiros N Naturais (Soma de Gauss)

## Especificação

- Pré-condição: n >= 0
- Pós-condição: s = n * (n + 1) / 2
- Função Variante: V(state) = n - i

## Invariante de Loop

0 <= i <= n  e  s == i * (i + 1) / 2

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
        s = s + i      # BUG: acumula usando o 'i' antigo, antes de incrementar
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

Teste realizado com n = 4:

```text
AssertionError: Erro: Invariante violado no corpo do loop!
```

## Explicação

O bug está na ordem das operações dentro do laço: a acumulação `s = s + i` usa o valor **antigo** de `i`, antes do incremento `i = i + 1`.

Com isso, o programa soma 0 + 0 + 1 + 2 + ... + (n - 1), computando a soma até n - 1 em vez de até n.

A consequência aparece já na primeira iteração: após `i` ser incrementado para 1, `s` ainda vale 0 (somou o 0, não o 1). Logo, o invariante `s == i * (i + 1) / 2` deixa de valer (0 ≠ 1), e a asserção de manutenção detecta a quebra e interrompe a execução.

Diferente de um erro de terminação, a função variante V(state) = n - i continua decrescendo normalmente a cada iteração — o laço terminaria, porém com o resultado errado. Trata-se, portanto, de uma falha de **correção** baseada em indução fraca (Módulo 1), e não de terminação: o invariante não se preserva do passo k para o passo k + 1.
