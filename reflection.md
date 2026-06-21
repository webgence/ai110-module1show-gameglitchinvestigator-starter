# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

The game looked like a guessing game where there is a input textbox and the user needs to input a guess number between 1-100.
There is also a hint that tells the user hints on what the number should be. It will say something like "Go Higher". 

- The hint doesn't seem accurace because it seems to always say "Go Higher" when I constantly increase the value of my guess(I used all my guesses and it kept saying "Go Higher").

- When the user inputs a number that isn't 1-100, instead of suggesting a error or acknowlegding invalid inputs, the program will continue to say "Go lower" or "Go Higher". For example, input = 101 -> the hint will say "Go Higher" or when input = 0 -> the hint will say "Go lower".


**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| (guess of 40) |  "Too Low hint" |  "Too High hint" |  None
| (guess of 0) |  "0 not a valid input"  |  "Go lower hint"  |  None
| (guess of 101) | "101 not a valid input"   |  "Go lower hint" | None

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).


- I used Claude Code for this project.

- For the get_range_for_difficulty function, the range of the difficulty is numbers for the game is off. Claude Code was able to implement the correct range for easy, normal, and hard. For parse_guess function it correctly identitied edge cases to handle None, empty, floatsm and non-numbers.

- For check_guess function it stated the correct numeric comparison for GO LOWER and GO HIGHER. But only implemented different solutions in app.py and logic_utils.py. And the solution wasn't fully correct because it also had to convert str to int.

- Claude Code also didn't recogize the edge case of when the guess were out of range(I had to manully add this part myself). But that could also be because I was not very that specific when prompting.



---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?


- I reviewed the output and ran test cases. 

- A few test I ran was on the values of the guessed value. I tested 
if the guess value equals the given value, whether the guess was too high, whether the guess was too low, and the messages provided. I used pytest and tested this manually by inputting values and seeing the response. After testing, I fixed this logical error. 

- AI helped generate the code and provided the test case. But I had to adjust it by converting the string to int to avoid further errors. It essentially fixed the problem but not fully.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?


Streamlit reruns your script from top to bottom every time you interact with your app. Each reruns takes place in a blank slate: no variables are shared between runs. Session State is a way to share variables between reruns, for each user session.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.


- Be specific when prompting and read through the response. While also trust your own intuition. Also, test your code always with various test edge cases.

- I would ask for some more random setup process or commands I don't know.

- Helpful as a very good assistance but I would not rely on it too much. It would definately help me produce more better software products.
