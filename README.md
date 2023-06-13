# BirdBrain.AI

Project Repository for the exam in Advanced Machine Learning at DHBW Mannheim.

To run the server, make sure you have `fastapi` and `uvicorn` installed in your environment and you are in the folder [app](/app/). Then, run the following command:

```
uvicorn main:app --reload
```

This allows you to access the app at [http://localhost:8000/](http://localhost:8000/).

FastAPI automatically generates a API documentation with swagger, which can not only be viewed at [http://localhost:8000/docs](http://localhost:8000/docs), but also tested or tried out there.
