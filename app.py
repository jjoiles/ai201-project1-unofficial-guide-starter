import gradio as gr

from generate import generate_answer


def ask_housing_guide(question):
    if not question.strip():
        return "Please enter a housing question.", ""

    answer, sources = generate_answer(question)

    source_text = "\n".join(f"- {source}" for source in sources)

    return answer, source_text


with gr.Blocks(title="Howard University Housing Guide") as demo:
    gr.Markdown(
        """
        # Howard University Housing Guide
        Ask questions about Howard University housing and off-campus housing.
        Answers are generated using the housing documents in this project.
        """
    )

    question_input = gr.Textbox(
        label="Ask a housing question",
        placeholder="Example: What should students consider when looking for off-campus housing?"
    )

    submit_button = gr.Button("Ask")

    answer_output = gr.Textbox(
        label="Answer",
        lines=8
    )

    sources_output = gr.Textbox(
        label="Sources",
        lines=4
    )

    submit_button.click(
        fn=ask_housing_guide,
        inputs=question_input,
        outputs=[answer_output, sources_output]
    )


if __name__ == "__main__":
    demo.launch()