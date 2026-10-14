"""Repositório de produtos usando SQLite (exemplo de teste com banco)."""


class ProdutoRepo:
    def __init__(self, conn):
        # Recebe a conexão de fora (injeção de dependência).
        self.conn = conn

    def buscar_por_categoria(self, categoria):
        cursor = self.conn.execute(
            "SELECT nome FROM produto WHERE categoria = ?", (categoria,)
        )
        return [linha[0] for linha in cursor.fetchall()]
