@reservation
@ui
@reservations_ui

Feature: Reservations Page

  Scenario: Get all Reservations
    Given I have at least 1 reservation
    When I navigate to the reservations page
    Then I can see a list of all reservations

  Scenario Outline: Edit and Delete reservation buttons are not clickable
    Given I have at least 1 reservation
    When I navigate to the reservations page
    Then  <buttons> are not clickable

    Examples:
       | buttons    |
       | edit_btn   |
       | delete_btn |

  Scenario: Create reservation form
    Given I have at least 1 reservation
    When I navigate to the reservations page
    And I click create button
    Then create reservation form appears
    And I click on cancel create

  Scenario: Delete reservation pop-up
    Given I have at least 1 reservation
    When I navigate to the reservations page
    And I click on the first reservation row
    And I click delete reservation button
    Then delete reservation appears
    And I click on cancel deleting

  Scenario: Edit reservation form
    Given I have at least 1 reservation
    When I navigate to the reservations page
    And I click on the first reservation row
    And I click edit reservation button
    Then edit reservation form appears
    And I click on cancel edit

  Scenario: Filter Reservations
    Given I have at least 1 reservation
    When I navigate to the reservations page
    And I search for a user first name match of Abel
    Then all the reservations displayed will have Abel in the name
