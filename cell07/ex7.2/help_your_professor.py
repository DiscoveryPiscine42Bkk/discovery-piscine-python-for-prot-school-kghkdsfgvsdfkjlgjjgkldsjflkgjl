def average(student_scores):
    if len(student_scores) == 0:
        return 0
    return sum(student_scores.values()) / len(student_scores)

class_3B = {
    'marine': 18,
    'jean': 15,
    'coline': 8,
    'luc': 9
}

class_3C = {
    'quentin': 17,
    'julie': 15,
    'marc': 8,
    'stephanie': 13
}

print(f"Average for class 3B: {average(class_3B)}.")
print(f"Average for class 3C: {average(class_3C)}.")