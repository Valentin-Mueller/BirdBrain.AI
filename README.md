# BirdBrain.AI

Project Repository for the exam in Advanced Machine Learning at DHBW Mannheim.

## Running the Project with Docker (used for production)

To build and run the Docker containers, run the following command in the project's root directory:

```
docker-compose up -d --build
```

To run without building (when already built) use the command without the `--build`-argument:

```
docker-compose up -d
```

To stop the containers from running, use the following command:

```
docker-compose down
```

If additionally the removal of created volumes is desired, add the argument `-v`:

```
docker-compose down -v
```

## Running the Project without Docker (used for development or when otherwise unavailable)

To run the backend server without Docker, make sure you are using `python 3.10` have `fastapi` and `uvicorn` installed in your environment and you are in the folder [backend](backend/). To install those and further requirements, use the following command first:

```
pip install -r requirements.txt
```

Then, run the following command for a development instance with hot reload:

```
uvicorn app.main:app --reload
```

The `--reload` argument can be omitted when no change is desired:

```
uvicorn app.main:app
```

Same goes for the frontend server. Provided `node.js` is installed, you can execute the following command inside the [frontend](frontend/) directory:

```
npm install
```

When the initial installation is done, run the server as shown below:

```
npm run dev
```

For a normal run:

```
npm start
```

## Accessing the Application

The frontend is running at [http://localhost:3000/](http://localhost:3000/), which is where the web-application is accessed for normal users.

You can access the backend API directly at [http://localhost:8000/](http://localhost:8000/).

FastAPI automatically generates a API documentation with swagger, which can not only be viewed at [http://localhost:8000/docs](http://localhost:8000/docs), but also tested or tried out there.

## Training Notebook and Model

You can access the training notebook directly at [https://colab.research.google.com/drive/13Cu-PLkuDb5e5b24IJsrPhc9IzwBfZit?usp=sharing).
You can access and download the model directly from [https://drive.google.com/drive/folders/1hnJDG6kKPq4EjY-3V5b0H-XjmmiKk7Kg?usp=sharing).
