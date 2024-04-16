from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

# create a search form
#
# variable names need to be identical to what they are in each html template file
class EntryForm(FlaskForm):
	name = StringField("Contestant Name")
	submit = SubmitField("Submit")

class SearchForm(FlaskForm):
	phrase = StringField("Phrase")
	submit = SubmitField("Submit")