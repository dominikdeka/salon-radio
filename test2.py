from mopidy import config, ext

__version__ = '0.3.0'

class Extension(ext.Extension):

    dist_name = 'Mopidy-Notifier'
    ext_name = 'notifier'
    version = __version__

    def setup(self, registry):
        from .test3 import NotifierFrontend
        registry.add('frontend', NotifierFrontend)