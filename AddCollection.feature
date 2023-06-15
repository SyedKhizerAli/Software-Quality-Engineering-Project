Feature: feature2
  Background: login
     Given Chrome Browser is opened
     When I open url http://localhost:3000/
     And I Enter email l201371@lhr.nu.edu.pk
     And I Enter password khizerali123
     And I click Login Button
     Then I am logged in

  Scenario Outline: Add Collection
     Given Collections section is visible
     When I Click menu button
     And I click new collection
     And I Enter name <name>
     And I Enter Description <description>
     And I Click create button
     Then New collection is added

    Examples:
    |name  |description         |
    |khizer|this is description |
    |      |this is description |

