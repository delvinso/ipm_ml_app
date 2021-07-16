"""Form object declaration."""
from flask_wtf import FlaskForm
from wtforms import  SubmitField, IntegerField, FloatField, BooleanField, RadioField
from wtforms.validators import DataRequired, Length


class CalculatorForm(FlaskForm):
    """
    IPM Calculator

    TODO: The variable names below follow the same naming pattern as Sabrina's JMP-python code except for where illegal characters are present.
    TODO: st4_unresec
    """

    # mandatory fields
    age = IntegerField('Age', validators = [DataRequired(message = "This should be in years, eg. 18, an integer."), ])
    ecog = IntegerField('ECOG', validators = [DataRequired()])
    albumin = FloatField('Albumin', validators = [DataRequired()])
    ca_125 = IntegerField('CA-125', validators = [DataRequired()])
    brca_any = BooleanField('BRCA', default = 0)

    # surgical resectability (n = 8)

    # convert _ to '/'
    splenic_hilum = BooleanField('Splenic Hilum or Splenic Ligaments Lesion', default = 0)
    gastro_lig = BooleanField("Gastrohepatic Ligament or Porta Hepatis Lesion",  default = 0)
    retroperi_supra = BooleanField("Retroperitoneal Lymph Nodes above the Renal Hilum (inclusding supradiaphragmtic",  default = 0)
    sb_adhesions = BooleanField("Diffuse Small Bowel Adhesions or Thickening", default = 0)
    ascites = RadioField("Moderate-Severe Abdominal Ascites or CA-125 >600", choices = [(1, 'Low'), (2, 'Moderate'), (3, 'Severe')], validators =  [DataRequired()], default = 0)
    # CHECK WITH SABRINA - looks binary to me
    gb_fossa = BooleanField("Gallbladder Fossa or Liver Intersegmental Fissure Lesion", default = 0)
    lesser_sac = BooleanField("Lesser Sac Lesion >1cm", default = 0)
    sma_root = BooleanField("Root of Superior Mesenteric Artery Lesion", default = 0)

    # surgical complexity (n = 11)

    pre_tahbso = BooleanField("TAH-BSO + Omentectomy", default = 0)
    pre_plnd = BooleanField("Pelvic Lymphadenectomy ", default = 0)
    pre_palnd = BooleanField("Para-Aortic Lymphadenectomy", default = 0)
    pre_pelvic = BooleanField("Pelvic Peritoneum Stripping", default = 0)
    pre_abdo = BooleanField("Abdominal Peritoneum Stripping", default = 0)
    pre_bowel = RadioField("Bowel Resection",choices = [(0, 'Small Bowel'), (1,  'Large Bowel'), (2, 'Both')], 
                           validators =  [DataRequired()], default = 0) # should be ordinal SB, LB, Both
    pre_diaphr = BooleanField("Diaphragm Stripping or Resection", default = 0)
    pre_splen = BooleanField("Splenectomy", default = 0)
    pre_liver = BooleanField("Liver Resection", default = 0)
    pre_lar = BooleanField("Rectosigmoidectomy with Reanstomosis", default = 0)
    pre_vats = BooleanField("VATS/Intrathoracic Resection ", default = 0)

    # recaptcha = RecaptchaField()
    
    submit = SubmitField('Submit')