from fasthtml.common import *

# In a real implementation, you would import and use the actual LLM here
# For this example, we'll use a simple function to simulate LLM responses


def generate_story_segment(context, is_correct=None):
    if context == "start":
        return Div(
            P(
                "You find yourself at the entrance of a mysterious jungle. The air is thick with the scent of exotic flowers and the sounds of unknown creatures."
            ),
            P("What would you like to do?"),
            Div(
                Button("Enter the jungle", hx_get="/choice/enter_jungle"),
                Button("Look for a guide", hx_get="/choice/find_guide"),
                Button("Check your backpack", hx_get="/choice/check_backpack"),
            ),
        )
    elif context == "enter_jungle":
        return Div(
            P(
                "As you step into the lush greenery, you notice a strange plant with glowing fruits."
            ),
            P("What's your next move?"),
            Div(
                Button("Examine the plant", hx_get="/question"),
                Button("Keep walking", hx_get="/choice/keep_walking"),
                Button("Take a fruit", hx_get="/choice/take_fruit"),
            ),
        )
    elif context == "question_result":
        if is_correct:
            return Div(
                P(
                    "Your knowledge serves you well! As if by magic, a hidden path appears before you."
                ),
                P("What would you like to do next?"),
                Div(
                    Button("Follow the path", hx_get="/choice/follow_path"),
                    Button("Stay where you are", hx_get="/choice/stay_put"),
                    Button("Call out for help", hx_get="/choice/call_for_help"),
                ),
            )
        else:
            return Div(
                P(
                    "Oops! That wasn't quite right, but don't worry. Every mistake is a chance to learn something new!"
                ),
                P(
                    "As you ponder the correct answer, you notice something interesting nearby."
                ),
                Div(
                    Button(
                        "Investigate the interesting thing",
                        hx_get="/choice/investigate",
                    ),
                    Button("Rest for a while", hx_get="/choice/rest"),
                    Button("Try to retrace your steps", hx_get="/choice/retrace"),
                ),
            )
    else:
        return Div(
            P("Your adventure comes to an exciting conclusion!"),
            Button("Finish the adventure", hx_get="/end"),
        )
