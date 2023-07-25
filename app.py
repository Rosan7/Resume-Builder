from flask import Flask, jsonify, request
from flask_cors import CORS
from os import environ
from config import db, SECRET_KEY
from config import load_dotenv
from models.user import User
from models.personalDetails import PersonalDetails
from models.projects import Projects
from models.experiences import Experiences
from models.education import Education
from models.certificates import Certificates
from models.skills import Skills


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = environ.get('DB_URI')
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_ECHO"] = False
    app.secret_key = SECRET_KEY
    db.init_app(app)
    print("DB initaialized Successfully")
    # projects = {}
    with app.app_context():
        # db.drop_all()
        """
        Create an end point

        User form data to take the responses from the user
        User username for indexing a user 
            -sign up user
            -add personal details
            -add expirience details
            -add projects detials
            -add education details 
            -add certificate datails
            -add skill details
        """

        @app.route('/sign_up', methods=['POST'])
        def sign_up():
            data = request.form.to_dict(flat=True)

            new_user = User(
                username = data["username"]
            )
            db.session.add(new_user)
            db.session.commit()
            return "User added successfully"

        @app.route('/add_personal_datails', methods=['POST'])
        def add_personal_details():
            username=request.args.get('username')
            user = User.query.filter_by (username=username).first()

            personal_details = request.get_json()
            new_personal_details = PersonalDetails(
                name = personal_details["name"],
                email = personal_details["email"],
                phone = personal_details["phone"],
                address = personal_details["address"],
                linkedin_link = personal_details["linkedin_link"]
            )

        @app.route("/add_experience_details", methods=['POST'])
        def add_experience_details():
            username=request.args.get('username')
            user = User.query.filter_by (username=username).first()

            experience_details = request.get_json()
            for experience in experience_details["data"]:
                new_experience = Experiences(
                    # company_name = experience
                )
                    


        @app.route("/add_project_details", methods=['POST'])
        def add_project_details():
            username=request.args.get('username')
            user = User.query.filter_by(username=username).first()

            print(user.id, user)
            project_details = request.get_json()
            for project in project_details["data"]:
                new_project = Projects(
                    name = project["name"],
                    desc = project["description"],
                    start_date = project["start_date"],
                    end_date = project["end_date"],
                    user_id = user.id
                )

                print(new_project.user_id)
                db.session.add(new_project)
                db.session.commit()
            return jsonify(msg="project added successfully")
            

        @app.route("/add_education_datails", methods=['POST'])
        def add_educational_details():
            username=request.args.get('user`name')
            user = User.query.filter_by (username=username).first()

            educational_details = request.get_json()

        @app.route("/add_certificate_datails", methods=['POST'])
        def add_certificate_details():
            username=request.args.get('username')
            user = User.query.filter_by (username=username).first()

            certificate_details = request.get_json()
            return "ff"

        @app.route("/add_skill_details", methods=['POST'])
        def add_skill_details():
            username=request.args.get('username')
            user = User.query.filter_by (username=username).first()

            skill_details = request.get_json()
        @app.route('/get_resume_json', methods=['GET'])
        def get_resume_json():
            username=request.args.get('username')
            user = User.query.filter_by (username=username).first()
            personalDetails = User.query.filter_by (user_id=user.id).all()
            experiences = User.query.filter_by (user_id=user.id).all()
            projects = User.query.filter_by (user_id=user.id).all()
            education = User.query.filter_by (user_id=user.id).all()
            certificates = User.query.filter_by (user_id=user.id).all()
            skills = User.query.filter_by (user_id=user.id).all()
            resume_data = {}
            experiences_data = []
            projects_data = []
            education_data = []
            certificates_data = []
            skills_data = []
            resume_data  = {
                "name": personalDetails.name,
                "email": personalDetails.email,
                "phone": personalDetails.phone,
                "address": personalDetails.address,
                "linkedin_link": personalDetails.linkedin_link
            }
            # add experience information
            for experience in experiences:
                experiences_data.append({
                        "company_name": experience.company_name,
                        "start_date": experience.start_date,
                        "end_date": experience.end_date,
                        "role": experience.role,
                        "role_description": experience.role_description})
            resume_data["experiences"]  = experiences_data
            # add project information
            for project in projects:
                projects_data.append({
                    "name": project.name,
                    "desc": project.desc,
                    "start_date": project.start_date,
                    "end_date": project.end_date
                })
            resume_data["projects"] = projects_data
            # add education information
            for education in education:
                education_data.append({
                    "school_name": education.school_name,
                    "degree_name": education.degree_name,
                    "start_date": education.start_date,
                    "end_date": education.end_date,
                    "user_id": user.id})
            resume_data["education"] = education_data

            # add certificate information
                    # "description": education.description,
                    # "location": education.location,
                    # "location_description": education.location_description
            return resume_data


            
        db.create_all()
        db.session.commit()
        return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="127.0.0.1", port = "5000", debug=True)