# Wrestling Sorted

API to retrieve and sort highlights from YouTube for wrestling tv shows. Currently offline.

## Table of Contents

1. [API Docs](#api-docs)
2. [Installation](#installation)
3. [Local Development](#local-development)
4. [Usage](#usage)

## API Docs

- See the latest [Swagger docs](https://wrestling-sorted-api-7f40c4b67ace.herokuapp.com/docs/)
- It can be accessed locally at http://127.0.0.1:8000/docs/
- There is only one endpoint available at the moment

### Endpoint - List all highlights for given episode of a TV show.

- `/v1/tv_shows/1/episodes/2023-12-18/highlights/`

```json
{
  "status": "success",
  "data": {
    "tv_show": "Monday Night Raw",
    "episode_date": "2023-12-18",
    "total_highlights": 2,
    "highlights": [
      {
        "id": 85,
        "title": "Raw’s most explosive moments: Raw highlights, Dec. 18, 2023",
        "url": "https://www.youtube.com/watch?v=8NBYuPBQ_9s",
        "thumbnail_default": "https://i.ytimg.com/vi/8NBYuPBQ_9s/default.jpg",
        "thumbnail_medium": "https://i.ytimg.com/vi/8NBYuPBQ_9s/mqdefault.jpg",
        "thumbnail_high": "https://i.ytimg.com/vi/8NBYuPBQ_9s/hqdefault.jpg"
      },
      {
        "id": 86,
        "title": "Niven & Green vs. Chance & Carter: Raw, Dec. 18, 2023",
        "url": "https://www.youtube.com/watch?v=9zmUs6N3pm4",
        "thumbnail_default": "https://i.ytimg.com/vi/9zmUs6N3pm4/default.jpg",
        "thumbnail_medium": "https://i.ytimg.com/vi/9zmUs6N3pm4/mqdefault.jpg",
        "thumbnail_high": "https://i.ytimg.com/vi/9zmUs6N3pm4/hqdefault.jpg"
      }
    ]
  }
}
```

## Installation

### Prerequisites

- Docker Compose
- Google Developer API key with access to the YouTube Data API v3

### Steps

1. Clone the repo

    ```bash
    git clone git@github.com:revalgovender/wrestling-sorted.git
    ```
2. Copy `.env.example.local` to `.env`

    ```bash 
    cp .env.example.local .env
    ```

3. Complete `.env` with your own values
4. Build the images

    ```bash
    make build
    ```
5. Run the containers

    ```bash
    make run
    ```

## Usage

- Import highlights from YouTube:

  ```bash
  make import_raw
  ```