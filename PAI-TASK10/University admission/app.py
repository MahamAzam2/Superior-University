from flask import Flask, render_template, request

app = Flask(__name__)


def get_response(user_input):
    user_input = user_input.lower()
    if "admission" in user_input:
        return "The admission process includes filling the form online and submitting required documents."
    elif "eligibility" in user_input:
        return "Eligibility: Minimum 60% in intermediate or equivalent."
    elif "documents" in user_input:
        return "You need to submit CNIC, academic transcripts, and passport-sized photos."
    elif "fee" in user_input:
        return "The fee structure varies by department. On average, it's around PKR 100,000 per semester."
    elif "contact" in user_input:
        return "You can contact the admission office at admissions@university.edu.pk"
    elif "deadline" in user_input or "last date" in user_input:
        return "The last date to apply is 30th June 2025."
    else:
        return "Sorry, I didn't understand. Please ask about admissions, documents, eligibility, etc."

@app.route("/", methods=["GET", "POST"])
def index():
    user_msg = ""
    bot_msg = ""
    if request.method == "POST":
        user_msg = request.form["msg"]
        bot_msg = get_response(user_msg)
    return render_template("index.html", user_msg=user_msg, bot_msg=bot_msg)


if __name__ == "__main__":
    app.run(debug=True)

