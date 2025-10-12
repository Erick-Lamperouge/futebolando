#!/usr/bin/env python3
import os, re, subprocess
from datetime import datetime
from zoneinfo import ZoneInfo
import frontmatter

DRAFTS_DIR = os.path.join('content', 'drafts')
POSTS_DIR = os.path.join('content', 'posts')

def slugify(text):
    import unicodedata
    text = unicodedata.normalize('NFKD', text)
    text = ''.join(c for c in text if not unicodedata.combining(c))
    text = re.sub(r'[^a-zA-Z0-9\s-]', '', text).strip().lower()
    text = re.sub(r'[\s-]+', '-', text)
    return text

def ensure_dirs():
    os.makedirs(DRAFTS_DIR, exist_ok=True)
    os.makedirs(POSTS_DIR, exist_ok=True)

def parse_publish_on(meta):
    value = meta.get('publish_on')
    if not value:
        return None
    for fmt in ('%Y-%m-%d %H:%M', '%Y-%m-%d'):
        try:
            return datetime.strptime(value, fmt)
        except ValueError:
            pass
    raise ValueError(f"Formato inválido em publish_on: {value!r}. Use 'YYYY-MM-DD' ou 'YYYY-MM-DD HH:MM'.")

def main():
    ensure_dirs()
    tz = ZoneInfo('America/Recife')
    now = datetime.now(tz).replace(second=0, microsecond=0)
    changed = False

    for name in sorted(os.listdir(DRAFTS_DIR)):
        if not name.endswith('.md'):
            continue
        path = os.path.join(DRAFTS_DIR, name)
        post = frontmatter.load(path)
        pub_dt = parse_publish_on(post.metadata)
        if pub_dt is None:
            continue
        if pub_dt.tzinfo is None:
            pub_dt = pub_dt.replace(tzinfo=tz)
        if pub_dt <= now:
            title = post.get('title') or post.metadata.get('Title') or 'sem-titulo'
            slug = post.metadata.get('slug') or slugify(title)
            post.metadata['date'] = now.strftime('%Y-%m-%d %H:%M')
            post.metadata.pop('publish_on', None)
            post.metadata.pop('status', None)
            outname = f"{slug}.md"
            outpath = os.path.join(POSTS_DIR, outname)
            with open(outpath, 'w', encoding='utf-8') as f:
                f.write(frontmatter.dumps(post))
            os.remove(path)
            print(f"Publicado: {outpath}")
            changed = True

    if changed and os.environ.get('GITHUB_ACTIONS') == 'true':
        subprocess.run(['git', 'config', 'user.name', 'github-actions[bot]'], check=True)
        subprocess.run(['git', 'config', 'user.email', 'github-actions[bot]@users.noreply.github.com'], check=True)
        subprocess.run(['git', 'add', '.'], check=True)
        subprocess.run(['git', 'commit', '-m', 'Publica posts agendados [skip ci]'], check=True)
        subprocess.run(['git', 'push'], check=True)

if __name__ == '__main__':
    main()
