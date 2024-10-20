"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from .Check import check_code
import google.generativeai as genai
import os

#from rxconfig import config
from reflex.style import set_color_mode, color_mode

class State(rx.State):
    code_input: str = ''
    var_input: str = ''
    malicious_outputer: str = ''
    outputer: str = ''
    answer: str = ''
    def call_gemini(self):
        #return check_code(x)
        self.answered()
        self.malicious_outputer = self.answer

    def answered(self):
        genai.configure(api_key=os.environ["API_KEY"])
        model = genai.GenerativeModel("gemini-1.5-flash")   
        # Our chatbot has some brains now!
        prompt = "Respond with 'SAFE' if the code is safe and 'EVIL' if it is malicious if you are unsure respond with 'idk'. DO NOT RESPOND WITH ANYTHING ELSE. THOSE 3 CHOICES ONLY "
        prompt += self.code_input  # Concatenate the question to the prompt

        # Generate content without streaming
        response = model.generate_content(
            prompt,
            generation_config=genai.GenerationConfig(
                max_output_tokens=100,
                temperature=0.1,
            )
        )

        # Assuming the response contains the text directly
        """if response and hasattr(response, 'choices') and len(response.choices) > 0:
            self.answer = response.choices[0].text  # Get the generated text
        else:
            self.answer = "Error: No valid response received."
"""     
        print(response)
        if len(response.text) > 0:
            self.answer = response.text
        else:
            self.answer = "No valid response received."
        # Clear the question input.
        self.code_input = ""
        print(self.answer)
        return self.answer  # Yield to clear the frontend input after getting the answer
        
def submit_button() -> rx.Component:
    return rx.button(
        "Submit",
        color_scheme="grass",
        size = '5',
        on_click = State.call_gemini
    )
def title() ->rx.Component:
    return  rx.box(rx.container(
            rx.center(
            rx.heading(rx.text("RunTime Calculator", color_scheme = "indigo", high_contrast = True), size = '9'),
            ),),
            rx.divider(size='4',cholor_scheme="red"), width = "100%")

def input() ->rx.Component:
    #Text Box and Submit Button
    return rx.vstack(
                rx.input(placeholder = "Insert Variable Here...", 
                         radius="medium", 
                         max_length=10,
                         required=True,
                         value = State.var_input,
                         on_change = State.set_var_input,
                         ),
                rx.text_area(placeholder="Insert Code Here...", 
                             radius="full", 
                             max_length = 1000, 
                             required = True, 
                             width = "500px", 
                             height = "400px", 
                             value = State.code_input, 
                             on_change = State.set_code_input,
                             border_radius="5px"
                             ),
                submit_button(),
                align = "end",
                width ="100%"

    )
def output() ->rx.Component: 

    return rx.vstack(
            rx.text("Estimated Run Time:", size="6",),
            rx.text(State.outputer),
            rx.text("Malicious-o-Meter:", size='6'),
            rx.text(State.malicious_outputer),

            spacing='4',
            width = "50%",
    )
"""rx.box(
                State.outputer, 
                color_scheme="tomato",
                background_color="#BABABA",
                border_radius="5px",
                width = "100px",
                margin="12px",
                padding="12px","""

def dark_mode_toggle() -> rx.Component:
    return rx.segmented_control.root(
        rx.segmented_control.item(
            rx.icon(tag="monitor", size=20),
            value="system",
        ),
        rx.segmented_control.item(
            rx.icon(tag="sun", size=20),
            value="light",
        ),
        rx.segmented_control.item(
            rx.icon(tag="moon", size=20),
            value="dark",
        ),
        on_change=set_color_mode,
        variant="classic",
        radius="large",
        value=color_mode,
    )

def index():
    return rx.container(
        rx.vstack(
        title(),
        rx.hstack(
            output(),
            input(),
            width = "100%",
            height = "400px"),
        dark_mode_toggle(),
        width = "100%",
        height = "80%", 
        spacing = "70px"
        )
    )
app = rx.App()
app.add_page(index)