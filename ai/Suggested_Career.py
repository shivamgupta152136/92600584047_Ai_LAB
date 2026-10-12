print("=============================================-")
print("               CAREER GUIDANCE SYSTEM                 ")
print("=============================================")

print("\nAnswer the following questions with yes or no.\n")

CD=str(input("Do you like coding? \t\t: ")).lower().strip()
MM=str(input("Do you like mathematics? \t: ")).lower().strip()
BL=str(input("Do you like biology? \t\t: ")).lower().strip()
DW=str(input("Do you like drawing? \t\t: ")).lower().strip()


print("\n==============Career Suggestion==============")
print("Suggested Career : ",end="")

if (CD=="no" and MM=="no" and BL=="no" and DW=="no"):
    print("Explore your interests and career options futher.")

elif (CD=="no" and MM=="no" and BL=="no" and DW=="yes"):
    print("Graphic Designer / Animator")

elif (CD=="no" and MM=="no" and BL=="yes" and DW=="no"):
    print("Pharmacist / Nurse")

elif (CD=="no" and MM=="no" and BL=="yes" and DW=="yes"):
    print("Medical Illustrator / Healthcare Educator")

elif (CD=="no" and MM=="yes" and BL=="no" and DW=="no"):
    print("Engineer / Data Analyst")

elif (CD=="no" and MM=="yes" and BL=="no" and DW=="yes"):
    print("Architect")

elif (CD=="no" and MM=="yes" and BL=="yes" and DW=="no"):
    print("Doctor")

elif (CD=="no" and MM=="yes" and BL=="yes" and DW=="yes"):
    print("Medical Illustrator / Biomedical Designer")

elif (CD=="yes" and MM=="no" and BL=="no" and DW=="no"):
    print("Programmer / Web Developer")

elif (CD=="yes" and MM=="no" and BL=="no" and DW=="yes"):
    print("Web Designer / UI - UX Developer")

elif (CD=="yes" and MM=="no" and BL=="yes" and DW=="no"):
    print("Health App Developer")

elif (CD=="yes" and MM=="no" and BL=="yes" and DW=="yes"):
    print("Medical Illustrator")

elif (CD=="yes" and MM=="yes" and BL=="no" and DW=="no"):
    print("Software Engineer / Computer Scientist")

elif (CD=="yes" and MM=="yes" and BL=="no" and DW=="yes"):
    print("Game Developer / UI Engineer")

elif (CD=="yes" and MM=="yes" and BL=="yes" and DW=="no"):
    print("Bioinformatics Scientist")

elif (CD=="yes" and MM=="yes" and BL=="yes" and DW=="yes"):
    print("Biomedical Software Engineer / Medical Technology Specialist")
    
print("\nThank you for using the Career Guidance Expert System!")

