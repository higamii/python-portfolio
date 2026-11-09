from organizador import categoria_de, organizar


def test_categoria_de(tmp_path):
    assert categoria_de(tmp_path / "foto.PNG") == "imagens"
    assert categoria_de(tmp_path / "script.py") == "codigo"
    assert categoria_de(tmp_path / "estranho.xyz") == "outros"


def test_organizar_move_arquivos(tmp_path):
    (tmp_path / "a.png").write_text("x")
    (tmp_path / "b.pdf").write_text("x")
    organizar(tmp_path)
    assert (tmp_path / "imagens" / "a.png").exists()
    assert (tmp_path / "documentos" / "b.pdf").exists()


def test_simulacao_nao_move(tmp_path):
    (tmp_path / "a.png").write_text("x")
    organizar(tmp_path, simular=True)
    assert (tmp_path / "a.png").exists()


def test_nao_sobrescreve(tmp_path):
    (tmp_path / "imagens").mkdir()
    (tmp_path / "imagens" / "a.png").write_text("antigo")
    (tmp_path / "a.png").write_text("novo")
    organizar(tmp_path)
    assert (tmp_path / "imagens" / "a (1).png").read_text() == "novo"
