
from requests import get
from bs4 import BeautifulSoup
from bs4.element import Tag


def get_property_cards() -> list:

    url = "https://www.rightmove.co.uk/property-to-rent/find.html?searchLocation=Oxford%20Street%20Area%2C%20Central%20London&useLocationIdentifier=true&locationIdentifier=REGION%5E93904&radius=5.0&maxPrice=2000&maxBedrooms=2&propertyTypes=detached%2Csemi-detached%2Cterraced&_includeLetAgreed=on"

    res = get(url, timeout=5)

    soup = BeautifulSoup(res.text, features="html.parser")

    cards = soup.find_all("div", class_="propertyCard-details")

    return cards


def extract_details_from_cards(card: Tag) -> dict:
    """Gets property details from a RightMove property card."""
    return {
        "monthly_price": card.find("div", class_="PropertyPrice_price__VL65t").get_text(),
        "weekly_price": card.find("div", class_="PropertyPrice_secondaryPrice__p_nsZ").get_text(),
        "description": card.find("p", itemprop="description").get_text(),
        "bedrooms": card.find("span", class_="PropertyInformation_bedroomsCount___2b5R").get_text(),
        "bathrooms": card.find("div", class_="PropertyInformation_bathContainer__ut8VY").get_text()
    }


if __name__ == "__main__":

    cards = get_property_cards()

    for i in range(len(cards)):
        print(extract_details_from_cards(cards[i]))
