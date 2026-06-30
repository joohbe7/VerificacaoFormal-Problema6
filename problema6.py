# 1. ASSERCAO DE PRE-CONDICAO
assert n > 0, "Erro: Pre-condicao violada!"

d = n - 1

# 2. ASSERCAO DE INICIALIZACAO (CASO BASE)
assert 0 < d < n, \
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
    assert 0 < d < n, \
        "Erro: Invariante violado no corpo do loop!"

    # 4. DECREMENTO DA VARIANTE
    assert d < velha_variante, \
        "Erro: Loop em execucao infinita (sem progresso)!"

resultado = 1

# 5. POS-CONDICAO FINAL
assert resultado < n and n % resultado == 0, \
    "Erro: A pos-condicao falhou na terminacao!"

return resultado
