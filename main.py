from transformers import pipeline
import uvicorn
from fastapi import FastAPI


classifier = pipeline("zero-shot-classification",
                      model="facebook/bart-large-mnli")
app = FastAPI()
candidate_tags = ["diabetes", "overweight", "healthy", "active", "athlete"]

@app.get("/")
async def classify_content(content: str) -> dict:
    scored_classes = classifier(content, candidate_tags)
    return {"scores": dict(zip(scored_classes["labels"], scored_classes["scores"]))}

if __name__ == "__main__":
    uvicorn.run(app, host = "0.0.0.0", port = 8000)