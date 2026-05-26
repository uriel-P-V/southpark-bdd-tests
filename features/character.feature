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
        |fields           |values         |
        |id          |11             |
        |name        |Eric Cartman   |
        |age         |10             |
        |sex         |Male           |
        |hair_color  |Brown          |
        |occupation  |Student        |
        |grade       |4th Grade      |
        |religion    |Roman Catholic |
        
  @regression
  Scenario: Validate that you are a 4th Grade student
    When I request the character with ID 11
    Then the character is in the 4th Grade

  @regression
  Scenario: Validate that he appeared in more than 50 episodes
    When I request the character with ID 11
    Then the character should have appeared in more than 50 episodes

  @regression
  Scenario: Validate that you have at least one family member
    When I request the character with ID 11
    Then the character has more than one family member

  @regression
  Scenario: invalid character
    When I request the character with ID 9999
    Then the response status code should be 404



