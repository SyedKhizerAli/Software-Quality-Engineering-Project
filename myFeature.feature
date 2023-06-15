Feature: Feature1
  Background: Login to the metabase
    Given Chrome Browser is Opened
    When open url http://localhost:3000/
    And enter email "fatima@gmail.com" and password "fatima@123" and click on login button

    Scenario Outline: Invite a Person

        When I click on settings icon
        And I go to admin settings
        And I click on people
        And I click on invite someone button
        And I enter first name "<firstName>"
        And I enter first last name "<lastName>"
        And I enter email "<email>"
        And I enter chose a group "<group>"
        And I click on create button
        Then the person with the name "<firstName>" is created
    Examples:
      | firstName | lastName | email | group |
      | fattii    | flfjkdj  | 122@gmail.com | Default |
      | fattii    | flfjkdj  |  | Default |