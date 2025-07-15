from flask import Flask, request, render_template_string
from email_assistant import summarize_email, generate_reply

app = Flask(__name__)

HTML = '''
    <h2>Email Reply Assistant</h2>
    <form method="POST">
        <textarea name="email_text" rows="10" cols="60" placeholder="Paste the received email here..."></textarea><br>
        <button type="submit" name="action" value="summarize">Summarize</button>
        <button type="submit" name="action" value="reply">Generate Reply</button>
    </form>
    {% if result %}
        <h3>Result:</h3>
        <pre>{{ result }}</pre>
    {% endif %}
'''

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        email_text = request.form["email_text"]
        action = request.form["action"]
        if action == "summarize":
            result = summarize_email(email_text)
        elif action == "reply":
            result = generate_reply(email_text)
    return render_template_string(HTML, result=result)

if __name__ == "__main__":
    app.run(debug=True)
