Feature: Login feature

  Scenario: Valid login
    Given I am on the login page
    When I enter the username "suvarna.kanawade@appliedaiconsulting.com"
    And I enter the password "Suvarna@1897"
    And I click the login button
    Then I should see the title containing "URL Test"
