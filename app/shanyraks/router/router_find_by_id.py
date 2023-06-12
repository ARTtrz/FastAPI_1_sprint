from fastapi import Depends, HTTPException, status

from app.utils import AppModel

from ..service import Service, get_service
from ..adapters.jwt_service import JWTData
from . import router_shanyrak
from ...auth.router.dependencies import parse_jwt_user_data



class GetShanyrakResponse(AppModel):
    _id: str
    type: str
    price: int
    address: str
    area: int
    rooms_count: int
    description: str



@router_shanyrak.get(
    "/{id}", response_model = GetShanyrakResponse
)
def find_shanyrak(
    
    id:str,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
) -> dict[str, str]:


    shanyrak = svc.repository.findById(id)
    return shanyrak
    
