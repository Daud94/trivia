# API Development and Documentation Final Project

## Trivia App

Udacity is invested in creating bonding experiences for its employees and students. A bunch of team members got the idea to hold trivia on a regular basis and created a webpage to manage the trivia app and play the game, but their API experience is limited and still needs to be built out.

That's where you come in! Help them finish the trivia app so they can start holding trivia and seeing who's the most knowledgeable of the bunch. The application must:

1. Display questions - both all questions and by category. Questions should show the question, category and difficulty rating by default and can show/hide the answer.
2. Delete questions.
3. Add questions and require that they include question and answer text.
4. Search for questions based on a text query string.
5. Play the quiz game, randomizing either all questions or within a specific category.

Completing this trivia app will give you the ability to structure plan, implement, and test an API - skills essential for enabling your future applications to communicate with others.

## Starting and Submitting the Project

[Fork](https://help.github.com/en/articles/fork-a-repo) the project repository and [clone](https://help.github.com/en/articles/cloning-a-repository) your forked repository to your machine. Work on the project locally and make sure to push all your changes to the remote repository before submitting the link to your repository in the Classroom.

## About the Stack

We started the full stack application for you. It is designed with some key functional areas:

### Backend

The [backend](./backend/README.md) directory contains a partially completed Flask and SQLAlchemy server. You will work primarily in `__init__.py` to define your endpoints and can reference models.py for DB and SQLAlchemy setup. These are the files you'd want to edit in the backend:

1. `backend/flaskr/__init__.py`
2. `backend/test_flaskr.py`

> View the [Backend README](./backend/README.md) for more details.

### Frontend

The [frontend](./frontend/README.md) directory contains a complete React frontend to consume the data from the Flask server. If you have prior experience building a frontend application, you should feel free to edit the endpoints as you see fit for the backend you design. If you do not have prior experience building a frontend application, you should read through the frontend code before starting and make notes regarding:

1. What are the end points and HTTP methods the frontend is expecting to consume?
2. How are the requests from the frontend formatted? Are they expecting certain parameters or payloads?

Pay special attention to what data the frontend is expecting from each API response to help guide how you format your API. The places where you may change the frontend behavior, and where you should be looking for the above information, are marked with `TODO`. These are the files you'd want to edit in the frontend:

1. `frontend/src/components/QuestionView.js`
2. `frontend/src/components/FormView.js`
3. `frontend/src/components/QuizView.js`

By making notes ahead of time, you will practice the core skill of being able to read and understand code and will have a simple plan to follow to build out the endpoints of your backend API.

> View the [Frontend README](./frontend/README.md) for more details.

## API DOCUMENTATION

### GET '/categories'
1. Fetches dictionary of categories in which the keys are the ids and the value is the corresponding string of the category.
2. Request Arguments:None
3. Returns: An object with a single key, categories, that contains an object of id: category_string key: value pairs.

    ```{
        'categories': { '1' : "Science",
        '2' : "Art",
        '3' : "Geography",
        '4' : "History",
        '5' : "Entertainment",
        '6' : "Sports" }
    }
    ```

### GET '/questions'
1. Fetches questions paginated to 10 questions per page.
2. Request Arguments: '/questions?page=${this.state.page}'
3. Returns: An object with keys questions, totalQuestions, categories, and currentCategory with their corresponding value.

   ```
   {
       'questions': [
           {
               'id': 1,
               'question': 'This is a question',
               'answer': 'This is an answer',
               'difficulty': 5,
               'category': 2
           },
       ],
       'totalQuestions': 100,
       'success':True
       'categories': { '1' : "Science",
       '2' : "Art",
       '3' : "Geography",
       '4' : "History",
       '5' : "Entertainment",
       '6' : "Sports" },
       'currentCategory': 'History'
   }
   
### DELETE '/questions/id'
1.Delete a question using a question ID.
2.Request argument: id - integer.
3.Returns: None

### POST '/questions'
1. Creates a new question which will require the question and answer text, category, and difficulty score.
2. Arguments: None
3. Returns: None

### POST '/questions/search'
1. Fetches question based on a search term. It should return any questions for whom the search term
    is a substring of the question.
2. Arguments: search - String
3. Returns: an object with keys questions, total_questions, success and current_category with their corresponding value.

   ``` 
   {
            'questions': ['This is a question',..],
            'total_questions': 40,
            'success': True,
            'current_category': 4
        }

### GET '/categories/id/questions'
1. Fetches questions based on category
2. Arguments:id- Integer
3. Returns: an object with a single key, data, which contains an object:
   ```
   {
    'questions': [
        {
            'id': 1,
            'question': 'This is a question',
            'answer': 'This is an answer',
            'difficulty': 5,
            'category': 4
        },
    ],
    'totalQuestions': 100,
    'currentCategory': 'History'
}

### GET '/quizzes'
1. Fetches questions to play the quiz
2. Arguments: None
3. Returns a radom question in an object with key - question.
   ```
   {
      'question':{
            'id': 1,
            'question': 'This is a question',
            'answer': 'This is an answer',
            'difficulty': 5,
            'category': 4
             }
   }