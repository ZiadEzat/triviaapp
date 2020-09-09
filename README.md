# Trivia API
Test your knowledge in this trivia web game!

1) Up to 6 categories to select from.
2) Can add custom questions for specific category.
3) Search for the questions and their answers.

## Getting Started

### Installing Dependecies
There are dependecies for frontend and backend.
### Backend

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

#### Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```


### Frontend

#### Installing Node and NPM

This project depends on Nodejs and Node Package Manager (NPM). Before continuing, you must download and install Node (the download includes NPM) from [https://nodejs.com/en/download](https://nodejs.org/en/download/).

#### Installing project dependencies

This project uses NPM to manage software dependencies. NPM Relies on the package.json file located in the `frontend` directory of this repository. After cloning, open your terminal and run:

```bash
npm install
```

>_tip_: **npm i** is shorthand for **npm install**

## API Reference

### Error Handling

Errors are returned as JSON in the following format:
```
  {
      "success": False,
      "error": 404,
      "message": "resource not found"
  }
```
The API will return three types of errors:

* 400 – bad request
* 404 – resource not found
* 422 – unprocessable
* 500 - internal error

### Endpoints

#### GET /categories
* General: returns a list of all categories
* Sample: `curl -X GET 127.0.0.1:5000/categories`

```
  {
      "categories":["Science","Art","Geography","History","Entertainment","Sports"],
      "success":true
  }
```
#### GET /questions

* General: returns a list of all questions
* Sample: `curl -X GET 127.0.0.1:5000/questions`

```
{
            "categories": {
                "1": "Science", 
                "2": "Art", 
                "3": "Geography", 
                "4": "History", 
                "5": "Entertainment", 
                "6": "Sports"
            }, 
            "questions": [
                {
                    "answer": "Colorado, New Mexico, Arizona, Utah", 
                    "category": 3, 
                    "difficulty": 3, 
                    "id": 164, 
                    "question": "Which four states make up the 4 Corners region of the US?"
                }, 
                {
                    "answer": "Muhammad Ali", 
                    "category": 4, 
                    "difficulty": 1, 
                    "id": 9, 
                    "question": "What boxer's original name is Cassius Clay?"
                }, 
                {
                    "answer": "Apollo 13", 
                    "category": 5, 
                    "difficulty": 4, 
                    "id": 2, 
                    "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
                }, 
                {
                    "answer": "Tom Cruise", 
                    "category": 5, 
                    "difficulty": 4, 
                    "id": 4, 
                    "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
                }, 
                {
                    "answer": "Edward Scissorhands", 
                    "category": 5, 
                    "difficulty": 3, 
                    "id": 6, 
                    "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
                }, 
                {
                    "answer": "Brazil", 
                    "category": 6, 
                    "difficulty": 3, 
                    "id": 10, 
                    "question": "Which is the only team to play in every soccer World Cup tournament?"
                }, 
                {
                    "answer": "Uruguay", 
                    "category": 6, 
                    "difficulty": 4, 
                    "id": 11, 
                    "question": "Which country won the first ever soccer World Cup in 1930?"
                }, 
                {
                    "answer": "George Washington Carver", 
                    "category": 4, 
                    "difficulty": 2, 
                    "id": 12, 
                    "question": "Who invented Peanut Butter?"
                }, 
                {
                    "answer": "Lake Victoria", 
                    "category": 3, 
                    "difficulty": 2, 
                    "id": 13, 
                    "question": "What is the largest lake in Africa?"
                }, 
                {
                    "answer": "The Palace of Versailles", 
                    "category": 3, 
                    "difficulty": 3, 
                    "id": 14, 
                    "question": "In which royal palace would you find the Hall of Mirrors?"
                }
            ], 
            "success": true, 
            "total_questions": 19
        }
```
#### GET /categories/{id}/questions
* General: Get all questions in the specified category
* Sample: `curl -X GET 127.0.0.1:5000/categories/1/questions` 
```
  {
    "current_category": "Science", 
    "questions": [
        {
            "answer": "The Liver", 
            "category": 1, 
            "difficulty": 4, 
            "id": 20, 
            "question": "What is the heaviest organ in the human body?"
        }, 
        {
            "answer": "Alexander Fleming", 
            "category": 1, 
            "difficulty": 3, 
            "id": 21, 
            "question": "Who discovered penicillin?"
        }, 
        {
            "answer": "Blood", 
            "category": 1, 
            "difficulty": 4, 
            "id": 22, 
            "question": "Hematology is a branch of medicine involving the study of what?"
        }
    ], 
    "success": true, 
    "total_questions": 18
  }

```


#### DELETE /questions/{question_id}
* General: Deletes the specified question.
* Sample: `curl -X DELETE  127.0.0.1:5000/question/2`
```

  {
    "deleted":2,"success":true
  }

```
#### POST /questions
* General: Searches or creates new question
* Sample: `curl -H "content-type:application/json" -X POST 127.0.0.1:5000/questions -d "{"query":"box"}"`
```
{
  "count":1,
  "questions":[
  {
  "answer":"Muhammad Ali",
  "category":4,
  "difficulty":1,
  "id":9,
  "question":"What boxer's original name is Cassius Clay?"
  }],
  "success":true
  }
```

#### POST /quizzes
* General: Returns random question that's not in `previous_questions`
* Sample: `curl -H "content-type:application/json" -X POST 127.0.0.1:5000/quizzes -d "{"quiz_category":{"id":1},"previous_questions":[1,2]}"`

```
  {
    "question":{"answer":"Alexander Fleming",
                "category":1,
                "difficulty":3,
                "id":21,
                "question":"Who discovered penicillin?"},
    "success":true
  }
```

## Authors
Ziad Esam Ezat for the backend implementations
Udacity Team for the frontend implementations
