from fastapi import Depends, HTTPException, status
from .dependencies import parse_jwt_user_data
from app.utils import AppModel

from ..service import Service, get_service
from . import router
from ..adapters.jwt_service import JWTData

class UserUpdateData(AppModel):
    phone: str
    name: str
    city: str



@router.patch(
    "/users/me"
)
def update_profile(
    input: UserUpdateData,
    svc: Service = Depends(get_service),
    jwt_data: JWTData = Depends(parse_jwt_user_data),
):
 

    user = svc.repository.update_profile(jwt_data.user_id, input.dict())

    return user
