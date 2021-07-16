from flask import Blueprint, jsonify, render_template, redirect, url_for
from .forms import CalculatorForm

from pprint import pprint # DELETE AFTER

routes = Blueprint("routes", __name__)

@routes.route("/", methods=["GET", "POST"])
def calculator():
    """Our ML app"""
    form = CalculatorForm()

    pprint(form.data)
    if form.validate_on_submit():
        return(jsonify(form.data))
        return redirect(url_for("success"))
    return render_template(
        "calculator.jinja2",
        form=form,
        template="form-template"
    )

@routes.route("/model", methods = ["POST"])
def predict2():
    return("hello")

def predict(data):

    # validation

    # scoring. data is identical so
    opt_score, ngr_score = opt.score(), ngr.score()

    return opt_score, ngr_score
