from flask import Flask, render_template, request, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import abort

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'
# Configure the SQLAlchemy database URI. You should replace 'sqlite:///posts.db' with your actual database URI.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_BINDS'] = {
    'login': 'sqlite:///login.db'
}

db = SQLAlchemy(app)


# Define the Post model
class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.now())
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)
    
class Login(db.Model):
    __bind_key__ = 'login' 
    id_log = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(50), unique=True, nullable=False)
    Password = db.Column(db.String(50), nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/')
def login_page():
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['Confirm_password']
        # Перевірка чи користувач з таким ім'ям вже існує у базі даних
        existing_user = Login.query.filter_by(Name=username).first()
        if password != confirm_password:
            flash('passwords do not match')
            return redirect(url_for('register_page'))
        
        if existing_user:
            flash('Username already taken. Please choose a different username.', 'error')
            return redirect(url_for('register_page'))

        # Якщо користувача немає, збереження його даних у базі даних
        new_login = Login(Name=username, Password=password)
        db.session.add(new_login)
        db.session.commit()

        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('login_page'))

    return render_template('register.html')

@app.route('/login', methods=['POST'])
def login():    
    username = request.form['Name']
    password = request.form['Password']

    existing_user = Login.query.filter_by(Name=username).first()
    
    if existing_user:
        # Перевірка правильності пароля
        if existing_user.Password == password:
            flash('Login successful!', 'success')
            return redirect(url_for('index',username=username))
        else:
            flash('Incorrect password. Please try again.', 'error')
            return redirect(url_for('login_page'))
    else:
        flash('User does not exist. Please register.', 'error')
        return redirect(url_for('login_page')) 


@app.route('/post')
def index():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)  


@app.route('/<int:post_id>')
def post(post_id):
    post = Post.query.get(post_id)
    if post:
        return render_template('post.html', post=post)
    else:
        abort(404)


@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            new_post = Post(title=title, content=content)
            db.session.add(new_post)
            db.session.commit()
            return redirect(url_for('index'))

    return render_template('create.html')


@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    post = Post.query.get(id)
    if not post:
        abort(404)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            post.title = title
            post.content = content
            db.session.commit()
            return redirect(url_for('index'))

    return render_template('edit.html', post=post)


@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    post = Post.query.get(id)
    if post:
        db.session.delete(post)
        db.session.commit()
        flash('"{}" was successfully deleted!'.format(post.title))
        return redirect(url_for('index'))
    else:
        abort(404)


if __name__ == '__main__':
    app.run(debug=True, port=5001)
