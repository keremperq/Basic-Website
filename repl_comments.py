from hashlib import sha256

password_hash = 'e40aa9d56ec908c9d868bad75e3079f772bbf5778b2264bd1abe2bf488cbddaf'

def create_hash(password):
    pw_bytestring = password.encode()
    return sha256(pw_bytestring).hexdigest()


comments_list = []

while(1):
    list_number = 1
    user_input = input("Please enter your comment(to exit write 'exit') : ")
  
    if (user_input == "exit"):
    	break
    
    passwordconfirming = input("Please enter your password :")
    password = create_hash(passwordconfirming)
    
    if (password_hash == password):
    	print("Your password is correct.")
    	comments_list.append(user_input)
    	print("All of your comments are: ")
    	for one_of_your_comment in comments_list:
    		print(str(list_number) + "-) " + one_of_your_comment)
    		list_number += 1
    else:
    	print("I'm sorry I can't let you do that.Try again please.")