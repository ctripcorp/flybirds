# Behave syntax
In order for Behave to understand the scenarios, they must follow some basic syntax rules, called Gherkin.

## Feature Files
A feature file has a natural language format describing a feature or part of a feature with representative examples of expected outcomes. They’re plain-text (encoded in UTF-8) and look something like:
```
Feature: Fight or flight
  In order to increase the ninja survival rate,
  As a ninja commander
  I want my ninjas to decide whether to take on an
  opponent based on their skill levels

  Scenario: Weaker opponent
    Given the ninja has a third level black-belt
     When attacked by a samurai
     Then the ninja should engage the opponent

  Scenario: Stronger opponent
    Given the ninja has a third level black-belt
     When attacked by Chuck Norris
     Then the ninja should run for his life
```
The “Given”, “When” and “Then” parts of this prose form the actual steps that will be taken by behave in testing your system. These map to Python step implementations. As a general guide:

Given we put the system in a known state before the user (or external system) starts interacting with the system (in the When steps). Avoid talking about user interaction in givens.

When we take key actions the user (or external system) performs. This is the interaction with your system which should (or perhaps should not) cause some state to change.

Then we observe outcomes.

You may also include “And” or “But” as a step - these are renamed by behave to take the name of their preceding step, so:
```
Scenario: Stronger opponent
  Given the ninja has a third level black-belt
   When attacked by Chuck Norris
   Then the ninja should run for his life
    And fall off a cliff
```
In this case behave will look for a step definition for "Then fall off a cliff".

## Scenario Outlines
Sometimes a scenario should be run with a number of variables giving a set of known states, actions to take and expected outcomes, all using the same basic actions. You may use a Scenario Outline to achieve this:
```
Scenario Outline: Blenders
   Given I put <thing> in a blender,
    when I switch the blender on
    then it should transform into <other thing>

 Examples: Amphibians
   | thing         | other thing |
   | Red Tree Frog | mush        |

 Examples: Consumer Electronics
   | thing         | other thing |
   | iPhone        | toxic waste |
   | Galaxy Nexus  | toxic waste |
```
behave will run the scenario once for each (non-heading) line appearing in the example data tables.

## Step Data
Sometimes it’s useful to associate a table of data with your step.

Any text block following a step wrapped in """ lines will be associated with the step. For example:
```
Scenario: some scenario
  Given a sample text loaded into the frobulator
     """
     Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do
     eiusmod tempor incididunt ut labore et dolore magna aliqua.
     """
 When we activate the frobulator
 Then we will find it similar to English
```
The text is available to the Python step code as the “.text” attribute in the Context variable passed into each step function.

You may also associate a table of data with a step by simply entering it, indented, following the step. This can be useful for loading specific required data into a model.
```
Scenario: some scenario
  Given a set of specific users
     | name      | department  |
     | Barry     | Beer Cans   |
     | Pudey     | Silly Walks |
     | Two-Lumps | Silly Walks |

 When we count the number of people in each department
 Then we will find two people in "Silly Walks"
  But we will find one person in "Beer Cans"
```

visit [Behave](https://github.com/behave/behave), you can learn more about behave syntax

[Visual Studio Code](https://code.visualstudio.com/) is a code editor for Windows, Linux, or macOS.

You can use it with a [Gherkin plugin](https://marketplace.visualstudio.com/items?itemName=alexkrechik.cucumberautocomplete).
