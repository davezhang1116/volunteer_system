from app import app, db
from flask import jsonify, request, render_template, flash, redirect, url_for
from app.models import User, Volunteer, Doctor, CareCoordinator, Resident
from app.services import Matcher
from flask_login import current_user, login_user, logout_user, login_required
from functools import wraps

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or current_user.role != 'admin':
            flash('You do not have permission to access this page.')
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if request.method == 'POST':
        user = User.query.filter_by(email=request.form['email']).first()
        if user is None or not user.check_password(request.form['password']):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=True, force=True)
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
@login_required
@admin_required
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        role = request.form.get('role')
        
        if User.query.filter_by(email=email).first():
            flash('Email address already exists')
            return redirect(url_for('register'))
            
        if role == 'volunteer':
            user = Volunteer(name=name, email=email)
        elif role == 'doctor':
            user = Doctor(name=name, email=email)
        elif role == 'care_coordinator':
            user = CareCoordinator(name=name, email=email)
        elif role == 'resident':
            user = Resident(name=name, email=email)
        else:
            flash('Invalid role selected')
            return redirect(url_for('register'))
            
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        flash('User registered successfully.')
        return redirect(url_for('admin'))
    return render_template('register.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/volunteers', methods=['GET'])
def get_volunteers():
    volunteers = Volunteer.query.all()
    active = [v for v in volunteers if v.is_active is not False]
    return jsonify([{'id': v.id, 'name': v.name} for v in active])

@app.route('/volunteers', methods=['POST'])
def create_volunteer():
    data = request.get_json()
    volunteer = Volunteer(
        name=data['name'],
        email=data['email'],
        major=data.get('major'),
        minor=data.get('minor'),
        year_of_study=data.get('year_of_study'),
        career_goals=data.get('career_goals'),
        skills=data.get('skills'),
        interest_keywords=data.get('interest_keywords'),
        availability=data.get('availability')
    )
    db.session.add(volunteer)
    db.session.commit()
    return jsonify({'message': 'Volunteer created successfully'}), 201

@app.route('/volunteers/<int:id>', methods=['GET'])
def get_volunteer(id):
    volunteer = Volunteer.query.get(id)
    if not volunteer:
        return jsonify({'message': 'Volunteer not found'}), 404
    return jsonify({
        'id': volunteer.id,
        'name': volunteer.name,
        'email': volunteer.email,
        'major': volunteer.major,
        'minor': volunteer.minor,
        'year_of_study': volunteer.year_of_study,
        'career_goals': volunteer.career_goals,
        'skills': volunteer.skills,
        'interest_keywords': volunteer.interest_keywords,
        'availability': volunteer.availability
    })

@app.route('/volunteers/<int:id>', methods=['PUT'])
def update_volunteer(id):
    volunteer = Volunteer.query.get(id)
    if not volunteer:
        return jsonify({'message': 'Volunteer not found'}), 404
    data = request.get_json()
    volunteer.name = data.get('name', volunteer.name)
    volunteer.email = data.get('email', volunteer.email)
    volunteer.major = data.get('major', volunteer.major)
    volunteer.minor = data.get('minor', volunteer.minor)
    volunteer.year_of_study = data.get('year_of_study', volunteer.year_of_study)
    volunteer.career_goals = data.get('career_goals', volunteer.career_goals)
    volunteer.skills = data.get('skills', volunteer.skills)
    volunteer.interest_keywords = data.get('interest_keywords', volunteer.interest_keywords)
    volunteer.availability = data.get('availability', volunteer.availability)
    db.session.commit()
    return jsonify({'message': 'Volunteer updated successfully'})

@app.route('/volunteers/<int:id>', methods=['DELETE'])
def delete_volunteer(id):
    volunteer = Volunteer.query.get(id)
    if not volunteer:
        return jsonify({'message': 'Volunteer not found'}), 404
    db.session.delete(volunteer)
    db.session.commit()
    return jsonify({'message': 'Volunteer deleted successfully'})

@app.route('/doctors', methods=['GET'])
def get_doctors():
    doctors = Doctor.query.all()
    active = [d for d in doctors if d.is_active is not False]
    return jsonify([{'id': d.id, 'name': d.name} for d in active])

@app.route('/doctors', methods=['POST'])
def create_doctor():
    data = request.get_json()
    doctor = Doctor(
        name=data['name'],
        email=data['email'],
        specialty=data.get('specialty'),
        current_projects=data.get('current_projects'),
        required_skills=data.get('required_skills')
    )
    db.session.add(doctor)
    db.session.commit()
    return jsonify({'message': 'Doctor created successfully'}), 201

