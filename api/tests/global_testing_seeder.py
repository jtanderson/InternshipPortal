# Justin Ventura

import hashlib
from flask_seeder import Seeder
from models import db, ClientsModel, UsersModel, CoursesModel, \
    ContactFormMessage, ListingsModel, Listings_CoursesModel, \
    TagsModel, Listings_TagsModel


class ClientsSeeder(Seeder):
    """
    This is the seeder for clients.
    No other models will be affected by this.
    """

    # run() will be called by Flask-Seeder
    def run(self):
        clients = [
            {
                'client_name': 'Amazon',
                'client_addr': '601 New Jersey Ave NW Suite 420,' +
                'Washington, DC 20001',
                'client_email': 'hr@amazon.com'
            },
            {
                'client_name': 'Google Inc.',
                'client_addr': '1600 Amphitheatre Pkwy, Mountain' +
                'View, CA 94043',
                'client_email': 'sundar_pichai@google.com'
            },
            {
                'client_name': 'Facebook Inc.',
                'client_addr': '1 Hacker Way, Menlo Park, CA 94025',
                'client_email': 'zuck@facebook.com'
            },
            {
                'client_name': 'SU Department of Computer Science',
                'client_addr': '1101 Camden Ave, Salisbury, MD 21801',
                'client_email': 'giulia_franchi@salisbury.edu'
            }
        ]
        for client in clients:
            db.session.add(ClientsModel(**client))
        db.session.commit()


