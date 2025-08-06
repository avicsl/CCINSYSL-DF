def get_valid_score(prompt, max_score):
    while True:
        try:
            score = float(input(prompt))
            if 0 <= score <= max_score:
                return score
            else:
                print(f"❌ Invalid input. Enter a number between 0 and {max_score}.\n")
        except ValueError:
            print("❌ Invalid input. Enter a valid number.\n")

def calculate_class_standing():
    print("\n======================= CLASS STANDING =======================")
    act1 = get_valid_score("📝 Activity 1 Score (over 30): ", 30)
    act2 = get_valid_score("📝 Activity 2 Score (over 20): ", 20)
    act3 = get_valid_score("📝 Activity 3 Score (over 10): ", 10)
    as1  = get_valid_score("\n📚 Assignment 1 Score (over 50): ", 50)
    as2  = get_valid_score("📚 Assignment 2 Score (over 50): ", 50)
    as3  = get_valid_score("📚 Assignment 3 Score (over 50): ", 50)

    total_score = act1 + act2 + act3 + as1 + as2 + as3
    total_items = 210
    cs_grade = (total_score / total_items) * 100
    cs_grade_percent = cs_grade * 0.4

    print("\n📍 CLASS STANDING SCORES")
    print(f"{'Component':<15}{'Score':>10}{'Items':>10}")
    print(f"{'Activity 1':<15}{act1:>10.0f}{30:>10}")
    print(f"{'Activity 2':<15}{act2:>10.0f}{20:>10}")
    print(f"{'Activity 3':<15}{act3:>10.0f}{10:>10}")
    print(f"{'Assignment 1':<15}{as1:>10.0f}{50:>10}")
    print(f"{'Assignment 2':<15}{as2:>10.0f}{50:>10}")
    print(f"{'Assignment 3':<15}{as3:>10.0f}{50:>10}")
    print(f"{'TOTAL':<15}{total_score:>10.0f}{total_items:>10}")

    print("\n📊 CLASS STANDING SUMMARY")
    print(f"  ➤  Class Standing Grade  : {cs_grade:.2f}%")
    print(f"  ➤  Weighted (40%)        : {cs_grade_percent:.2f}%\n")

    return cs_grade, cs_grade_percent

def calculate_long_exam():
    print("========================= LONG EXAM =========================")
    score = get_valid_score("🧾 Long Exam Score (over 50): ", 50)
    max_score = 50
    lexm_grade = (score / max_score) * 100
    lexm_grade_percent = lexm_grade * 0.4

    print("\n📍 LONG EXAM SCORES")
    print(f"{'Component':<15}{'Score':>10}{'Items':>10}")
    print(f"{'Long Exam':<15}{score:>10.0f}{max_score:>10}")

    print("\n📊 LONG EXAM SUMMARY")
    print(f"  ➤  Long Exam Grade      : {lexm_grade:.2f}%")
    print(f"  ➤  Weighted (40%)       : {lexm_grade_percent:.2f}%\n")

    return lexm_grade, lexm_grade_percent

def calculate_final_project():
    print("======================= FINAL PROJECT =======================")
    score = get_valid_score("💻 Final Project Score (over 50): ", 50)
    max_score = 50
    fproj_grade = (score / max_score) * 100
    fproj_grade_percent = fproj_grade * 0.2

    print("\n📍 FINAL PROJECT SCORES")
    print(f"{'Component':<15}{'Score':>10}{'Items':>10}")
    print(f"{'Final Project':<15}{score:>10.0f}{max_score:>10}")

    print("\n📊 FINAL PROJECT SUMMARY")
    print(f"  ➤  Final Project Grade  : {fproj_grade:.2f}%")
    print(f"  ➤  Weighted (20%)       : {fproj_grade_percent:.2f}%\n")

    return fproj_grade, fproj_grade_percent

def compute_final_grade():
    print("====================== GRADE COMPUTATION ======================")
    cs_grade, cs_percent = calculate_class_standing()
    lexm_grade, lexm_percent = calculate_long_exam()
    fproj_grade, fproj_percent = calculate_final_project()

    final_grade = cs_percent + lexm_percent + fproj_percent
    remarks = "✅ PASSED" if final_grade >= 60 else "❌ FAILED"

    print("====================== FINAL GRADE SUMMARY ======================")
    print(f"🎯 Final Weighted Grade : {final_grade:.2f}%")
    print(f"🏁 Remarks              : {remarks}")
    print("=================================================================\n")


while True:
    compute_final_grade()

    while True:
        again = input("🔁 Do you want to compute again? (yes/no): ").strip().lower()
        if again == "yes" or again == "no":
            break
        else:
            print("❌ Invalid input. Please type only yes or no.\n")

    if again == "no":
        print("\n👋 Program ended. Thank you!")
        break
