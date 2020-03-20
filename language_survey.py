from survey import  AnonymousSurvey

question = "What's your favorite language? "
my_survey = AnonymousSurvey(question)

"""显示问题并存储答案"""
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)


print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()