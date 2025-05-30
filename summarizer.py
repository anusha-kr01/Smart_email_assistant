from transformers import pipeline

# Initialize the Hugging Face summarization pipeline
try:
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
except Exception as e:
    print(f"⚠️ Failed to load summarization model: {e}")
    summarizer = None

def summarize_text(text):
    if not summarizer:
        return "Summarizer model not available."

    if not text or len(text.strip().split()) < 30:
        return "⚠️ Text too short to summarize."

    try:
        result = summarizer(text, max_length=150, min_length=30, do_sample=False)
        return result[0]['summary_text']
    except Exception as e:
        return f"❌ Error during summarization: {e}"
