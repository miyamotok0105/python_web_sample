from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "hello!"

@app.get("/get1")
def get1():
    return "hello!"

# endpointはurl_forでURL一覧から探すときのキー
@app.route("/get2", methods=["GET"], endpoint="get2-endpoint")
def get2():
    return "hello!"

if __name__ == "__main__":
    # app.run()
    app.run(host="0.0.0.0", port=80, debug=True)
