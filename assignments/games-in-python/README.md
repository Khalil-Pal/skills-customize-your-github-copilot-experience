
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a Hangman game in Python to practice string manipulation, loops, conditionals, and user input.

## 📝 Tasks

### 🛠️ Game Setup and Word Selection

#### Description

Create the game structure and choose a word randomly from a predefined list.

#### Requirements
Completed program should:

- Use a list of words to choose from
- Select a random word for each game session
- Replace each letter with an underscore (`_`) for the hidden word display
- Show the initial hidden word state to the player

### 🛠️ Player Guesses and Progress Display

#### Description

Let the player guess letters and update the displayed word progress accordingly.

#### Requirements
Completed program should:

- Prompt the player to guess one letter at a time
- Reveal correctly guessed letters in the hidden word display
- Keep already guessed letters visible to the player
- Show the current progress in a format like: `_ a _ g _ a _`

### 🛠️ Guess Tracking and Game End Conditions

#### Description

Track incorrect guesses and determine when the game ends with a win or loss.

#### Requirements
Completed program should:

- Count incorrect guesses and limit the number of attempts
- End the game when the player guesses the entire word or runs out of attempts
- Display a win message when the word is guessed correctly
- Display a lose message and reveal the hidden word when attempts are exhausted

### 🛠️ Example Gameplay

#### Description

Provide sample input/output to reinforce how the game should behave.

#### Requirements
Completed program should support gameplay like:

- Example output:
  ```text
  Guess a letter: a
  Word: _ a _ g _ a _
  Incorrect guesses left: 5
  ```
  ```text
  Guess a letter: h
  Word: h a _ g _ a _
  Incorrect guesses left: 5
  ```
