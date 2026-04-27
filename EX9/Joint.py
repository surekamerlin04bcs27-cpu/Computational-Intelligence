
SUIT_LABELS = ["Hearts", "Diamonds", "Clubs", "Spades"]

def input_table():
    print("\nRows    = A = Suit of 1st card drawn (0=Hearts,1=Diamonds,2=Clubs,3=Spades)")
    print("Columns = B = Suit of 2nd card drawn (0=Hearts,1=Diamonds,2=Clubs,3=Spades)\n")

    r = 4
    c = 4
    table = []

    print("Enter joint probability values P(Ai, Bj):")
    print("(For a fair deck each value = 0.0625)\n")

    for i in range(r):
        row = []
        for j in range(c):
            val = float(input(f"  P(A={SUIT_LABELS[i]}, B={SUIT_LABELS[j]}) = "))
            row.append(val)
        table.append(row)

    return table, r, c


def print_table(table, r, c):
    print("\n===== Joint Probability Table P(A,B) =====")
    header = f"{'':12}" + "".join(f"{SUIT_LABELS[j]:12}" for j in range(c))
    print(header)
    print("-" * (12 + 12 * c))
    for i in range(r):
        row_str = f"{SUIT_LABELS[i]:12}" + "".join(f"{table[i][j]:<12.4f}" for j in range(c))
        print(row_str)


def marginal_A(table, r, c):
    print("\n--- Marginal P(A) = P(suit of 1st card) ---")
    for i in range(r):
        s = sum(table[i][j] for j in range(c))
        print(f"  P(A = {SUIT_LABELS[i]}) = {round(s, 4)}")


def marginal_B(table, r, c):
    print("\n--- Marginal P(B) = P(suit of 2nd card) ---")
    for j in range(c):
        s = sum(table[i][j] for i in range(r))
        print(f"  P(B = {SUIT_LABELS[j]}) = {round(s, 4)}")


def conditional_A_given_B(table, r, c):
    print("\nConditional P(A | B): Given the suit of 2nd card, find P of 1st card suit")
    i = int(input("  Enter row index i (0=Hearts,1=Diamonds,2=Clubs,3=Spades): "))
    j = int(input("  Enter col index j (0=Hearts,1=Diamonds,2=Clubs,3=Spades): "))

    joint = table[i][j]
    pb    = sum(table[x][j] for x in range(r))

    print(f"\n  Step 1: P(A={SUIT_LABELS[i]}, B={SUIT_LABELS[j]}) = {joint}")
    print(f"  Step 2: P(B={SUIT_LABELS[j]})                    = {round(pb, 4)}")

    if pb == 0:
        print("  Cannot divide by zero!")
        return

    print(f"  Step 3: P(A={SUIT_LABELS[i]} | B={SUIT_LABELS[j]}) = {joint}/{round(pb,4)} = {round(joint/pb, 4)}")


def conditional_B_given_A(table, r, c):
    print("\nConditional P(B | A): Given suit of 1st card, find P of 2nd card suit")
    i = int(input("  Enter row index i (0=Hearts,1=Diamonds,2=Clubs,3=Spades): "))
    j = int(input("  Enter col index j (0=Hearts,1=Diamonds,2=Clubs,3=Spades): "))

    joint = table[i][j]
    pa    = sum(table[i][x] for x in range(c))

    print(f"\n  Step 1: P(A={SUIT_LABELS[i]}, B={SUIT_LABELS[j]}) = {joint}")
    print(f"  Step 2: P(A={SUIT_LABELS[i]})                    = {round(pa, 4)}")

    if pa == 0:
        print("  Cannot divide by zero!")
        return

    print(f"  Step 3: P(B={SUIT_LABELS[j]} | A={SUIT_LABELS[i]}) = {joint}/{round(pa,4)} = {round(joint/pa, 4)}")


def menu():
    table, r, c = input_table()
    print_table(table, r, c)

    while True:
        print("\n===== MENU =====")
        print("1. Marginal P(A)         - P(suit of 1st card)")
        print("2. Marginal P(B)         - P(suit of 2nd card)")
        print("3. Conditional P(A | B)  - P(1st suit | given 2nd suit)")
        print("4. Conditional P(B | A)  - P(2nd suit | given 1st suit)")
        print("5. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1: marginal_A(table, r, c)
        elif choice == 2: marginal_B(table, r, c)
        elif choice == 3: conditional_A_given_B(table, r, c)
        elif choice == 4: conditional_B_given_A(table, r, c)
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice")

menu()
