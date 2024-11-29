# Spotify Playlist Data Pipeline with Apache Airflow

This project automates the process of fetching the top 50 most played tracks globally from Spotify and stores the data in MongoDB using Apache Airflow for orchestration.

## Overview

The pipeline has three main steps:
1. **Obtain the Access Token**: Retrieve the Spotify API access token using `client_id` and `client_secret`.
2. **Fetch Playlist Data**: Use the access token to query the Spotify API and retrieve the top 50 tracks from the "Top 50 Global" playlist.
3. **Store Data in MongoDB**: Save the playlist data as a JSON object in MongoDB for later analysis.

The process is orchestrated using **Apache Airflow**, and the data is stored in **MongoDB** using a **MongoHook**.

## Technologies Used

- **Apache Airflow**: For orchestrating the pipeline.
- **Spotify API**: To fetch the top 50 tracks.
- **MongoDB**: For storing the fetched data.
- **Python**: As the main programming language, with requests to interact with the Spotify API and MongoDB.
- **Docker**: To containerize the Airflow environment.

## Prerequisites

Before running the project, you need to:

1. **Set up an account on MongoDB**: Create a MongoDB cluster, a database, and a collection.
2. **Create a Spotify Developer Account**: Obtain `client_id` and `client_secret` to access the Spotify API.
3. **Configure Apache Airflow**: Set up Airflow to run the pipeline, including necessary connections and variables.

## Setup

1. Clone this repository.
2. Set up your MongoDB and Spotify credentials in Apache Airflow as variables.
3. Use the provided **Docker Compose** setup to launch Airflow with the necessary dependencies.
4. Run the Airflow DAG manually for the first time and let Airflow handle the daily execution automatically.

## How to Run

1. **Clone the repository:**

    ```bash
    git clone https://github.com/lucasbral/spotify_pipeline.git
    cd spotify_pipeline
    ```

2. **Build and run the Docker container:**

    ```bash
    docker-compose up --build
    ```

3. **Access the Airflow UI:**

    Open your browser and go to `http://localhost:8080`. Log in with the default credentials (`airflow/airflow`).

4. **Trigger the DAG manually**: Once the DAG is triggered, Airflow will automatically fetch the data daily.

## MongoDB

The fetched data will be stored in the MongoDB database in the `spotify` collection. The document will include details like the track name, artist, and the time the data was fetched.

## Blog Post

For a detailed explanation of how this pipeline works, check out the [blog post](https://lucasbral.github.io/posts/airflow_spotify/).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
