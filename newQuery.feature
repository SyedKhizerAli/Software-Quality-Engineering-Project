Feature: Feature1
  Background: Login to the metabase
     Given Chrome Browser is opened
     When I open url http://localhost:3000/
     And I Enter email l201274@lhr.nu.edu.pk
     And I Enter password naima12345
     And I click Login Button
     Then I am logged in

    Scenario Outline: writing a new query
        Given Data section is visible
        When I click on browse data
        And I select the database "<databaseName>"
        And click on new button
        And I select new query
        And I enter the new query "<query>"
        And i click on run icon
        Then the query is executed
    Examples:
      | databaseName | name |
      | Sample Database   | select * from Orders where ID=2  |