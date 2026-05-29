# MEMBUAT MAIN FASTAPI app
from fastapi import FastAPI, Depends
from app.database import Base, engine
from app.models.user_model import User
from app.database import get_db
from app.auth import require_admin
from sqlalchemy.orm import Session

# from app.database import create_user_table
from app.middleware import LoggingMiddleware
from app.routers.auth_router import router as auth_router

from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.responses import HTMLResponse


app = FastAPI()


@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)


# @app.on_event("startup")
# def startup():
#    create_user_table()


app.add_middleware(LoggingMiddleware)
app.include_router(auth_router)


templates = Jinja2Templates(directory="app/templates")

app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.get("/register-page", response_class=HTMLResponse)
async def register_page(request: Request):

    return templates.TemplateResponse(request=request, name="register.html")


@app.get("/", response_class=HTMLResponse)
async def login_page(request: Request):

    return templates.TemplateResponse(request=request, name="login.html")


@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):

    return templates.TemplateResponse(request=request, name="dashboard.html")


@app.get("/admin", response_class=HTMLResponse)
async def admin(request: Request):

    return templates.TemplateResponse(request=request, name="admin.html")


@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()

    return {"data": users}


@app.get("/admin")
def admin_dashboard(current_user: User = Depends(require_admin)):

    return {
        "message": "Welcome Admin",
        "user": current_user.email,
        "role": current_user.role,
    }


app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")
