# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import time

# !! This is the configuration of Nikola. !! #
# !!  You should edit it to your liking.  !! #


# ! Some settings can be different in different languages.
# ! A comment stating (translatable) is used to denote those.
# ! There are two ways to specify a translatable setting:
# ! (a) BLOG_TITLE = "My Blog"
# ! (b) BLOG_TITLE = {"en": "My Blog", "es": "Mi Blog"}
# ! Option (a) is used when you don't want that setting translated.
# ! Option (b) is used for settings that are different in different languages.


# Data about this site
BLOG_AUTHOR = "Biblioteca de Los Navalmorales"  # (translatable)
BLOG_TITLE = "Biblioteca Los Navalmorales"  # (translatable)
# This is the main URL for your site. It will be used
# in a prominent link
SITE_URL = "http://biblioln.es/"
# This is the URL where Nikola's output will be deployed.
# If not set, defaults to SITE_URL
# BASE_URL = "http://biblioln.es/"
BLOG_EMAIL = "carlosvin@gmail.com"
BLOG_DESCRIPTION = "Biblioteca P\u00fablica Municipal de Los Navalmorales"  # (translatable)

# What is the default language?
DEFAULT_LANG = "es"

# What other languages do you have?
# The format is {"translationcode" : "path/to/translation" }
# the path will be used as a prefix for the generated pages location
TRANSLATIONS = {
    DEFAULT_LANG: "",
    # Example for another language:
    # "es": "./es",
}

# What will translated input files be named like?

# If you have a page something.rst, then something.pl.rst will be considered
# its Polish translation.
#     (in the above example: path == "something", ext == "rst", lang == "pl")
# this pattern is also used for metadata:
#     something.meta -> something.pl.meta

TRANSLATIONS_PATTERN = "{path}.{lang}.{ext}"

# Links for the sidebar / navigation bar.  (translatable)
# This is a dict.  The keys are languages, and values are tuples.
#
# For regular links:
#     ('http://getnikola.com/', 'Nikola Homepage')
#
# For submenus:
#     (
#         (
#             ('http://apple.com/', 'Apple'),
#             ('http://orange.com/', 'Orange'),
#         ),
#         'Fruits'
#     )
#
# WARNING: Support for submenus is theme-dependent.
#          Only one level of submenus is supported.
# WARNING: Some themes, including the default Bootstrap 3 theme,
#          may present issues if the menu is too large.
#          (in bootstrap3, the navbar can grow too large and cover contents.)
# WARNING: If you link to directories, make sure to follow
#          ``STRIP_INDEXES``.  If it’s set to ``True``, end your links
#          with a ``/``, otherwise end them with ``/index.html`` — or
#          else they won’t be highlighted when active.

NAVIGATION_LINKS = {
    DEFAULT_LANG: (
        ("/stories/la-biblioteca-de-los-navalmorales.html", "La Biblioteca"),
        ("/stories/la-biblioteca-de-los-navalmorales/contacto.html", "Contacto"),
         ((("http://reddebibliotecas.jccm.es/portal/", "Catálogo JCCM"),
          ("http://www.losnavalmorales.com/mesa/", "Revista Forja")), 'Enlaces'),
        ("/categories/index.html", "Categorías"),
        ("/rss.xml", "RSS"),
    ),
}


# Name of the theme to use.
THEME = "bootblog4"

# Below this point, everything is optional

# Post's dates are considered in UTC by default, if you want to use
# another time zone, please set TIMEZONE to match. Check the available
# list from Wikipedia:
# http://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# (e.g. 'Europe/Zurich')
# Also, if you want to use a different time zone in some of your posts,
# you can use the ISO 8601/RFC 3339 format (ex. 2012-03-30T23:00:00+02:00)
TIMEZONE = 'Europe/Madrid'

# If you want to use ISO 8601 (also valid RFC 3339) throughout Nikola
# (especially in new_post), set this to True.
# Note that this does not affect DATE_FORMAT.
# FORCE_ISO8601 = False

# Date format used to display post dates.
# (str used by datetime.datetime.strftime)
DATE_FORMAT = '%d-%m-%Y'

# Date format used to display post dates, if local dates are used.
# (str used by moment.js)
JS_DATE_FORMAT = 'DD-MM-YYYY'

# Date fanciness.
#
# 0 = using DATE_FORMAT and TIMEZONE
# 1 = using JS_DATE_FORMAT and local user time (via moment.js)
# 2 = using a string like “2 days ago”
#
# Your theme must support it, bootstrap and bootstrap3 already do.
# DATE_FANCINESS = 0

# While Nikola can select a sensible locale for each language,
# sometimes explicit control can come handy.
# In this file we express locales in the string form that
# python's locales will accept in your OS, by example
# "en_US.utf8" in Unix-like OS, "English_United States" in Windows.
# LOCALES = dict mapping language --> explicit locale for the languages
# in TRANSLATIONS. You can omit one or more keys.
# LOCALE_FALLBACK = locale to use when an explicit locale is unavailable
# LOCALE_DEFAULT = locale to use for languages not mentioned in LOCALES; if
# not set the default Nikola mapping is used.

# POSTS and PAGES contains (wildcard, destination, template) tuples.
#
# The wildcard is used to generate a list of reSt source files
# (whatever/thing.txt).
#
# That fragment could have an associated metadata file (whatever/thing.meta),
# and optionally translated files (example for Spanish, with code "es"):
#     whatever/thing.es.txt and whatever/thing.es.meta
#
#     This assumes you use the default TRANSLATIONS_PATTERN.
#
# From those files, a set of HTML fragment files will be generated:
# cache/whatever/thing.html (and maybe cache/whatever/thing.html.es)
#
# These files are combined with the template to produce rendered
# pages, which will be placed at
# output / TRANSLATIONS[lang] / destination / pagename.html
#
# where "pagename" is the "slug" specified in the metadata file.
#
# The difference between POSTS and PAGES is that POSTS are added
# to feeds and are considered part of a blog, while PAGES are
# just independent HTML pages.
#

POSTS = (
            ("posts/*.rst", "posts", "post.tmpl"),
            ("posts/*.txt", "posts", "post.tmpl"),
            ("posts/*.md", "posts", "post.tmpl"),
            ("posts/*.wp", "posts", "post.tmpl"),
        )
PAGES = (
            ("stories/*.rst", "stories", "story.tmpl"),
            ("stories/*.txt", "stories", "story.tmpl"),
            ("stories/*.md", "stories", "story.tmpl"),
            ("stories/*.wp", "stories", "story.tmpl"),
        )

# One or more folders containing files to be copied as-is into the output.
# The format is a dictionary of {source: relative destination}.
# Default is:
# FILES_FOLDERS = {'files': ''}
# Which means copy 'files' into 'output'

# One or more folders containing listings to be processed and stored into
# the output. The format is a dictionary of {source: relative destination}.
# Default is:
# LISTINGS_FOLDERS = {'listings': 'listings'}
# Which means process listings from 'listings' into 'output/listings'

# A mapping of languages to file-extensions that represent that language.
# Feel free to add or delete extensions to any list, but don't add any new
# compilers unless you write the interface for it yourself.
#
# 'rest' is reStructuredText
# 'markdown' is MarkDown
# 'html' assumes the file is HTML and just copies it
COMPILERS = {
        "rest": ('.txt', '.rst'),
        "markdown": ('.md', '.mdown', '.markdown', '.wp'),
        "html": ('.html', '.htm')
        }


