def calculate_performance_scores(*args, **kwargs):
    """
    Computes performance metrics from varying sets of assessment grades.
    Input:
        *args: Variable length sequence of numeric grades (ints or floats).
        **kwargs: Optional keyword configurations (e.g., student_name, course).
    Output:
        tuple: (min_score, max_score, average, letter_distribution_dict)
    """
    if not args:
        return None, None, 0.0, {}
    min_score = min(args)
    max_score = max(args)
    average = sum(args) / len(args)
    distribution = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    for score in args:
        if score >= 90:
            distribution["A"] += 1
        elif score >= 80:
            distribution["B"] += 1
        elif score >= 70:
            distribution["C"] += 1
        elif score >= 60:
            distribution["D"] += 1
        else:
            distribution["F"] += 1
    student = kwargs.get("student_name", "Unknown Class/Student")
    course = kwargs.get("course", "General")
    print(f"--- Statistics for {student} | Course: {course} ---")
    return min_score, max_score, average, distribution


if __name__ == "__main__":
    grades_set_1 = [85, 92, 78, 90, 65, 88, 72, 95, 54, 80]
    
    min_val, max_val, avg, dist = calculate_performance_scores(
        *grades_set_1, 
        student_name="Batch A", 
        course="Python Programming"
    )

    print(f"Minimum Score: {min_val}")
    print(f"Maximum Score: {max_val}")
    print(f"Average Score: {avg:.2f}")
    print(f"Letter Distributions: {dist}\n")
    min_val2, max_val2, avg2, dist2 = calculate_performance_scores(
        100, 95, 89, 92, 
        student_name="Alice", 
        course="Advanced Math"
    )
    
    print(f"Minimum Score: {min_val2}")
    print(f"Maximum Score: {max_val2}")
    print(f"Average Score: {avg2:.2f}")
    print(f"Letter Distributions: {dist2}")