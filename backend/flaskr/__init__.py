import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random
import sys
from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10
def paginiation(request, array):
      page = request
      start = (page - 1) * 10
      end = start + 10
      return array[start:end]
def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)


  CORS(app, resources={'/': {'origins': '*'}})

  @app.after_request
  def after_request(response):
        '''
        Sets access control.
        '''
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,PUT,POST,DELETE,OPTIONS')
        return response

  @app.route('/categories')
  def categories():
    categories = Category.query.all()
    everycat = []
    for category in categories:
      everycat.append(category.type)
    if (len(everycat) == 0):
      abort(404)
    return jsonify({
        'success': True,
        'categories': everycat
       })

  @app.route('/questions')
  def questions():
    categories = Category.query.all()
    questions = Question.query.all()
    everycat = []
    questlist = []
    
    for category in categories:
      everycat.append(category.type)
    for question in questions:
      questlist.append(question.format())
    pagination1 = paginiation(request.args.get('page',1,type=int),questlist)
    if (len(pagination1) == 0):
      abort(404)

    return jsonify({
      "success": True,
      "questions": pagination1,
      'total_questions': len(questlist),
      'categories': everycat
    })

  @app.route('/questions/<int:question_id>', methods = ['DELETE'])
  def delete(question_id):

      question = Question.query.filter_by(id=question_id).one_or_none()
      if question is None:
        abort(404)
      else:
        question.delete()
        return jsonify({
        "success": True,
        "deleted": question_id
        })

  @app.route('/questions', methods=['POST'])
  def post_question():
    body = request.get_json()
    questlist = []
    if (body.get('query')):
      
      query = body.get('query')
      result = Question.query.filter(Question.question.ilike(f'%{query}%')).all()
      for question in result:
        questlist.append(question.format())
      return jsonify({
        "success": True,
        "questions": paginiation(request.args.get('page',1,type=int),questlist),
        "count": len(result)
      })
    else:
      new_question = {
        "question": body.get('question'),
        "answer": body.get('answer'),
        "category": body.get('category'),
        "difficulty": body.get('difficulty'), 
      }
      if None in new_question.values():
        abort(400)
      question = Question(**new_question)
      question.insert()
    
      return jsonify({
        "success": True,
        "question":question.format(),
        "count":1
      })

  @app.route('/categories/<int:id>/questions')
  def get_categories(id):

  
      id = id + 1
      category = Category.query.filter_by(id=id).one_or_none()
      questions = Question.query.filter_by(category=id).all()
      questlist = []
      if (category is None):
        abort(400)
      for question in questions:
        questlist.append(question.format())
      return jsonify({
        "success": True,
        "questions": paginiation(request.args.get('page',1,type=int),questlist),
        'total_questions': len(questlist),
        'current_category': category.type
      })

  @app.route('/quizzes', methods=['POST'])
  def random_questions():
    body = request.get_json()
    category = body.get('quiz_category')
    previous = body.get('previous_questions')
    total = 0

    if((category is None)):
      abort(400)
    if (category['id'] == 0):
      questions = Question.query.all()
      total = len(questions)
    else:
      questions = Question.query.filter_by(category=category['id']).all()
      total = len(questions)
    def get_random_question():
        return questions[random.randrange(0, len(questions), 1)]

    def check_if_used(question):
        used = False
        for q in previous:
            if (q == question.id):
                used = True

        return used

    question = get_random_question()

    # check if used, execute until unused question found
    while (check_if_used(question)):
        question = get_random_question()    

    
    if (len(previous) == total):
        return jsonify({
            'success': True
        })
    return jsonify({
      'success':True,
      'question': question.format()
    })

  @app.errorhandler(404)
  def not_found(error):
      return jsonify({
          "success": False,
          "error": 404,
          "message": "resource not found"
      }), 404

  @app.errorhandler(422)
  def unprocessable(error):
      return jsonify({
          "success": False,
          "error": 422,
          "message": "unprocessable"
      }), 422

  @app.errorhandler(500)
  def unprocessable(error):
      return jsonify({
          "success": False,
          "error": 500,
          "message": "internal error"
      }), 500
  @app.errorhandler(400)
  def bad_request(error):
      return jsonify({
          "success": False,
          "error": 400,
          "message": "bad request"
      }), 400

  return app

    