class CoursesSeeder(Seeder):
    '''
    This is the seeder for clients.
    No other models will be affected by this.
    '''

    # run() will be called by Flask-Seeder
    def run(self):
        courses = [
            {'course_num': 'COSC 116',
                'course_title': 'Introduction to Computer Systems'},
            {'course_num': 'COSC 117', 'course_title': 'Programming Fundamentals'},
            {'course_num': 'COSC 118',
                'course_title': 'Introductory Scientific Programming'},
            {'course_num': 'COSC 119', 'course_title': 'Introduction to Web Development'},
            {'course_num': 'COSC 120', 'course_title': 'Computer Science I'},
            {'course_num': 'COSC 220', 'course_title': 'Computer Science II'},
            {'course_num': 'COSC 250', 'course_title': 'Microcomputer Organization'},
            {'course_num': 'COSC 290', 'course_title': 'Introductory Special Topics'},
            {'course_num': 'COSC 311',
                'course_title': 'Introduction to Data Visualization and Interpretation'},
            {'course_num': 'COSC 320',
                'course_title': 'Advanced Data Structures and Algorithm Analysis'},
            {'course_num': 'COSC 330',
                'course_title': 'OO Design Patterns and GUI/Event-Driven Programming'},
            {'course_num': 'COSC 350', 'course_title': 'Systems Software'},
            {'course_num': 'COSC 362', 'course_title': 'Theory of Computation'},
            {'course_num': 'COSC 370', 'course_title': 'Computer Networks'},
            {'course_num': 'COSC 380', 'course_title': 'Internship'},
            {'course_num': 'COSC 385', 'course_title': 'Directed Study'},
            {'course_num': 'COSC 386',
                'course_title': 'Database Design and Implementation'},
            {'course_num': 'COSC 390', 'course_title': 'Undergraduate Research Project'},
            {'course_num': 'COSC 401',
                'course_title': 'Methods of Teaching Computer Science'},
            {'course_num': 'COSC 420', 'course_title': 'High-Performance Computing'},
            {'course_num': 'COSC 422',
                'course_title': 'Organization of Programming Languages'},
            {'course_num': 'COSC 425', 'course_title': 'Software Engineering I'},
            {'course_num': 'COSC 426', 'course_title': 'Software Engineering II'},
            {'course_num': 'COSC 432', 'course_title': 'Compiler Construction'},
            {'course_num': 'COSC 450', 'course_title': 'Operating Systems'},
            {'course_num': 'COSC 451', 'course_title': 'Robotics'},
            {'course_num': 'COSC 456', 'course_title': 'Computer Architecture'},
            {'course_num': 'COSC 472', 'course_title': 'Network Security'},
            {'course_num': 'COSC 482', 'course_title': 'Computer Graphics'},
            {'course_num': 'COSC 490', 'course_title': 'Special Topics'},
            {'course_num': 'COSC 495', 'course_title': 'Directed Consulting'},
            {'course_num': 'COSC 501',
                'course_title': 'Methods of Teaching Computer Science'},
            {'course_num': 'COSC 522',
                'course_title': 'Organization of Programming Languages'},
            {'course_num': 'COSC 550', 'course_title': 'Operating Systems'},
            {'course_num': 'COSC 582', 'course_title': 'Computer Graphics'},
            {'course_num': 'COSC 590', 'course_title': 'Special Topics'},
            {'course_num': 'MATH 105', 'course_title': 'Liberal Arts Mathematics'},
            {'course_num': 'MATH 130', 'course_title': 'Fundamental Concepts I'},
            {'course_num': 'MATH 135',
                'course_title': 'College Algebra: A Modeling Approach'},
            {'course_num': 'MATH 140',
                'course_title': 'College Algebra and Trigonometry'},
            {'course_num': 'MATH 144', 'course_title': 'Environmental Mathematics'},
            {'course_num': 'MATH 150',
                'course_title': 'Data and Probability Connections'},
            {'course_num': 'MATH 155',
                'course_title': 'Modern Statistics with Computer Analysis'},
            {'course_num': 'MATH 160',
                'course_title': 'Introduction to Applied Calculus'},
            {'course_num': 'MATH 198',
                'course_title': 'Calculus I For Biology and Medicine'},
            {'course_num': 'MATH 201', 'course_title': 'Calculus I'},
            {'course_num': 'MATH 202', 'course_title': 'Calculus II'},
            {'course_num': 'MATH 203', 'course_title': 'Honors Theory of Calculus'},
            {'course_num': 'MATH 210',
                'course_title': 'Introduction to Discrete Mathematics'},
            {'course_num': 'MATH 214', 'course_title': 'Statistics Laboratory'},
            {'course_num': 'MATH 215',
                'course_title': 'Introduction to Financial Mathematics'},
            {'course_num': 'MATH 216', 'course_title': 'Statistical Thinking'},
            {'course_num': 'MATH 230', 'course_title': 'Fundamental Concepts II'},
            {'course_num': 'MATH 290', 'course_title': 'Introductory Special Topics'},
            {'course_num': 'MATH 300',
                'course_title': 'Introduction to Abstract Mathematics'},
            {'course_num': 'MATH 306', 'course_title': 'Linear Algebra'},
            {'course_num': 'MATH 310', 'course_title': 'Calculus III'},
            {'course_num': 'MATH 311', 'course_title': 'Differential Equations I'},
            {'course_num': 'MATH 313', 'course_title': 'Survey Design and Sampling'},
            {'course_num': 'MATH 314', 'course_title': 'Regression Analysis'},
            {'course_num': 'MATH 380', 'course_title': 'Internship'},
            {'course_num': 'MATH 385', 'course_title': 'Directed Study'},
            {'course_num': 'MATH 390', 'course_title': 'Undergraduate Research Project'},
            {'course_num': 'MATH 402', 'course_title': 'Theory of Numbers'},
            {'course_num': 'MATH 406', 'course_title': 'Geometric Structures'},
            {'course_num': 'MATH 411',
                'course_title': 'Design and Analysis of Experiments'},
            {'course_num': 'MATH 413', 'course_title': 'Mathematical Statistics I'},
            {'course_num': 'MATH 414', 'course_title': 'Mathematical Statistics II'},
            {'course_num': 'MATH 415', 'course_title': 'Actuarial and Financial Methods'},
            {'course_num': 'MATH 422', 'course_title': 'Advanced Differential Equations'},
            {'course_num': 'MATH 430',
                'course_title': 'Mathematical Connections for Secondary School Teachers'},
            {'course_num': 'MATH 441', 'course_title': 'Abstract Algebra I'},
            {'course_num': 'MATH 442', 'course_title': 'Abstract Algebra II'},
            {'course_num': 'MATH 447', 'course_title': 'Cryptography'},
            {'course_num': 'MATH 451', 'course_title': 'Analysis I'},
            {'course_num': 'MATH 452', 'course_title': 'Analysis II'},
            {'course_num': 'MATH 458', 'course_title': 'Complex Analysis'},
            {'course_num': 'MATH 465',
                'course_title': 'Mathematical Models and Applications'},
            {'course_num': 'MATH 471', 'course_title': 'Numerical Methods'},
            {'course_num': 'MATH 472', 'course_title': 'Numerical Linear Algebra'},
            {'course_num': 'MATH 475',
                'course_title': 'Introduction to Dynamics and Chaos'},
            {'course_num': 'MATH 480', 'course_title': 'History of Mathematics'},
            {'course_num': 'MATH 482', 'course_title': 'Computer Graphics'},
            {'course_num': 'MATH 490', 'course_title': 'Special Topics'},
            {'course_num': 'MATH 493', 'course_title': 'Advanced Topics in Statistics'},
            {'course_num': 'MATH 495', 'course_title': 'Directed Consulting'},
            {'course_num': 'MATH 500', 'course_title': 'Foundations of Number Theory'},
            {'course_num': 'MATH 501',
                'course_title': 'Number Theory from a Multicultural and Historical Perspective'},
            {'course_num': 'MATH 502', 'course_title': 'Applied Statistics'},
            {'course_num': 'MATH 503', 'course_title': 'Data Analysis'},
            {'course_num': 'MATH 506', 'course_title': 'Selected Topics'},
            {'course_num': 'MATH 507', 'course_title': 'Seminar: Algebra'},
            {'course_num': 'MATH 508', 'course_title': 'Seminar: Geometry'},
            {'course_num': 'MATH 510', 'course_title': 'Mathematical Reasoning'},
            {'course_num': 'MATH 511',
                'course_title': 'Design and Analysis of Experiments'},
            {'course_num': 'MATH 512', 'course_title': 'Theory of Numbers'},
            {'course_num': 'MATH 513', 'course_title': 'Mathematical Statistics I'},
            {'course_num': 'MATH 514', 'course_title': 'Mathematical Statistics II'},
            {'course_num': 'MATH 515',
                'course_title': 'Mathematical Models and Applications'},
            {'course_num': 'MATH 516', 'course_title': 'Geometric Structures'},
            {'course_num': 'MATH 520',
                'course_title': 'Middle-school Mathematics in a Teaching Context with Instructional Technology'},
            {'course_num': 'MATH 522', 'course_title': 'Advanced Differential Equations'},
            {'course_num': 'MATH 530', 'course_title': 'Directed Research'},
            {'course_num': 'MATH 531',
                'course_title': 'Mathematical Connections for Secondary School Teachers'},
            {'course_num': 'MATH 541', 'course_title': 'Conceptual Algebra for Teachers'},
            {'course_num': 'MATH 551', 'course_title': 'Analysis I'},
            {'course_num': 'MATH 552', 'course_title': 'Analysis II'},
            {'course_num': 'MATH 555', 'course_title': 'Cartesian Triad'},
            {'course_num': 'MATH 558', 'course_title': 'Complex Analysis'},
            {'course_num': 'MATH 561', 'course_title': 'Abstract Algebra I'},
            {'course_num': 'MATH 562', 'course_title': 'Abstract Algebra II'},
            {'course_num': 'MATH 565',
                'course_title': 'Mathematical Modeling for Middle-School Teachers'},
            {'course_num': 'MATH 566',
                'course_title': 'Geometry: From Euclid to Modern Day'},
            {'course_num': 'MATH 571', 'course_title': 'Numerical Methods'},
            {'course_num': 'MATH 572', 'course_title': 'Numerical Linear Algebra'},
            {'course_num': 'MATH 575',
                'course_title': 'Introduction to Dynamics and Chaos'},
            {'course_num': 'MATH 580', 'course_title': 'History of Mathematics'},
            {'course_num': 'MATH 582', 'course_title': 'Computer Graphics'},
            {'course_num': 'MATH 590', 'course_title': 'Special Problems in Mathematics'},
            {'course_num': 'MATH 593', 'course_title': 'Advanced Topics in Statistics'},
        ]
        for course in courses:
            db.session.add(CoursesModel(**course))
        db.session.commit()


