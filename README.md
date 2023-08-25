# Word Counter

Index:

1. [Overview](#Overview)
1. [Installation with Docker Compose](#installation-with-docker-compose)
1. [Manual Installation](#manual-installation)
	1. [UI](#ui)
	1. [API](#api)
1. [API Tests](#api-tests)
1. [Future improvements](#future-improvements)
1. [Observations](#observations)
## Overview

A simple form where a user may input some text. If so, then the result of the word count must be displayed back to the user.

Built with:
- UI:
	- [Vuejs](https://vuejs.org/): 3.3.4
	- [Axios](https://axios-http.com/docs/intro): 1.4.0
	- [FormKit](https://formkit.com/getting-started/what-is-formkit): 0.18.4 
- API:
	- [Python](https://www.python.org/): 3.10.11
	- [FastAPI](https://fastapi.tiangolo.com/): 0.101.1
	- [uvicorn](https://www.uvicorn.org/): 0.23.2
	- [pytest](https://docs.pytest.org/en/7.4.x/): 7.4.0

Commit messages were written using [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) specification.

## Installation with Docker Compose

Before proceeding, make sure that [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/) are installed.

In the root folder, execute:

```
$ docker-compose build
```

Then:
```
$ docker-compose up
```

The project should be available at `http://127.0.0.1:4173`.


## Manual installation

### UI

Before proceeding, make sure that you have [npm](https://www.npmjs.com/) installed.

Move to the `ui` directory:

```
$ cd ui
```

Then run:

```
$ npm install
```

Finally:

```
$ npm run dev
```

Check if the ui is available at `http://127.0.0.1:5173`.

### API

To run the API component manually, first make sure that you have `poetry` installed:

```
$ pip install poetry
```

Set `poetry` flag `in-project` to `true` with:

```
$ poetry config virtualenvs.in-project true
```

Then move to the `api` directory:

```
$ cd api
```

Now execute:

```
$ poetry install
```

Activate poetry's new virtual environment:

```
$ source .venv/bin/activate
```

And finally:

```
(.venv)$ uvicorn word_counter.main:app --host 0.0.0.0 --port 8000
```

Check if the api is available at `http://127.0.0.1:8000/docs`. At the root (`http://127.0.0.1:8000`) you should also be redirected to `/docs`.
## API Tests

To execute the API's test suite, first follow the manual installation steps (you won't need to execute the project, as described in the last step).

Inside the api's directory, and with the virtual environment active, just run:

```
(.venv) $ pytest tests -v
```

The output of the execution should be prompted out.
## Future improvements

- **Characters separated by white spaces will be counted as words:**
	- Everything between white spaces (except for the first and the last words), is considered as a word;
	- If someone inputs a text like `This is some text .`, the dot would be also counted as a word;
	- So even though both sentences `This is some text.` and `This is some text .` are essencialy the "same", the latter would return a word count of 6 because it is counting the last period.
- **UI unit tests:**
	- Since this is a job for backend development, I didn't mind including unit tests for the interface;
	- Although it is a simple ui, in a real application unit tests should be included;
	- In a real application there should be also a automatic pipeline to execute these unit tests (along with other tests as well).
- **Alert could be replaced by a proper component:**
	- Thinking on the user, the word count should probably displayed in a proper component such as a card;
	- Whenever the user inputs some text and hits "Submit" -> the word count is displayed at the card;
	- The behavior of no text input should remain the same as now;
	- But again, due to the scope of the job I think this is a pretty reasonable solution.

## Observations

- **Logging on the API service:**
	- I didn't mind including logs on the API service because of the following two reasons:
		- There is too little code on the API service (a single file with 36 lines) to justify the usage of logs;
		- `uvicorn` has already some built-in logs, e.g.:
		
			```INFO:     172.18.0.1:40442 - "OPTIONS /word-count HTTP/1.1" 200 OK```
- **Scalability:**
	- Since we are talking about two light-weight compoments, I think that a serverless approach (on AWS) would fit our needs:
		- UI: deployed on a S3 bucket and take advantage on CloudFront's global edge network;
		- API: use Amazon's API Gateway to invoke an AWS Lambda function - we can easily increase the amount of concurrent functions and set API throtling limits according to our needs.
- **Deploys & CI/CD:**
	- A pipeline on GitHub Actions (since we are using GitHub) should execute the proper tests (unit and integration) automatically;
	- We could also include formatting steps, e.g.: run `black`, `isort` and `flake8`;
	- Infrastructure should be created and updated using *infrastructure-as-code* tools, such as [Terraform](https://www.terraform.io/) or [Ansible](https://www.ansible.com/);
	- If we choose the serverless approach we could also user [serverless](https://www.serverless.com/) framework.
