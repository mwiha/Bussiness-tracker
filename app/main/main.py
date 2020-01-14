from flask import Flask,render_template,redirect
from werkzeug.security import generate_password_hash,check_password_hash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm 
from wtforms import StringField,BooleanField, PasswordField
from wtforms.validators import InputRequired,Email,Length
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager,UserMixin,login_user,login_required,logout_user,current_user


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisissuppossedtobesecret!'
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:////mnt/c/users/alice/Documents/login-example/ database.db'
Bootstrap(app)
db =SQLAlchemy (app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view ='login'

class user(UserMixin,db.Model):
    id =db.Column(db.Integer,primary_key=True)
    username =db.Column(db.String(15),unique=True)
    email =db.Column(db.String(50),unique=True)
    password =db.Column(db.String(80))
    
@login_manager.user_loader
def load_user(user_id):
    return user.query.get(int(user_id))

class Loginforms(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=4, max=15)])
    remember =BooleanField('remember me')
    
    
class Registerform(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message ='Invalid email'), Length(max=50)])  
    username = StringField('username', validatiors=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validatiors=[InputRequired(), Length(min=4, max=15)])  


@app.route('/')
@app.route("/index")
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET','POST'])
def login():
    form =Loginform()
    if form.validate_on_submit():
        user =user.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_harsh(user.password,form.password.data):
            # if user.password == form.password.data:
            #    login_user(user,remember=form.remember.data)
              return redirect(url_for('dashboard'))
            
        return '<h1>Invalid username or password<h1>'  
            # return '<h1> "form.username.date +'' + form.password.data + '<h1>"
    return render_template(login.html, form=form)


@app.route('/signup', methods=['GET','POST'])
def signup():
    form = Registerform()
    
    if form.validate_on_submit():
        harsh_password = generate_password_harsh(form.password.data, method ='sha256')
        new_user = user( username =form.username.data, email=form.email.data,password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        
        return '<h1>New user has been created!'
        # return '<h1> "form.username.date +'' + form.email.data+ '' + form.password.data + '<h1>"
    return render_template(signup.html, form=form)


@app.route('/dashboard')
@login_required
def dashboard():
    return render_template(dashboard.html,name=current_user.userename)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
    
    
if __name__== '__main__':
    app.run(debug=True)