class ContactFormMessagesSeeder(Seeder):
    """
    This is the seeder for contact form messages.
    No other models will be affected by this.
    """

    # run() will be called by Flask-Seeder
    def run(self):
        messages = [
            {
                'name': 'Meg Finnegan',
                'email': 'mfinnegan1@gulls.salisbury.edu',
                'message': 'This should work.',
                'was_seen': False,
            },
            {
                'name': 'Justin Ventura',
                'email': 'jventura3@gulls.salisbury.edu',
                'message': 'Joe momma was so fat, not even NASA\'s super ' +
                        ' computers could fit her in storage.',
                'was_seen': False,
            },
            {
                'name': 'Jacob Duncan',
                'email': 'jduncan5@gulls.salisbury.edu',
                'message': 'OmegaLUL',
                'was_seen': True,
            }
        ]
        for message in messages:
            db.session.add(ContactFormMessage(**message))
        db.session.commit()


class ListingsSeeder(Seeder):
    """
    This is the listings seeder.  It will also create tags, which will
    affect the listing-tag table.
    """
    # run() will be called by Flask-Seeder

    def run(self):
        # ListingsSeeder Phase 1: Seed 'listings'
        listings = [
            {
                'client_id': 1,

                'position': 'Summer 2022 Software Development Engineer',

                'pos_responsibility': 'Collaborate with experienced cross-' +
                'disciplinary Amazonians to conceive, design, and bring ' +
                'innovative products and services to market.',

                'min_qualifications': 'Programming experience with at least ' +
                'one modern language such as Java, C++, or C# including ' +
                'object-oriented design.',

                'pref_qualifications': 'Experience with distributed, ' +
                'multi-tiered systems, algorithms, and relational databases.',

                'additional_info': None,

                'starred': True,

                'duration': 12,

                'app_open': '08/01/2021',

                'app_close': '12/31/2021',

                'status': 'active'
            },
            {
                'client_id': 2,

                'position': 'Software Engineering Intern Summer 2022',

                'pos_responsibility': 'You will design, test, deploy and ' +
                'maintain software solutions as you grow and evolve during ' +
                'your internship.',

                'min_qualifications': 'Experience in Software Development ' +
                'and coding in a general purpose programming language.',

                'pref_qualifications': 'Experience with data structures ' +
                'or algorithms gathered from inside or outside of school ' +
                'or work.',

                'additional_info': '(Colorado only*) Minimum salary of ' +
                '$90,000 + benefits.',

                'duration': 12,

                'app_open': '08/01/2021',

                'app_close': '12/31/2021',

                'status': 'pending'
            },
            {
                'client_id': 3,

                'position': 'Facebook University - Engineering - Summer 2022',

                'pos_responsibility': 'Work on a project with product team ' +
                'and receive coaching from an intern manager.',

                'min_qualifications': 'Knowledge of at least one programming' +
                ' language (ie: C/C++, JavaScript, Java, PHP, Ruby, Python, ' +
                'Lua, Objective C etc.)',

                'pref_qualifications': 'Demonstrated interest in science and' +
                ' technology.',

                'duration': 10,

                'app_open': '08/01/2021',

                'app_close': '12/31/2021',

                'status': 'active'
            },
            {
                'client_id': 4,

                'position': 'Software Engineering Student Team Member',

                'pos_responsibility': 'Attend weekly lectures on software ' +

                'engineering and work on a real world problem with a team.',

                'min_qualifications': 'C or better in COSC320.',
                'pref_qualifications': 'Senior standing and a passion for ' +
                'software development.',

                'additional_info': 'This course is two semesters long.',

                'duration': 14,

                'app_open': '03/26/2021',

                'app_close': '08/31/2021',

                'status': 'active'
            },
            {
                'client_id': 4,

                'position': 'SPAM asfjaslkfjlskfl',

                'status': 'rejected'
            },
            {
                'client_id': 1,

                'position': 'Software Development Engineering Intern',

                'pos_responsibility': 'Collaborate with experienced cross-' +
                'disciplinary Amazonians to conceive, design, and bring ' +
                'innovative products and services to market.',

                'pref_qualifications': 'Code',

                'status': 'inactive'
            },
            {
                'client_id': 3,

                'position': 'Software Engineering Intern',

                'status': 'pending'
            },
            {
                'client_id': 4,

                'position': 'Dr. Tu Software Engineering Project',

                'min_qualifications': 'C or better in COSC320.',

                'pref_qualifications': 'Senior standing and a passion for ' +
                'software development.',

                'additional_info': 'This course is two semesters long.',

                'duration': 14,

                'app_open': '03/26/2021',

                'app_close': '08/31/2021',

                'status': 'active'
            },
        ]
        for listing in listings:
            db.session.add(ListingsModel(**listing))
        db.session.commit()

        # ListingsSeeder Phase 2: Seed 'tags'
        tags = [
            'data structures and algorithms',
            'database',
            'web development',
            'testing/automation',
            'mobile development',
            'machine learning',
            'course'
        ]
        for tag in tags:
            db.session.add(TagsModel(tag))
        db.session.commit()

        # ListingsSeeder Phase 3: Seed 'listings_tags'
        listing_tag_pairs = [
            {
                'l_id': 1,
                't_id': 1
            },
            {
                'l_id': 1,
                't_id': 2
            },
            {
                'l_id': 1,
                't_id': 3
            },
            {
                'l_id': 2,
                't_id': 1
            },
            {
                'l_id': 2,
                't_id': 2
            },
            {
                'l_id': 2,
                't_id': 5
            },
            {
                'l_id': 3,
                't_id': 1
            },
            {
                'l_id': 3,
                't_id': 3
            },
            {
                'l_id': 3,
                't_id': 5
            },
            {
                'l_id': 4,
                't_id': 3
            },
            {
                'l_id': 4,
                't_id': 5
            },
            {
                'l_id': 4,
                't_id': 7
            },
            {
                'l_id': 6,
                't_id': 1
            },
            {
                'l_id': 6,
                't_id': 4
            },
            {
                'l_id': 7,
                't_id': 1
            },
            {
                'l_id': 8,
                't_id': 7
            },
            {
                'l_id': 8,
                't_id': 4
            },
            {
                'l_id': 8,
                't_id': 2
            }
        ]

        for listing_tag in listing_tag_pairs:
            db.session.add(Listings_TagsModel(**listing_tag))
        db.session.commit()

        listings_course_pairs = [
            {
                'l_id': 1,
                'c_id': 10
            },
            {
                'l_id': 1,
                'c_id': 17
            },
            {
                'l_id': 1,
                'c_id': 22
            },
            {
                'l_id': 3,
                'c_id': 10
            },
            {
                'l_id': 3,
                'c_id': 20
            },
            {
                'l_id': 3,
                'c_id': 22
            },
            {
                'l_id': 8,
                'c_id': 10
            },
            {
                'l_id': 8,
                'c_id': 20
            },
            {
                'l_id': 8,
                'c_id': 22
            },
            {
                'l_id': 4,
                'c_id': 5
            },
            {
                'l_id': 4,
                'c_id': 12
            },
            {
                'l_id': 4,
                'c_id': 19
            },
        ]

        for listing_course in listings_course_pairs:
            db.session.add(Listings_CoursesModel(**listing_course))

        db.session.commit()


