@batch

Feature: Testing with batch files

  Scenario: I can run a batch file
    Given I have a batch file
    When I run it
    Then it executes
