from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Instance of WSGI object: app
app = Flask(__name__)

# DATABASES
# Configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

nowTimeKeeper = datetime.now().strftime("%m/%d/%y, %I:%M %p")

# Database Tables
class BlogPost(db.Model): # Inherit SQLAlchemy(app).Model
    id = db.Column(db.Integer, primary_key=True)
    content =  db.Column(db.String(500), nullable=False)
    actions = db.Column(db.Integer, default=0)
    timestamp = db.Column(db.String(30), default=nowTimeKeeper)

    def __repr__(self):
        return '<Task %r>' % self.id

# Generating database file: 'database.db'
# Be sure that your current working directory is the project folder
# Go to Python shell and enter the following
# >>> from app import db 
# >>> db.create_all()
# >>> exit()

# WEB PAGE ROUTES
@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        post_content = request.form['post_content']
        new_post = BlogPost(content=post_content, timestamp=nowTimeKeeper)

        try:
            db.session.add(new_post)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue submitting your new blog post.'
    else:
        blogs = BlogPost.query.order_by(BlogPost.timestamp).all()
        return render_template('index.html', blogs=blogs)

@app.route('/updateblog/<int:id>', methods=['GET','POST'])
def update_post(id):
    blog = BlogPost.query.get_or_404(id)

    if request.method == 'POST':
        blog.content = request.form['post_content']
        try:
            db.session.commit()
            return redirect('/')
        except:
            return "There's an issue while attempting to update this post."
    else:
        return render_template('updateblog.html', blog=blog)

@app.route('/deleteblog/<int:id>')
def delete_blog(id):
    post_to_delete = BlogPost.query.get_or_404(id)

    try:
        db.session.delete(post_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return "There's an issue deleting this blog post."

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)