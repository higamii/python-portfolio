# 03 · Organizador de Arquivos

Ferramenta de linha de comando que separa arquivos de uma pasta em subpastas (`imagens`, `documentos`, `codigo`...).

## Uso
```bash
python organizador.py ~/Downloads --simular   # só mostra o que faria
python organizador.py ~/Downloads             # move de verdade
```

## Testes
```bash
pytest
```

## Destaques
- Modo `--simular` (dry run) para segurança
- Nunca sobrescreve arquivos existentes
- Testes com `tmp_path` (sem tocar no seu disco)