# Create by default posts in one file format?
# Set to False for two-file posts, with separate metadata.
# ONE_FILE_POSTS = True

# If this is set to True, the DEFAULT_LANG version will be displayed for
# untranslated posts.
# If this is set to False, then posts that are not translated to a language
# LANG will not be visible at all in the pages in that language.
# Formerly known as HIDE_UNTRANSLATED_POSTS (inverse)
# SHOW_UNTRANSLATED_POSTS = True

# Nikola supports logo display.  If you have one, you can put the URL here.
# Final output is <img src="LOGO_URL" id="logo" alt="BLOG_TITLE">.
# The URL may be relative to the site root.
# LOGO_URL = 'logo.png'

# If you want to hide the title of your website (for example, if your logo
# already contains the text), set this to False.
# SHOW_BLOG_TITLE = True

# Writes tag cloud data in form of tag_cloud_data.json.
# Warning: this option will change its default value to False in v8!
WRITE_TAG_CLOUD = True

# Paths for different autogenerated bits. These are combined with the
# translation paths.

# Final locations are:
# output / TRANSLATION[lang] / TAG_PATH / index.html (list of tags)
# output / TRANSLATION[lang] / TAG_PATH / tag.html (list of posts for a tag)
# output / TRANSLATION[lang] / TAG_PATH / tag.xml (RSS feed for a tag)
# TAG_PATH = "categories"

# If TAG_PAGES_ARE_INDEXES is set to True, each tag's page will contain
# the posts themselves. If set to False, it will be just a list of links.
# TAG_PAGES_ARE_INDEXES = False

# Set descriptions for tag pages to make them more interesting. The
# default is no description. The value is used in the meta description
# and displayed underneath the tag list or index page’s title.
#TAG_PAGES_DESCRIPTIONS = {
#    DEFAULT_LANG: {
#        "blogging": "Meta-blog posts about blogging about blogging.",
#        "open source": "My contributions to my many, varied, ever-changing, and eternal libre software projects."
#    },
#}

# Only include tags on the tag list/overview page if there are at least
# TAGLIST_MINIMUM_POSTS number of posts or more with every tag. Every tag
# page is still generated, linked from posts, and included in the sitemap.
# However, more obscure tags can be hidden from the tag index page.
# TAGLIST_MINIMUM_POSTS = 1

# Final locations are:
# output / TRANSLATION[lang] / CATEGORY_PATH / index.html (list of categories)
# output / TRANSLATION[lang] / CATEGORY_PATH / CATEGORY_PREFIX category.html (list of posts for a category)
# output / TRANSLATION[lang] / CATEGORY_PATH / CATEGORY_PREFIX category.xml (RSS feed for a category)
# CATEGORY_PATH = "categories"
# CATEGORY_PREFIX = "cat_"

# If CATEGORY_PAGES_ARE_INDEXES is set to True, each category's page will contain
# the posts themselves. If set to False, it will be just a list of links.
# CATEGORY_PAGES_ARE_INDEXES = False

# Set descriptions for category pages to make them more interesting. The
# default is no description. The value is used in the meta description
# and displayed underneath the category list or index page’s title.
# CATEGORY_PAGES_DESCRIPTIONS = {
#    DEFAULT_LANG: {
#        "blogging": "Meta-blog posts about blogging about blogging.",
#        "open source": "My contributions to my many, varied, ever-changing, and eternal libre software projects."
#    },
#}

# Final location for the main blog page and sibling paginated pages is
# output / TRANSLATION[lang] / INDEX_PATH / index-*.html
# INDEX_PATH = ""

# Create per-month archives instead of per-year
# CREATE_MONTHLY_ARCHIVE = False
# Create one large archive instead of per-year
# CREATE_SINGLE_ARCHIVE = False
# Create year, month, and day archives each with a (long) list of posts
# (overrides both CREATE_MONTHLY_ARCHIVE and CREATE_SINGLE_ARCHIVE)
# CREATE_FULL_ARCHIVES = False
# If monthly archives or full archives are created, adds also one archive per day
# CREATE_DAILY_ARCHIVE = False
# Final locations for the archives are:
# output / TRANSLATION[lang] / ARCHIVE_PATH / ARCHIVE_FILENAME
# output / TRANSLATION[lang] / ARCHIVE_PATH / YEAR / index.html
# output / TRANSLATION[lang] / ARCHIVE_PATH / YEAR / MONTH / index.html
# output / TRANSLATION[lang] / ARCHIVE_PATH / YEAR / MONTH / DAY / index.html
# ARCHIVE_PATH = ""
# ARCHIVE_FILENAME = "archive.html"

# If ARCHIVES_ARE_INDEXES is set to True, each archive page which contains a list
# of posts will contain the posts themselves. If set to False, it will be just a
# list of links.
# ARCHIVES_ARE_INDEXES = False

# URLs to other posts/pages can take 3 forms:
# rel_path: a relative URL to the current page/post (default)
# full_path: a URL with the full path from the root
# absolute: a complete URL (that includes the SITE_URL)
# URL_TYPE = 'rel_path'

# Final location for the blog main RSS feed is:
# output / TRANSLATION[lang] / RSS_PATH / rss.xml
# RSS_PATH = ""

# Number of posts in RSS feeds
# FEED_LENGTH = 10

# Slug the Tag URL easier for users to type, special characters are
# often removed or replaced as well.
# SLUG_TAG_PATH = True

