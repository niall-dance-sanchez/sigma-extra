import logging

# filter


def show_only_debug(record):
    return record.levelname == "DEBUG"


logger = logging.getLogger(__name__)
logger.setLevel("DEBUG")

if __name__ == "__main__":
    # instantiate handlers:

    # send your logs to the console
    console_handler = logging.StreamHandler()
    console_handler.setLevel("DEBUG")
    console_handler.addFilter(show_only_debug)

    # writes logs to a file
    file_handler = logging.FileHandler("app2.log", mode="a", encoding="utf-8")
    file_handler.setLevel("WARNING")

    # add handlers to the logger:

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    # shows the location of where your logs will be written
    print(logger.handlers)

    formatter = logging.Formatter(
        "{asctime} - {levelname} - {message}",
        style="{",
        datefmt="%Y-%m-%d %H:%M",
    )

    # handler method to add formatting from formatter above
    console_handler.setFormatter(formatter)

    logger.warning("sdfalsd!")
