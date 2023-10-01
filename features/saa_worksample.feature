Feature: Report Search
  Scenario: Search LD1/LD2 Reports Page
    Given user launch the LD1/LD2 reports page
    When  user enters report details
    And   user clicks search report button
    Then  user should land on the reports page
    And   user should be able to see the desired reports
