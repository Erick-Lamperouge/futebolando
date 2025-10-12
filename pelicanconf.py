AUTHOR = 'Erick'
SITENAME = 'Erick Labs'
SITESUBTITLE = 'notas, código e ideias'
SITEURL = ''

PATH = 'content'
TIMEZONE = 'America/Recife'
DEFAULT_LANG = 'pt'

THEME = 'theme'
THEME_TEMPLATES_OVERRIDES = ['overrides']

DEFAULT_PAGINATION = 10
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{slug}.html'

STATIC_PATHS = ['images', 'extra/ads.txt']
EXTRA_PATH_METADATA = {
    'extra/ads.txt': {'path': 'ads.txt'},
}

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.toc': {'permalink': True},
    },
    'output_format': 'html5',
}
