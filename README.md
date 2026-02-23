# pullback_ema_bot

Execution-focused EMA pullback bot for Bybit USDT perpetuals.

Logger mode first.
Real execution later.

Philosophy:
- trader defines context
- bot executes idea
- no market interpretation

### Project structure

```
pullback-stack/
├── README.md
├── .getignore
├── .env_example
├── docker-compose.yaml
├── .env.example
│
├── api/
│   ├── Dockerfile
│   ├── requirements.txt
│   │
│   ├── app/
│   │   ├── __init__.py         
│   │   ├── main.py         

```