# A list of redirection tuples, [("foo/from.html", "/bar/to.html")].
#
# A HTML file will be created in output/foo/from.html that redirects
# to the "/bar/to.html" URL. notice that the "from" side MUST be a
# relative URL.
#
# If you don't need any of these, just set to []
REDIRECTIONS = [["2014/04/dia-del-libro-2014/index.html", "/posts/2014/04/dia-del-libro-2014.html"], ["2014/12/taller-de-navidad/index.html", "/posts/2014/12/taller-de-navidad.html"], ["2013/01/novedades-para-ninos-a-partir-de-10-anos/index.html", "/posts/2013/01/novedades-para-ninos-a-partir-de-10-anos.html"], ["2014/05/cuentacuentos/index.html", "/posts/2014/05/cuentacuentos.html"], ["2014/04/viaje-a-toledo-exposicion-el-greco-2014/index.html", "/posts/2014/04/viaje-a-toledo-exposicion-el-greco-2014.html"], ["2012/06/tormenta-de-espadas-cancion-de-hielo-y-fuego-3-de-george-r-r-martin/index.html", "/posts/2012/06/tormenta-de-espadas-cancion-de-hielo-y-fuego-3-de-george-r-r-martin.html"], ["2015/05/celebracion-dia-del-libro-2015-en-la-biblioteca/index.html", "/posts/2015/05/celebracion-dia-del-libro-2015-en-la-biblioteca.html"], ["2012/02/12-razones-para-amar-las-bibliotecas-publicas/index.html", "/posts/2012/02/12-razones-para-amar-las-bibliotecas-publicas.html"], ["2013/01/novedades-para-adultos-2/index.html", "/posts/2013/01/novedades-para-adultos-2.html"], ["2014/02/presentacion-del-libro-el-amuleto-de-abraxas-del-autor-guillermo-de-los-mozos-alventosa/index.html", "/posts/2014/02/presentacion-del-libro-el-amuleto-de-abraxas-del-autor-guillermo-de-los-mozos-alventosa.html"], ["2014/04/tarde-de-poesia-con-mo-antonia-ricas-peces/index.html", "/posts/2014/04/tarde-de-poesia-con-mo-antonia-ricas-peces.html"], ["2014/11/taller-de-comprension-lectora-5-noviembre/index.html", "/posts/2014/11/taller-de-comprension-lectora-5-noviembre.html"], ["2015/04/cuentacuentos-pep-bruno/index.html", "/posts/2015/04/cuentacuentos-pep-bruno.html"], ["2013/12/los-viernes-talleres-de-navidad/index.html", "/posts/2013/12/los-viernes-talleres-de-navidad.html"], ["la-biblioteca-de-los-navalmorales/contacta-con-nosotros/index.html", "/stories/la-biblioteca-de-los-navalmorales/contacta-con-nosotros.html"], ["2015/03/cronica-de-la-presentacion-de-esencias/index.html", "/posts/2015/03/cronica-de-la-presentacion-de-esencias.html"], ["2015/06/cronica-de-la-conferencia-de-maria-victoria-navas-sanchez-elez/index.html", "/posts/2015/06/cronica-de-la-conferencia-de-maria-victoria-navas-sanchez-elez.html"], ["2013/06/xv-encuentro-provincial-de-clubes-de-lectura-los-yebenes-2013/index.html", "/posts/2013/06/xv-encuentro-provincial-de-clubes-de-lectura-los-yebenes-2013.html"], ["2012/10/cuentos-para-disfrutar-y-jugar/index.html", "/posts/2012/10/cuentos-para-disfrutar-y-jugar.html"], ["2012/02/dibujos-de-la-hora-del-cuento/index.html", "/posts/2012/02/dibujos-de-la-hora-del-cuento.html"], ["2011/07/comenzamos-a-andar/index.html", "/posts/2011/07/comenzamos-a-andar.html"], ["2013/08/centro-de-interes-durante-el-mes-de-agosto/index.html", "/posts/2013/08/centro-de-interes-durante-el-mes-de-agosto.html"], ["2012/03/libros-leidos-en-la-hora-del-cuento-2012/index.html", "/posts/2012/03/libros-leidos-en-la-hora-del-cuento-2012.html"], ["2013/12/novedades-diciembre-2013/index.html", "/posts/2013/12/novedades-diciembre-2013.html"], ["2011/08/xiii-encuentro-de-clubes-de-lectura-de-toledo/index.html", "/posts/2011/08/xiii-encuentro-de-clubes-de-lectura-de-toledo.html"], ["2014/06/taller-de-comprension-lectora/index.html", "/posts/2014/06/taller-de-comprension-lectora.html"], ["2012/11/las-tardes-de-los-viernes-en-la-biblioteca/index.html", "/posts/2012/11/las-tardes-de-los-viernes-en-la-biblioteca.html"], ["2013/07/novedades-julio-2013/index.html", "/posts/2013/07/novedades-julio-2013.html"], ["2012/01/vuelta-de-vacaciones-de-navidad/index.html", "/posts/2012/01/vuelta-de-vacaciones-de-navidad.html"], ["2015/01/conferencia-impartida-por-ma-soledad-campillo/index.html", "/posts/2015/01/conferencia-impartida-por-ma-soledad-campillo.html"], ["2012/04/359/index.html", "/stories/2012/04/359.html"], ["2013/02/unas-fotografias-del-encuentro-con-la-escritora-consolacion-gonzalez-rico/index.html", "/posts/2013/02/unas-fotografias-del-encuentro-con-la-escritora-consolacion-gonzalez-rico.html"], ["2015/05/taller-de-comprension-lectora-los-10-fantasticos/index.html", "/posts/2015/05/taller-de-comprension-lectora-los-10-fantasticos.html"], ["2014/12/por-navidad-algunas-novedades/index.html", "/posts/2014/12/por-navidad-algunas-novedades.html"], ["2012/12/ultimos-libros-recibidos/index.html", "/posts/2012/12/ultimos-libros-recibidos.html"], ["2013/02/encuentro-con-la-escritora-consolacion-gonzalez-rico/index.html", "/posts/2013/02/encuentro-con-la-escritora-consolacion-gonzalez-rico.html"], ["2011/11/217/index.html", "/posts/2011/11/217.html"], ["2012/11/los-abuelos-nos-cuentan-cuentos-2/index.html", "/posts/2012/11/los-abuelos-nos-cuentan-cuentos-2.html"], ["2011/11/233/index.html", "/stories/2011/11/233.html"], ["2012/01/comienza-la-hora-del-cuento-2012/index.html", "/posts/2012/01/comienza-la-hora-del-cuento-2012.html"], ["2011/09/prometeme-que-seras-libre-jorge-molist/index.html", "/posts/2011/09/prometeme-que-seras-libre-jorge-molist.html"], ["2015/01/1178/index.html", "/stories/2015/01/1178.html"], ["2013/11/hora-del-cuento-2013-2014/index.html", "/posts/2013/11/hora-del-cuento-2013-2014.html"], ["2014/10/ebiblio-prestamo-de-libros-electronicos/index.html", "/posts/2014/10/ebiblio-prestamo-de-libros-electronicos.html"], ["2013/01/fin-de-talleres-en-vacaciones/index.html", "/posts/2013/01/fin-de-talleres-en-vacaciones.html"], ["2011/08/memoria-del-taller-de-literatura-2010-2011/index.html", "/posts/2011/08/memoria-del-taller-de-literatura-2010-2011.html"], ["2013/03/todos-los-jueves-a-las-1630-en-la-biblioteca-tenemos-la-hora-del-cuento/index.html", "/posts/2013/03/todos-los-jueves-a-las-1630-en-la-biblioteca-tenemos-la-hora-del-cuento.html"], ["2012/01/el-puente-de-los-asesinos-arturo-perez-reverte/index.html", "/posts/2012/01/el-puente-de-los-asesinos-arturo-perez-reverte.html"], ["2013/06/horario-de-verano-2013/index.html", "/posts/2013/06/horario-de-verano-2013.html"], ["2012/09/novedades-libros-adultos-2/index.html", "/posts/2012/09/novedades-libros-adultos-2.html"], ["2015/04/teatro-en-la-biblioteca-con-el-grupo-adeltea/index.html", "/posts/2015/04/teatro-en-la-biblioteca-con-el-grupo-adeltea.html"], ["2014/12/el-taller-de-literatura-celebra-la-navidad/index.html", "/posts/2014/12/el-taller-de-literatura-celebra-la-navidad.html"], ["2015/06/conferencia-impartida-por-maria-victoria-navas-sanchez-elez/index.html", "/posts/2015/06/conferencia-impartida-por-maria-victoria-navas-sanchez-elez.html"], ["2011/11/biblioteca-cerrada-por-vacaciones/index.html", "/posts/2011/11/biblioteca-cerrada-por-vacaciones.html"], ["2015/03/presentacion-del-libro-esencias/index.html", "/posts/2015/03/presentacion-del-libro-esencias.html"], ["2011/10/inscripcion-al-taller-de-literatura-2011-2012/index.html", "/posts/2011/10/inscripcion-al-taller-de-literatura-2011-2012.html"], ["2015/02/conferencia-homenaje-a-antonio-machado-en-el-76-aniversario-de-su-muerte/index.html", "/posts/2015/02/conferencia-homenaje-a-antonio-machado-en-el-76-aniversario-de-su-muerte.html"], ["2013/03/tres-nuevos-libros-incorporados-al-catalogo-de-la-biblioteca/index.html", "/posts/2013/03/tres-nuevos-libros-incorporados-al-catalogo-de-la-biblioteca.html"], ["2013/04/actividades-del-dia-del-libro/index.html", "/posts/2013/04/actividades-del-dia-del-libro.html"], ["2014/07/xvi-encuentro-provincial-de-clubes-de-lectura/index.html", "/posts/2014/07/xvi-encuentro-provincial-de-clubes-de-lectura.html"], ["2014/10/hora-del-cuento-2014-2015/index.html", "/posts/2014/10/hora-del-cuento-2014-2015.html"], ["2013/11/club-de-lectura-infantil/index.html", "/posts/2013/11/club-de-lectura-infantil.html"], ["2012/06/mis-amigos-tigger-pooh-para-todo-el-ano/index.html", "/posts/2012/06/mis-amigos-tigger-pooh-para-todo-el-ano.html"], ["2011/12/cronica-y-agradecimiento-conferencia-de-jose-maria-bravo-profesor-de-enologia/index.html", "/posts/2011/12/cronica-y-agradecimiento-conferencia-de-jose-maria-bravo-profesor-de-enologia.html"], ["2014/07/hemos-comenzado-con-el-taller-de-comprension-lectora/index.html", "/posts/2014/07/hemos-comenzado-con-el-taller-de-comprension-lectora.html"], ["2015/02/club-de-lectura-juvenil/index.html", "/posts/2015/02/club-de-lectura-juvenil.html"], ["2012/06/410/index.html", "/posts/2012/06/410.html"], ["2014/02/taller-de-carnaval/index.html", "/posts/2014/02/taller-de-carnaval.html"], ["2013/09/club-de-lectura-infantil-verano-2013/index.html", "/posts/2013/09/club-de-lectura-infantil-verano-2013.html"], ["2015/04/novedades-literatura-infantil/index.html", "/posts/2015/04/novedades-literatura-infantil.html"], ["2012/03/libro-y-articulo-en-memoria-de-anabel-medez/index.html", "/posts/2012/03/libro-y-articulo-en-memoria-de-anabel-medez.html"], ["2015/01/retomamos-las-actividades-de-animacion-a-la-lectura/index.html", "/posts/2015/01/retomamos-las-actividades-de-animacion-a-la-lectura.html"], ["2015/04/dia-del-libro-2015/index.html", "/posts/2015/04/dia-del-libro-2015.html"], ["2012/02/encuentro-con-el-actor-paco-torres/index.html", "/posts/2012/02/encuentro-con-el-actor-paco-torres.html"], ["2012/06/visita-al-palacio-de-galiana/index.html", "/posts/2012/06/visita-al-palacio-de-galiana.html"], ["2012/04/encuentro-con-el-actor-y-autor-paco-torres/index.html", "/posts/2012/04/encuentro-con-el-actor-y-autor-paco-torres.html"], ["2012/06/el-imperio-eres-tu-de-javier-moro/index.html", "/posts/2012/06/el-imperio-eres-tu-de-javier-moro.html"], ["2013/11/novedades/index.html", "/posts/2013/11/novedades.html"], ["2013/04/agradecimientos-a-juan-ribera-llopis/index.html", "/posts/2013/04/agradecimientos-a-juan-ribera-llopis.html"], ["2013/01/visita-de-la-autora-consolacion-gonzalez-rico/index.html", "/posts/2013/01/visita-de-la-autora-consolacion-gonzalez-rico.html"], ["2014/07/taller-de-comprension-lectora-2/index.html", "/posts/2014/07/taller-de-comprension-lectora-2.html"], ["la-biblioteca-de-los-navalmorales/calendario-de-eventos/index.html", "/stories/la-biblioteca-de-los-navalmorales/calendario-de-eventos.html"], ["2011/11/al-llegar-el-invierno-de-rafael-canadilla-saldana/index.html", "/posts/2011/11/al-llegar-el-invierno-de-rafael-canadilla-saldana.html"], ["2013/11/los-viernes-talleres/index.html", "/posts/2013/11/los-viernes-talleres.html"], ["2011/11/la-casa-de-los-siete-pecados-mari-p-dominguez/index.html", "/posts/2011/11/la-casa-de-los-siete-pecados-mari-p-dominguez.html"], ["2013/12/conferencia-sobre-criminologia/index.html", "/posts/2013/12/conferencia-sobre-criminologia.html"], ["2015/06/cierre-por-vacaciones-16-26-jun-2015/index.html", "/posts/2015/06/cierre-por-vacaciones-16-26-jun-2015.html"], ["2011/09/hijos-de-un-rey-godo-maria-gudin/index.html", "/posts/2011/09/hijos-de-un-rey-godo-maria-gudin.html"], ["2011/07/dime-quien-soy-julia-navarro/index.html", "/posts/2011/07/dime-quien-soy-julia-navarro.html"], ["2012/11/horario-de-invierno/index.html", "/posts/2012/11/horario-de-invierno.html"], ["2013/11/taller-de-literatura-2013-2014/index.html", "/posts/2013/11/taller-de-literatura-2013-2014.html"], ["2012/03/visitas-de-alumnos-del-i-e-s-los-navalmorales/index.html", "/posts/2012/03/visitas-de-alumnos-del-i-e-s-los-navalmorales.html"], ["2015/05/certamen-relato-breve-marivi-fernandez-gonzalez/index.html", "/posts/2015/05/certamen-relato-breve-marivi-fernandez-gonzalez.html"], ["2012/10/nuevas-peliculas-para-ver-en-familia-este-otono/index.html", "/posts/2012/10/nuevas-peliculas-para-ver-en-familia-este-otono.html"], ["2011/12/conferencia-de-jose-maria-bravo-profesor-de-enologia/index.html", "/posts/2011/12/conferencia-de-jose-maria-bravo-profesor-de-enologia.html"], ["la-biblioteca-de-los-navalmorales/index.html", "/stories/la-biblioteca-de-los-navalmorales.html"], ["2012/01/el-lector-de-cadaveres-antonio-garrido/index.html", "/posts/2012/01/el-lector-de-cadaveres-antonio-garrido.html"], ["2011/07/44/index.html", "/stories/2011/07/44.html"], ["2012/09/memoria-del-taller-de-literatura-temporada-2011-2012/index.html", "/posts/2012/09/memoria-del-taller-de-literatura-temporada-2011-2012.html"], ["2015/05/club-de-lectura-jovenes-lectores/index.html", "/posts/2015/05/club-de-lectura-jovenes-lectores.html"], ["2012/09/cerramos-unos-dias-por-vacaciones/index.html", "/posts/2012/09/cerramos-unos-dias-por-vacaciones.html"], ["la-biblioteca-de-los-navalmorales/reglamento-de-la-biblioteca-publica-municipal-de-los-navalmorales/index.html", "/stories/la-biblioteca-de-los-navalmorales/reglamento-de-la-biblioteca-publica-municipal-de-los-navalmorales.html"], ["2012/06/cancion-de-hielo-y-fuego-1-juego-de-tronos-de-george-martin/index.html", "/posts/2012/06/cancion-de-hielo-y-fuego-1-juego-de-tronos-de-george-martin.html"], ["2012/06/conferencia-impartida-por-ma-victoria-navas-sanchez-elez/index.html", "/posts/2012/06/conferencia-impartida-por-ma-victoria-navas-sanchez-elez.html"], ["2015/06/xvii-encuentro-provincial-de-clubes-de-lectura/index.html", "/posts/2015/06/xvii-encuentro-provincial-de-clubes-de-lectura.html"], ["2011/10/informacion-de-la-biblioteca/index.html", "/posts/2011/10/informacion-de-la-biblioteca.html"], ["2014/04/el-cretense/index.html", "/posts/2014/04/el-cretense.html"], ["2014/08/nuevas-adquisiciones-2/index.html", "/posts/2014/08/nuevas-adquisiciones-2.html"], ["2013/03/dia-mundial-de-la-poesia/index.html", "/posts/2013/03/dia-mundial-de-la-poesia.html"], ["2012/10/novedades-para-adultos/index.html", "/posts/2012/10/novedades-para-adultos.html"], ["2014/11/novedades-2/index.html", "/posts/2014/11/novedades-2.html"], ["2012/09/novedades-infantil/index.html", "/posts/2012/09/novedades-infantil.html"], ["2012/06/el-enredo-de-la-bolsa-y-la-vida-eduardo-mendoza/index.html", "/posts/2012/06/el-enredo-de-la-bolsa-y-la-vida-eduardo-mendoza.html"], ["2013/09/nuevas-adquisiciones/index.html", "/posts/2013/09/nuevas-adquisiciones.html"], ["2013/04/conferencia-por-d-juan-ribera-llopis/index.html", "/posts/2013/04/conferencia-por-d-juan-ribera-llopis.html"], ["2015/01/1181/index.html", "/stories/2015/01/1181.html"], ["2015/04/novedades-literatura-adultos/index.html", "/posts/2015/04/novedades-literatura-adultos.html"], ["2014/09/taller-de-literatura-2014-2015/index.html", "/posts/2014/09/taller-de-literatura-2014-2015.html"], ["2015/02/antonio-machado-un-gran-poeta/index.html", "/posts/2015/02/antonio-machado-un-gran-poeta.html"], ["2011/09/la-tierra-de-las-cuevas-pintadas-jean-m-auel/index.html", "/posts/2011/09/la-tierra-de-las-cuevas-pintadas-jean-m-auel.html"], ["2014/12/los-viernes-talleres-2/index.html", "/posts/2014/12/los-viernes-talleres-2.html"], ["2014/03/proximas-actividades-en-el-taller-de-literatura/index.html", "/posts/2014/03/proximas-actividades-en-el-taller-de-literatura.html"], ["2014/11/bebeteca-2014/index.html", "/posts/2014/11/bebeteca-2014.html"], ["2012/12/novedades-infantil-2/index.html", "/posts/2012/12/novedades-infantil-2.html"], ["2011/11/perdona-si-te-llamo-amor-federico-moccia/index.html", "/posts/2011/11/perdona-si-te-llamo-amor-federico-moccia.html"], ["2015/01/1179/index.html", "/stories/2015/01/1179.html"], ["2013/10/en-la-biblioteca-en-este-curso-2013-2014-se-van-a-realizar-las-siguientes-actividades/index.html", "/posts/2013/10/en-la-biblioteca-en-este-curso-2013-2014-se-van-a-realizar-las-siguientes-actividades.html"], ["2011/11/las-huellas-imborrables-camilla-lackberg/index.html", "/posts/2011/11/las-huellas-imborrables-camilla-lackberg.html"], ["2013/05/23-de-abril-dia-del-libro-2013/index.html", "/posts/2013/05/23-de-abril-dia-del-libro-2013.html"], ["2013/10/horario-de-invierno-2/index.html", "/posts/2013/10/horario-de-invierno-2.html"], ["2014/03/conferencia-impartida-por-juan-jose-ortega-roman/index.html", "/posts/2014/03/conferencia-impartida-por-juan-jose-ortega-roman.html"], ["2013/01/articulo-de-consolacion-gonzalez-rico/index.html", "/posts/2013/01/articulo-de-consolacion-gonzalez-rico.html"], ["2011/11/yo-el-rey-de-juan-antonio-vallejo-nagera/index.html", "/posts/2011/11/yo-el-rey-de-juan-antonio-vallejo-nagera.html"]]

