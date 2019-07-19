@backend
@user
@delete_user

Feature: Delete users

  Scenario: I can delete an user using a valid user_id
    Given I already have a new user
    And I have the related user id
    When I do a DELETE request to the user endpoint
    Then I successfully deleted the user

  Scenario: I cannot delete an user using an invalid user_id
    Given I have an user_id for an user that doesn't exist
    When I do a DELETE request to the user endpoint with that ID
    Then I receive an error that the user was not found
