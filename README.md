# BookGiveAway   A RESTful API for a Book Giveaway Service where registered users can offer books for free and
also take books that are offered by others. Non-registered users should be able to view the list of
available books.



To Run this project locally, run this steps:

1.  Clone the repository:   git clone https://github.com/your-username/BookGiveAway.git



2.  Create and activate virtual environment (it is optional, but recommended)
      python -m venv venv
      source venv/bin/activate   - for linux
      venv\Scripts\activate  - for windows

    
4. Install project dependencies:
      pip install -r requirements.txt


5. Apply database migrations:
    python manage.py makemigrations
    python manage.py migrate



6. Start the development server:
    project will be accessible at 'http://localhost:8000/'.

7. How to RUN this project in a Docker container:
    1) Build the docker image:   docker build -t bookgiveaway
    2) Run docker container: docker run -p 8000:8000 bookgiveaway
       it will be accessible at 'http://localhost:8000/'.


Thank you!!!!




     
