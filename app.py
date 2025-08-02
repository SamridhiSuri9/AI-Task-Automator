import gradio as gr
from search import search_articles
from summarize import summarize_text
from markdown_gen import convert_to_markdown
from ppt_generator import markdown_to_ppt
import os
import time

def generate_presentation(topic):
    if not topic.strip():
        return "Please enter a valid topic.", None

    articles = search_articles(topic, num_results=3)
    if not articles:
        return "No content found online. Try a different topic.", None

    full_text = "\n".join(articles)
    summary = summarize_text(full_text)
    markdown = convert_to_markdown(topic, summary)

    output_path = os.path.join("output", f"{topic.replace(' ', '_')}_{int(time.time())}.pptx")
    markdown_to_ppt(markdown, output_path)

    return "✅ Presentation generated successfully!", output_path

# Gradio UI
iface = gr.Interface(
    fn=generate_presentation,
    inputs=gr.Textbox(label="Enter Homework Topic", placeholder="e.g., Solar Energy for Beginners"),
    outputs=[
        gr.Textbox(label="Status"),
        gr.File(label="Download PPT")
    ],
    title="🎓 AI Task Automator for Students",
    description="Enter a topic and generate a summarized PowerPoint presentation automatically using AI.",
    theme="soft",
    allow_flagging="never" 
)

if __name__ == "__main__":
    os.makedirs("output", exist_ok=True)
    iface.launch()
