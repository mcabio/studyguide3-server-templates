"""A simple Flask app."""

from flask import Flask, render_template, session, request, redirect

app = Flask(__name__)
app.secret_key = "RANDOM SECRET KEY"

@app.route('/')
def show_homepage():
    """Show homepage."""
    return render_template('homepage.html')

###############################
#                             #
# 1) Finish the routes below. #
#                             #
###############################

# Finish the file server.py so that:
#the /form route renders form.html
# the /results route renders results.html

@app.route('/form')
def show_form():
    """Show form with message options."""
    return render_template('form.html')

# Finish the /results route so that it returns an appropriately cheery, honest, 
# or dreary message. Then, use Jinja to display the results of the user submitting 
# the form in results.html. Feel free to get creative here!

@app.route('/results')
def show_results():
    """Show resulting message."""

    cheery = request.args.get('cheery')
    honest = request.args.get('honest')
    dreary = request.args.get('dreary')
    
    if cheery and honest and dreary:
        msg = "Hm, that's a tall order"
    elif cheery and honest and not dreary:
        msg = "Here's a cheery and honest message: You're cool!"
    elif cheery and dreary and not honest:
        msg = "Cheery AND dreary? Be careful what you wish for. It just might come true."
    elif dreary and honest:
        msg = "All good things must come to an end."
    elif not dreary and not honest and cheery:
        msg = "Unicorns are real!"
    elif not honest and not cheery:
        msg = "All fun activities have been cancelled for the day."
    else:
        msg = "You will find what you've been looking for."

    return render_template('results.html', msg=msg)

    # Handle the initial GET request to display the form
  

# Create a form on homepage.html that asks for the user’s name 
# in a text input. The form should submit to a new route called /save-name 
# that you create, and add it to the session with the key, name. 
# The route should take the user back to the homepage.
# request.form.get: is a dictionary provided by the Request object (request). 
# It is used to access data from different parts of an HTTP request:
# Used to access data submitted through an HTML form with the *POST* method.
# If you have an HTML form with input fields, the data entered into those fields will 
# be available in request.form. With request.args.get, it is used to 
# access data from the query string of a URL. It's typically associated 
# with data sent in the URL as parameters with the *GET* method.
# responsible for storing the value of the name variable in the Flask session. 
# In Flask, the session object is a dictionary-like object that you can use 
# to store data that will be available across requests for the same user. 
# The 'name' key was used here instead of username because the provided base.html code
# already had it as the key.
@app.route('/save-name', methods=["POST"])
def save_name():
    """Show resulting message."""
    name = request.form.get('name') 
    session['name'] = name 
    return redirect('/')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

