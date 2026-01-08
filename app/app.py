from fastapi import FastAPI, HTTPException
from app.schemas import PostCreate, PostResponse

app= FastAPI()

text_posts = {
    1: {"title": "January", "content": "Cold winter conditions across most of India; northern regions experience fog and very low temperatures."},
    2: {"title": "February", "content": "Cool and pleasant weather, with winter slowly retreating and mild temperatures across the country."},
    3: {"title": "March", "content": "Beginning of summer; temperatures rise and days become warmer, especially in central and western India."},
    4: {"title": "April", "content": "Hot summer intensifies; many regions experience dry heat and rising temperatures."},
    5: {"title": "May", "content": "Peak summer heat with high temperatures and heatwaves, especially in northern and central India."},
    6: {"title": "June", "content": "Onset of monsoon in southern India; early rains mix with lingering summer heat in many regions."},
    7: {"title": "July", "content": "Widespread monsoon rains across India, bringing cooler temperatures and high humidity."},
    8: {"title": "August", "content": "Heavy monsoon rainfall continues, with cloudy skies and humid conditions nationwide."},
    9: {"title": "September", "content": "Monsoon begins to withdraw; rainfall decreases gradually with warm and humid weather."},
    10: {"title": "October", "content": "Post-monsoon transition; pleasant weather returns with cooler evenings, especially in the north."},
    11: {"title": "November", "content": "Mild and pleasant climate; winter begins in northern India while the south may still get some rain."},
    12: {"title": "December", "content": "Winter sets in fully; cold temperatures in the north and cool, comfortable weather elsewhere."}
}

@app.get("/posts")
def get_all_posts(limit: int = None):
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts

@app.get("/posts/{id}")
def get_post(id: int):
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found")
    return text_posts.get(id)

@app.post("/posts")
def create_post(post: PostCreate) -> PostResponse:
    new_post={"title": post.title, "content":post.content}
    text_posts[max(text_posts.keys())+1]= new_post
    return new_post