@app.route('/doctors/<int:id>', methods=['GET'])
def get_doctor(id):
    doctor = Doctor.query.get(id)
    if not doctor:
        return jsonify({'message': 'Doctor not found'}), 404
    return jsonify({
        'id': doctor.id,
        'name': doctor.name,
        'email': doctor.email,
        'specialty': doctor.specialty,
        'current_projects': doctor.current_projects,
        'required_skills': doctor.required_skills
    })

@app.route('/doctors/<int:id>', methods=['PUT'])
def update_doctor(id):
    doctor = Doctor.query.get(id)
    if not doctor:
        return jsonify({'message': 'Doctor not found'}), 404
    data = request.get_json()
    doctor.name = data.get('name', doctor.name)
    doctor.email = data.get('email', doctor.email)
    doctor.specialty = data.get('specialty', doctor.specialty)
    doctor.current_projects = data.get('current_projects', doctor.current_projects)
    doctor.required_skills = data.get('required_skills', doctor.required_skills)
    db.session.commit()
    return jsonify({'message': 'Doctor updated successfully'})

@app.route('/doctors/<int:id>', methods=['DELETE'])
def delete_doctor(id):
    doctor = Doctor.query.get(id)
    if not doctor:
        return jsonify({'message': 'Doctor not found'}), 404
    db.session.delete(doctor)
    db.session.commit()
    return jsonify({'message': 'Doctor deleted successfully'})

@app.route('/care-coordinators', methods=['GET'])
def get_care_coordinators():
    care_coordinators = CareCoordinator.query.all()
    active = [cc for cc in care_coordinators if cc.is_active is not False]
    return jsonify([{'id': cc.id, 'name': cc.name} for cc in active])

@app.route('/care-coordinators', methods=['POST'])
def create_care_coordinator():
    data = request.get_json()
    care_coordinator = CareCoordinator(
        name=data['name'],
        email=data['email'],
        facility_programs=data.get('facility_programs'),
        shift_requirements=data.get('shift_requirements')
    )
    db.session.add(care_coordinator)
    db.session.commit()
    return jsonify({'message': 'Care Coordinator created successfully'}), 201

@app.route('/care-coordinators/<int:id>', methods=['GET'])
def get_care_coordinator(id):
    care_coordinator = CareCoordinator.query.get(id)
    if not care_coordinator:
        return jsonify({'message': 'Care Coordinator not found'}), 404
    return jsonify({
        'id': care_coordinator.id,
        'name': care_coordinator.name,
        'email': care_coordinator.email,
        'facility_programs': care_coordinator.facility_programs,
        'shift_requirements': care_coordinator.shift_requirements
    })

@app.route('/care-coordinators/<int:id>', methods=['PUT'])
def update_care_coordinator(id):
    care_coordinator = CareCoordinator.query.get(id)
    if not care_coordinator:
        return jsonify({'message': 'Care Coordinator not found'}), 404
    data = request.get_json()
    care_coordinator.name = data.get('name', care_coordinator.name)
    care_coordinator.email = data.get('email', care_coordinator.email)
    care_coordinator.facility_programs = data.get('facility_programs', care_coordinator.facility_programs)
    care_coordinator.shift_requirements = data.get('shift_requirements', care_coordinator.shift_requirements)
    db.session.commit()
    return jsonify({'message': 'Care Coordinator updated successfully'})

@app.route('/care-coordinators/<int:id>', methods=['DELETE'])
def delete_care_coordinator(id):
    care_coordinator = CareCoordinator.query.get(id)
    if not care_coordinator:
        return jsonify({'message': 'Care Coordinator not found'}), 404
    db.session.delete(care_coordinator)
    db.session.commit()
    return jsonify({'message': 'Care Coordinator deleted successfully'})

@app.route('/residents', methods=['GET'])
def get_residents():
    residents = Resident.query.all()
    active = [r for r in residents if r.is_active is not False]
    return jsonify([{'id': r.id, 'name': r.name} for r in active])

@app.route('/residents', methods=['POST'])
def create_resident():
    data = request.get_json()
    resident = Resident(
        name=data['name'],
        life_history=data.get('life_history'),
        hobbies=data.get('hobbies'),
        cognitive_profile=data.get('cognitive_profile')
    )
    db.session.add(resident)
    db.session.commit()
    return jsonify({'message': 'Resident created successfully'}), 201

