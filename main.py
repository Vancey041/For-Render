from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>The Good Boy Hub</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background-color: #f0f4f8;
                color: #333;
                text-align: center;
                padding: 40px 20px;
                margin: 0;
            }
            h1 {
                color: #2c3e50;
                font-size: 2.5rem;
            }
            p.subtitle {
                font-size: 1.2rem;
                color: #555;
                margin-bottom: 40px;
            }
            .dog-card {
                background: #ffffff;
                border-left: 6px solid #e74c3c;
                border-radius: 8px;
                padding: 20px 30px;
                margin: 20px auto;
                max-width: 600px;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
                text-align: left;
            }
            .dog-card h2 {
                margin-top: 0;
                color: #e74c3c;
            }
            .footer {
                margin-top: 50px;
                font-size: 0.9rem;
                color: #888;
            }
        </style>
    </head>
    <body>
        <h1>Welcome to The Good Boy Hub 🐾</h1>
        <p class="subtitle">Your text-only destination for canine appreciation!</p>
        
        <div class="dog-card">
            <h2>Did You Know?</h2>
            <p>Dogs have an incredible sense of smell. Their noses secrete a thin layer of mucous that helps them absorb scent chemicals. They then lick their noses to sample the scent through their mouth!</p>
        </div>

        <div class="dog-card">
            <h2>Breed Spotlight: Greyhound</h2>
            <p>Greyhounds are the fastest dogs on earth. They can reach speeds of up to 45 miles per hour within just six strides, making them the Ferraris of the dog world.</p>
        </div>

        <div class="dog-card">
            <h2>Canine Vocabulary</h2>
            <p><strong>Bloop:</strong> A gentle tap on the nose.<br>
            <strong>Sploot:</strong> When a dog lies on its stomach with its hind legs stretched straight back.</p>
        </div>

        <div class="footer">
            <p>Built with FastAPI and deployed on Render.</p>
        </div>
    </body>
    </html>
    """
