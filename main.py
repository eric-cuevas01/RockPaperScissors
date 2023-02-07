import random
import check_input


def weapon_menu():
  while True:
    weapon = input(
      "Choose your weapon:\nR. Rock\nP. Paper\nS. Scissors\nB. Back:\n").upper(
      )
    if weapon == "R" or weapon == "P" or weapon == "S" or weapon == "B":
      return weapon
    print("Invalid input. Try again.")


def comp_weapon():
  return random.choice(("R", "P", "S"))


def find_winner(player, comp):
  print("You chose:", player)
  print("Computer chose:", comp)
  if player == comp:
    print("Tie.")
    return 0
  elif (player == "R" and comp == "S") or (player == "P" and comp == "R") or (
      player == "S" and comp == "P"):
    print("Player wins.")
    return 1
  else:
    print("Computer wins.")
    return 2


def display_scores(player, comp):
  print("Player =", player)
  print("Computer =", comp)


def main_menu():

  getInput = True
  while getInput:
    choice = check_input.get_int_range(
      "1. Play game\n2. Show scores\n3. Quit\nEnter choice: ", 1, 3)
    # if choice == 1 or choice == 2 or choice == 3:
    # choice = input("1. Play game\n2. Show scores\n3. Quit\nEnter choice: ")
    # if choice in ["1", "2", "3"]:
    getInput = False
    return choice
    print("Invalid input. Try again.")


def main():
  player_score = 0
  comp_score = 0
  while True:
    choice = main_menu()
    if choice == 3:
      break
    if choice == 2:
      display_scores(player_score, comp_score)
      continue
    weapon = weapon_menu()
    if weapon == "B":
      continue
    comp = comp_weapon()
    winner = find_winner(weapon, comp)
    if winner == 1:
      player_score += 1
    elif winner == 2:
      comp_score += 1


if __name__ == "__main__":
  main()
