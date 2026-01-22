import aiohttp
import asyncio


async def get_plant_data(session, url):
    """Fetches the plant data from the API with the url provided."""
    async with session.get(url) as response:
        if response.status == 200:
            content = await response.json()
            return content
        if response.status == 404:
            # No plant found, so return None
            return None
        if response.status == 500:
            return get_plant_data(url, session)


async def get_batch_plant_data(start: int, end: int) -> list[dict]:
    """"""

    urls = [
        f"https://sigma-labs-bot.herokuapp.com/api/plants/{i}" for i in range(start, end)]

    async with aiohttp.ClientSession() as session:
        tasks = [get_plant_data(session, url) for url in urls]
        responses = await asyncio.gather(*tasks)

    return responses


def extract_all_plant_data(batch_size: int = 10) -> list[list]:
    """"""

    plants_exist = True
    i = 0
    plant_data = []

    while plants_exist:
        start = batch_size*i + 1
        end = batch_size*(i+1) + 1

        plants = asyncio.run(get_batch_plant_data(start, end))

        if not any(plants):
            plants_exist = False
        else:
            plant_data.extend(plants)
            i += 1

    return plant_data


def filter_plant_data(plant_data: list[dict]) -> list[dict]:
    """Returns the plant data with any None values removed."""

    return [p for p in plant_data if p]


if __name__ == "__main__":
    plant_data = extract_all_plant_data()
