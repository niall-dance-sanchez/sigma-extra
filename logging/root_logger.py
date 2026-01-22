import logging

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logging.basicConfig(
        filename="app.log",
        encoding="utf-8",
        # append changes to the file instead of overwriting
        filemode="a",

        format="{asctime} - {levelname} - {message}",
        style="{",
        datefmt="%Y-%m-%d %H:%M",

        # will log at this level AND above
        # (level order below)
        level=logging.DEBUG)

    name = "Niall"

    logging.debug("name=%s", name)
    logging.debug("This is a debug message")

    logging.info("This is an info message")

    logging.warning("This is a warning message")

    logging.error("This is an error message")

    logging.critical("This is a critical message")

    # capturing stack traces
    donuts = 5
    guests = 0
    try:
        donuts_per_guest = donuts / guests
    except ZeroDivisionError:
        # logging.error("DonutCalculationError", exc_info=True)

        # same as above but can only be used in an exception handler
        logging.exception("DonutCalculationError")
