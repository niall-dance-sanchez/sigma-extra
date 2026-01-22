"""Solution for the present wrapping puzzle."""


def get_surface_area(dimensions: list[int]) -> int:
    """Returns the surface area of a present."""
    # 2*l*w + 2*w*h + 2*h*l

    l, w, h = dimensions

    return 2*l*w + 2*w*h + 2*h*l


def extract_dimensions(present: str) -> list[int]:
    """Extracts dimensions from a present string."""
    pass


if __name__ == "__main__":
    pass
