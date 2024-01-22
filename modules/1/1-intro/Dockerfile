FROM python:3.9
# video is 3.9.1, mine is 3.9.18

RUN pip install pandas

WORKDIR /app
COPY pipeline.py pipeline.py

ENTRYPOINT ["bash"]
#ENTRYPOINT ["python", "pipeline.py"]