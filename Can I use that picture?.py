'''
This program takes the user through questions regarding "Can I use that picture" and gives a final verdict by using Boolean.
'''

answer1 = input("Did you take or create the image yourself? (Yes/No) ")
if answer1 == "Yes":
    answer_yes1 = input("Was the picture you created an original idea? (Yes/No/Not) ")
    if answer_yes1 == "Yes":
        print("If you took a picture with your camera or if you drew or designed "
                  "an image and the concept was completely your own, you automatically "
                  "own all copyrights to it and no one can use it or districute it without "
                  "your permission.")
    elif answer_yes1 == "No":
        print("If you created a picture that is so similar to someone else's that it might "
                  "be thought of as theirs, you cannot use your picture for anything other than "
                  "personal use.")
    else:
        print("When in doubt, do your research to find out if your copied an idea. Otherwise, "
                  "don't use the picture for anything other than limited personal use.")
else:
    print("Ask yourself the fair use questions")
    answer_no1 = input("Are you using the image for personal, non-profit, educational, research, "
                       "or scholarly purposes AND are you using the image sparingly, only for "
                       "limited purposes? (Yes/No) ")
    if answer_no1 == "Yes":
        print("If you are using an image in an educational or research setting, for limited non-profit "
              "uses (don't distribute on a brocure, for example), or to just hang on your wall, you are "
              "usually safe to use the image without permission.")
    elif answer_no1 == "No":
        answer_no2 = input("Are you transforming or repurposing the image to create a new purpose or "
                       "meaning? (Yes/No) ")
        if answer_no2 == "Yes":
            print("If you completely rewor the image so that it isn't recognizable from the original, "
                  "you can use it. Or, if you completely change the meaning (as you might in a parody), "
                  "you are usually safe to use the image.")
        elif answer_no2 == "No":
            answer_no3 = input("Are you publishing the image in a fact-based context or publication that "
                       "benefits the public as a whole (such as in a news source where it is important "
                       "that people see the image)? (Yes/No) ")
            if answer_no3 == "Yes":
                print("On a case-by-case basis, an image may be safe to use under fair use laws if the image "
                      "is published in a non-biased way in order to inform or educate the public for the "
                      "public's good.")
            if answer_no3 == "No":
                answer_no4 = input("Would it be considered impossible to obtain permission from the original "
                                   "source? (Yes/No) ")
                if answer_no4 == "Yes":
                    print("If you are certain that it is impossible to obtain permission from the person or "
                          "entity that created the image (if the creator died and no one owns the rights, "
                          "for example), you are usually safe to use the image without permission.")
                if answer_no4 == "No":
                    answer_no5 = input("Will you be using the image for personal or commercial gain? (Yes) (If "
                                       "you answered 'No' to all the fair use questions, the use of your "
                                       "image would most likely be considered for personal or commercial gain.")
                    if answer_no5 == "Yes":
                        answer_yes2 = input("Is the image in the pulic domain or protected by creative common agreements? (Yes/No) ")
                        if answer_yes2 == "Yes":
                            print("If your picture is in the public domain (meaning the original creator(s) "
                                  "released their rights to the image) or if you purchased the image and "
                                  "its copyright (like from a stock photo company), you can feel comfortable "
                                  "using the image for whatever you like. If your image is protected under creatie commons, "
                                  "be sure to check the conditions under which you can use it (you may not "
                                  "be able to modify it or profit from it, for example). If you are uncertain if "
                                  "the image is in the public domain or creative commons, assume it is not and avoid "
                                  "using it until you've obtained permission.")
                        if answer_yes2 == "No":
                            answer_no6 = input("Did you purchase the image or obtain permission from the original source? (Yes/No) ")
                            if answer_no6 == "Yes":
                                print("If your picture is in the public domain (meaning the original creator(s) "
                                  "released their rights to the image) or if you purchased the image and "
                                  "its copyright (like from a stock photo company), you can feel comfortable "
                                  "using the image for whatever you like. If your image is protected under creatie commons, "
                                  "be sure to check the conditions under which you can use it (you may not "
                                  "be able to modify it or profit from it, for example). If you are uncertain if "
                                  "the image is in the public domain or creative commons, assume it is not and avoid "
                                  "using it until you've obtained permission.")
                            if answer_no6 == "No":
                                print("If you couldn't answer 'yes' to any of the fair use questions and you haven't "
                                      "purchased or obtained permission to use the image, you sould under no "
                                      "circumstances use the image, regardless of where you found it. It is not only "
                                      "considered unethical to use another person's or company's image without "
                                      "permission, it is illegal.")
    answer_no5 = input("Will you be using the image for personal or commercial gain? (Yes) (If "
                        "you answered 'No' to all the fair use questions, the use of your "
                       "image would most likely be considered for personal or commercial gain.")
    if answer_no5 == "Yes":
        answer_yes2 = input("Is the image in the pulic domain or protected by creative common agreements? (Yes/No) ")
        if answer_yes2 == "Yes":
            print("If your picture is in the public domain (meaning the original creator(s) "
                  "released their rights to the image) or if you purchased the image and "
                  "its copyright (like from a stock photo company), you can feel comfortable "
                  "using the image for whatever you like. If your image is protected under creatie commons, "
                  "be sure to check the conditions under which you can use it (you may not "
                  "be able to modify it or profit from it, for example). If you are uncertain if "
                  "the image is in the public domain or creative commons, assume it is not and avoid "
                  "using it until you've obtained permission.")
        if answer_yes2 == "No":
            answer_no6 = input("Did you purchase the image or obtain permission from the original source? (Yes/No) ")
            if answer_no6 == "Yes":
                print("If your picture is in the public domain (meaning the original creator(s) "
                      "released their rights to the image) or if you purchased the image and "
                      "its copyright (like from a stock photo company), you can feel comfortable "
                      "using the image for whatever you like. If your image is protected under creatie commons, "
                      "be sure to check the conditions under which you can use it (you may not "
                      "be able to modify it or profit from it, for example). If you are uncertain if "
                      "the image is in the public domain or creative commons, assume it is not and avoid "
                      "using it until you've obtained permission.")
            if answer_no6 == "No":
                print("If you couldn't answer 'yes' to any of the fair use questions and you haven't "
                      "purchased or obtained permission to use the image, you sould under no "
                      "circumstances use the image, regardless of where you found it. It is not only "
                      "considered unethical to use another person's or company's image without "
                      "permission, it is illegal.")
