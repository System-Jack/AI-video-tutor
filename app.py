from flask import Flask, render_template, request, jsonify
from groq import Groq
from dotenv import load_dotenv

app = Flask(
    __name__,
    static_folder="templates/components",
    static_url_path="/components",
)

load_dotenv()
client = Groq()


@app.get("/")
def index():
    return render_template("index.html")

@app.post("/ask")
def ask():
    question = request.get_json()["question"]
    messages = [
        {
            "role": "system",
            "content": (
                "Whatever question you are about to answer, you will answer by explaining on a whiteboard and speaking, like a tutor.\n"
                "Instead of giving off answers as text, I want you to generate JSON instructions on drawing.\n\n"
                "Each JSON object contains two variables: \"points\", which is an array of coordinates to connect, and \"speed\", which is the drawing speed in pixels per second.\n"
                "(0, 0) is top left corner; X increases rightward and Y increases downward.\n"
                "The first coordinate point in the list is simply gone to, drawing begins FROM that point only and connects the remaining points and that point together.\n"
                "Coordinates are in the form of [X, Y].\n"
                "Speed should be STRICTLY positive.\n\n"
                "You should output an array of JSON objects.\n"
                "You MUST return valid JSON, which means the following are PROHIBITED: markdown, code fences, and explanatory text outside the JSON array."
            )
        },
        {
            "role": "user",
            "content": question
        }
    ]
    completion = client.chat.completions.create(model="openai/gpt-oss-120b", messages=messages)
    return jsonify({"answer": completion.choices[0].message.content})
