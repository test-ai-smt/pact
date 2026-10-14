"""PACT web app: HTTP API around greet()."""
from flask import Flask, jsonify, request

from src.pact_app import GREETINGS, greet

MAX_NAME_LEN = 64


def create_app() -> Flask:
    app = Flask(__name__)
    app.json.ensure_ascii = False  # return Arabic as UTF-8, not \u escapes

    @app.get("/health")
    def health():
        return jsonify(status="ok")

    @app.get("/languages")
    def languages():
        return jsonify(languages=sorted(GREETINGS))

    @app.get("/greet")
    def greet_endpoint():
        name = request.args.get("name", "").strip()
        lang = request.args.get("lang", "en")
        if not name or len(name) > MAX_NAME_LEN:
            return jsonify(error=f"name is required (1-{MAX_NAME_LEN} chars)"), 400
        try:
            return jsonify(message=greet(name, lang), lang=lang)
        except ValueError as exc:
            return jsonify(error=str(exc)), 400

    @app.after_request
    def security_headers(resp):
        resp.headers["X-Content-Type-Options"] = "nosniff"
        resp.headers["Content-Security-Policy"] = "default-src 'none'"
        resp.headers["Cache-Control"] = "no-store"
        return resp

    return app


if __name__ == "__main__":
    # Local dev only: loopback, no debugger. Use a WSGI server (gunicorn/waitress) in production.
    create_app().run(host="127.0.0.1", port=5000, debug=False)
