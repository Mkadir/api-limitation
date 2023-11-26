from fastapi import APIRouter, Request, Depends
from fastapi_versioning import VersionedFastAPI, version
from starlette.middleware import Middleware
from starlette.middleware.sessions import SessionMiddleware
from auth.oauth2 import get_current_method

router = APIRouter()


@router.get('/greet')
@version(1)
def greet(request: Request):
    return 'Hello'


@router.get('/check')
@version(1)
def check_(request: Request, token: str = Depends(get_current_method)):
    return {
        'checking': 'Successfully checked !'
    }
