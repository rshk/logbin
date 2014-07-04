import logging
import io

from logbin import PackStreamHandler, replay_log


# ------------------------------------------------------------
# INITIALIZE STUFF
# ------------------------------------------------------------

stream = io.BytesIO()
handler = PackStreamHandler(stream)
logger = logging.getLogger('test')
handler.setLevel(logging.DEBUG)
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)

# ------------------------------------------------------------
# LOG
# ------------------------------------------------------------

logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
try:
    10 / 0
except:
    logger.exception("This is an exception message")


del logger, handler


# ------------------------------------------------------------
# REPLAY
# ------------------------------------------------------------

from nicelog.formatters import ColorLineFormatter
import sys

stream.seek(0)

logger = logging.getLogger('')
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(levelname)s %(msg)s")

handler = logging.StreamHandler(sys.stderr)
# handler.setFormatter(ColorLineFormatter())
handler.setFormatter(formatter)
handler.setLevel(logging.DEBUG)
logger.addHandler(handler)

replay_log(stream)
