import sqlite3

import pytest

from src.produto_repo import ProdutoRepo


@pytest.fixture
def conn():
    # ARRANGE reutilizável: banco em memória, rápido e isolado por teste.
    c = sqlite3.connect(":memory:")
    c.execute("CREATE TABLE produto (nome TEXT, categoria TEXT)")
    c.executemany(
        "INSERT INTO produto VALUES (?, ?)",
        [
            ("Clean Code", "livro"),
            ("Mouse", "eletronico"),
            ("Refactoring", "livro"),
        ],
    )
    return c


def test_busca_produtos_por_categoria(conn):
    repo = ProdutoRepo(conn)                          # Arrange
    livros = repo.buscar_por_categoria("livro")       # Act
    assert livros == ["Clean Code", "Refactoring"]    # Assert


def test_retorna_vazio_para_categoria_inexistente(conn):
    repo = ProdutoRepo(conn)
    assert repo.buscar_por_categoria("roupa") == []
