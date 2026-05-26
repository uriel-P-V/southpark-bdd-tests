from behave import given, when, then
import requests

API_BASE_URL = "https://spapi.dev/api"


@given("the South Park API is available")
def step_given_api_available(context):
    response=requests.get(f"{API_BASE_URL}/characters/1")
    assert response.status_code == 200

@when("I request the character with ID {character_id:d}")
def step_request_character_ID(context, character_id):
    context.response=requests.get(f"{API_BASE_URL}/characters/{character_id}")

@then("the response status code should be {expected_status:d}")
def step_response_status_code(context, expected_status):
    assert context.response.status_code == expected_status

@then("the basic fields should match:")
def step_basic_fields_should_match(context):
    data = context.response.json().get("data", {})
    
    for row in context.table:
            field = row["fields"]
            expected = row["values"]
            actual_value = data.get(field)
            assert str(actual_value) == str(expected)


@then("the character is in the 4th Grade")
def step_character_grade(context):
    data=context.response.json()

    assert(data['data']["grade"] == "4th Grade")

@then("the character should have appeared in more than 50 episodes")
def step_character_episodes(context):
    data=context.response.json()

    assert len(data['data']["episodes"]) > 50

@then("the character has more than one family member")
def step_character_family_member(context):
    data=context.response.json()
    assert len(data['data']["relatives"]) >= 1



