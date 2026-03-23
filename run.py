from app import app, db
from app.models import User, Volunteer, Doctor, CareCoordinator, Resident

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Volunteer': Volunteer, 'Doctor': Doctor, 'CareCoordinator': CareCoordinator, 'Resident': Resident}

if __name__ == '__main__':
    app.run(debug=True)
