
def classify(card):
    """Returns category: F=Face, A=Ace, N=Number"""
    return card

def check_event(c1, c2, c3, event_type, condition, target):
    """
    event_type: "total_face"/"total_ace"/"total_number"/"first"/"second"/"third"
    condition : "equal"/"greater"/"less" (for total) OR "F"/"A"/"N" (for specific card)
    target    : integer (for total conditions)
    """
    cards = (c1, c2, c3)

    if event_type == "total_face":
        count = cards.count('F')
        if condition == "equal":   return count == target
        elif condition == "greater": return count > target
        elif condition == "less":    return count < target

    elif event_type == "total_ace":
        count = cards.count('A')
        if condition == "equal":   return count == target
        elif condition == "greater": return count > target
        elif condition == "less":    return count < target

    elif event_type == "total_number":
        count = cards.count('N')
        if condition == "equal":   return count == target
        elif condition == "greater": return count > target
        elif condition == "less":    return count < target

    elif event_type == "first":  return c1 == condition.upper()
    elif event_type == "second": return c2 == condition.upper()
    elif event_type == "third":  return c3 == condition.upper()

    return False


def bayes_cards():
    print("=== Bayes Rule: 3 Card Draws (with replacement) ===")
    print("Card types: F=Face(Jack/Queen/King), A=Ace, N=Number(2-10)")
    print(f"P(F)={12/52:.4f}, P(A)={4/52:.4f}, P(N)={36/52:.4f}\n")

    # ----- Define Event A -----
    print("--- Define Event A (what you want to find P of) ---")
    print("Types: total_face / total_ace / total_number / first / second / third")
    type_a = input("Type of A? ").lower()

    if "total" in type_a:
        print("Condition: equal / greater / less")
        cond_a = input().lower()
        target_a = int(input("Target count (0-3): "))
    else:
        print("Which card type? F / A / N")
        cond_a   = input().upper()
        target_a = 0

    # ----- Define Event B -----
    print("\n--- Define Event B (the evidence/given condition) ---")
    print("Types: total_face / total_ace / total_number / first / second / third")
    type_b = input("Type of B? ").lower()

    if "total" in type_b:
        print("Condition: equal / greater / less")
        cond_b = input().lower()
        target_b = int(input("Target count (0-3): "))
    else:
        print("Which card type? F / A / N")
        cond_b   = input().upper()
        target_b = 0

    # ----- Generate all outcomes (weighted probabilities) -----
    p_face = 12/52
    p_ace  =  4/52
    p_num  = 36/52
    p_map  = {'F': p_face, 'A': p_ace, 'N': p_num}

    card_types = ['F', 'A', 'N']

    prob_B       = 0.0
    prob_A_and_B = 0.0

    print("\n--- Computing over all outcomes ---")

    for c1 in card_types:
        for c2 in card_types:
            for c3 in card_types:
                prob_combo = p_map[c1] * p_map[c2] * p_map[c3]

                A = check_event(c1, c2, c3, type_a, cond_a, target_a)
                B = check_event(c1, c2, c3, type_b, cond_b, target_b)

                if B:
                    prob_B += prob_combo
                    if A:
                        prob_A_and_B += prob_combo

    if prob_B == 0:
        print("\nP(B) = 0 -> Event B never occurs. Bayes rule cannot be applied.")
        return

    result = prob_A_and_B / prob_B

    print("\n======= BAYES RESULT =======")
    print(f"P(B)       = {round(prob_B, 5)}")
    print(f"P(A and B) = {round(prob_A_and_B, 5)}")
    print(f"P(A | B)   = P(A and B) / P(B)")
    print(f"           = {round(prob_A_and_B,5)} / {round(prob_B,5)}")
    print(f"           = {round(result, 5)}")


bayes_cards()
