# hospital_triage.py

"""
Real-world application: Hospital Emergency Triage System
Bubble sort prioritizes patients by severity so critical cases are treated first.

Severity scale:
  1  — Minor (cold, bruise)
  5  — Moderate (fracture, high fever)
  8  — Severe (chest pain, head trauma)
  10 — Critical (cardiac arrest, stroke)
"""


def bubble_sort_patients(patients):
    n = len(patients)
    for pass_num in range(n - 1):
        swapped = False
        for i in range(n - 1 - pass_num):
            if patients[i]["severity"] < patients[i + 1]["severity"]:
                patients[i], patients[i + 1] = patients[i + 1], patients[i]
                swapped = True
        if not swapped:
            break
    return patients


def display_queue(patients, title="Patient Queue"):
    print(f"\n{'─' * 55}")
    print(f"  {title}")
    print(f"{'─' * 55}")
    print(f"  {'#':<5} {'Name':<20} {'Condition':<22} {'Severity'}")
    print(f"  {'─'*4:<5} {'─'*18:<20} {'─'*20:<22} {'─'*8}")
    for rank, p in enumerate(patients, 1):
        s = p["severity"]
        color = "\033[91m" if s >= 8 else "\033[93m" if s >= 5 else "\033[92m"
        reset = "\033[0m"
        print(f"  {color}#{rank:<4}{reset} {p['name']:<20} {p['condition']:<22} {color}{s}/10{reset}")
    print(f"{'─' * 55}\n")


def main():
    patients = [
        {"name": "Alice Mathew",  "condition": "Sprained ankle",   "severity": 3},
        {"name": "Ravi Kumar",    "condition": "Cardiac arrest",    "severity": 10},
        {"name": "Sara Lim",      "condition": "High fever",        "severity": 5},
        {"name": "James Okoye",   "condition": "Head trauma",       "severity": 9},
        {"name": "Meena Pillai",  "condition": "Common cold",       "severity": 1},
        {"name": "Tom Nguyen",    "condition": "Severe chest pain", "severity": 8},
        {"name": "Divya Sharma",  "condition": "Broken arm",        "severity": 6},
        {"name": "Carlos Reyes",  "condition": "Mild rash",         "severity": 2},
    ]

    print("\n🏥  Hospital Emergency Triage System")
    print("    Bubble Sort — prioritizing patients by severity\n")

    display_queue(patients, title="Arrival Order (unsorted)")

    sorted_patients = bubble_sort_patients(patients.copy())

    display_queue(sorted_patients, title="Treatment Priority Queue (sorted)")

    first = sorted_patients[0]
    print(f"  ⚠️  Treat first: \033[91m{first['name']}\033[0m"
          f" — {first['condition']} (severity {first['severity']}/10)\n")


if __name__ == "__main__":
    main()
