from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import pandas as pd

app = Flask(__name__)
# Configure the SQLAlchemy database URI. SQLite database named `rental.db` will be used here.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rental.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Rental(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    INSEE_C = db.Column(db.String(20), unique=True, nullable=False)
    LIBGEO = db.Column(db.String(100), nullable=False)
    loypredm2 = db.Column(db.Float, nullable=False)
    lwr_IPm2 = db.Column(db.Float, nullable=False)
    upr_IPm2 = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Rental {self.LIBGEO}>'


@app.route('/init-db')
def init_db():
    db.create_all()
    # Load data from CSV file
    file_path = 'pred-mai-mef-dhup-3.csv'  # Update this path if necessary
    data = pd.read_csv(file_path, encoding='ISO-8859-1', delimiter=';')
    
    # Iterate over the rows of the DataFrame and add each as a Rental object
    for _, row in data.iterrows():
        rental = Rental(
            INSEE_C=row['INSEE_C'],
            LIBGEO=row['LIBGEO'],
            loypredm2=float(row['loypredm2'].replace(',', '.')),  # Assuming 'loypredm2' is in European format
            lwr_IPm2=float(row['lwr.IPm2'].replace(',', '.')),    # Replace commas with dots if necessary
            upr_IPm2=float(row['upr.IPm2'].replace(',', '.'))     # Convert to float after replacing comma
        )
        db.session.add(rental)
    
    # Commit the session once all Rental objects are added
    db.session.commit()
    return 'Database initialized with CSV data!'


@app.route('/rental-prices/overview')
def overview():
    page = request.args.get('page', 1, type=int)
    per_page = 10
    rentals = Rental.query.paginate(page=page, per_page=per_page, error_out=False)
    return render_template('overview-fr.html', rentals=rentals.items)

@app.route('/rental-prices/detail/<insee_c>')
def detail(insee_c):
    rental = Rental.query.filter_by(INSEE_C=insee_c).first_or_404()
    return render_template('detail-fr.html', rental=rental)

if __name__ == '__main__':
    app.run(debug=True)
