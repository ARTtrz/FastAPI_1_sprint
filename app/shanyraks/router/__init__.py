from fastapi import APIRouter

from app.utils import import_routers

router_shanyrak = APIRouter()

import_routers(__name__)
