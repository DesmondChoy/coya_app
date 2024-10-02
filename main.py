# main.py
from fasthtml.common import *
from anthropic import Anthropic
from api_key import ANTHROPIC_API_KEY
from database import get_questions, setup_database
import random

# Setup the database
setup_database()

# Initialize Anthropic client
client = Anthropic(api_key=ANTHROPIC_API_KEY)

# FastHTML app setup
app, rt = fast_app()


@rt("/")
def home():
    return Titled(
        "Choose Your Own Adventure",
        Form(
            H2("Choose your adventure settings:"),
            Label("Trivia Topic:"),
            Select(id="trivia_topic", name="trivia_topic")(
                Option("Magical Realms", value="Magical Realms"),
                Option("Animal Adventures", value="Animal Adventures"),
                Option("Mystery and Detectives", value="Mystery and Detectives"),
                Option("Inventions and Gadgets", value="Inventions and Gadgets"),
            ),
            Label("Learning Topic:"),
            Select(id="learning_topic", name="learning_topic")(
                Option("Singapore history", value="Singapore history"),
                Option("Farm animals", value="Farm animals"),
                Option("Human body", value="Human body"),
            ),
            Button("Start Adventure", type="submit"),
            hx_post="/start_adventure",
            hx_target="#content",
        ),
        Div(id="content"),
        Script("""
        document.querySelector('form').addEventListener('submit', function(e) {
            console.log('Form submitted');
        });
        """),
    )


@rt("/start_adventure")
def start_adventure(trivia_topic: str, learning_topic: str, req):
    try:
        print(
            f"Received request: trivia_topic={trivia_topic}, learning_topic={learning_topic}"
        )

        req.session["trivia_topic"] = trivia_topic
        req.session["learning_topic"] = learning_topic
        req.session["questions"] = get_questions(learning_topic)
        req.session["story"] = []
        req.session["decision_count"] = 0
        req.session["question_count"] = 0

        prompt = f"Create a short introduction for a children's adventure story about {trivia_topic}. The story should be exciting and end with a choice for the child to make."

        response = client.messages.create(
            model="claude-3-5-sonnet-20240620",
            max_tokens=300,
            messages=[{"role": "user", "content": prompt}],
        )
        story_start = response.content[0].text
        req.session["story"].append(story_start)

        print("Story generated successfully")

        return adventure(req)
    except Exception as e:
        print(f"Error in /start_adventure: {str(e)}")
        return P(f"An error occurred: {str(e)}")


@rt("/adventure")
def adventure(req):
    try:
        if "decision_count" not in req.session or "question_count" not in req.session:
            return RedirectResponse("/", status_code=303)

        if req.session["decision_count"] >= 5 and req.session["question_count"] >= 3:
            return Div(
                H2("Congratulations! You've completed your adventure!"),
                P("Here's a summary of your journey:"),
                Ul(*[Li(step) for step in req.session.get("story", [])]),
                A("Start a New Adventure", href="/", hx_get="/"),
            )

        current_story = (
            req.session.get("story", [])[-1]
            if req.session.get("story")
            else "Your adventure begins..."
        )

        if req.session["question_count"] < 3 and random.choice([True, False]):
            questions = req.session.get("questions", [])
            if not questions:
                return RedirectResponse("/", status_code=303)

            question, answer = questions[req.session["question_count"]]
            req.session["question_count"] += 1

            return Div(
                P(current_story),
                H3("Answer this question to continue your adventure:"),
                P(question),
                Form(
                    Input(type="text", name="answer", placeholder="Your answer"),
                    Input(type="hidden", name="correct_answer", value=answer),
                    Button("Submit", type="submit"),
                    hx_post="/check_answer",
                    hx_target="#content",
                ),
            )
        else:
            req.session["decision_count"] += 1

            return Div(
                P(current_story),
                H3("What do you want to do?"),
                Form(
                    Button("Option A", name="choice", value="A", type="submit"),
                    Button("Option B", name="choice", value="B", type="submit"),
                    hx_post="/make_choice",
                    hx_target="#content",
                ),
            )
    except Exception as e:
        print(f"Error in /adventure: {str(e)}")
        return P("An error occurred. Please try again.")


@rt("/check_answer")
def check_answer(answer: str, correct_answer: str, req):
    is_correct = answer.lower() == correct_answer.lower()

    prompt = f"Continue the story about {req.session['trivia_topic']}. The child just {'correctly' if is_correct else 'incorrectly'} answered a question about {req.session['learning_topic']}. Make the story reflect this outcome, but keep it positive and encouraging. End with a new choice for the child."

    try:
        response = client.messages.create(
            model="claude-3-5-sonnet-20240620",
            max_tokens=300,
            messages=[{"role": "user", "content": prompt}],
        )
        story_continuation = response.content[0].text
        req.session["story"].append(story_continuation)
    except Exception as e:
        print(f"Error calling Claude: {e}")
        story_continuation = "The adventure continued..."
        req.session["story"].append(story_continuation)

    return adventure(req)


@rt("/make_choice")
def make_choice(choice: str, req):
    prompt = f"Continue the story about {req.session['trivia_topic']}. The child chose option {choice}. Develop the story based on this choice and end with a new situation or question for the child."

    try:
        response = client.messages.create(
            model="claude-3-5-sonnet-20240620",
            max_tokens=300,
            messages=[{"role": "user", "content": prompt}],
        )
        story_continuation = response.content[0].text
        req.session["story"].append(story_continuation)
    except Exception as e:
        print(f"Error calling Claude: {e}")
        story_continuation = "The adventure took an unexpected turn..."
        req.session["story"].append(story_continuation)

    return adventure(req)


serve()
