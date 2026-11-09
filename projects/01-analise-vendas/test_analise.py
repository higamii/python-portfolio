from analise import gerar_dados, receita_mensal, top_produtos


def test_dados_sao_reproduziveis():
    assert gerar_dados(seed=1).equals(gerar_dados(seed=1))


def test_soma_mensal_igual_ao_total():
    df = gerar_dados()
    assert receita_mensal(df).sum() == df["receita"].sum()


def test_top_produtos_tamanho_e_ordem():
    top = top_produtos(gerar_dados(), n=3)
    assert len(top) == 3
    assert list(top) == sorted(top, reverse=True)
