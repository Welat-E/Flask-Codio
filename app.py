import datetime
from flask import Flask, render_template, request 

app = Flask(__name__)

@app.route('/')
def index():
    users = {
    'Alice': {'age': 25, 'country': 'USA'},
    'Bob': {'age': 30, 'country': 'UK'},
    'Charlie': {'age': 35, 'country': 'Australia'}
    }
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    #retrieve the name from the GET parameter ‘name’
    user = request.args.get('name', 'World')  # 'World' ist der Standardname, falls keiner angegeben ist

    return render_template('index.html', title='Home', user=user, time=now, users= users)

@app.route('/form')
def form():
  return render_template('form.html', value= 'Submit')


@app.route('/greet', methods=['GET'])
def greet():
    name = request.args.get('name', 'Guest')  # Use 'Guest' as default value if no 'name' parameter is provided
    return f"Hello, {name}!"


@app.route('/all-users')
def all_users():
    users = {
    'Alice': {'age': 25, 'country': 'USA'},
    'Bob': {'age': 30, 'country': 'UK'},
    'Charlie': {'age': 35, 'country': 'Australia'}
    }
    return render_template('allusers.html', users= users)


@app.route('/post/<int:post_id>')
def show_post(post_id):
  # The varibale post_id is an int
  return f"Post {post_id}"


@app.route('/update_profile', methods=['POST'])
def update_profile():
  username = request.form['username']
  email = request.form['email']

  #Update the user's profile with the new data
  return f"Updateing profile of {username} with email {email}"


@app.route('/update-country', methods=['GET', 'POST'])
def update_country():
    users = {
    'Alice': {'age': 25, 'country': 'USA'},
    'Bob': {'age': 30, 'country': 'UK'},
    'Charlie': {'age': 35, 'country': 'Australia'}
    }
    if request.method == 'POST':
        name = request.form['name']
        new_country = request.form['country']

        if name in users:
            users[name]['country'] = new_country
            return f"Updated profile of {name} with new country {new_country}"
        else:
            return f"User {name} not found."


@app.route('/all-user')
def all_user():
    return render_template('allusers.html', title="All Users", users=users)


@app.errorhandler(404)
def page_not_found(error):
  return render_template('404.html'), 404


if __name__ == "__main__":
    #launch the Flask dev server 
    app.run(host="0.0.0.0", port=5000)

