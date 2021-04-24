FROM python:slim
WORKDIR people
COPY . /people/ 
RUN useradd -m -r pac && chown pac /people
RUN pip install -r requirements.txt
USER pac
CMD ["python", "app.py"]

