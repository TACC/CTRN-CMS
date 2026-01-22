# CUSTOM SETTINGS VALUES.
# TACC WMA CMS SITE:
# *.CTRN-WEB.TACC.UTEXAS.EDU

########################
# DJANGO_CMS
########################

CMS_TEMPLATES = (
    ('standard.html', 'Standard'),
    ('fullwidth.html', 'Full Width'),
    ('content.html', 'Content Only'),
)

########################
# TACC: BRANDING
########################

from taccsite_cms._settings.branding import *

PORTAL_BRANDING = [ PORTAL_BRANDING_TACC, PORTAL_BRANDING_UTEXAS ]

########################
# LOGO & FAVICON
########################

PORTAL_LOGO = {
    "is_remote": True,
    "img_file_src": "https://cdn.jsdelivr.net/gh/wesleyboar/CTRN-CMS@refactor/identify-as-ctrn/assets/logo.svg",
    "img_class": "",
    "link_href": "/",
    "link_target": "_self",
    "img_alt_text": "CTRN Portal",
    "img_crossorigin": "anonymous",
}

PORTAL_FAVICON = {
    "img_file_src": "https://cdn.jsdelivr.net/gh/wesleyboar/CTRN-CMS@refactor/identify-as-ctrn/assets/favicon.svg",
    "is_remote": True
}

########################
# PORTAL
########################

PORTAL_IS_TACC_CORE_PORTAL = False
PORTAL_HAS_LOGIN = False
PORTAL_HAS_SEARCH = True

########################
# STYLES
########################

PORTAL_NAV_WIDTH = 'md'

PORTAL_STYLES = [
    {
        "is_remote": True,
        "path": "https://cdn.jsdelivr.net/gh/wesleyboar/CTRN-CMS@refactor/identify-as-ctrn/assets/cms.css",
    },
    # For white header
    {
        "is_remote": True,
        "path": "https://cdn.jsdelivr.net/gh/TACC/Core-Styles@v2.40.2/dist/core-styles.theme.has-dark-logo.css"
    }
]

# Only use integer numbers (not "v1", not "0.11.0")
TACC_CORE_STYLES_VERSION = 2

########################
# DJANGOCMS_BLOG
########################

BLOG_AUTO_SETUP = False # Set to False after setup (minimize overhead)
BLOG_AUTO_HOME_TITLE ='Home'
BLOG_AUTO_BLOG_TITLE = 'News'
BLOG_AUTO_APP_TITLE = 'News'
BLOG_AUTO_NAMESPACE = 'News'
BLOG_ENABLE_COMMENTS = False

########################
# DJANGOCMS_BLOG: TACC
########################

PORTAL_BLOG_SHOW_CATEGORIES = True
PORTAL_BLOG_SHOW_TAGS = False

########################
# SEARCH
########################

# To support Google search
PORTAL_SEARCH_PATH = '/search/'
PORTAL_SEARCH_QUERY_PARAM_NAME = 'q' # as Google expects
PORTAL_SEARCH_INDEX_IS_AUTOMATIC = False
# https://github.com/TACC/Core-CMS/pull/885
SEARCH_PAGE_AUTO_SETUP = True
GOOGLE_SEARCH_ENGINE_ID = '3490b7442a6244be3'