# Presets of commands to execute to deploy. Can be anything, for
# example, you may use rsync:
# "rsync -rav --delete output/ joe@my.site:/srv/www/site"
# And then do a backup, or run `nikola ping` from the `ping`
# plugin (`nikola plugin -i ping`).  Or run `nikola check -l`.
# You may also want to use github_deploy (see below).
# You can define multiple presets and specify them as arguments
# to `nikola deploy`.  If no arguments are specified, a preset
# named `default` will be executed.  You can use as many presets
# in a `nikola deploy` command as you like.
# DEPLOY_COMMANDS = {
#     'default': [
#         "rsync -rav --delete output/ joe@my.site:/srv/www/site",
#     ]
# }

# For user.github.io OR organization.github.io pages, the DEPLOY branch
# MUST be 'master', and 'gh-pages' for other repositories.
# GITHUB_SOURCE_BRANCH = 'master'
# GITHUB_DEPLOY_BRANCH = 'gh-pages'

# The name of the remote where you wish to push to, using github_deploy.
# GITHUB_REMOTE_NAME = 'origin'

# Where the output site should be located
# If you don't use an absolute path, it will be considered as relative
# to the location of conf.py
# OUTPUT_FOLDER = 'output'

# where the "cache" of partial generated content should be located
# default: 'cache'
# CACHE_FOLDER = 'cache'

