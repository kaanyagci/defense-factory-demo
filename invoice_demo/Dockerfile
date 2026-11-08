FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && \
    useradd --create-home app && mkdir -p /var/lib/invoices && chown app:app /var/lib/invoices
COPY --chown=app:app . .
USER app
ENV INVOICE_DB_PATH=/var/lib/invoices/invoices.sqlite3
EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "1", "--threads", "1", "app:app"]
