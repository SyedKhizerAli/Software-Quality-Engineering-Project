Feature: feature1
  Scenario Outline: login
     Given Chrome Browser is opened
     When I open url http://localhost:3000/
     And I Enter email <Email>
     And I Enter password <Password>
     And I click Login Button
     Then I am logged in

    Examples:
    | Email                 | Password     |
    | l201371@lhr.nu.edu.pk | khizerali123 |

