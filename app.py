from flask import Flask, jsonify, render_template, redirect, request
from utils import *

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def temp1():
    return redirect("/process_resume")

@app.route("/process_resume", methods = ["GET", "POST"])
def temp2():
    if(request.method == "POST"):
        #process resume and simply return json
        file = request.files['doc']
        option = request.form['document_type']

        if(option == "pdf"):
            text = get_pdf_text(file)
        elif(option == "docx"):
            text = get_docx_text(file)
        else:
            text = file.read().decode("utf-8")

        query_res = query_response(text)
        return jsonify(json.loads(query_res))               #converts valid JSON string to JSON

    else:
        return render_template("resume_upload.html")

if(__name__ == "__main__"):
    app.run(debug = True)