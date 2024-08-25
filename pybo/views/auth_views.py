from flask import Blueprint, url_for, render_template, flash, request, session, g, jsonify, redirect
from werkzeug.security import generate_password_hash, check_password_hash
from pybo import db
from pybo.forms import UserCreateForm, UserLoginForm
from pybo.models import User, Word
import functools

bp = Blueprint('auth', __name__, url_prefix='/auth')

# 로그인 필요 데코레이터
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(*args, **kwargs):
        if g.user is None:
            _next = request.url if request.method == 'GET' else ''
            return redirect(url_for('auth.login', next=_next))
        return view(*args, **kwargs)
    return wrapped_view

# 회원 가입
@bp.route('/signup/', methods=('GET', 'POST'))
def signup():
    form = UserCreateForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if not user:
            user = User(username=form.username.data,
                        password=generate_password_hash(form.password1.data),
                        email=form.email.data)
            db.session.add(user)
            db.session.commit()
            flash('You have successfully created an account!')
            return redirect(url_for('main.index'))  # 로그인 페이지로 리디렉션
        else:
            flash('Existing username')
    return render_template('auth/signup.html', form=form)

# 로그인
@bp.route('/login/', methods=('GET', 'POST'))
def login():
    form = UserLoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        error = None
        user = User.query.filter_by(username=form.username.data).first()
        if not user:
            error = "This user does not exist."
        elif not check_password_hash(user.password, form.password.data):
            error = "Wrong password."
        if error is None:
            session.clear()
            session['user_id'] = user.id
            flash('You were successfully logged in.')
            return redirect(url_for('question._list'))  # 메인 페이지로 리디렉션
        flash(error)
    return render_template('auth/login.html', form=form)
# 로그아웃
@bp.route('/logout/')
def logout():
    session.clear()
    flash('You were successfully logged out.')
    return redirect(url_for('main.index'))  # 메인 페이지로 리디렉션

# 사용자 로그인 상태 확인
@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get(user_id)

# 검색 기능
#@bp.route('/search', methods=['POST'])
#def search():
#    searchbox = request.form.get("text")
#    result = Word.query.filter(Word.word_eng.like(searchbox + '%')).all()
#    result = [word.word_eng for word in result]
#    return jsonify(result)