# Filters to apply to the output.
# A directory where the keys are either: a file extensions, or
# a tuple of file extensions.
#
# And the value is a list of commands to be applied in order.
#
# Each command must be either:
#
# A string containing a '%s' which will
# be replaced with a filename. The command *must* produce output
# in place.
#
# Or:
#
# A python callable, which will be called with the filename as
# argument.
#
# By default, only .php files uses filters to inject PHP into
# Nikola’s templates. All other filters must be enabled through FILTERS.
#
# Many filters are shipped with Nikola. A list is available in the manual:
# <http://getnikola.com/handbook.html#post-processing-filters>
#
# from nikola import filters
# FILTERS = {
#    ".html": [filters.typogrify],
#    ".js": [filters.closure_compiler],
#    ".jpg": ["jpegoptim --strip-all -m75 -v %s"],
# }

# Expert setting! Create a gzipped copy of each generated file. Cheap server-
# side optimization for very high traffic sites or low memory servers.
# GZIP_FILES = False
# File extensions that will be compressed
# GZIP_EXTENSIONS = ('.txt', '.htm', '.html', '.css', '.js', '.json', '.xml')
# Use an external gzip command? None means no.
# Example: GZIP_COMMAND = "pigz -k {filename}"
# GZIP_COMMAND = None
# Make sure the server does not return a "Accept-Ranges: bytes" header for
# files compressed by this option! OR make sure that a ranged request does not
# return partial content of another representation for these resources. Do not
# use this feature if you do not understand what this means.

