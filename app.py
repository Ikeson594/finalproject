from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("main.html")


@app.route("/excitement", methods=['get'])
def excitement():
    t = request.values.get("t")
    t = t.upper() + "!!!"
    return render_template("excitement.html", t=t)


@app.route("/CaseCheck", methods = ['get'])
def case():
    string = request.values.get("t")
    debug = True
    while debug:
        if string[-1] == " ":
            string = string[:-1]
        else:            debug = False
    string = string.lower()

    capitalise = True

    li = list(string.split(" "))

    for a in range(0, len(li)):
        if capitalise:
            li[a] = li[a][0].upper() + li[a][1:]
            capitalise = False
        if li[a][-1] == "." or li[a][-1] == "!" or li[a][-1] == "?":
            capitalise = True

    string = ""
    for a in range(0, len(li)):
        string = string + li[a] + " "

    return render_template("CaseCheck.html", string=string)


@app.route("/CamelCase", methods = ['get'])
def CamelCase():
    string = request.values.get("t")
    debug = True
    while debug:
        if string[-1] == " ":
            string = string[:-1]
        else:
            debug = False
    string = string.lower()
    li = list(string.split(" "))

    for a in range(0, len(li)):
        li[a] = li[a][0].upper() + li[a][1:]

    string = ""
    for a in range(0, len(li)):
        string = string + li[a]
    return render_template("CamelCase.html", string=string)


@app.route("/sarcasm", methods = ['get'])
def sarcasm():
    string = request.values.get("t")
    sarcastic = ""
    count = 1
    for a in string:
        sarcastic = sarcastic + str(a) * count
        count += 1
    return render_template("sarcasm.html", sarcastic = sarcastic)


if __name__ == '__main__':
    app.run()
