from flask import (
    Blueprint,
    jsonify,
    render_template,
    request,
    current_app as app,
    abort,
)
from .forms import CalculatorForm
from project import ngr, opt

routes = Blueprint("routes", __name__)


@routes.route("/", methods=["GET", "POST"])
def calculator():
    """
    Our ML app

    Luckily wtforms provides input validation
    """
    form = CalculatorForm()
    if form.validate_on_submit():

        dat = form.data.copy()
        # 999999 is the associated value with 'None' which needs to be converted.
        # This is done as SelectField coerces the choice to an int + None is not a valid input, see : https://stackoverflow.com/questions/46335763/make-a-selectfield-select-nothing-by-default
        # assume valid if we're here, except for Nones which need to be converted
        for k in dat:
            if dat[k] == 999999:
                dat[k] = None
        # app.logger.debug(predict(form.data))
        app.logger.debug(dat)
        predictions = predict(dat)
        # return(jsonify(predict(form.data)))
        return render_template(
            "calculator.jinja2",
            form=form,
            template="form-template",
            predictions=predictions,
        )
    app.logger.debug("Form Errors: {}".format(form.errors))
    return render_template("calculator.jinja2", form=form, template="form-template")


# @routes.route("/api/predict", methods=["POST"])
# def predict2():
#     data = request.json
#     return jsonify(predict(data))


def predict(data):

    """
    should there be additional input validation here?
    """

    model_vars = list(ngr.getInputMetadata().keys())
    missing_vars = [k for k in model_vars if k not in data]
    # app.logger.debug('Missing Variables: ', missing_vars)
    if len(missing_vars) > 0:
        app.logger.error('Not all form variables were found in the model metadata...please check')
        abort(500)

    relevant_d = {k: data[k] for k in list(ngr.getInputMetadata().keys()) if k in data}

    if len(relevant_d) != len(model_vars):
        app.logger.error(
            "Not all form variables were found in the model metadata...please check"
        )
        abort(500)

    app.logger.debug(relevant_d)

    # ngr model prediction occurs first as it makes use of st_4unresec. it is subsequently removed in the opt model.
    ngr_score, opt_score = (
        ngr.score(indata=relevant_d, outdata=ngr.getOutputMetadata()),
        opt.score(indata=relevant_d, outdata=opt.getOutputMetadata()),
    )

    return {
        "Optimal Cytoreduction           ": opt_score["Prob(pds_opt==1)_1"],
        "No Growth Residual Cytoreduction": ngr_score["Prob(pds_ngr==1)_1"],
    }
