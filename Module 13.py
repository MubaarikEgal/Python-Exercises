import json
from flask import Flask, Response

app = Flask(__name__)


def is_prime(n: int) -> bool:

    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>Prime Number checker</title>
        </head>
        <body>
            <h1>Prime Number Checker</h1>
            <p>
                <a href="/prime_number/31">
                    Click here to check if 31 is a prime number
                </a>
            </p>
        </body>
    </html>
    """





@app.route("/prime_number/<number>")
def prime_number(number):

    try:
        n = int(number)
    except ValueError:
        response = {
            "status": 400,
            "message": "Invalid number. Please provide an integer like /prime_number/31"
        }
        return Response(
            response=json.dumps(response),
            status=400,
            mimetype="application/json"
        )

    response = {
        "Number": n,
        "isPrime": is_prime(n)
    }

    return response


@app.errorhandler(404)
def page_not_found(_error):
    response = {
        "status": 404,
        "message": "Invalid endpoint"
    }
    return Response(
        response=json.dumps(response),
        status=404,
        mimetype="application/json"
    )


if __name__ == "__main__":
    app.run(use_reloader=True, host="127.0.0.1", port=5000)
