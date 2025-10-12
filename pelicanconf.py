AUTHOR = 'Você'
SITENAME = 'Meu Blog Automatizado'
SITEURL = ''

PATH = 'content'
TIMEZONE = 'America/Recife'
DEFAULT_LANG = 'pt'

DEFAULT_PAGINATION = 10

ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{slug}.html'

# Opções de Markdown
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.toc': {'permalink': True},
    },
    'output_format': 'html5',
}
