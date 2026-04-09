while True:
    try:
        num_subjects = int(input("Enter number of subjects: "))

        if num_subjects <= 0:
            print("Enter valid number")
            continue

        total = 0
        max_marks = -1
        min_marks = 101
        Result = "Pass"

        for i in range(1, num_subjects + 1):

            while True:
                try:
                    mark = int(input(f"Enter subject {i} mark: "))

                    if mark < 0 or mark > 100:
                        print("Marks should be between 0 and 100")
                        continue

                    break
                except ValueError:
                    print("Invalid input!")

            if mark < 35:
                Result = "Fail"

            total = total + mark

            if mark > max_marks:
                max_marks = mark

            if mark < min_marks:
                min_marks = mark

        average = total / num_subjects
        percentage = (total / (num_subjects * 100)) * 100

        print("\n----- Result -----")
        print("Total:", total)
        print("Average:", average)
        print("Percentage:", percentage)
        print("Maximum:", max_marks)
        print("Minimum:", min_marks)
        print("Result:", Result)

    except ValueError:
        print("Invalid input!")
        continue

    choice = input("\nDo you want to continue? (yes/no): ").lower()
    if choice != "yes":
        break