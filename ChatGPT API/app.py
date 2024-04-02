from flask import Flask, render_template, request
import openai
import os


app = Flask(__name__)

# Set up OpenAI API credentials
openai.api_key = "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" 
# openai.api_key = os.environ.get("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")


# Define the default route to return the index.html file
@app.route("/")
def index():
    return render_template("/ChatGPT API/templates/index.html")

# Define the /api route to handle POST requests
@app.route("/api", methods=["POST"])
def api():
    # Get the message from the POST request
    message = request.form.get("message")
    # Send the message to OpenAI's API and receive the response
    print(message)
    
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-0613",
    messages=[
        {"role": "user", "content": message}
    ]
    )

    reponse = completion.choices[0].message.content
    
    if completion.choices[0].message!=None:
        return reponse

    else :
        return 'Failed to Generate response!'
    
    print (reponse)


if __name__=='__main__':
    app.run()

