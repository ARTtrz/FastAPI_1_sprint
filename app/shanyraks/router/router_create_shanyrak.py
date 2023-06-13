from fastapi import Depends, HTTPException, status

from app.utils import AppModel

from ..service import Service, get_service
from ..adapters.jwt_service import JWTData
from . import router_shanyrak
from ...auth.router.dependencies import parse_jwt_user_data



class ICreateShanyrak(AppModel):
    type: str
    price: int
    address: str
    area: int
    rooms_count: int
    description: str

class IResponseModel(AppModel):
    _id: str
    type: str
    price: int
    address: str
    area: int
    rooms_count: int
    description: str



@router_shanyrak.post(
    "/", status_code=status.HTTP_201_CREATED
)
def create_shanyrak(
    
    input: ICreateShanyrak,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
) -> dict[str, str]:


    item = svc.repository.create_shanyrak(input.dict())
    return {"message": "created"}

     
    
