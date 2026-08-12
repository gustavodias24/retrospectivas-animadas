from flask import Flask, render_template


app = Flask(__name__)

CHECKOUT_URL = (
    "https://pay.hotmart.com/H104386802Y?checkoutMode=10&bid=1786541078179"
)
YOUTUBE_VIDEO_ID = "MK6VgU0MLDY"


@app.get("/")
def home():
    return render_template(
        "index.html",
        checkout_url=CHECKOUT_URL,
        youtube_video_id=YOUTUBE_VIDEO_ID,
    )


@app.get("/health")
def health():
    return {"status": "ok"}


@app.after_request
def add_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "SAMEORIGIN"
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    response.headers["Permissions-Policy"] = (
        "camera=(), microphone=(), geolocation=(), payment=()"
    )
    response.headers["Content-Security-Policy"] = "; ".join(
        [
            "default-src 'self'",
            "img-src 'self' data:",
            "style-src 'self'",
            "script-src 'self'",
            "frame-src https://www.youtube-nocookie.com https://www.youtube.com",
            "connect-src 'self'",
            "font-src 'self'",
            "base-uri 'self'",
            "form-action 'self' https://pay.hotmart.com",
            "frame-ancestors 'self'",
        ]
    )
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
