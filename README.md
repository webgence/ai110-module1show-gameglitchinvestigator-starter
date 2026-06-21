# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- The purpose of the game is for the user to guess the correct value that a computer generated.

- There were various logical errors such as the program not handling values that were below or above the range of possible values. The program also didn't handle non int values such as None, empty, floats, and non-numbers. There was also a mismatch in the hint message which lead to the user receiving misleading information on there next guess(eg. "go lower" when the number is larger or "go higher" when the number is lower). The score system is also weird and should be scale down with attempts.


- Ultizing Claude Code and my brain, I fixed all of these logical errors. Although some parts I had to manually debug myself because Claude Code wasn't able to fix everything.


## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User enters a guess of 40
2. Game returns "Too Low"
3. User enters a guess of 70 -> "Too High"
4. User enters a guess that is above the maximum range or enters a guess that is below the minimum range -> "Guess must be between 1 and 100."
5. Score updates correctly after each guess
6. Game ends after correct guess 



**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
