import random
from typing import Tuple
from google.adk import Agent

# -------------------------
# GAME STATE (persistent, not in prompt)
# -------------------------
game_state = {
    "round": 1,
    "max_rounds": 3,
    "user_score": 0,
    "bot_score": 0,
    "user_bomb_used": False,
    "bot_bomb_used": False,
    "game_over": False,
}

VALID_MOVES = ["rock", "paper", "scissors", "bomb"]

# =====================================================
# EXPLICIT TOOLS (registered with ADK Agent)
# =====================================================

def validate_move(move: str, bomb_used: bool) -> Tuple[bool, str]:
    """Validates user input and bomb usage."""
    move = move.lower().strip()

    if move not in VALID_MOVES:
        return False, "Invalid move. This round is wasted."

    if move == "bomb" and bomb_used:
        return False, "Bomb already used. This round is wasted."

    return True, move


def resolve_round(user_move: str, bot_move: str) -> str:
    """Determines round winner."""
    if user_move == bot_move:
        return "draw"

    if user_move == "bomb" and bot_move == "bomb":
        return "draw"

    if user_move == "bomb":
        return "user"

    if bot_move == "bomb":
        return "bot"

    rules = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock",
    }

    return "user" if rules[user_move] == bot_move else "bot"


def update_game_state(result: str) -> None:
    """Mutates persistent game state."""
    if result == "user":
        game_state["user_score"] += 1
    elif result == "bot":
        game_state["bot_score"] += 1

    game_state["round"] += 1

    if game_state["round"] > game_state["max_rounds"]:
        game_state["game_over"] = True


# =====================================================
# ADK AGENT (THIS IS THE KEY ADK USAGE)
# =====================================================

referee_agent = Agent(
    name="rps_plus_referee",
    description="AI referee for Rock–Paper–Scissors–Plus",
    tools=[validate_move, resolve_round, update_game_state],
)

# =====================================================
# GAME LOOP
# =====================================================

def bot_choose_move():
    if not game_state["bot_bomb_used"] and random.random() < 0.2:
        game_state["bot_bomb_used"] = True
        return "bomb"
    return random.choice(["rock", "paper", "scissors"])


def explain_rules():
    print(
        "Rock–Paper–Scissors–Plus (Best of 3)\n"
        "Moves: rock, paper, scissors, bomb (once per player)\n"
        "Bomb beats all moves\n"
        "Bomb vs bomb = draw\n"
        "Invalid input wastes the round\n"
    )


def run_game():
    explain_rules()

    while not game_state["game_over"]:
        print(f"\nRound {game_state['round']}")
        user_input = input("Your move: ")

        valid, result = validate_move(user_input, game_state["user_bomb_used"])
        if not valid:
            print(result)
            update_game_state("draw")
            continue

        user_move = result
        if user_move == "bomb":
            game_state["user_bomb_used"] = True

        bot_move = bot_choose_move()
        outcome = resolve_round(user_move, bot_move)
        update_game_state(outcome)

        print(f"You played: {user_move}")
        print(f"Bot played: {bot_move}")

        if outcome == "draw":
            print("Round result: Draw")
        elif outcome == "user":
            print("Round result: You win this round")
        else:
            print("Round result: Bot wins this round")

    print("\nGame Over")
    print(f"Final Score → You: {game_state['user_score']} | Bot: {game_state['bot_score']}")

    if game_state["user_score"] > game_state["bot_score"]:
        print("Final Result: You win!")
    elif game_state["user_score"] < game_state["bot_score"]:
        print("Final Result: Bot wins!")
    else:
        print("Final Result: Draw")


if __name__ == "__main__":
    run_game()