@app.route('/residents/<int:id>', methods=['GET'])
def get_resident(id):
    resident = Resident.query.get(id)
    if not resident:
        return jsonify({'message': 'Resident not found'}), 404
    return jsonify({
        'id': resident.id,
        'name': resident.name,
        'life_history': resident.life_history,
        'hobbies': resident.hobbies,
        'cognitive_profile': resident.cognitive_profile
    })

@app.route('/residents/<int:id>', methods=['PUT'])
def update_resident(id):
    resident = Resident.query.get(id)
    if not resident:
        return jsonify({'message': 'Resident not found'}), 404
    data = request.get_json()
    resident.name = data.get('name', resident.name)
    resident.life_history = data.get('life_history', resident.life_history)
    resident.hobbies = data.get('hobbies', resident.hobbies)
    resident.cognitive_profile = data.get('cognitive_profile', resident.cognitive_profile)
    db.session.commit()
    return jsonify({'message': 'Resident updated successfully'})

@app.route('/residents/<int:id>', methods=['DELETE'])
def delete_resident(id):
    resident = Resident.query.get(id)
    if not resident:
        return jsonify({'message': 'Resident not found'}), 404
    db.session.delete(resident)
    db.session.commit()
    return jsonify({'message': 'Resident deleted successfully'})

@app.route('/match', methods=['POST'])
@login_required
def match():
    volunteers = [v for v in Volunteer.query.all() if v.is_active is not False]
    doctors = [d for d in Doctor.query.all() if d.is_active is not False]
    care_coordinators = [cc for cc in CareCoordinator.query.all() if cc.is_active is not False]
    residents = [r for r in Resident.query.all() if r.is_active is not False]

    current_role = getattr(current_user, 'role', 'user')

    if current_user.role != 'admin':
        if Volunteer.query.get(current_user.id):
            current_role = 'volunteer'
            volunteers = [v for v in volunteers if v.id == current_user.id]
        elif Doctor.query.get(current_user.id):
            current_role = 'doctor'
            doctors = [d for d in doctors if d.id == current_user.id]
            care_coordinators = []
            residents = []
        elif CareCoordinator.query.get(current_user.id):
            current_role = 'care_coordinator'
            care_coordinators = [cc for cc in care_coordinators if cc.id == current_user.id]
            doctors = []
            residents = []
        elif Resident.query.get(current_user.id):
            current_role = 'resident'
            residents = [r for r in residents if r.id == current_user.id]
            doctors = []
            care_coordinators = []

    matcher = Matcher(volunteers, doctors, care_coordinators, residents)
    matches = matcher.match()
    matches['current_role'] = current_role
    return jsonify(matches)
    
@app.route('/admin/volunteer/<int:id>/matches', methods=['GET'])
@login_required
@admin_required
def get_volunteer_matches(id):
    volunteer = Volunteer.query.get(id)
    if not volunteer:
        return jsonify({'error': 'Volunteer not found'}), 404
        
    doctors = [d for d in Doctor.query.all() if d.is_active is not False]
    care_coordinators = [cc for cc in CareCoordinator.query.all() if cc.is_active is not False]
    residents = [r for r in Resident.query.all() if r.is_active is not False]
    
    matcher = Matcher([volunteer], doctors, care_coordinators, residents)
    matches = matcher.match()
    matches['current_role'] = 'admin'
    
    return jsonify(matches)

@app.route('/admin/confirm_match', methods=['POST'])
@login_required
@admin_required
def confirm_match():
    data = request.get_json()
    volunteer_id = data.get('volunteer_id')
    match_type = data.get('match_type')
    match_id = data.get('match_id')
    keep_active = data.get('keep_active', False)

    volunteer = Volunteer.query.get(volunteer_id)
    if not volunteer:
        return jsonify({'error': 'Volunteer not found'}), 404

    matched_entity = None
    if match_type == 'doctor':
        matched_entity = Doctor.query.get(match_id)
    elif match_type == 'resident':
        matched_entity = Resident.query.get(match_id)
    elif match_type == 'care_coordinator':
        matched_entity = CareCoordinator.query.get(match_id)

    if not matched_entity:
        return jsonify({'error': 'Matched entity not found'}), 404

    try:
        # Append to volunteer's status
        vol_link = f"Matched with {matched_entity.name} ({match_type.replace('_', ' ').title()})"
        if volunteer.linked_status:
            if vol_link not in volunteer.linked_status:
                volunteer.linked_status += f", {vol_link}"
        else:
            volunteer.linked_status = vol_link

        # Append to the matched entity's status
        ent_link = f"Matched with {volunteer.name} (Volunteer)"
        if matched_entity.linked_status:
            if ent_link not in matched_entity.linked_status:
                matched_entity.linked_status += f", {ent_link}"
        else:
            matched_entity.linked_status = ent_link

        volunteer.is_active = keep_active
        matched_entity.is_active = keep_active

        db.session.commit()
        return jsonify({'message': 'Match confirmed successfully!'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'Failed to confirm match. Ensure is_active and linked_status exist on models. Error: {str(e)}'}), 500