# Compiler to process LESS files.
# LESS_COMPILER = 'lessc'

# A list of options to pass to the LESS compiler.
# Final command is: LESS_COMPILER LESS_OPTIONS file.less
# LESS_OPTIONS = []

# Compiler to process Sass files.
# SASS_COMPILER = 'sass'

# A list of options to pass to the Sass compiler.
# Final command is: SASS_COMPILER SASS_OPTIONS file.s(a|c)ss
# SASS_OPTIONS = []

# #############################################################################
# Image Gallery Options
# #############################################################################

# One or more folders containing galleries. The format is a dictionary of
# {"source": "relative_destination"}, where galleries are looked for in
# "source/" and the results will be located in
# "OUTPUT_PATH/relative_destination/gallery_name"
# Default is:
# GALLERY_FOLDERS = {"galleries": "galleries"}
# More gallery options:
# THUMBNAIL_SIZE = 180
# MAX_IMAGE_SIZE = 1280
USE_FILENAME_AS_TITLE = True
# EXTRA_IMAGE_EXTENSIONS = []
#
# If set to False, it will sort by filename instead. Defaults to True
# GALLERY_SORT_BY_DATE = True
#
# Folders containing images to be used in normal posts or
# pages. Images will be scaled down according to THUMBNAIL_SIZE and
# MAX_IMAGE_SIZE options, but will have to be referenced manually to
# be visible on the site. The format is a dictionary of {source:
# relative destination}.
#
# IMAGE_FOLDERS = {'images': ''}

# #############################################################################
# HTML fragments and diverse things that are used by the templates
# #############################################################################

# Data about post-per-page indexes.
# INDEXES_PAGES defaults to ' old posts, page %d' or ' page %d' (translated),
# depending on the value of INDEXES_PAGES_MAIN.
#
# (translatable) If the following is empty, defaults to BLOG_TITLE:
# INDEXES_TITLE = ""
#
# (translatable) If the following is empty, defaults to ' [old posts,] page %d' (see above):
# INDEXES_PAGES = ""
#
# If the following is True, INDEXES_PAGES is also displayed on the main (the
# newest) index page (index.html):
# INDEXES_PAGES_MAIN = False
#
# If the following is True, index-1.html has the oldest posts, index-2.html the
# second-oldest posts, etc., and index.html has the newest posts. This ensures
# that all posts on index-x.html will forever stay on that page, now matter how
# many new posts are added.
# If False, index-1.html has the second-newest posts, index-2.html the third-newest,
# and index-n.html the oldest posts. When this is active, old posts can be moved
# to other index pages when new posts are added.
# INDEXES_STATIC = True
#
# (translatable) If PRETTY_URLS is set to True, this setting will be used to create
# more pretty URLs for index pages, such as page/2/index.html instead of index-2.html.
# Valid values for this settings are:
#   * False,
#   * a list or tuple, specifying the path to be generated,
#   * a dictionary mapping languages to lists or tuples.
# Every list or tuple must consist of strings which are used to combine the path;
# for example:
#     ['page', '{number}', '{index_file}']
# The replacements
#     {number}     --> (logical) page number;
#     {old_number} --> the page number inserted into index-n.html before (zero for
#                      the main page);
#     {index_file} --> value of option INDEX_FILE
# are made.
# Note that in case INDEXES_PAGES_MAIN is set to True, a redirection will be created
# for the full URL with the page number of the main page to the normal (shorter) main
# page URL.
# INDEXES_PRETTY_PAGE_URL = False

# Color scheme to be used for code blocks. If your theme provides
# "assets/css/code.css" this is ignored.
# Can be any of autumn borland bw colorful default emacs friendly fruity manni
# monokai murphy native pastie perldoc rrt tango trac vim vs
# CODE_COLOR_SCHEME = 'default'

# If you use 'site-reveal' theme you can select several subthemes
# THEME_REVEAL_CONFIG_SUBTHEME = 'sky'
# You can also use: beige/serif/simple/night/default

# Again, if you use 'site-reveal' theme you can select several transitions
# between the slides
# THEME_REVEAL_CONFIG_TRANSITION = 'cube'
# You can also use: page/concave/linear/none/default

# FAVICONS contains (name, file, size) tuples.
# Used for create favicon link like this:
# <link rel="name" href="file" sizes="size"/>
# FAVICONS = {
#     ("icon", "/favicon.ico", "16x16"),
#     ("icon", "/icon_128x128.png", "128x128"),
# }

# Show only teasers in the index pages? Defaults to False.
# INDEX_TEASERS = False

# HTML fragments with the Read more... links.
# The following tags exist and are replaced for you:
# {link}                        A link to the full post page.
# {read_more}                   The string “Read more” in the current language.
# {reading_time}                An estimate of how long it will take to read the post.
# {remaining_reading_time}      An estimate of how long it will take to read the post, sans the teaser.
# {min_remaining_read}          The string “{remaining_reading_time} min remaining to read” in the current language.
# {paragraph_count}             The amount of paragraphs in the post.
# {remaining_paragraph_count}   The amount of paragraphs in the post, sans the teaser.
# {{                            A literal { (U+007B LEFT CURLY BRACKET)
# }}                            A literal } (U+007D RIGHT CURLY BRACKET)

# 'Read more...' for the index page, if INDEX_TEASERS is True (translatable)
INDEX_READ_MORE_LINK = '<p class="more"><a href="{link}">{read_more}…</a></p>'
# 'Read more...' for the RSS_FEED, if RSS_TEASERS is True (translatable)
FEED_READ_MORE_LINK = '<p><a href="{link}">{read_more}…</a> ({min_remaining_read})</p>'

# Append a URL query to the RSS_READ_MORE_LINK and the //rss/item/link in
# RSS feeds. Minimum example for Piwik "pk_campaign=rss" and Google Analytics
# "utm_source=rss&utm_medium=rss&utm_campaign=rss". Advanced option used for
# traffic source tracking.
FEED_LINKS_APPEND_QUERY = False

# A HTML fragment describing the license, for the sidebar.
# (translatable)
LICENSE = '<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />'
# I recommend using the Creative Commons' wizard:
# http://creativecommons.org/choose/
# LICENSE = """
# <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/2.5/ar/">
# <img alt="Creative Commons License BY-NC-SA"
# style="border-width:0; margin-bottom:12px;"
# src="http://i.creativecommons.org/l/by-nc-sa/2.5/ar/88x31.png"></a>"""

# A small copyright notice for the page footer (in HTML).
# (translatable)
CONTENT_FOOTER = 'Contents &copy; {date}         <a href="mailto:{email}">{author}</a> - Powered by         <a href="http://getnikola.com" rel="nofollow">Nikola</a>         {license}'

