'''
This program takes the user through questions regarding "Are you looking for a relaxing outlet escape?" and gives a final verdict by using using if-else functions.
'''

answer1 = input("Are you looking for a relaxing outlet escape? (Y/N) ")
if answer1 == "Y":
    yes1 = input("Would you like staff at your beck and call? (Y/N) ")
    if yes1 == "Y":
        yes2 = input("Are you in need of serious spa-style pampering? (Y/N) ")
        if yes2 == "Y":
            yes4 = input("Do you fancy haggling in a colourful bazaar? (Y/N) ")
            if yes4 == "Y":
                print("Moroccan riad")
            if yes4 == "N":
                no2 = input("Do you fancy a countryside escape? (Y/N) ")
                if no2 == "Y":
                    yes3 = input("Are you a wine connoisseur or a sommelier wannabe? (Y/N) ")
                    if yes3 == "Y":
                        print("Wine estate")
                    if yes3 == "N":
                        no5 = input("Are you a golf nut or a tennis junkie? (Y/N) ")
                        if no5 == "Y":
                            print("Wine estate")
                        if no5 == "N":
                           no3 = input("Are you dreaming of a sunny beach escape? (Y/N) ")
                           if no3 == "Y":
                              print("Beachfront villa")
                           if no3 == "N":
                              no4 = input("Impossible. Everyone loves the seaside! (Y/N) ")
                              if no4 == "Y":
                                  print("Beachfront villa")
                              if no4 == "N":
                                  print("Beachfront villa")
                if no2 == "N":
                    no3 = input("Are you dreaming of a sunny beach escape? (Y/N) ")
                    if no3 == "Y":
                        print("Beachfront villa")
                    if no3 == "N":
                        no4 = input("Impossible. Everyone loves the seaside! (Y/N) ")
                        if no4 == "Y":
                            print("Beachfront villa")
                        if no4 == "N":
                            print("Beachfront villa")
        if yes2 == "N":
            no3 = input("Are you dreaming of a sunny beach escape? (Y/N) ")
            if no3 == "Y":
                print("Beachfront villa")
                if no3 == "N":
                    no4 = input("Impossible. Everyone loves the seaside! (Y/N) ")
                    if no4 == "Y":
                        print("Beachfront villa")
                    if no4 == "N":
                        print("Beachfront villa")
    if yes1 == "N":
        no2 = input("Do you fancy a countryside escape? (Y/N) ")
        if no2 == "Y":
            yes3 = input("Are you a wine connoisseur or a sommelier wannabe? (Y/N) ")
            if yes3 == "Y":
                print("Wine estate")
        if no2 == "N":
           no3 = input("Are you dreaming of a sunny beach escape? (Y/N) ")
           if no3 == "Y":
               print("Beachfront villa")
               if no3 == "N":
                   no4 = input("Impossible. Everyone loves the seaside! (Y/N) ")
                   if no4 == "Y":
                       print("Beachfront villa")
                   if no4 == "N":
                       print("Beachfront villa")

if answer1 == "N":
    no1 = input("Do you want a place with a glamorous nightlife? (Y/N) ")
    if no1 == "Y":
        yes5 = input("Are you a culture vulture in need of a museum or gallery fix? (Y/N) ")
        if yes5 == "Y":
            print("City apartment")
        if yes5 == "N":
            no6 = input("Dying to hit the ski slopes? (Y/N) ")
            if no6 == "Y":
                print("Ski chalet")
            if no6 == "N":
                no7 = input("Are you a snow bunny? (Y/N) ")
                if no7 == "Y":
                    print("Ski chalet")
                if no7 == "N":
                    print("City apartment")
    if no1 == "N":
        no8 = input("Does surfing scuba diving or parasailing float your boat? (Y/N) ")
        if no8 == "Y":
           no3 = input("Are you dreaming of a sunny beach escape? (Y/N) ")
           if no3 == "Y":
               print("Beachfront villa")
               if no3 == "N":
                   no4 = input("Impossible. Everyone loves the seaside! (Y/N) ")
                   if no4 == "Y":
                       print("Beachfront villa")
                   if no4 == "N":
                       print("Beachfront villa")
        if no8 == "N":
            no6 = input("Dying to hit the ski slopes? (Y/N) ")
            if no6 == "Y":
                print("Ski chalet")
            if no6 == "N":
                no7 = input("Are you a snow bunny? (Y/N) ")
                if no7 == "Y":
                    print("Ski chalet")
                if no7 == "N":
                    print("City apartment")
