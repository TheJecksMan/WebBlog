FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY ./backend/requirements.txt .
RUN python -m pip install -r requirements.txt --no-cache-dir

WORKDIR backend/app
COPY ./backend/app /app

EXPOSE 8000

CMD ["uvicorn", "main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8000", "--workers", "4", "--timeout-keep-alive", "30", "--no-server-header"]
