from fastapi import FastAPI, Request
from fastapi.params import Depends
from fastapi_versioning import VersionedFastAPI, version
from starlette.middleware import Middleware
from starlette.middleware.sessions import SessionMiddleware
from starlette_admin.contrib.sqla import Admin, ModelView
from auth.panel import UsernameAndPasswordProvider
from database.db import engine
from auth.oauth2 import get_current_method
from routers.base import router as base_router
from models.mbase import Users

app = FastAPI(
    title='Road 23',
    description='Full api for road24 similarity 1x1 ',
    middleware=[
        Middleware(SessionMiddleware, secret_key='mysecretkey')
    ]
)
app.include_router(router=base_router)
app = VersionedFastAPI(app,
                       version_format='{major}',
                       prefix_format='/v{major}',
                       description="Full api for road24 similarity 1x1",
                       middleware=[
                           Middleware(SessionMiddleware, secret_key='mysecretkey')
                       ]
                       )

admin = Admin(engine, base_url='/not-admin', title="API Dashboard", auth_provider=UsernameAndPasswordProvider(),
              middlewares=[Middleware(SessionMiddleware, secret_key='mysecretkey')])


class UserBaseAdmin(ModelView):
    name = "User"
    label = "API User"
    icon = "fa fa fa-user"


admin.add_view(UserBaseAdmin(Users))


admin.mount_to(app)