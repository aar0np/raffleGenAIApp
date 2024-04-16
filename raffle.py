from flask import Flask, render_template
from webForms import EntryForm, SearchForm
from raffleServices import submit_name
from raffleServices import get_names

app = Flask(__name__)
app.config.from_object('config.ProdConfig')

# add names on main page/form
@app.route('/')
def index():
	form = EntryForm()
	return render_template('main.html',form=form)

@app.route('/enter_names', methods=["POST"])
async def enterNames():
	form = EntryForm()
	if form.name.data != "":
		await submit_name(form.name.data)
		return render_template('main.html', form=form)

@app.route('/winners')
async def winners():
	response = await get_names("Midnight Bomber")
	if response != "":
		return render_template('winners.html', data=response)