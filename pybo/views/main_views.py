from flask import Blueprint, url_for, render_template, jsonify, request, redirect
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello')
def hello_pybo():
    return 'Hello, pybo!'
if __name__ == "__main__":
    bp.run(ssl_context='adhoc')

@bp.route('/')
def index():
    return redirect(url_for('question._list'))

#@bp.route('/search', methods=['GET', 'POST'])
#def search():
#    if request.method == 'POST':
#        # 검색 기능 구현
#        search_text = request.form['search_text']
#        # 검색 결과 처리
#        return jsonify({'result': 'Search results for "{}"'.format(search_text)})
#    else:
#        # 검색 폼 템플릿 렌더링
#        return render_template('search_form.html')