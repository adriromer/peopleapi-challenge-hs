# peopleApiChallenge
Simple People api for HungerStation Challenge developed in Python with Flask Framework and SQLArchemy library ORM.

**Application Pod Details:**

**- Ingress:**
Ingress is created with the following example host value: peopleapi-challenge-hs.local
Please modified accordingly in the Helm Value.yml file section ingress.

**- Endpoints:**
all endpoints are declared in http;//peopleapi-challenge-hs.local/ui as swagger is implemented.

**DataBase Pod Details:**
The database used is a Generic Image of MariaDB, not PVC was defined therefore all information added is destroyed if the pod is restarted. The focused of the project was on the Application Pod.

**Docker compose**
For docker compose run "docker-compose" from the base dir.

**Helm Chart**
To install the helm chart run the folloing bash script: ./peopleapi-challenge-hs.sh
