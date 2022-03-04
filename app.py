from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pandas as pd

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///winners.db'
#Initialize the database
db = SQLAlchemy(app)

#Create db model
class Winners(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	game_id = db.Column(db.Integer, nullable=False)
	name = db.Column(db.String(200), nullable=False)
	created_at = db.Column(db.DateTime, default=datetime.utcnow())

	#Function to return string when adding
	def __repr__(self):
		#return '<Name %r>' % self.id
		return f"<id={self.id}, name={self.name}>, game_id={self.game_id}"

preds = pd.read_csv('predictions_with_seeds.csv')
teams = list(preds['TeamName_1'].unique())

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'GET':
		db.session.query(Winners).delete()
		db.session.commit()
		return render_template('index.html', teams=teams)

	elif request.method == 'POST':
		game_winner = request.form.get('matchup', 'world')
		game_id = game_winner.split('-')[-1]
		name = game_winner.split('-')[0]
		winner = Winners(game_id=game_id, name=name)

		#Push to Database
		try:
			db.session.add(winner)
			db.session.commit()
			redirect('/predict')
		except:
			return 'There was an error adding a winner to the db'

		return render_template('predict.html', winners=winners)

@app.route('/top-bracket', methods=['GET', 'POST'])
def top_predict():
	if request.method == 'POST':
		game_winner = request.form.get('matchup', 'world')
		game_id = game_winner.split('-')[-1]
		name = game_winner.split('-')[0]

		data = Winners.query.all()
		filtered_data = [x for x in data if x.game_id == game_id]

		if len(filtered_data) > 0:
			winner_to_update = Winners.query.get_or_404(filtered_data[0].id)
			winner_to_update.name = name
			try:
				db.session.commit()
				return redirect('/top-bracket')
				
			except:
				return "There was a problem updating"
		else:

			#Push to Database
			winner = Winners(game_id=game_id, name=name)

			try:
				db.session.add(winner)
				db.session.commit()
				return redirect('/top-bracket')
			except:
				return 'There was an error adding a winner to the db'
	else:
		winners = Winners.query.order_by(Winners.created_at)
		game_ids = [winner.game_id for winner in winners]
		winner_dict = {winner.game_id: winner.name for winner in winners}

		game_map = {1:9, 2:9, 3:10, 4:10, 5:11, 6:11, 7:12, 8:12, 9:13, 10:13, 11:14, 12:14, 13:15, 14:15, 15:16}

		return render_template('top_bracket.html', winners=winners, game_ids=game_ids, winner_dict=winner_dict, game_map=game_map)

@app.route('/bottom-bracket', methods=['GET', 'POST'])
def bottom_predict():
	if request.method == 'POST':
		game_winner = request.form.get('matchup', 'world')
		game_id = game_winner.split('-')[-1]
		name = game_winner.split('-')[0]

		data = Winners.query.all()
		filtered_data = [x for x in data if x.game_id == game_id]

		if len(filtered_data) > 0:
			winner_to_update = Winners.query.get_or_404(filtered_data[0].id)
			winner_to_update.name = name
			try:
				db.session.commit()
				return redirect('/bottom-bracket')
				
			except:
				return "There was a problem updating"
		else:

			#Push to Database
			winner = Winners(game_id=game_id, name=name)

			try:
				db.session.add(winner)
				db.session.commit()
				return redirect('/bottom-bracket')
			except:
				return 'There was an error adding a winner to the db'
	else:
		winners = Winners.query.order_by(Winners.created_at)
		game_ids = [winner.game_id for winner in winners]
		winner_dict = {winner.game_id: winner.name for winner in winners}

		game_map = {1:9, 2:9, 3:10, 4:10, 5:11, 6:11, 7:12, 8:12, 9:13, 10:13, 11:14, 12:14, 13:15, 14:15, 15:16}

		return render_template('bottom_bracket.html', winners=winners, game_ids=game_ids, winner_dict=winner_dict, game_map=game_map)


@app.route('/final-four', methods=['GET', 'POST'])
def ff_predict():
	if request.method == 'POST':
		game_winner = request.form.get('matchup', 'world')
		game_id = game_winner.split('-')[-1]
		name = game_winner.split('-')[0]

		data = Winners.query.all()
		filtered_data = [x for x in data if x.game_id == game_id]

		if len(filtered_data) > 0:
			winner_to_update = Winners.query.get_or_404(filtered_data[0].id)
			winner_to_update.name = name
			try:
				db.session.commit()
				return redirect('/final-four')
				
			except:
				return "There was a problem updating"
		else:

			#Push to Database
			winner = Winners(game_id=game_id, name=name)

			try:
				db.session.add(winner)
				db.session.commit()
				return redirect('/final-four')
			except:
				return 'There was an error adding a winner to the db'
	else:
		winners = Winners.query.order_by(Winners.created_at)
		game_ids = [winner.game_id for winner in winners]
		winner_dict = {winner.game_id: winner.name for winner in winners}

		game_map = {1:9, 2:9, 3:10, 4:10, 5:11, 6:11, 7:12, 8:12, 9:13, 10:13, 11:14, 12:14, 13:15, 14:15, 15:16}

		return render_template('final_four.html', winners=winners, game_ids=game_ids, winner_dict=winner_dict, game_map=game_map)