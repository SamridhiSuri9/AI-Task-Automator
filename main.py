from search import search_articles
from summarize import summarize_text
from markdown_gen import convert_to_markdown
from ppt_generator import markdown_to_ppt
import os

def main():
    topic = input("Enter a homework topic: ")
    
    print("\n🔍 Searching online...")
    articles = search_articles(topic, num_results=3)
    
    print("\n🧠 Summarizing content...")
    full_text = "\n".join(articles)
    summary = summarize_text(full_text)
    
    print("\n📝 Converting to Markdown...")
    markdown = convert_to_markdown(topic, summary)
    
    print("\n📊 Creating PowerPoint...")
    output_path = os.path.join("output", f"{topic.replace(' ', '_')}.pptx")
    markdown_to_ppt(markdown, output_path)
    
    print(f"\n✅ Presentation saved to {output_path}")

if __name__ == "__main__":
    os.makedirs("output", exist_ok=True)
    main()
