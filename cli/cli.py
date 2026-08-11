import requests
import sys
import json

# BASE_URL = "http://localhost:5000"
BASE_URL = "https://lusada-marketday.onrender.com/api"

ENDPOINTS = [
    ("Event Name", "/event-name"),
    ("Interval", "/interval"),
    ("Status", "/status"),
    ("Today's Date", "/today-date"),
    ("Next Event", "/next-event"),
    ("Cycle Progress", "/cycle-progress"),
    ("Remaining Days", "/remaining-days"),
    ("Upcoming Rotation", "/upcoming-rotation"),
    ("All Data", "/all")
]


def clear_screen():
    print("\033[H\033[J", end="")


def display_menu():
    print("=== Lusada Market Day CLI ===")
    for i, (name, _) in enumerate(ENDPOINTS, 1):
        print(f"{i}. Get {name}")
    print("q. Quit")
    print("=============================")


def call_api(endpoint):
    try:
        response = requests.get(
            f"{BASE_URL}{endpoint}",
            timeout=10
        )

        if response.status_code == 200:
            print("\n--- Result ---")
            print(json.dumps(response.json(), indent=4))
            print("--------------")
        else:
            print(f"\nError: Received status code {response.status_code}")

    except requests.exceptions.Timeout:
        print("\nError: The API request timed out after 10 seconds.")

    except requests.exceptions.ConnectionError:
        print(
            "\nError: Could not connect to the API. "
            "Make sure the Flask server is running on http://localhost:5000"
        )


def main():
    while True:
        clear_screen()
        display_menu()
        choice = input("\nSelect an option: ").strip().lower()

        if choice == 'q':
            print("Goodbye!")
            break

        try:
            idx = int(choice)

            if 1 <= idx <= len(ENDPOINTS):
                name, path = ENDPOINTS[idx - 1]
                clear_screen()
                print(f"Fetching {name}...")
                call_api(path)

                while True:
                    back = input(
                        "\nEnter 0 to go back to main menu or q to quit: "
                    ).strip().lower()

                    if back == '0':
                        break
                    elif back == 'q':
                        print("Goodbye!")
                        sys.exit(0)

            else:
                input("\nInvalid option. Press Enter to try again.")

        except ValueError:
            input(
                "\nInvalid input. Please enter a number or 'q'. "
                "Press Enter to try again."
            )


if __name__ == "__main__":
    main()
