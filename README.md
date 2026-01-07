
# 🎮 Rock–Paper–Scissors–Plus — AI Game Referee

A minimal **AI Game Referee** for **Rock–Paper–Scissors–Plus**, implemented in **Python** using **Google ADK**.  
The referee enforces game rules, validates inputs, maintains state across turns, and automatically ends the game after three rounds.

This project runs in a simple **conversational (CLI-style) loop** and focuses on correctness, clean state modeling, and clear agent/tool separation.

---

## 📌 Assignment Objective

Build a minimal AI referee chatbot that:
- Runs a short game of Rock–Paper–Scissors–Plus
- Enforces all game rules correctly
- Tracks state across conversational turns
- Uses **Google ADK agents and tools**
- Ends automatically after a fixed number of rounds

---

## 🎯 Game Rules

- **Game type:** Best of 3 rounds  
- **Valid moves:** `rock`, `paper`, `scissors`, `bomb`
- **Special rules:**
  - `bomb` beats all other moves
  - Each player may use `bomb` **only once per game**
  - `bomb` vs `bomb` results in a draw
  - Invalid input wastes the round
- The game **automatically ends after 3 rounds**

---

## 🏗️ Architecture & Design

The solution is structured to clearly separate responsibilities:

| Layer | Responsibility |
|-----|----------------|
| Intent Understanding | Read and interpret user input |
| Game Logic | Decide the winner of each round |
| State Management | Persist and mutate game state |
| Response Generation | Display round-by-round feedback |

This separation ensures clarity, correctness, and easy reasoning about system behavior.

---

## 📦 State Model

Game state is stored in a **persistent Python dictionary**, ensuring it does **not live only in the prompt**:

```python
game_state = {
    "round": 1,
    "max_rounds": 3,
    "user_score": 0,
    "bot_score": 0,
    "user_bomb_used": False,
    "bot_bomb_used": False,
    "game_over": False,
}
````

The state:

* Persists across turns
* Is mutated only through explicit logic
* Requires no databases or external APIs

---

## 🧰 Google ADK Usage

This project uses **Google ADK** to define an **AI referee agent** with explicit tools.

### ADK Agent

```python
referee_agent = Agent(
    name="rps_plus_referee",
    description="AI referee for Rock–Paper–Scissors–Plus",
    tools=[validate_move, resolve_round, update_game_state],
)
```

### Explicit Tools

The following functions are registered as tools under the ADK agent:

* **`validate_move`**
  Validates user input and enforces one-time bomb usage.

* **`resolve_round`**
  Determines the winner of a round based on game rules.

* **`update_game_state`**
  Mutates persistent game state (scores, rounds, game termination).

These tools are used for **state mutation and validation**, satisfying the technical tooling requirements.

---

## 🔄 Game Flow

1. Rules are explained in ≤ 5 lines
2. User is prompted for a move
3. Input is validated
4. Bot selects a move
5. Round outcome is resolved and explained
6. Game state is updated
7. After 3 rounds, the game ends automatically with a final result

Each round clearly displays:

* Round number
* User move
* Bot move
* Round winner

---

## ▶️ How to Run

### Requirements

* Python 3.9+
* Google ADK

### Install dependency

```bash
pip install google-adk
```

### Run the game

```bash
python game_refree.py
```

---

## 🧪 Testing & Validation

The game was manually tested for:

* Normal gameplay
* One-time bomb usage per player
* Bomb reuse rejection
* Invalid input handling (round wasted)
* Automatic termination after exactly three rounds

All edge cases behave as expected.

---

## ⚖️ Tradeoffs

* The bot uses a simple randomized strategy to keep the implementation minimal.
* The conversational loop is deterministic instead of LLM-driven to ensure correctness and easy testing.

---

## 🚀 Possible Improvements

With more time, the following could be added:

* Smarter bot strategy using opponent history
* Structured JSON outputs
* Unit tests for game logic
* Schema-based validation for tools

---

## ✅ Requirement Checklist

* ✔ Python implementation
* ✔ Google ADK agent used
* ✔ Explicit tools defined
* ✔ State not stored in prompt
* ✔ Invalid input handled gracefully
* ✔ Automatic game termination

---

## 📌 Summary

This project demonstrates:

* Correct game logic
* Clear state modeling
* Proper use of Google ADK agents and tools
* Clean, minimal, and readable architecture

The focus is on **correctness, clarity, and engineering fundamentals**.

```

---

### ✅ Final step
1. Paste this into `README.md`
2. Commit
3. Push
4. Submit

You’re **fully done** now.  
If you want, I can do a **final repo audit** before submission — just say the word 👊
```