# Things that will be passed to CONTENT_FOOTER.format().  This is done
# for translatability, as dicts are not formattable.  Nikola will
# intelligently format the setting properly.
# The setting takes a dict. The keys are languages. The values are
# tuples of tuples of positional arguments and dicts of keyword arguments
# to format().  For example, {'en': (('Hello'), {'target': 'World'})}
# results in CONTENT_FOOTER['en'].format('Hello', target='World').
# WARNING: If you do not use multiple languages with CONTENT_FOOTER, this
#          still needs to be a dict of this format.  (it can be empty if you
#          do not need formatting)
# (translatable)
CONTENT_FOOTER_FORMATS = {
    DEFAULT_LANG: (
        (),
        {
            "email": BLOG_EMAIL,
            "author": BLOG_AUTHOR,
            "date": time.gmtime().tm_year,
            "license": LICENSE
        }
    )
}

# To use comments, you can choose between different third party comment
# systems.  The following comment systems are supported by Nikola:
#   disqus, facebook, googleplus, intensedebate, isso, livefyre, muut
# You can leave this option blank to disable comments.
COMMENT_SYSTEM = "facebook"
# And you also need to add your COMMENT_SYSTEM_ID which
# depends on what comment system you use. The default is
# "nikolademo" which is a test account for Disqus. More information
# is in the manual.
COMMENT_SYSTEM_ID = "biblioln"

# Enable annotations using annotateit.org?
# If set to False, you can still enable them for individual posts and pages
# setting the "annotations" metadata.
# If set to True, you can disable them for individual posts and pages using
# the "noannotations" metadata.
# ANNOTATIONS = False

# Create index.html for page (story) folders?
# WARNING: if a page would conflict with the index file (usually
#          caused by setting slug to `index`), the STORY_INDEX
#          will not be generated for that directory.
# STORY_INDEX = False
# Enable comments on story pages?
# COMMENTS_IN_STORIES = False
# Enable comments on picture gallery pages?
# COMMENTS_IN_GALLERIES = False

# What file should be used for directory indexes?
# Defaults to index.html
# Common other alternatives: default.html for IIS, index.php
# INDEX_FILE = "index.html"

# If a link ends in /index.html,  drop the index.html part.
# http://mysite/foo/bar/index.html => http://mysite/foo/bar/
# (Uses the INDEX_FILE setting, so if that is, say, default.html,
# it will instead /foo/default.html => /foo)
# (Note: This was briefly STRIP_INDEX_HTML in v 5.4.3 and 5.4.4)
# Default = False
# STRIP_INDEXES = False

# Should the sitemap list directories which only include other directories
# and no files.
# Default to True
# If this is False
# e.g. /2012 includes only /01, /02, /03, /04, ...: don't add it to the sitemap
# if /2012 includes any files (including index.html)... add it to the sitemap
# SITEMAP_INCLUDE_FILELESS_DIRS = True

# List of files relative to the server root (!) that will be asked to be excluded
# from indexing and other robotic spidering. * is supported. Will only be effective
# if SITE_URL points to server root. The list is used to exclude resources from
# /robots.txt and /sitemap.xml, and to inform search engines about /sitemapindex.xml.
# ROBOTS_EXCLUSIONS = ["/archive.html", "/category/*.html"]

# Instead of putting files in <slug>.html, put them in
# <slug>/index.html. Also enables STRIP_INDEXES
# This can be disabled on a per-page/post basis by adding
#    .. pretty_url: False
# to the metadata
# PRETTY_URLS = False

# If True, publish future dated posts right away instead of scheduling them.
# Defaults to False.
# FUTURE_IS_NOW = False

# If True, future dated posts are allowed in deployed output
# Only the individual posts are published/deployed; not in indexes/sitemap
# Generally, you want FUTURE_IS_NOW and DEPLOY_FUTURE to be the same value.
# DEPLOY_FUTURE = False
# If False, draft posts will not be deployed
# DEPLOY_DRAFTS = True

# Allows scheduling of posts using the rule specified here (new_post -s)
# Specify an iCal Recurrence Rule: http://www.kanzaki.com/docs/ical/rrule.html
# SCHEDULE_RULE = ''
# If True, use the scheduling rule to all posts by default
# SCHEDULE_ALL = False

# Do you want a add a Mathjax config file?
# MATHJAX_CONFIG = ""

# If you are using the compile-ipynb plugin, just add this one:
# MATHJAX_CONFIG = """
# <script type="text/x-mathjax-config">
# MathJax.Hub.Config({
#     tex2jax: {
#         inlineMath: [ ['$','$'], ["\\\(","\\\)"] ],
#         displayMath: [ ['$$','$$'], ["\\\[","\\\]"] ],
#         processEscapes: true
#     },
#     displayAlign: 'left', // Change this to 'center' to center equations.
#     "HTML-CSS": {
#         styles: {'.MathJax_Display': {"margin": 0}}
#     }
# });
# </script>
# """

# Do you want to customize the nbconversion of your IPython notebook?
# IPYNB_CONFIG = {}
# With the following example configuration you can use a custom jinja template
# called `toggle.tpl` which has to be located in your site/blog main folder:
# IPYNB_CONFIG = {'Exporter':{'template_file': 'toggle'}}

# What Markdown extensions to enable?
# You will also get gist, nikola and podcast because those are
# done in the code, hope you don't mind ;-)
# Note: most Nikola-specific extensions are done via the Nikola plugin system,
#       with the MarkdownExtension class and should not be added here.
# MARKDOWN_EXTENSIONS = ['fenced_code', 'codehilite']

# Extra options to pass to the pandoc comand.
# by default, it's empty, is a list of strings, for example
# ['-F', 'pandoc-citeproc', '--bibliography=/Users/foo/references.bib']
# PANDOC_OPTIONS = []

# Social buttons. This is sample code for AddThis (which was the default for a
# long time). Insert anything you want here, or even make it empty.
# (translatable)
# SOCIAL_BUTTONS_CODE = """
# <!-- Social buttons -->
# <div id="addthisbox" class="addthis_toolbox addthis_peekaboo_style addthis_default_style addthis_label_style addthis_32x32_style">
# <a class="addthis_button_more">Share</a>
# <ul><li><a class="addthis_button_facebook"></a>
# <li><a class="addthis_button_google_plusone_share"></a>
# <li><a class="addthis_button_linkedin"></a>
# <li><a class="addthis_button_twitter"></a>
# </ul>
# </div>
# <script src="//s7.addthis.com/js/300/addthis_widget.js#pubid=ra-4f7088a56bb93798"></script>
# <!-- End of social buttons -->
# """
SOCIAL_BUTTONS_CODE = """<!-- Go to www.addthis.com/dashboard to customize your tools -->
<script type="text/javascript" src="//s7.addthis.com/js/300/addthis_widget.js#pubid=ra-4ec7029a5c9222a6" async="async"></script>
"""

# Show link to source for the posts?
# Formerly known as HIDE_SOURCELINK (inverse)
# SHOW_SOURCELINK = True
# Copy the source files for your pages?
# Setting it to False implies SHOW_SOURCELINK = False
# COPY_SOURCES = True

# Modify the number of Post per Index Page
# Defaults to 10
# INDEX_DISPLAY_POST_COUNT = 10

# By default, Nikola generates RSS files for the website and for tags, and
# links to it.  Set this to False to disable everything RSS-related.
# GENERATE_RSS = True

# RSS_LINK is a HTML fragment to link the RSS or Atom feeds. If set to None,
# the base.tmpl will use the feed Nikola generates. However, you may want to
# change it for a FeedBurner feed or something else.
# RSS_LINK = None