@app.route('/admin/links/doctors')
@login_required
@admin_required
def links_doctors():
    # Query volunteers matched specifically with Doctors
    volunteers = Volunteer.query.filter(Volunteer.linked_status.like('%(Doctor)%')).all()
    links = []
    for v in volunteers:
        parts = [p.strip() for p in v.linked_status.split(',')]
        for part in parts:
            if '(Doctor)' in part:
                doctor_name = part.replace('Matched with ', '').replace(' (Doctor)', '')
                doctor = Doctor.query.filter_by(name=doctor_name).first()
                links.append({'volunteer': v, 'target': doctor, 'target_role': 'doctor', 'status': part})
    return render_template('links_doctors.html', links=links)

@app.route('/admin/links/coordinators')
@login_required
@admin_required
def links_coordinators():
    # Query volunteers matched with Care Coordinators or Residents
    volunteers_cc = Volunteer.query.filter(Volunteer.linked_status.like('%(Care Coordinator)%')).all()
    volunteers_res = Volunteer.query.filter(Volunteer.linked_status.like('%(Resident)%')).all()
    links = []
    for v in volunteers_cc:
        parts = [p.strip() for p in v.linked_status.split(',')]
        for part in parts:
            if '(Care Coordinator)' in part:
                cc_name = part.replace('Matched with ', '').replace(' (Care Coordinator)', '')
                cc = CareCoordinator.query.filter_by(name=cc_name).first()
                links.append({'volunteer': v, 'target': cc, 'target_role': 'care_coordinator', 'status': part})
    for v in volunteers_res:
        parts = [p.strip() for p in v.linked_status.split(',')]
        for part in parts:
            if '(Resident)' in part:
                res_name = part.replace('Matched with ', '').replace(' (Resident)', '')
                res = Resident.query.filter_by(name=res_name).first()
                links.append({'volunteer': v, 'target': res, 'target_role': 'resident', 'status': part})
    return render_template('links_coordinators.html', links=links)

@app.route('/admin/links_dashboard')
@login_required
@admin_required
def admin_links_dashboard():
    volunteers = Volunteer.query.filter(Volunteer.linked_status.isnot(None), Volunteer.linked_status != '').all()
    doctors = Doctor.query.filter(Doctor.linked_status.isnot(None), Doctor.linked_status != '').all()
    care_coordinators = CareCoordinator.query.filter(CareCoordinator.linked_status.isnot(None), CareCoordinator.linked_status != '').all()
    residents = Resident.query.filter(Resident.linked_status.isnot(None), Resident.linked_status != '').all()
    return render_template('admin_links_dashboard.html', 
                           volunteers=volunteers,
                           doctors=doctors,
                           care_coordinators=care_coordinators,
                           residents=residents)

@app.route('/admin')
@login_required
@admin_required
def admin():
    search_query = request.args.get('search', '')
    role_filter = request.args.get('role', '')

    users = User.query.all()
    
    volunteers_ids = {v.id for v in Volunteer.query.all()}
    doctors_ids = {d.id for d in Doctor.query.all()}
    cc_ids = {cc.id for cc in CareCoordinator.query.all()}
    
    for u in users:
        if u.id in volunteers_ids:
            u.actual_role = 'volunteer'
        elif u.id in doctors_ids:
            u.actual_role = 'doctor'
        elif u.id in cc_ids:
            u.actual_role = 'care_coordinator'
        else:
            u.actual_role = u.role
            
    residents = Resident.query.all()
    for r in residents:
        r.actual_role = 'resident'
        r.role = 'resident'
        
    all_entities = users + residents

    if search_query:
        search_lower = search_query.lower()
        all_entities = [
            e for e in all_entities 
            if search_lower in (getattr(e, 'name', '') or '').lower() 
            or search_lower in (getattr(e, 'email', '') or '').lower()
        ]
        
    if role_filter:
        all_entities = [e for e in all_entities if getattr(e, 'actual_role', '') == role_filter]

    return render_template('admin.html', users=all_entities, search_query=search_query, role_filter=role_filter)

