# database.py
import sqlite3


def setup_database():
    conn = sqlite3.connect("adventure.db")
    c = conn.cursor()

    # Create table for learning questions
    c.execute("""CREATE TABLE IF NOT EXISTS learning_questions
                 (id INTEGER PRIMARY KEY, topic TEXT, question TEXT, answer TEXT)""")

    # Insert sample questions
    questions = [
        ("Singapore history", "What year did Singapore gain independence?", "1965"),
        (
            "Singapore history",
            "Who was the first Prime Minister of Singapore?",
            "Lee Kuan Yew",
        ),
        (
            "Singapore history",
            "What is the name of Singapore's national flower?",
            "Vanda Miss Joaquim",
        ),
        ("Farm animals", "What animal gives us milk?", "Cow"),
        ("Farm animals", "What do you call a baby sheep?", "Lamb"),
        ("Farm animals", "Which farm animal lays eggs?", "Chicken"),
        ("Human body", "How many bones are in the human body?", "206"),
        ("Human body", "What is the largest organ in the human body?", "Skin"),
        ("Human body", "What organ pumps blood throughout your body?", "Heart"),
    ]

    c.executemany(
        "INSERT OR REPLACE INTO learning_questions (topic, question, answer) VALUES (?, ?, ?)",
        questions,
    )

    conn.commit()
    conn.close()


def get_questions(topic):
    conn = sqlite3.connect("adventure.db")
    c = conn.cursor()
    c.execute(
        "SELECT question, answer FROM learning_questions WHERE topic = ?", (topic,)
    )
    questions = c.fetchall()
    conn.close()
    return questions


if __name__ == "__main__":
    setup_database()
