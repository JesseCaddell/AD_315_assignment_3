from itertools import chain, combinations

def get_power_set(input_set):
    """Generate the power set of the given set."""
    power_set = list(chain.from_iterable(combinations(input_set, r) for r in range(len(input_set) + 1)))
    return [set(subset) for subset in power_set]

def main():
    # Get input from user
    user_input = input("Enter elements of the set separated by spaces: ")
    input_set = set(user_input.split())

    # Generate power set
    power_set = get_power_set(input_set)

    # Display power set
    print("Power Set:")
    for subset in power_set:
        print(subset)

if __name__ == "__main__":
    main()