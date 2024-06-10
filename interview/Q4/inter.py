from flask import Flask, request

app = Flask(__name__)

@app.route('/contact')
def contact():
    return """
    <h2>Contact Us</h2>
    <form method="post" action="/submit">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required><br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required><br>
        <label for="message">Message:</label><br>
        <textarea id="message" name="message" rows="4" required></textarea><br>
        <button type="submit">Submit</button>
    </form>
    """

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        return f"Thank you, {name}, for your message!<br>We'll get back to you at {email}."
    else:
        return "Method not allowed."

@app.route('/user/<username>')
def user_profile(username):
    return f"Hello, {username}! This is your profile page."

if __name__ == '__main__':
    app.run(debug=True)
