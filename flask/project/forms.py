from flask_wtf import FlaskForm
from wtforms import (
    SubmitField,
    IntegerField,
    FloatField,
    BooleanField,
    RadioField,
    SelectField,
)
from wtforms.validators import DataRequired


class CalculatorForm(FlaskForm):
    """
    IPM Calculator

    The form names here match the input metadata of the ngr.py and opt.py model scripts as the dictionary keys have been appropriately renamed.
    This allows for the form data to be directly passed into the scoring functions of the aforementioned scripts.
    """

    # mandatory fields
    age = IntegerField(
        "Age (years)",
        validators=[
            DataRequired(message="This should be in years, eg. 18, an integer."),
        ],
    )
    ecog = IntegerField("ECOG", validators=[DataRequired()])
    alb = FloatField("Albumin", validators=[DataRequired()])
    ca_125 = IntegerField("CA-125", validators=[DataRequired()])
    brca = SelectField(
        "BRCA1/2 Mutation (Germline or Somatic)",
        choices=[(999999, "Unk"), (0, "BRCA1"), (1, "BRCA2")],
        # validators=[DataRequired()],
        default=999999,
        coerce=int,
    )

    # surgical resectability (n = 8)

    splenic_hilum = BooleanField("Splenic Hilum or Splenic Ligaments Lesion", default=0)
    gastrohepatic_lig = BooleanField(
        "Gastrohepatic Ligament or Porta Hepatis Lesion", default=0
    )
    retroperitoneal_suprarenal_ln = BooleanField(
        "Retroperitoneal Lymph Nodes above the Renal Hilum", default=0
    )
    sb_adhesions = BooleanField(
        "Diffuse Small Bowel Adhesions or Thickening", default=0
    )
    ascites = RadioField(
        "Moderate-Severe Abdominal Ascites or CA-125 >600",
        choices=[(1, "Low"), (2, "Moderate"), (3, "Severe")],
        # validators=[DataRequired()],
        default=1,
        coerce=int,
    )
    # CHECK WITH SABRINA - looks binary to me
    gb_fossa = BooleanField(
        "Gallbladder Fossa or Liver Intersegmental Fissure Lesion", default=0
    )
    lesser_sac = BooleanField("Lesser Sac Lesion >1cm", default=0)
    sma_root = BooleanField("Root of Superior Mesenteric Artery Lesion", default=0)

    # surgical complexity (n = 11)

    pre_tahbso_omx = BooleanField("TAH-BSO + Omentectomy", default=0)
    pre_plnd = BooleanField("Pelvic Lymphadenectomy ", default=0)
    pre_palnd = BooleanField("Para-Aortic Lymphadenectomy", default=0)
    pre_pelvicperit = BooleanField("Pelvic Peritoneum Stripping", default=0)
    pre_abdoperit = BooleanField("Abdominal Peritoneum Stripping", default=0)
    pre_bowelresect = RadioField(
        "Bowel Resection",
        choices=[(1, "Small Bowel"), (2, "Large Bowel"), (3, "Both")],
        # validators=[DataRequired()],
        default=1,
        coerce=int,
    )  # should be ordinal SB, LB, Both
    pre_diaphr = BooleanField("Diaphragm Stripping or Resection", default=0)
    pre_splen = BooleanField("Splenectomy", default=0)
    pre_liver = BooleanField("Liver Resection", default=0)
    pre_lar = BooleanField("Rectosigmoidectomy with Reanstomosis", default=0)
    pre_vats = BooleanField("VATS/Intrathoracic Resection ", default=0)

    st_4unresec = BooleanField(
        "Stage 4 Unresection (Used only in NGR prediction) ", default=0
    )

    submit = SubmitField("Submit")
