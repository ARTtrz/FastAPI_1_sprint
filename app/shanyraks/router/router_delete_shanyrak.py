from fastapi import Depends, HTTPException, status
from ...auth.router.dependencies import parse_jwt_user_data
from app.utils import AppModel

from ..service import Service, get_service
from . import router_shanyrak
from ..adapters.jwt_service import JWTData




@router_shanyrak.delete(
    "/{id}", 
)
def delete_shanyrak(
    id: str,
    
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
    
    
):
 

    shanyrak = svc.repository.delete_shanyrak(id)

    return {"ok"}

