"""
from flask import Blueprint, render_template, request
from pybo.models import Question

bp = Blueprint('search', __name__, url_prefix='/search')

@bp.route('/', methods=['GET'])
def search():
    # 검색어 가져오기

    query = request.args.get('q', '')

    # 검색어를 포함하는 질문 검색
    questions = Question.query.filter(Question.subject.ilike(f'%{query}%')).all()

    # 검색 결과를 템플릿에 전달하여 표시
    return render_template('search_form.html', query=query)


@bp.route('/search_results', methods=['GET'])
def result():

    query = request.args.get('q', '')

    questions = Question.query.filter(Question.subject.ilike(f'%{query}%')).all()

    return render_template('search_results.html', query=query)
"""

from flask import Blueprint, render_template, request
from pybo.models import Question

bp = Blueprint('search', __name__, url_prefix='/search_list.html')

@bp.route('/list/')
def _list():
    page = request.args.get('page', type=int, default=1)
    query = request.args.get('query', '')
    if query:
        # 검색어를 포함하는 질문 검색
        question_list = Question.query.filter(Question.subject.contains(query)).order_by(Question.create_date.desc())
    else:
        # 검색어가 없을 경우 모든 질문 가져오기
        question_list = Question.query.order_by(Question.create_date.desc())
    question_list = question_list.paginate(page=page, per_page=10)
    return render_template('question/question_list.html', question_list=question_list, query=query)
