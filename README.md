# Blog Automatizado com Pelican + GitHub Pages

Este repositório é um _starter_ para você publicar um blog **de graça** usando **Python** (Pelican) e **GitHub Pages**, com **agendamento automático** via **GitHub Actions**.

## Como usar

1. Crie um repositório no GitHub e faça o upload destes arquivos.
2. No GitHub, vá em **Settings → Pages** e em **Build and deployment** selecione **Source: GitHub Actions**.
3. Edite `.github/workflows/pages.yml` (horário em UTC) e ajuste o `cron` para quando você deseja publicar diariamente.
4. Faça commits de _drafts_ em `content/drafts/` com `publish_on: YYYY-MM-DD HH:MM`. O workflow executa `publish.py`, que move os arquivos prontos para `content/posts/` e faz o _commit_.
5. O Pelican gera o site em `output/` e o Actions publica no GitHub Pages.

> **Timezone:** o script considera `America/Recife`. Ajuste em `publish.py` e `pelicanconf.py` se precisar.

## Escrevendo um post

Crie um arquivo Markdown em `content/drafts/` com front matter:

```markdown
---
title: Título do post
tags: [tag1, tag2]
category: Categoria
publish_on: 2025-10-12 09:00
summary: Um resumo curto do post.
---

Seu conteúdo em **Markdown** aqui.
```

Quando a data/hora chegar (no seu fuso), o post será automaticamente movido para `content/posts/` e publicado.

## Desenvolver localmente

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pelican content -o output -s pelicanconf.py
python -m http.server -d output 8000  # abra http://localhost:8000
```

## Créditos

- [Pelican](https://getpelican.com/) — gerador de site estático em Python.
- [GitHub Pages + Actions](https://docs.github.com/en/pages) — hospedagem gratuita e automação.
```