# Show only teasers in the RSS feed? Default to True
# RSS_TEASERS = True

# Strip HTML in the RSS feed? Default to False
# RSS_PLAIN = False

# A search form to search this site, for the sidebar. You can use a Google
# custom search (http://www.google.com/cse/)
# Or a DuckDuckGo search: https://duckduckgo.com/search_box.html
# Default is no search form.
# (translatable)
# SEARCH_FORM = ""
#
# This search form works for any site and looks good in the "site" theme where
# it appears on the navigation bar:
#
# SEARCH_FORM = """
# <!-- Custom search -->
# <form method="get" id="search" action="//duckduckgo.com/"
#  class="navbar-form pull-left">
# <input type="hidden" name="sites" value="%s"/>
# <input type="hidden" name="k8" value="#444444"/>
# <input type="hidden" name="k9" value="#D51920"/>
# <input type="hidden" name="kt" value="h"/>
# <input type="text" name="q" maxlength="255"
#  placeholder="Search&hellip;" class="span2" style="margin-top: 4px;"/>
# <input type="submit" value="DuckDuckGo Search" style="visibility: hidden;" />
# </form>
# <!-- End of custom search -->
# """ % SITE_URL
#
# If you prefer a Google search form, here's an example that should just work:
SEARCH_FORM = """
<form method="get" action="http://www.google.com/search" class="navbar-form navbar-right" role="search">
<div class="form-group">
<input type="text" name="q" class="form-control" placeholder="Search"/>
</div>
<input type="hidden" name="sitesearch" value="%s"/>
</form>
""" % SITE_URL

# Use content distribution networks for jQuery, twitter-bootstrap css and js,
# and html5shiv (for older versions of Internet Explorer)
# If this is True, jQuery and html5shiv are served from the Google CDN and
# Bootstrap is served from BootstrapCDN (provided by MaxCDN)
# Set this to False if you want to host your site without requiring access to
# external resources.
USE_CDN = False

# Check for USE_CDN compatibility.
# If you are using custom themes, have configured the CSS properly and are
# receiving warnings about incompatibility but believe they are incorrect, you
# can set this to False.
# USE_CDN_WARNING = True

# Extra things you want in the pages HEAD tag. This will be added right
# before </head>
# (translatable)
# EXTRA_HEAD_DATA = ""
# Google Analytics or whatever else you use. Added to the bottom of <body>
# in the default template (base.tmpl).
# (translatable)

# The possibility to extract metadata from the filename by using a
# regular expression.
# To make it work you need to name parts of your regular expression.
# The following names will be used to extract metadata:
# - title
# - slug
# - date
# - tags
# - link
# - description
#
# An example re is the following:
# '(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.*)-(?P<title>.*)\.md'
# FILE_METADATA_REGEXP = None

BODY_END = """<!-- Start of StatCounter Code for Default Guide -->
<script type="text/javascript">
var sc_project=7089865;
var sc_invisible=1;
var sc_security="c6347cb2";
var scJsHost = (("https:" == document.location.protocol) ?
"https://secure." : "http://www.");
document.write("<sc"+"ript type='text/javascript' src='" +
scJsHost+
"statcounter.com/counter/counter.js'></"+"script>");
</script>
<noscript><div class="statcounter"><a title="shopify site
analytics" href="http://statcounter.com/shopify/"
target="_blank"><img class="statcounter"
src="http://c.statcounter.com/7089865/0/c6347cb2/1/"
alt="shopify site analytics"></a></div></noscript>
<!-- End of StatCounter Code for Default Guide -->"""

# If you hate "Filenames with Capital Letters and Spaces.md", you should
# set this to true.
FILE_METADATA_UNSLUGIFY_TITLES = True

# Additional metadata that is added to a post when creating a new_post
# ADDITIONAL_METADATA = {}

# Nikola supports Open Graph Protocol data for enhancing link sharing and
# discoverability of your site on Facebook, Google+, and other services.
# Open Graph is enabled by default.
# USE_OPEN_GRAPH = True

# Nikola supports Twitter Card summaries, but they are disabled by default.
# They make it possible for you to attach media to Tweets that link
# to your content.
#
# IMPORTANT:
# Please note, that you need to opt-in for using Twitter Cards!
# To do this please visit https://cards-dev.twitter.com/validator
#
# Uncomment and modify to following lines to match your accounts.
# Images displayed come from the `previewimage` meta tag.
# You can specify the card type by using the `card` parameter in TWITTER_CARD.
TWITTER_CARD = {
	'use_twitter_cards': True,  # enable Twitter Cards
	'card': 'Biblioteca Municipal de Los Navalmorales',          # Card type, you can also use 'summary_large_image',
	'site': '@biblioln',         # twitter nick for the website
	'creator': '@biblioln',     # Username for the content creator / author.
}

# If webassets is installed, bundle JS and CSS to make site loading faster
# USE_BUNDLES = True

# Plugins you don't want to use. Be careful :-)
# DISABLED_PLUGINS = ["render_galleries"]

# Add the absolute paths to directories containing plugins to use them.
# For example, the `plugins` directory of your clone of the Nikola plugins
# repository.
# EXTRA_PLUGINS_DIRS = []

# List of regular expressions, links matching them will always be considered
# valid by "nikola check -l"
# LINK_CHECK_WHITELIST = []

# If set to True, enable optional hyphenation in your posts (requires pyphen)
# HYPHENATE = False

# The <hN> tags in HTML generated by certain compilers (reST/Markdown)
# will be demoted by that much (1 → h1 will become h2 and so on)
# This was a hidden feature of the Markdown and reST compilers in the
# past.  Useful especially if your post titles are in <h1> tags too, for
# example.
# (defaults to 1.)
# DEMOTE_HEADERS = 1

# If you don’t like slugified file names ([a-z0-9] and a literal dash),
# and would prefer to use all the characters your file system allows.
# USE WITH CARE!  This is also not guaranteed to be perfect, and may
# sometimes crash Nikola, your web server, or eat your cat.
# USE_SLUGIFY = True

# You can configure the logging handlers installed as plugins or change the
# log level of the default stderr handler.
# WARNING: The stderr handler allows only the loglevels of 'INFO' and 'DEBUG'.
#          This is done for safety reasons, as blocking out anything other
#          than 'DEBUG' may hide important information and break the user
#          experience!

LOGGING_HANDLERS = {
    'stderr': {'loglevel': 'INFO', 'bubble': True},
    # 'smtp': {
    #     'from_addr': 'test-errors@example.com',
    #     'recipients': ('test@example.com'),
    #     'credentials':('testusername', 'password'),
    #     'server_addr': ('127.0.0.1', 25),
    #     'secure': (),
    #     'level': 'DEBUG',
    #     'bubble': True
    # }
}

# Templates will use those filters, along with the defaults.
# Consult your engine's documentation on filters if you need help defining
# those.
# TEMPLATE_FILTERS = {}

# Put in global_context things you want available on all your templates.
# It can be anything, data, functions, modules, etc.
GLOBAL_CONTEXT = {}

# Add functions here and they will be called with template
# GLOBAL_CONTEXT as parameter when the template is about to be
# rendered
GLOBAL_CONTEXT_FILLER = []
