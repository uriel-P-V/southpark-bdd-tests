# southpark-bdd-tests

![CI](https://github.com/uriel-P-V/southpark-bdd-tests/actions/workflows/tests.yml/badge.svg)

A BDD-based test suite for the South Park API —
demonstrates deep contract validation with Behave and Gherkin,
testing nested JSON structures wrapped in a data envelope,
list size validation, and mock-based regression testing.

---

## Project Structure

```
southpark-bdd-tests/
├── .github/
│   └── workflows/
│       └── tests.yml              ← GitHub Actions CI
├── features/
│   ├── steps/
│   │   └── character_steps.py     ← All step definitions
│   ├── environment.py             ← Hooks and mock setup
│   └── character.feature          ← 6 deep BDD scenarios
└── requirements.txt
```

---

## Features

- **Data envelope validation** — response fields accessed via `response["data"]` wrapper
- **Deep contract validation** — validates basic fields, grade, episodes count and relatives
- **List size validation** — verifies episode appearances and family members from lists
- **Single mock** — one `patch("requests.get")` with URL discrimination
- **Tag-driven execution** — `@smoke` hits real API, `@regression` fully mocked
- **GitHub Actions CI** — smoke runs first, regression only if smoke passes

---

## BDD Scenarios

```gherkin
Feature: South Park API

  Background:
    Given the South Park API is available

  @smoke
  Scenario: Get Eric Cartman by ID
    When I request the character with ID 11
    Then the response status code should be 200

  @regression
  Scenario: Validate basic fields with table
    When I request the character with ID 11
    Then the basic fields should match:
      | fields     | values         |
      | id         | 11             |
      | name       | Eric Cartman   |
      | age        | 10             |
      | sex        | Male           |
      | hair_color | Brown          |
      | occupation | Student        |
      | grade      | 4th Grade      |
      | religion   | Roman Catholic |

  @regression
  Scenario: Validate that he appeared in more than 50 episodes
    When I request the character with ID 11
    Then the character should have appeared in more than 50 episodes

  @regression
  Scenario: Validate that he has at least one family member
    When I request the character with ID 11
    Then the character has more than one family member

  @regression
  Scenario: Invalid character
    When I request the character with ID 9999
    Then the response status code should be 404
```

---

## Mock Strategy

Single `patch("requests.get")` with URL discrimination —
returns Eric Cartman mock data for valid requests, 404 for anything else.
The 404 response returns HTML as the real API does — `.json()` is not called on error responses.

```python
def mock_character_get(url, **kwargs):
    mock = MagicMock()
    if url == f"{API_BASE_URL}/characters/11":
        mock.status_code = 200
        mock.json.return_value = MOCK_CARTMAN_RESPONSE
    else:
        mock.status_code = 404
        mock.text = "Not Found"
    return mock
```

---

## Setup

```bash
git clone https://github.com/uriel-P-V/southpark-bdd-tests.git
cd southpark-bdd-tests
pip install -r requirements.txt
behave
```

---

## Running Tests

```bash
# All scenarios
behave

# Smoke only — hits real South Park API
behave --tags=smoke

# Regression only — fully mocked, no internet required
behave --tags=regression
```

---

## CI/CD Pipeline

Two dependent jobs run on every push and pull request to `main`:

```
push / PR → smoke (1 scenario) → regression (5 scenarios)
```

If `smoke` fails, `regression` is skipped automatically.

---

## Tech Stack

- **Python 3.11+**
- **Behave** — BDD framework with Gherkin support
- **Requests** — HTTP client for API calls
- **unittest.mock** — patch, MagicMock, side_effect
- **GitHub Actions** — CI/CD pipeline

---

## Author

**Uriel Alejandro Pérez Valdovinos**  
[github.com/uriel-P-V](https://github.com/uriel-P-V) · [linkedin.com/in/uriel-pv](https://linkedin.com/in/uriel-pv)