import logging

try:
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())



# FileModeWarnings go off per the default.
warnings.simplefilter('default', FileModeWarning, append=True)

# http://www.jianshu.com/p/feb86c06c4f4
