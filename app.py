# הוסיפו טמפלייט לדף איש קשר בודד. 

# תכניסו בדפים - bootstrap

# הוסיפו דף שמראה favorite contacts, 
# contact הוסיפו לכל boolean is_favorite 
# במידה והוא true הראו את ה-contact
# השתמשו ב-   ….. {% for … %} {% if %} ….
# (קראו את אנשי הקשר מ-json בתחילת התוכנית)
# https://docs.google.com/presentation/d/19BG6nZu9NuCUwFezrRLWIgUll0uzOvyn-0G-GZTETOI/edit#slide=id.g2e7121aab36_0_125
# page 78

# https://github.com/ranerlich7/flask_contacts



from flask import Flask,render_template

app = Flask(__name__)
# print: THIS IS A CONTACT LIST PAGE

# my_contacts = [
#     {"name": "Ran", "age": 44, "email": "admin@", "phone": 6546895865, "fav":True},
#     {"name": "aviad", "age": 21, "email": "admin@", "phone": 6546895865, "fav":False},
#     {"name": "tal", "age": 25, "email": "admin@", "phone": 6546895865, "fav":False},
# ]


@app.route("/")
# http://127.0.0.1:9000 works
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/contacts")
# http://127.0.0.1:9000/contacts works
def contact_list():
    return render_template('contacts_list.html', contacts = my_contacts)
    # final_html_str = ""
    # for contact in my_contacts:
    #     final_html_str += f"<li>{contact['name']} - {contact['age']} - {contact['email']} - {contact['phone']}</li>"
    # return final_html_str

@app.route("/fav contacts")
# http://127.0.0.1:9000//fav%20contacts
def fav_contact_list():
    return render_template('fav_list.html', contacts = my_contacts)


@app.route("/single contact/<int:index>")
# http://127.0.0.1:9000/single%20contact/1 works
def single_contact(index):
    return f"<h1>Single Contact Page </h1><li>the user is {my_contacts[index]['name']} the age is {my_contacts[index]['age']} the email is {my_contacts[index]['email']} the phone is {my_contacts[index]['phone']}</li>"
# return f"user is {my_contacts[index]["name"]} - {my_contacts[index]["phone"]}"


@app.route("/add contact")
# http://127.0.0.1:9000/add%20contact
# return "please add a contact"
def add_contact():
    name = input("name?")
    age = input("age?")
    email = input("email?")
    phone = input("phone?")
    new_contact = {"name": name, "age": age, "email": email, "phone": phone}
    my_contacts.append(new_contact)
    return f"<h1>add Contact Page </h1><h2>the user is {my_contacts[len(my_contacts)-1]['name']}, age {my_contacts[len(my_contacts)-1]['age']}, email {my_contacts[len(my_contacts)-1]['email']}, phone number {my_contacts[len(my_contacts)-1]['phone']}</h2>"


@app.route("/write name/<username>")
# http://127.0.0.1:9000/write%20name/ran works
def write_name(username):
    return f"<h1>the name is {username} </h1><h2>"


if __name__ == "__main__":
    app.run(debug=True, port=9000)
