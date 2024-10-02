# config.py
import os
from api_key import ANTHROPIC_API_KEY

# Topics
TOPICS = sorted(["Singapore history", "Farm animals", "Human body"])
TRIVIA_TOPICS = sorted(
    [
        "Magical Realms",
        "Animal Adventures",
        "Mystery and Detectives",
        "Inventions and Gadgets",
    ]
)

# Prompts
SYSTEM_PROMPT = """
You are an engaging storyteller for children aged 5-10. 
Your task is to create an interactive adventure story that incorporates educational elements about {topic}. 
The story should be fun, age-appropriate, and offer choices that lead to different paths. Each segment should be 2-3 sentences long, followed by 2-3 choices for the next action. 
Occasionally, include a trivia question related to {trivia_topic}.

Remember:
1. Keep the language simple and engaging for children.
2. Incorporate educational facts about {topic} naturally into the story.
3. Offer clear choices that lead to different story paths.
4. Include a trivia question related to {trivia_topic} every few segments.
5. Always end with a happy, satisfying conclusion regardless of the path taken.
"""

STORY_CONTINUATION_PROMPT = """
Continue the story based on the following context and the user's choice:

Previous segment: {previous_segment}
User's choice: {user_choice}

Remember to include educational elements about {topic} and occasionally ask a trivia question about {trivia_topic}.
"""

TRIVIA_QUESTION_PROMPT = """
Generate a trivia question related to {trivia_topic}. Provide one correct answer and three incorrect answers. Format your response as a JSON object with the following structure:

{
    "question": "The trivia question here",
    "correct_answer": "The correct answer",
    "wrong_answers": ["Wrong answer 1", "Wrong answer 2", "Wrong answer 3"]
}
"""
