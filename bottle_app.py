
#####################################################################
### Assignment skeleton
### You can alter the below code to make your own dynamic website.
### The landing page for assignment 3 should be at /
#####################################################################

from bottle import route, run, default_app, debug, static_file, post, request, get, redirect
from hashlib import sha256

commentlist = []
user_name = []

def htmlifyIndex():
    html = """
        <!DOCTYPE html>
<html lang = "en">
<head>
	<link rel="shortcut icon" href="/static/images/logo2.png">

	<title>Volvo Cars | Luxury Sedans, Wagons, Crossovers, SUVs</title>

	<meta charset="utf-8"/>
	

	<link rel="stylesheet" type="text/css" href="/static/mystyle.css">

</head>
	<body>

		<h1><img src="/static/images/logo2.png" width="55" height="35" alt="volvo_logo"> Volvo Cars | Luxury Sedans, Wagons, Crossovers, SUVs <img src="/static/images/logo2.png" width="55" height="35" alt="volvo_logo"></h1> 

		<ul>
 			<li><a class="active" href="/static/index.html">Home</a></li>
 			<li><a href="https://www.motorauthority.com/news/volvo">News</a></li>
  			<li><a href="/static/contact.html">Contact</a></li>
  			<li><a href="/static/gimp.html">GimpPhoto and Logo</a>
  			<li><a href="">Comments</a>
		</ul>
		<br /><br />
		<form action="/" method="post">
                    <h3>Nickname:</h3> <input name="nick" type="text" />
                    <h3>Comment:</h3>  <input name="comment" type="text" />
                    <h3>Password:</h3> <input name="password" type="password" />
                    <input value="Submit" type="submit">
                </form>
                <h2>Comments</h2>
                {}
	</body>


</html>

    """.format(htmlify_ulist(user_name, commentlist))
    return html

def htmlify_ulist(user_name, commentlist):
    listString = "<ul>"
    namecount = 0
    for listItem in commentlist:
    	listString += "<li>{}: {}</li>".format(user_name[namecount], listItem)
    	namecount += 1
    listString += "</ul>"
    return listString

#This function was copied from "https://bitbucket.org/damienjadeduff/hashing_example/raw/master/hash_password.py"
def create_hash(password):
    pw_bytestring = password.encode()
    return sha256(pw_bytestring).hexdigest()

#My password stored as hash
password_hash = 'e40aa9d56ec908c9d868bad75e3079f772bbf5778b2264bd1abe2bf488cbddaf'

@route('/')
def index():
    return htmlifyIndex()

@post('/')
def do_login():
	xxx = 0
	global commentlist
	global user_name
	nick = request.forms.get('nick')
	comment = request.forms.get('comment')
	password = request.forms.get('password')

	if create_hash(password) == password_hash:
		user_name.insert(xxx, nick)
		commentlist.insert(xxx, comment)
		xxx += 1
	redirect('/')

#HTML Routing
@route('/static/<htmlPath>')
def html(htmlPath):
    return static_file(htmlPath, root="./static")

#Image Routing
@route('/static/images/<imgPath>')
def images(imgPath):
	return static_file(imgPath,root="./static/images")

#CSS Routing
@route('/static/<cssPath>')
def css(cssPath):
	return static_file(cssPath,root="./static/")

#Gimp Routing
@route('/static/gimp/<imgPath>')
def gimp(imgPath):
	return static_file(imgPath,root="./static/gimp")

#####################################################################
### Don't alter the below code.
### It allows this website to be hosted on Heroku
### OR run on your computer.
#####################################################################

# This line makes bottle give nicer error messages
debug(True)
# This line is necessary for running on Heroku
app = default_app()
# The below code is necessary for running this bottle app standalone on your computer.
if __name__ == "__main__":
  run()

