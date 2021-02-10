from src.dao.session import Session
from src.models.base_model import BaseModel


class BaseDao:
    def __init__(self, type_model) -> None:
        self.__type_model = type_model

    def save(self, model: BaseModel) -> BaseModel:
        with Session() as session:
            session.add(model)
            session.commit()
            session.refresh(model)
            return model

    def read_all(self) -> list:
        with Session() as session:
            result = session.query(self.__type_model).order_by('id').all()
            return result

    def read_by_id(self, id: int) -> BaseModel:
        if isinstance(id, int):
            with Session() as session:
                result = session.query(self.__type_model).filter_by(id_=id).first()
            return result
        else:
            raise TypeError("ID must be an integer number!")

    def delete(self, model: BaseModel) -> None:
        with Session() as session:
            session.delete(model)
            session.commit()
