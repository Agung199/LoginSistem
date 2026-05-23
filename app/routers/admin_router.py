from fastapi import APIRouter, Depends
from app.dependencies.auth import admin_only

router = APIRouter(prefix="/admin", tags=["Admin"])


@router.get("/dashboard")
def admin_dashboard(current_user=Depends(admin_only)):
    return {"message": "Welcome Admin"}
