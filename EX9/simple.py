def card_probability(target_count, condition, card_type):

    # Each draw: either Face Card (F) or Non-Face (N)
    outcomes = []
    for c1 in ['F', 'N']:
        for c2 in ['F', 'N']:
            for c3 in ['F', 'N']:
                outcomes.append((c1, c2, c3))

    # 12 face cards out of 52 => P(F) = 12/52 = 3/13
    # We calculate exact probability (weighted)
    p_face = 12 / 52
    p_non  = 40 / 52

    total_prob = 0.0
    favorable_prob = 0.0

    print(f"\nAll possible outcomes (F=Face, N=Non-Face) for 3 draws:")

    for combo in outcomes:
        face_count = combo.count('F')
        non_count  = combo.count('N')

        # Probability of this specific combo
        prob = (p_face ** face_count) * (p_non ** non_count)
        total_prob += prob

        match = False
        if condition == "equal"   and face_count == target_count: match = True
        elif condition == "greater" and face_count >  target_count: match = True
        elif condition == "less"    and face_count <  target_count: match = True

        status = " <-- MATCH" if match else ""
        print(f"  {combo}  face_cards={face_count}  prob={round(prob,5)}{status}")

        if match:
            favorable_prob += prob

    print(f"\nTotal probability (sum, should be ~1): {round(total_prob, 5)}")
    print(f"Outcomes where '{condition} {target_count} face cards': favorable_prob = {round(favorable_prob, 5)}")
    print(f"\nP(face cards {condition} {target_count}) = {round(favorable_prob, 5)}")


# ---- USER INPUT ----
print("=== 3 Card Draw Probability (Face Cards) ===")
print("Face Cards = Jack, Queen, King (12 out of 52 cards)")
target = int(input("\nEnter target number of Face Cards (0-3): "))
print("Choose condition: equal / greater / less")
cond = input().lower()
card_probability(target, cond, "face")
