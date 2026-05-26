from unittest.mock import patch, MagicMock

API_BASE_URL = "https://rickandmortyapi.com/api"

MOCK_CARTMAN_RESPONSE = {
    "id": 11,
    "name": "Eric Cartman",
    "age": 10,
    "sex": "Male",
    "hair_color": "Brown",
    "occupation": "Student",
    "grade": "4th Grade",
    "religion": "Roman Catholic",
    "voiced_by": "",
    "created_at": "2022-03-10T17:02:57.000000Z",
    "updated_at": "2022-03-10T17:02:57.000000Z",
    "url": "https://spapi.dev/api/characters/11",
    "family": "https://spapi.dev/api/families/2",
    "relatives": [
    {
      "url": "https://spapi.dev/api/characters/10",
      "relation": "Son"
    }
    ],
    "episodes": [
        "https://spapi.dev/api/episodes/1",
        "https://spapi.dev/api/episodes/2",
        "https://spapi.dev/api/episodes/3",
        "https://spapi.dev/api/episodes/4",
        "https://spapi.dev/api/episodes/5",
        "https://spapi.dev/api/episodes/6",
        "https://spapi.dev/api/episodes/7",
        "https://spapi.dev/api/episodes/8",
        "https://spapi.dev/api/episodes/9",
        "https://spapi.dev/api/episodes/10",
        "https://spapi.dev/api/episodes/11",
        "https://spapi.dev/api/episodes/12",
        "https://spapi.dev/api/episodes/13",
        "https://spapi.dev/api/episodes/15",
        "https://spapi.dev/api/episodes/16",
        "https://spapi.dev/api/episodes/17",
        "https://spapi.dev/api/episodes/18",
        "https://spapi.dev/api/episodes/19",
        "https://spapi.dev/api/episodes/20",
        "https://spapi.dev/api/episodes/21",
        "https://spapi.dev/api/episodes/22",
        "https://spapi.dev/api/episodes/23",
        "https://spapi.dev/api/episodes/24",
        "https://spapi.dev/api/episodes/25",
        "https://spapi.dev/api/episodes/26",
        "https://spapi.dev/api/episodes/27",
        "https://spapi.dev/api/episodes/28",
        "https://spapi.dev/api/episodes/29",
        "https://spapi.dev/api/episodes/30",
        "https://spapi.dev/api/episodes/31",
        "https://spapi.dev/api/episodes/32",
        "https://spapi.dev/api/episodes/33",
        "https://spapi.dev/api/episodes/34",
        "https://spapi.dev/api/episodes/35",
        "https://spapi.dev/api/episodes/36",
        "https://spapi.dev/api/episodes/37",
        "https://spapi.dev/api/episodes/38",
        "https://spapi.dev/api/episodes/41",
        "https://spapi.dev/api/episodes/42",
        "https://spapi.dev/api/episodes/43",
        "https://spapi.dev/api/episodes/44",
        "https://spapi.dev/api/episodes/45",
        "https://spapi.dev/api/episodes/46",
        "https://spapi.dev/api/episodes/47",
        "https://spapi.dev/api/episodes/48",
        "https://spapi.dev/api/episodes/49",
        "https://spapi.dev/api/episodes/50"
        ]
}

def mock_character_get(url, **kwargs):
    mock = MagicMock()
    if url == f"{API_BASE_URL}/characters/11":
        mock.status_code = 200
        mock.json.return_value = MOCK_CARTMAN_RESPONSE
    else:
        mock.status_code = 404
        mock.json.return_value = {"error": "Character not found"}
    return mock

def before_scenario(context, scenario):
    print(f"Starting scenario: {scenario.name}")

    if "regression" in scenario.tags:
        context.mock_get = patch("requests.get", side_effect=mock_character_get)
        context.mock_get.start()


def after_scenario(context, scenario):
    print( f"Finished scenario: " f"{scenario.name} - Status: {scenario.status}")

    if "regression" in scenario.tags:
        context.mock_get.stop()