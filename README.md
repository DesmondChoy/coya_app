# Choose Your Own Adventure: Learn & Play

## Description

This interactive web application combines the excitement of a "Choose Your Own Adventure" story with educational content, designed for children aged 5-10. The app uses AI-generated storytelling to create unique adventures based on the child's choices, while seamlessly integrating educational questions on selected topics.

## Features

- Dynamic story generation using Claude AI (Anthropic's language model)
- Interactive storytelling with user choices affecting the narrative
- Educational questions integrated into the adventure
- Multiple-choice questions from a pre-defined database
- Real-time story streaming for an engaging user experience
- Simple and intuitive user interface

## Technologies Used

- Python
- FastHTML (next-generation web framework)
- Anthropic's Claude API
- SQLite for database management
- HTMX for dynamic content updates

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/DesmondChoy/coya_app.git
   cd choose-your-own-adventure
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv .venv
   source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install python-fasthtml anthropic sqlite3
   ```

4. Set up your Anthropic API key:
   Create a file named `api_key.py` in the project root and add your API key:
   ```python
   ANTHROPIC_API_KEY = "your_api_key_here"
   ```

5. Initialize the database:
   ```
   python database.py
   ```

## Running the Application

1. Start the server:
   ```
   python main.py
   ```

2. Open a web browser and navigate to `http://localhost:5001`

## How to Play

1. Select a Trivia Topic and a Learning Topic from the dropdown menus.
2. Click "Start Adventure" to begin your journey.
3. Read the story and make choices to progress through the adventure.
4. Answer educational questions when prompted.
5. Enjoy a unique story experience every time you play!

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Anthropic for providing the Claude AI API
- FastHTML developers for the web framework
- All contributors and testers who helped shape this project
