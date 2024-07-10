# main.py
from game import Game

def main():
    my_cat = Game("Tom", 1)

    while True:
        user_input = input(f"Do you want to interact with {my_cat.name}? (yes/no): ").strip().lower()

        if user_input == 'yes':
            while True:
                action = input(f"What do you want to do with {my_cat.name}? (feed/play/nap/check stamina/talk/groom/exit): ").strip().lower()

                if action == 'feed':
                    food_choice = input(f"What do you want to feed {my_cat.name}? (milk/fish): ").strip().lower()
                    if food_choice in ['milk', 'fish']:
                        my_cat.eat(food_choice)
                    else:
                        print("Invalid food choice.")
                elif action == 'play':
                    play_choice = input(f"What do you want to play with {my_cat.name}? (ball/mud/toys): ").strip().lower()
                    my_cat.play(play_choice)
                elif action == 'nap':
                    my_cat.sleep()
                elif action == 'check stamina':
                    my_cat.check_stamina()
                elif action == 'talk':
                    my_cat.talk()
                elif action == 'groom':
                    my_cat.groom()
                elif action == 'exit':
                    print("Exiting the game. Have a nice day!")
                    return
                else:
                    print("Invalid action. Please choose again.")
        elif user_input == 'no':
            print("Goodbye!")
            break
        else:
            print("Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()
