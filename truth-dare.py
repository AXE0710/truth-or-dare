import random
print("""

╭━━━━╮╱╱╱╭╮╭╮
┃╭╮╭╮┃╱╱╭╯╰┫┃
╰╯┃┃┣┻┳╮┣╮╭┫╰━╮
╱╱┃┃┃╭┫┃┃┃┃┃╭╮┃
╱╱┃┃┃┃┃╰╯┃╰┫┃┃┃
╱╱╰╯╰╯╰━━┻━┻╯╰╯
""")
print("""

░█████╗░██████╗░
██╔══██╗██╔══██╗
██║░░██║██████╔╝
██║░░██║██╔══██╗
╚█████╔╝██║░░██║
░╚════╝░╚═╝░░╚═╝
""")

print("""

█▀▄ ▄▀█ █▀█ █▀▀
█▄▀ █▀█ █▀▄ ██▄
""")

      
print("choose 1 for starting game,\n choose 2 for adding truth,\n choose 3 for adding dare,\n choose 4 for removing last truth,\n choose 5 for removing last dares,\n choose 6 for showing all truth and dares,\n choose 7 for quit:")
option = int(input('choose:'))

truth = ['whats your name','where do you live']
dare = ['1 pushup','2 pushup']

while option < 7:
  if option == 1:
    choose = input('truth or dare?, quit?:')
    if choose == 'truth':
      print(random.choice(truth))
    elif choose == 'dare':
      print(random.choice(dare))
    
    else:
      option = int(input('choose option again:'))
      
  elif option == 2:
    #adding truth
    truth.append(input("add truth:"))
    option = int(input('choose again:'))
    
  elif option == 3:
    dare.append(input('add dare:'))
    option = int(input('choose again:'))
  elif option == 4:
    print(truth[-1] + ' is deleted')
    truth.pop()
    option = int(input('choose again:'))
  elif option == 5:
    print(dare[-1] + ' is deleted')
    dare.pop()
    option = int(input('choose again:'))
  elif option == 6:
    print(truth) 
    print(dare)
    option = int(input('choose again:'))

  else: option = int(input('choose again:'))
print('bye')    