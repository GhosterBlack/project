from fastapi import FastAPI
from app.routes.user_routes import router as user_router
from fastapi.responses import JSONResponse
from fastapi import Request
from app.core.exceptions import ApiException


app = FastAPI()

@app.exception_handler(ApiException)
async def api_exception_handler(
    request: Request,
    exc: ApiException
):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "message": exc.message
        }
    )

app.include_router(
    user_router,
    prefix="/users",
    tags=["Users"]
)

@app.get("/")
async def root():
    return {
        "success": True
    }