# All seeders inherit from Seeder
class UsersSeeder(Seeder):
    """
    This is the seeder for the users.  This basically just generates
    data for admins at this point.
    """

    # run() will be called by Flask-Seeder
    def run(self):
        # Create a new Faker and tell it how to create User objects

        admins = [
            {
                'username': 'jventura3',
                'email': 'jventura3@gulls.salisbury.edu',
                'password': self.password_hash('justinventura426'),
                'is_admin': True
            },
            {
                'username': 'jduncan5',
                'email': 'jduncan5@gulls.salisbury.edu',
                'password': self.password_hash('jacobduncan426'),
                'is_admin': True
            },
            {
                'username': 'bmason3',
                'email': 'bmason3@gulls.salisbury.edu',
                'password': self.password_hash('blainemason426'),
                'is_admin': True
            },
            {
                'username': 'jtanderson',
                'email': 'jtanderson@gulls.salisbury.edu',
                'password': self.password_hash('joeanderson426'),
                'is_admin': True
            },
            {
                'username': 'gfranchi',
                'email': 'gfranchi@gulls.salisbury.edu',
                'password': self.password_hash('guliafranchi426'),
                'is_admin': True
            },
            {
                'username': 'mfinnegan1',
                'email': 'mfinnegan1@gulls.salisbury.edu',
                'password': self.password_hash('megfinnegan426'),
                'is_admin': True
            }
        ]
        for admin in admins:
            db.session.add(UsersModel(**admin))
        db.session.commit()

    def password_hash(password: str):
        """Returns the hashed password"""
        return hashlib.sha256(password.encode()).hexdigest()
