from flask import Flask, jsonify
app=Flask(__name__)
@app.route("/even/<int:n>")
def even(n):

    if n%2==0:
        result={
            "number": n,
            "Even": True,
            "Ans": "yes"
        }
    else:
        result={
            "number": n,
            "Even": False,
            "Ans": "no"
        }
    
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)