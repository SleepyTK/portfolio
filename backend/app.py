from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# ------------------------------------------------------------------ TEMPORARY CODE NOT FOR ACTUAL USE ------------------------------------------------------------------

# SQLite configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
db = SQLAlchemy(app)

# Define a simple model for storing projects
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(500))

@app.route('/projects')
def get_projects():
    projects = Project.query.all()
    return jsonify([{"title": project.title, "description": project.description} for project in projects])

# ------------------------------------------------------------------ TEMPORARY CODE NOT FOR ACTUAL USE ------------------------------------------------------------------


if __name__ == '__main__':
    app.run(debug=True)
