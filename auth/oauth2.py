from fastapi import Depends, HTTPException, status
from fastapi.security import APIKeyHeader
from database.db import db
from database.methods import get_user_token, update_token

oauth2_scheme = APIKeyHeader(name="greetings", description="You need key for use it !",
                             auto_error=False)


async def get_current_method(token: str = Depends(oauth2_scheme)):
    token_in_db = get_user_token(db=db, token=token)
    token_usage = token_in_db.usage if token is not None else 0
    """
    Check if the provided token is valid. If valid, return the token.

    :param token: The token to be checked.
    :return: The provided token if valid.
    :raises HTTPException: If the token is invalid.
    """
    if token is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Ohhh sh#t, Where is your access token bro ?",
            headers={"WWW-Authenticate": "Bearer"},
        )
    elif token_usage == 0:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Ohhh sh#t, Your token usage limit is ended",
            headers={"WWW-Authenticate": "Bearer"},
        )
    update_token(db=db, token=token, data={
        'usage': token_usage-1
    })
    return token_in_db.token

