# How to Wrap a RESTful API with a GraphQL Endpoint

**Prerequisites:**
- Have `virtualenv` installed
```bash
pip install virtualenv
```
- Get a [Square account](https://squareup.com/signup?v=developerss)

**Steps to Setup:**
```bash
git clone https://github.com/mootrichard/pycon-square.git
```
```bash
cd pycon-square
```

```bash
touch .env
```

Put your sandbox token into your `.env` file as
```
ACCESS_TOKEN=YOUR_ACCESS_TOKEN
```
replacing `YOUR_ACCESS_TOKEN` with your access token found at [https://connect.squareup.com/apps](https://connect.squareup.com/apps)

```bash
virtualenv venv
```

```bash
source ./venv/bin/activate
```

```bash
pip install -r requirements.txt
```

```bash
python server.py
```

Open browser to [http://localhost:5000/graphql](http://localhost:5000/graphql)
