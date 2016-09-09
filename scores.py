def scoresgrade():
    print "Scores and Grades"
    for count in range (1,11):
        scores = input("What is your score?")
        if (scores <= 59):
            print "I think you need to try a bit harder"
        elif (scores >= 60 and scores <=69):
            print "Your score is:", scores, "Your grade is D"
        elif (scores >= 70 and scores <=79):
            print "Your score is:", scores, "Your grade is C"
        elif (scores >= 80 and scores <= 89):
            print "Your score is:", scores, "Your grade is B"
        elif (scores >=90 and scores <=100):
            print "Your score is:", scores, "Your grade is A"
        elif (scores > 100):
            print "Your score is:", scores, "Your grade is A+"
    print "End of program. Bye!"

scoresgrade()
