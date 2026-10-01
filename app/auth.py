from datetime import datetime, timedelta, timezone

from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext


router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


SECRET_KEY = "devops-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60


pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)


# Временно храним пользователей здесь.
# Позже можно вынести в PostgreSQL.
users = [
    {
        "username": "admin",
        "hashed_password": pwd_context.hash("admin123"),
        "role": "admin"
    },
    {
        "username": "buyer",
        "hashed_password": pwd_context.hash("buyer123"),
        "role": "buyer"
    }
]


def find_user(username: str):
    for user in users:
        if user["username"] == username:
            return user

    return None


def verify_password(
    plain_password: str,
    hashed_password: str
):
    return pwd_context.verify(
        plain_password,
        hashed_password
    )


def create_access_token(
    username: str,
    role: str
):
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload = {
        "sub": username,
        "role": role,
        "exp": expire
    }

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )


@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends()
):
    user = find_user(form_data.username)

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Неверный логин или пароль"
        )

    if not verify_password(
        form_data.password,
        user["hashed_password"]
    ):
        raise HTTPException(
            status_code=401,
            detail="Неверный логин или пароль"
        )

    token = create_access_token(
        username=user["username"],
        role=user["role"]
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }


def get_current_user(
    token: str = Depends(oauth2_scheme)
):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        username = payload.get("sub")
        role = payload.get("role")

        if username is None or role is None:
            raise HTTPException(
                status_code=401,
                detail="Некорректный токен"
            )

        return {
            "username": username,
            "role": role
        }

    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Некорректный или просроченный токен"
        )


def admin_required(
    user=Depends(get_current_user)
):
    if user["role"] != "admin":
        raise HTTPException(
            status_code=403,
            detail="Недостаточно прав"
        )

    return user