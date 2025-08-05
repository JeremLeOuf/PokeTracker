from pydantic import BaseModel, EmailStr, constr
from typing import Optional
from datetime import date

class UserCreate(BaseModel):
    username: constr(pattern=r'^\w+$', min_length=3, max_length=50)
    email: EmailStr
    password: constr(min_length=6)

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class UserLogin(BaseModel):
    username: str
    password: str

class PokemonSetBase(BaseModel):
    id: str
    name: str
    series: str
    printed_total: int | None
    total: int | None
    ptcgo_code: str | None
    release_date: date | None

    class Config:
        from_attributes = True

class PokemonSetCreate(PokemonSetBase):
    pass

class PokemonSet(PokemonSetBase):
    id: int