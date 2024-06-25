from flask import Flask

app = Flask(__name__)
# print: THIS IS A CONTACT LIST PAGE

my_contacts = [{"name": "Ran", "age": 44},
              {"name": "Itzik", "age": 21}]


@app.route("/")
# http://127.0.0.1:9000 works
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/contacts") 
# http://127.0.0.1:9000/contacts works 
def contacts_list():
   final_html_str = ''
   for contact in my_contacts:
       final_html_str += f"{contact['name']} - {contact['age']}<br>"
   return final_html_str

@app.route("/single contact/<int:index>")
# http://127.0.0.1:9000/single%20contact/1 works
def single_contact(index):
   return f"<h1>Single Contact Page </h1><h2>{my_contacts[index]['name']}"

@app.route("/add contact")
# http://127.0.0.1:9000/add%20contact works
def add_contact():
   return f"<h1>add Contact Page </h1><h2>"


if __name__ == "__main__":
    app.run(debug=True, port=9000)
