import datetime
from typing import Optional
from pydantic import BaseModel, Field, PositiveInt, field_validator
from enums import CryptocurrencyListingStatusEnum, CryptocurrencySortEnum



class CoinMarketBaseResponseStatusSchema(BaseModel):
    timestamp: datetime.datetime = Field(description="Current timestamp (ISO 8601) on the server.")
    error_code: int = Field(description="An internal error code for the current error. If a unique platform error code is not available the HTTP status code is returned. null is returned if there is no error.")
    error_message: Optional[str] = Field(description="An error message to go along with the error code.")
    elapsed: int = Field(description="Number of milliseconds taken to generate this response.")
    credit_count: int = Field(description="Number of API call credits that were used for this call.")


class CoinMarketBaseResponse(BaseModel):
    status: CoinMarketBaseResponseStatusSchema


# ************************************
#
# Cryptocurrency Category
#
# ************************************


class CryptocurrencyCategoryListRequest(BaseModel):
    start: PositiveInt = Field(default=1, min=1)
    limit: PositiveInt = Field(default=10, min=1, max=5000)
    id: Optional[PositiveInt] = None
    slug: Optional[str] = None
    symbol: Optional[str] = None


class CryptocurrencyCategoryListResponse(CoinMarketBaseResponse):
    data: list["CryptocurrencyCategoryData"] = []


class CryptocurrencyCategoryData(BaseModel):
    id: str
    name: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    num_tokens: Optional[int] = None
    avg_price_change: Optional[float] = None
    market_cap: Optional[float] = None
    market_cap_change: Optional[float] = None
    volume: Optional[float] = None
    volume_change: Optional[float] = None
    last_updated: Optional[datetime.datetime] = None


class CryptocurrencyCategoryInfoRequest(BaseModel):
    id: str
    start: PositiveInt = Field(default=1, min=1)
    limit: PositiveInt = Field(default=100, min=1, max=1000)
    # convert
    # convert_id


class CryptocurrencyCategoryInfoResponse(CoinMarketBaseResponse):
    data: "CryptocurrencyCategoryInfoData" = []


class CryptocurrencyCategoryInfoData(CryptocurrencyCategoryData):
    coins: list[dict] = []


class CryptocurrencyCategoryInfoDataCoin(BaseModel):
    pass


# ************************************
#
# Cryptocurrency
#
# ************************************


class CryptocurrencyListRequest(BaseModel):
    start: PositiveInt = Field(default=1, min=1)
    limit: PositiveInt = Field(default=1, min=1, max=5000)
    listing_status: Optional[list[CryptocurrencyListingStatusEnum]] = None
    sort: Optional[CryptocurrencySortEnum] = None


class CryptocurrencyListResponse(CoinMarketBaseResponse):
    data: list["CryptocurrencyData"] = []


class CryptocurrencyData(BaseModel):
    id: PositiveInt
    rank: Optional[PositiveInt] = None
    name: Optional[str] = None
    symbol: Optional[str] = None
    slug: Optional[str] = None
    is_active: Optional[PositiveInt] = None
    first_historical_data: Optional[datetime.datetime] = None
    last_historical_data: Optional[datetime.datetime] = None
    platform: Optional["CryptocurrencyDataPlatform"] = None
    
    logo: Optional[str] = None
    date_added: Optional[datetime.datetime] = None
    date_launched: Optional[datetime.datetime] = None
    tags: Optional[list[str]] = []


class CryptocurrencyDataPlatform(BaseModel):
    id: int
    name: Optional[str] = None
    symbol: Optional[str] = None
    slug: Optional[str] = None
    token_address: Optional[str] = None


class CryptocurrencyInfoRequest(BaseModel):
    id: Optional[PositiveInt] = None
    slug: Optional[str] = None
    symbol: Optional[str] = None
    address: Optional[str] = None
    # skip_invalid
    # aux


class CryptocurrencyInfoResponse(CoinMarketBaseResponse):
    data: 'CryptocurrencyInfoData'

    @field_validator("data", mode="before")
    @classmethod
    def validate_data(cls, value: dict) -> 'CryptocurrencyInfoData':
        return list(value.values())[0]


class CryptocurrencyInfoData(BaseModel):
    id: PositiveInt
    rank: Optional[PositiveInt] = None
    name: Optional[str] = None
    symbol: Optional[str] = None
    slug: Optional[str] = None    
    logo: Optional[str] = None
    date_added: Optional[datetime.datetime] = None
    date_launched: Optional[datetime.datetime] = None
    tags: Optional[list[str]] = []
    platform: Optional["CryptocurrencyDataPlatform"] = None
    urls: Optional['CryptocurrencyDataURL'] = None


class CryptocurrencyDataURL(BaseModel):
    website: list[str] = []
    technical_doc: list[str] = []
    twitter: list[str] = []
    reddit: list[str] = []
    message_board: list[str] = []
    announcement: list[str] = []
    chat: list[str] = []
    explorer: list[str] = []
    source_code: list[str] = []
