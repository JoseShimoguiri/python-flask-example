from flask import Flask
app = Flask(__name__)

index_add_counter = 0

@app.route("/count")
def test():
    global index_add_counter 
    index_add_counter += 1
    return str(index_add_counter)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
