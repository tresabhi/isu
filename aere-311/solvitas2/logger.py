import loguru
import sys

loguru.logger.remove()
loguru.logger.add(sys.stdout, format="{message}", colorize=True)

logger = loguru.logger.opt(colors=True)


def log(message):
    logger.info(message, end="asd")
