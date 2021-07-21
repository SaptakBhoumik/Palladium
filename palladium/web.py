from flask import Flask, render_template, request, redirect, flash,url_for
import os
import ctscan_cnn,xray_cnn
from werkzeug.utils import secure_filename


web = Flask(__name__)
web.secret_key = "#$%#$%^%^BFGBFGhkjdfhjhjdiufiuwuhuhsushkjhskjfnvcxbjsuioiopehkh67762784367667764798398290898827frchjnhjchjcvchhfhhfghfghgjgkhl;lh'm,/.;;;ikjpppoiiuiuyuydsuudshjhjhhjhhgjhjhjhjhjhjhjhjhjhjhjjhjhjBSFGNSGJTNADFHH@#%$%#T#FFWF$^F@$F#$FW"

UPLOAD_FOLDER = 'static/uploads/'
web.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@web.route("/lungs")
def lungs():
    return render_template("lungs.html")

@web.route("/lungs_xray",methods=["GET"])
def lungs_xray():
    if request.method == "GET":
        return render_template("lung_xray.html")

@web.route("/lungs_ctscan",methods=["GET"])
def lungs_ctscan():
    if request.method == "GET":
        return render_template("lung_ctscan.html")


@web.route('/lungs_ctscan', methods=['POST'])
def upload__ctscan_image():
	file = request.files['file']
	filename = secure_filename(file.filename)
	file.save(os.path.join(web.config['UPLOAD_FOLDER'], filename))
	try:
		report=ctscan_cnn.prediction(f"./static/uploads/{filename}")
		if report.lower() =="normal":
			report="Congratulations your lungs are in normal condition"
			symptoms=""
		elif report.lower()=="covid19":
			report="Looks like you are infected by covid 19. You should go and see a doctor"
			symptoms="Some of the symptoms of covid19 are fever, dry cough, tiredness, loss of taste or smell,difficulty breathing or shortness of breath and headache"
	except:
		report="Unable to process image"
		symptoms=""

	return render_template('upload.html', filename=filename,report=report,symptoms=symptoms)

@web.route('/lungs_xray', methods=['POST'])
def upload_xray_image():
	file = request.files['file']
	filename = secure_filename(file.filename)
	file.save(os.path.join(web.config['UPLOAD_FOLDER'], filename))
	try:
		report=xray_cnn.prediction(f"./static/uploads/{filename}")
		if report.lower() =="normal":
			report="Congratulations your lungs are in normal condition"
			symptoms=""
		elif report.lower()=="covid19":
			report="Looks like you are infected by covid 19. You should go and see a doctor"
			symptoms="Some of the symptoms of covid19 are fever, dry cough, tiredness, loss of taste or smell,difficulty breathing or shortness of breath and headache"
		elif report.lower()=="pneumonia":
			report="Looks like you are infected by pneumonia. You should go and see a doctor"
			symptoms="Some of the symptoms of pneumonia are cough, which may produce greenish, yellow or even bloody mucus, fever, shortness of breath rapid, shallow breathing, sharp or stabbing chest pain that gets worse when you breathe deeply or cough, loss of appetite, low energy, and fatigue."           
	except:
		report="Unable to process image"
		symptoms=""

	return render_template('upload.html', filename=filename,report=report,symptoms=symptoms)

	
	       

@web.route('/display/<filename>')
def display_image(filename):
	return redirect(url_for('static', filename='uploads/' + filename), code=301)


