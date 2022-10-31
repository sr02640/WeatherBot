### Some code copied from https://github.com/Rapptz/discord.py/ ###
# Libraries
import logging

# Formatter 
class _ColourFormatter(logging.Formatter):
    LEVEL_COLOURS = [
        (logging.DEBUG, '\x1b[40;1m'),
        (logging.INFO, '\x1b[34;1m'),
        (logging.WARNING, '\x1b[33;1m'),
        (logging.ERROR, '\x1b[31m'),
        (logging.CRITICAL, '\x1b[41m'),
    ]

    FORMATS = {
        level: logging.Formatter(
            f'\x1b[30;1m%(asctime)s\x1b[0m {colour}%(levelname)-8s\x1b[0m \x1b[35m%(name)s\x1b[0m %(message)s',
            '%Y-%m-%d %H:%M:%S',
        )
        for level, colour in LEVEL_COLOURS
    }

    def format(self, record):
        formatter = self.FORMATS.get(record.levelno)
        if formatter is None:
            formatter = self.FORMATS[logging.DEBUG]

        # Override the traceback to always print in red
        if record.exc_info:
            text = formatter.formatException(record.exc_info)
            record.exc_text = f'\x1b[31m{text}\x1b[0m'

        output = formatter.format(record)

        # Remove the cache layer
        record.exc_text = None
        return output

# LowLevel logger
initlogger = logging.getLogger("Init Level")
initlogger.setLevel(logging.INFO)
stream_handler = logging.StreamHandler()

# Formatter
dt_fmt = '%Y-%m-%d %H:%M:%S'
# Stream Format
if isinstance(stream_handler, logging.StreamHandler):
    formatter = _ColourFormatter()
else:
    formatter = logging.Formatter('[{asctime}] [{levelname:<8}] {name}: {message}', dt_fmt, style='{')
# Setting Handler
stream_handler.setFormatter(formatter)
initlogger.addHandler(stream_handler)