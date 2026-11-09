"""CLI que organiza arquivos de uma pasta em subpastas por tipo."""
import argparse
import shutil
from pathlib import Path

CATEGORIAS = {
    "imagens": {".jpg", ".jpeg", ".png", ".gif", ".webp"},
    "documentos": {".pdf", ".docx", ".txt", ".md", ".xlsx", ".pptx"},
    "codigo": {".py", ".js", ".html", ".css", ".json"},
    "compactados": {".zip", ".rar", ".7z", ".tar", ".gz"},
}


def categoria_de(arquivo: Path) -> str:
    ext = arquivo.suffix.lower()
    for nome, extensoes in CATEGORIAS.items():
        if ext in extensoes:
            return nome
    return "outros"


def _destino_livre(destino: Path) -> Path:
    """Evita sobrescrever: arquivo.txt -> arquivo (1).txt"""
    if not destino.exists():
        return destino
    i = 1
    while True:
        candidato = destino.with_name(f"{destino.stem} ({i}){destino.suffix}")
        if not candidato.exists():
            return candidato
        i += 1


def organizar(pasta: Path, simular: bool = False) -> list[tuple[Path, Path]]:
    """Move arquivos para subpastas. Retorna a lista de (origem, destino)."""
    movimentos = []
    for arquivo in sorted(pasta.iterdir()):
        if not arquivo.is_file():
            continue
        destino = _destino_livre(pasta / categoria_de(arquivo) / arquivo.name)
        movimentos.append((arquivo, destino))
        if not simular:
            destino.parent.mkdir(exist_ok=True)
            shutil.move(str(arquivo), str(destino))
    return movimentos


def main() -> None:
    parser = argparse.ArgumentParser(description="Organiza arquivos por tipo.")
    parser.add_argument("pasta", type=Path, help="Pasta a organizar")
    parser.add_argument("--simular", action="store_true", help="Mostra o que seria feito")
    args = parser.parse_args()

    if not args.pasta.is_dir():
        parser.error(f"'{args.pasta}' não é uma pasta válida")

    for origem, destino in organizar(args.pasta, args.simular):
        prefixo = "[simulação] " if args.simular else ""
        print(f"{prefixo}{origem.name} -> {destino.relative_to(args.pasta)}")


if __name__ == "__main__":
    main()
