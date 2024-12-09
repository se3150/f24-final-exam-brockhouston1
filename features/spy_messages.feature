Feature: encode or decode a secret message
As a secret spy
I should be able to encode and decode messages
So that I can chat with my spy friends like a pro.

Scenario: I can successfully encode a secret message
    Given I open the url "https://www.hanginghyena.com/solvers_a/caesar-cipher-decoder"
    When I enter "TOP SECRET" in the message field
    And I enter "3" in the shift field
    And I click the encode button
    And I wait 200 milliseconds
    Then I should see "WRS VHFUHW" in the result field

Scenario: I can successfully decode a secret message
    Given I open the url "https://www.hanginghyena.com/solvers_a/caesar-cipher-decoder"
    When I enter "WRS VHFUHW" in the message field
    And I enter "3" in the shift field
    And I click the decode button
    And I wait 200 milliseconds
    Then I should see "TOP SECRET" in the result field