@app.route('/admin/toggle_active/<string:entity_type>/<int:user_id>', methods=['POST'])
@login_required
@admin_required
def toggle_active(entity_type, user_id):
    if entity_type == 'resident':
        user = Resident.query.get(user_id)
    else:
        user = User.query.get(user_id)
        
    if user:
        current_status = getattr(user, 'is_active', True)
        if current_status is None:
            current_status = True
        user.is_active = not current_status
        db.session.commit()
        flash(f"Status for {user.name} changed to {'Active' if user.is_active else 'Inactive'}.")
    return redirect(request.referrer or url_for('admin'))

@app.route('/admin/unlink/<string:entity_type>/<int:user_id>', methods=['POST'])
@login_required
@admin_required
def unlink_user(entity_type, user_id):
    if entity_type == 'resident':
        user = Resident.query.get(user_id)
    else:
        user = User.query.get(user_id)
        
    if user and getattr(user, 'linked_status', None):
        all_users = User.query.filter(User.linked_status.isnot(None)).all()
        all_residents = Resident.query.filter(Resident.linked_status.isnot(None)).all()
        for u in (all_users + all_residents):
            if u is not user and getattr(u, 'linked_status', None):
                if user.name in u.linked_status:
                    # Remove only this user's link string
                    links = [l.strip() for l in u.linked_status.split(',')]
                    links = [l for l in links if user.name not in l]
                    u.linked_status = ", ".join(links) if links else None
                    
                    if not u.linked_status:
                        u.is_active = True
        
        user.linked_status = None
        user.is_active = True
        db.session.commit()
        flash(f"Link(s) terminated for {user.name}. Relevant users are now active.")
    return redirect(request.referrer or url_for('admin'))

@app.route('/admin/unlink_specific/<string:entity_type>/<int:user_id>', methods=['POST'])
@login_required
@admin_required
def unlink_specific(entity_type, user_id):
    target_name = request.form.get('target_name')
    target_role = request.form.get('target_role')
    
    if not target_name or not target_role:
        flash("Target information missing.")
        return redirect(request.referrer or url_for('admin'))

    if entity_type == 'resident':
        user = Resident.query.get(user_id)
    else:
        user = User.query.get(user_id)
        
    if user and getattr(user, 'linked_status', None):
        # 1. Remove target from user's linked_status
        user_links = [l.strip() for l in user.linked_status.split(',')]
        target_link_str = f"Matched with {target_name} ({target_role})"
        user_links = [l for l in user_links if l != target_link_str]
        user.linked_status = ", ".join(user_links) if user_links else None
        if not user.linked_status:
            user.is_active = True
            
        # 2. Remove user from target's linked_status
        user_role_str = "Volunteer" if entity_type == "volunteer" else entity_type.replace('_', ' ').title()
        
        target_entity = None
        if target_role == "Volunteer":
            target_entity = Volunteer.query.filter_by(name=target_name).first()
        elif target_role == "Doctor":
            target_entity = Doctor.query.filter_by(name=target_name).first()
        elif target_role == "Care Coordinator":
            target_entity = CareCoordinator.query.filter_by(name=target_name).first()
        elif target_role == "Resident":
            target_entity = Resident.query.filter_by(name=target_name).first()
            
        if target_entity and getattr(target_entity, 'linked_status', None):
            target_links = [l.strip() for l in target_entity.linked_status.split(',')]
            user_link_str = f"Matched with {user.name} ({user_role_str})"
            target_links = [l for l in target_links if l != user_link_str]
            target_entity.linked_status = ", ".join(target_links) if target_links else None
            if not target_entity.linked_status:
                target_entity.is_active = True
                
        db.session.commit()
        flash(f"Link with {target_name} terminated for {user.name}.")
    return redirect(request.referrer or url_for('admin'))

@app.route('/admin/delete_user/<string:entity_type>/<int:id>', methods=['POST'])
@login_required
@admin_required
def delete_user(entity_type, id):
    if entity_type == 'resident':
        user = Resident.query.get(id)
    else:
        user = User.query.get(id)
        
    if user:
        db.session.delete(user)
        db.session.commit()
        flash('User deleted successfully.')
    return redirect(url_for('admin'))

