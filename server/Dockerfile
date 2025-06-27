# First stage: builder - builds python wheels
FROM python:3.9-alpine AS builder

RUN apk add --no-cache build-base

WORKDIR /app

COPY requirements.txt .

RUN pip wheel --no-cache-dir --wheel-dir /wheels -r requirements.txt

# Second stage: final runtime image
FROM python:3.9-alpine

# Create app user and group
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

WORKDIR /app

# Copy built wheels from builder stage
COPY --from=builder /wheels /wheels

# Install wheels
RUN pip install --no-cache /wheels/*

COPY . .

USER appuser

EXPOSE 5000

CMD ["python", "run.py"]
