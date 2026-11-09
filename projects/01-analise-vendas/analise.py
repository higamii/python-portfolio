"""Análise exploratória de vendas com dados sintéticos."""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # backend sem interface gráfica
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

SAIDA = Path(__file__).parent / "output"
PRECOS = {"Notebook": 3500, "Mouse": 80, "Teclado": 150, "Monitor": 900, "Headset": 250}


def gerar_dados(n: int = 1000, seed: int = 42) -> pd.DataFrame:
    """Gera um DataFrame de vendas reproduzível."""
    rng = np.random.default_rng(seed)
    datas = pd.to_datetime("2025-01-01") + pd.to_timedelta(rng.integers(0, 365, n), unit="D")
    df = pd.DataFrame(
        {
            "data": datas,
            "produto": rng.choice(list(PRECOS), n),
            "quantidade": rng.integers(1, 5, n),
        }
    )
    df["receita"] = df["produto"].map(PRECOS) * df["quantidade"]
    return df


def receita_mensal(df: pd.DataFrame) -> pd.Series:
    return df.groupby(df["data"].dt.to_period("M"))["receita"].sum()


def top_produtos(df: pd.DataFrame, n: int = 3) -> pd.Series:
    return df.groupby("produto")["receita"].sum().sort_values(ascending=False).head(n)


def main() -> None:
    SAIDA.mkdir(exist_ok=True)
    df = gerar_dados()
    mensal = receita_mensal(df)
    top = top_produtos(df)

    print(f"Receita total: R$ {df['receita'].sum():,.2f}")
    print("\nTop 3 produtos por receita:")
    print(top.to_string())

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
    mensal.plot(ax=ax1, marker="o", title="Receita mensal")
    top.plot(kind="bar", ax=ax2, title="Top produtos")
    fig.tight_layout()
    fig.savefig(SAIDA / "resumo.png", dpi=150)
    print(f"\nGráfico salvo em {SAIDA / 'resumo.png'}")


if __name__ == "__main__":
    main()
