def computegrade(score):
    if 1.0 >= score >= 0.9:
        print("A")
    elif 0.8 <= score <= .89:
        print("B")
    elif 0.7 <= score <= .79:
        print("C")
    elif 0.6 <= score <= .69:
        print("D")
    elif 0 < score < 0.6:
        print("F")
    else:
        print("Bad score")

computegrade(float(input("Enter score: ")))