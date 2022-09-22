Feature: Amazon validations



  Scenario: Validate that it is not possible to login with a valid but unregistered email
    Given I am on the Arab Emirates Amazon homepage
    When I navigate to the sign in page
    And I attempt to sign in with a valid but unregistered email
    Then I should remain in the sig in page
    And an error message should be displayed

  Scenario: Validate that the items are added correctly to the cart
    Given I am on the Arab Emirates Amazon homepage
    When i select the first item in the second category in todays deals
    And i attempt to add three units of the first item displayed to my cart
    Then i should see that the three items are added to my cart
    And the price and subtotal values are as expected

  Scenario Outline: Validate that a signed out user can access the lists page but not the orders and addresses pages
    Given I am on the Arab Emirates Amazon homepage
    When i go to the Accounts and Lists option
    And i select the "<option>" option
    Then i should be sent to the "<page>" page

    Examples:
    |option   |page   |
    |addresses|sign in|
    |orders   |sign in|
    |lists    |lists  |