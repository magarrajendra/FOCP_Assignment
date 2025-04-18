import json
import random
import datetime


def main():
    # Loads configuration from JSON file
    try:
        with open('config.json', 'r') as f:
            config = json.load(f)
    except FileNotFoundError:
        print("Error: Configuration file 'config.json' not found.")
        return

    # Randomly selects an agent name
    agent_name = random.choice(config['agent_names'])
    exit_commands = config['exit_commands']
    disconnect_prob = config['disconnect_probability']

    # Gets user's name
    user_name = input("Please enter your name: ").strip()
    print(f"\nHello {user_name}! My name is {agent_name}. How can I assist you today?")

    # Creates a log file with a timestamp
    start_time = datetime.datetime.now()
    log_filename = start_time.strftime("chat_log_%Y%m%d_%H%M%S.txt")

    with open(log_filename, 'w', encoding='utf-8') as log_file:
        # Log initial session details
        log_file.write(f"Session started at: {start_time}\n")
        log_file.write(f"User Name: {user_name}\n")
        log_file.write(f"Agent Name: {agent_name}\n\n")

        # Main chat loop
        while True:
            user_input = input("\nYou: ").strip()
            current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            log_file.write(f"[{current_time}] User: {user_input}\n")

            # Check if the user wants to exit
            if user_input.lower() in exit_commands:
                print(f"{agent_name}: Goodbye, {user_name}! Have a wonderful day!")
                log_file.write(f"[{current_time}] Bot: Goodbye, {user_name}! Have a wonderful day!\n")
                break

            # Checks for random disconnection
            if random.random() < disconnect_prob:
                print(f"{agent_name}: Sorry, our connection has been lost. Goodbye!")
                log_file.write(f"[{current_time}] Bot: Connection lost. Session terminated.\n")
                break

            # Determines the bot's response
            user_input_lower = user_input.lower()
            found_responses = []
            for keyword in config['keywords']:
                if keyword in user_input_lower:
                    found_responses.extend(config['keywords'][keyword])

            if found_responses:
                chosen_response = random.choice(found_responses)
                # Replace placeholder with user's name if present
                chosen_response = chosen_response.replace("{name}", user_name)
            else:
                chosen_response = random.choice(config['default_responses'])

            # Display and log the response
            print(f"{agent_name}: {chosen_response}")
            log_file.write(f"[{current_time}] Bot: {chosen_response}\n")


if __name__ == "__main__":
    main()