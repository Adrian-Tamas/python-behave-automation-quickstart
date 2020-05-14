@file
Feature: Read and write from files

  Scenario: Save to csv and read it back
    Given I get all books info
    When I save it to a csv
    And read the content back
    Then I can ensure all data was written correctly