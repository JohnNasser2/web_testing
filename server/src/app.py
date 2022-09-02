from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from rembg import remove
from PIL import Image
# import requests
# from io import BytesIO
import os

# import matplotlib.image as mpimg
app = Flask(__name__)
app.config['SECRET_KEY'] = 'super secret key'
app.config["UPLOAD_FOLDER"] = "static/images/"
# app.config['SESSION_TYPE'] = 'filesystem'

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=['POST', 'GET'])
def homePage():
    if request.method == "POST":
        # return render_template("index.html", title="Lebsy", staticImage="/static/images/result.jpg", loading = "yas")
        # flash("Hello John Nasser",warning)
        # if(1 == 1):
        #     return render_template("index.html", title="Lebsy", staticImage="/static/images/result.jpg", loading = "yas")
        if "download" in request.form:

            # response = requests.get("10:9000")
            # img = Image.open(BytesIO(response.content))

            return render_template("index.html", title="Lebsy", staticImage="/static/images/result.jpg", loading="notLoading")

        if 'rightRotate' in request.form:
            imageRotating = request.form['rightRotate'].replace(
                "/static/images/", "")
            colorImage = Image.open(
                app.config["UPLOAD_FOLDER"] + imageRotating)
            rotated = colorImage.rotate(-90)
            lastesFile = secure_filename(imageRotating)
            rgb_im = rotated.convert('RGB')
            rgb_im.save(os.path.join(
                app.config['UPLOAD_FOLDER'], "rotated.jpg"))
            input_path = app.config['UPLOAD_FOLDER']+"rotated.jpg"
            output_path = app.config['UPLOAD_FOLDER']+"result.jpg"
            with open(input_path, 'rb') as i:
                with open(output_path, 'wb') as o:
                    input = i.read()
                    output = remove(input)
                    o.write(output)

            return render_template("index.html", title="Lebsy", staticImage="/static/images/result.jpg", loading="notLoading")
        if 'leftRotate' in request.form:
            # john = "/John/Nasser/"

            imageRotating = request.form['leftRotate'].replace(
                "/static/images/", "")
            colorImage = Image.open(
                app.config["UPLOAD_FOLDER"] + imageRotating)
            rotated = colorImage.rotate(90)
            lastesFile = secure_filename(imageRotating)
            rgb_im = rotated.convert('RGB')
            rgb_im.save(os.path.join(
                app.config['UPLOAD_FOLDER'], "rotated.jpg"))
            input_path = app.config['UPLOAD_FOLDER']+"rotated.jpg"
            output_path = app.config['UPLOAD_FOLDER']+"result.jpg"
            with open(input_path, 'rb') as i:
                with open(output_path, 'wb') as o:
                    input = i.read()
                    output = remove(input)
                    o.write(output)

            return render_template("index.html", title="Lebsy", staticImage="/static/images/result.jpg", loading="notLoading")
        if 'crop' in request.files:
            file = request.files['crop']
            if file.filename == '':
                return render_template("index.html", title="Lebsy", staticImage="/static/images/result.jpg", loading="notLoading")

            if file and allowed_file(file.filename):
                lastesFile = secure_filename(file.filename)
                file.save(os.path.join(
                    app.config['UPLOAD_FOLDER'], lastesFile))
                input_path = app.config['UPLOAD_FOLDER']+lastesFile
                output_path = app.config['UPLOAD_FOLDER']+'result.jpg'
                with open(input_path, 'rb') as i:
                    with open(output_path, 'wb') as o:
                        input = i.read()
                        output = remove(input)
                        o.write(output)
                    return render_template("index.html", title="Lebsy", staticImage="/static/images/result.jpg", loading="notLoading")

            else:
                return render_template("index.html", title="Lebsy", staticImage="/static/images/result.jpg", loading="notLoading")
        return render_template("index.html", title="Lebsy", staticImage="/static/images/result.jpg", loading="notLoading")
    else:
        return render_template("index.html", title="Lebsy", staticImage="/static/images/result.jpg", loading="notLoading")


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
    # app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT',8080)))

# port=9000, debug=True, host="192.168.1.102"
# leftRotate     ,   rightRotate   ,   download    ,    crop
# lebsy-6577a 


