welcome = """
░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗  ████████╗░█████╗░
░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝  ╚══██╔══╝██╔══██╗
░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░  ░░░██║░░░██║░░██║
░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░  ░░░██║░░░██║░░██║
░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗  ░░░██║░░░╚█████╔╝
░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝  ░░░╚═╝░░░░╚════╝░
"""

logo = """
  ___                         ___ ___                     _______ __               __               
 |   |  .-----.---.-.-----.  |   Y   .-----.---.-.----.  |   _   |  |--.-----.----|  |--.-----.----.
 |.  |  |  -__|  _  |  _  |  |   1   |  -__|  _  |   _|  |.  1___|     |  -__|  __|    <|  -__|   _|
 |.  |__|_____|___._|   __|   \_   _/|_____|___._|__|    |.  |___|__|__|_____|____|__|__|_____|__|  
 |:  1   |          |__|       |:  |                     |:  1   |                                  
 |::.. . |                     |::.|                     |::.. . |                                  
 `-------'                     `---'                     `-------'                                  
                                                                                                    
"""

year = int(input("Which year do you want to check? "))

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("This is a Leap Year!")
    else:
      print("This is a Not Leap Year!")
  else:
    print("This is a Leap Year!")
else: 
  print("This is not a Leap Year!")
