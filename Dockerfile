FROM python:3.13-alpine as builder

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PIP_DISABLE_PIP_VERSION_CHECK 1

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install --user --no-warn-script-location -r requirements.txt

FROM python:3.13-alpine

# Set environment variables
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
ENV PATH="/home/app/.local/bin:${PATH}"
ENV PYTHONPATH "${PYTHONPATH}:/home/app/web"

# Create and switch to user
RUN addgroup -S app && adduser -S app -G app \
    && mkdir -p $APP_HOME \
    && chown app:app $APP_HOME 

WORKDIR $APP_HOME

# Copy only necessary files from builder
COPY --from=builder --chown=app:app /root/.local /home/app/.local
COPY --chown=app:app . .

USER app

# Application ports
EXPOSE 8000

ENTRYPOINT ["/home/app/web/entrypoint.sh"]

#CMD ["gunicorn", "comanda_tech.wsgi:application", "--bind", "0.0.0.0:8000"]
