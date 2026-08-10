# from fastapi import FastAPI

# from app.core.config import settings

# app = FastAPI(
#     title=settings.APP_NAME,
#     version=settings.APP_VERSION,
# )


# @app.get("/")
# def root():
#     return {
#         "message": settings.APP_NAME,
#         "version": settings.APP_VERSION,
#         "debug": settings.DEBUG,
#     }


from fastapi import FastAPI

from app.api.router import api_router
from app.core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)

app.include_router(api_router)