@app.route('/admin/volunteer/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_volunteer(id):
    volunteer = Volunteer.query.get(id)
    if not volunteer:
        flash('Volunteer not found.')
        return redirect(url_for('index'))
        
    if request.method == 'POST':
        volunteer.name = request.form['name']
        volunteer.email = request.form['email']
        volunteer.major = request.form.get('major', '')
        volunteer.minor = request.form.get('minor', '')
        volunteer.year_of_study = request.form.get('year_of_study', '')
        volunteer.career_goals = request.form.get('career_goals', '')
        volunteer.skills = request.form.get('skills', '')
        volunteer.interest_keywords = request.form.get('interest_keywords', '')
        volunteer.availability = request.form.get('availability', '')
        db.session.commit()
        flash('Volunteer updated successfully.')
        return redirect(url_for('index'))
        
    return render_template('edit_volunteer.html', volunteer=volunteer)

@app.route('/admin/doctor/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_doctor(id):
    doctor = Doctor.query.get(id)
    if not doctor:
        flash('Doctor not found.')
        return redirect(url_for('index'))
        
    if request.method == 'POST':
        doctor.name = request.form['name']
        doctor.email = request.form['email']
        doctor.specialty = request.form.get('specialty', '')
        doctor.current_projects = request.form.get('current_projects', '')
        doctor.required_skills = request.form.get('required_skills', '')
        db.session.commit()
        flash('Doctor updated successfully.')
        return redirect(url_for('index'))
        
    return render_template('edit_doctor.html', doctor=doctor)

@app.route('/admin/care_coordinator/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_care_coordinator(id):
    care_coordinator = CareCoordinator.query.get(id)
    if not care_coordinator:
        flash('Care Coordinator not found.')
        return redirect(url_for('index'))
        
    if request.method == 'POST':
        care_coordinator.name = request.form['name']
        care_coordinator.email = request.form['email']
        care_coordinator.facility_programs = request.form.get('facility_programs', '')
        care_coordinator.shift_requirements = request.form.get('shift_requirements', '')
        db.session.commit()
        flash('Care Coordinator updated successfully.')
        return redirect(url_for('index'))
        
    return render_template('edit_care_coordinator.html', care_coordinator=care_coordinator)

@app.route('/admin/resident/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_resident(id):
    resident = Resident.query.get(id)
    if not resident:
        flash('Resident not found.')
        return redirect(url_for('index'))
        
    if request.method == 'POST':
        resident.name = request.form['name']
        resident.life_history = request.form.get('life_history', '')
        resident.hobbies = request.form.get('hobbies', '')
        resident.cognitive_profile = request.form.get('cognitive_profile', '')
        db.session.commit()
        flash('Resident updated successfully.')
        return redirect(url_for('index'))
        
    return render_template('edit_resident.html', resident=resident)

@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    volunteer = Volunteer.query.get(current_user.id)
    doctor = Doctor.query.get(current_user.id)
    cc = CareCoordinator.query.get(current_user.id)
    resident = Resident.query.get(current_user.id)

    is_volunteer = volunteer is not None
    is_doctor = doctor is not None
    is_cc = cc is not None
    is_resident = resident is not None

    user_profile = volunteer or doctor or cc or resident or current_user

    if request.method == 'POST':
        user_profile.name = request.form['name']
        user_profile.email = request.form['email']

        if is_volunteer:
            user_profile.major = request.form.get('major', '')
            user_profile.minor = request.form.get('minor', '')
            user_profile.year_of_study = request.form.get('year_of_study', '')
            user_profile.career_goals = request.form.get('career_goals', '')
            user_profile.skills = request.form.get('skills', '')
            user_profile.interest_keywords = request.form.get('interest_keywords', '')
            user_profile.availability = request.form.get('availability', '')
        if is_doctor:
            user_profile.specialty = request.form.get('specialty', '')
            user_profile.current_projects = request.form.get('current_projects', '')
            user_profile.required_skills = request.form.get('required_skills', '')
        if is_cc:
            user_profile.facility_programs = request.form.get('facility_programs', '')
            user_profile.shift_requirements = request.form.get('shift_requirements', '')
        if is_resident:
            user_profile.life_history = request.form.get('life_history', '')
            user_profile.hobbies = request.form.get('hobbies', '')
            user_profile.cognitive_profile = request.form.get('cognitive_profile', '')

        db.session.commit()
        flash('Your profile has been updated.')
        return redirect(url_for('profile'))
    return render_template('profile.html', 
                           user_profile=user_profile,
                           is_volunteer=is_volunteer, 
                           is_doctor=is_doctor, 
                           is_cc=is_cc, 
                           is_resident=is_resident)
