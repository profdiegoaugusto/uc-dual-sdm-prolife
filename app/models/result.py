from sqlalchemy import Column, BigInteger, DateTime, ForeignKey, Numeric, String, Table

from sqlalchemy.orm import relationship
from sqlalchemy.sql.functions import current_timestamp
from app.models.test_result import TestResult

from app import db

Base = db.make_declarative_base(TestResult)
test_result = Table('Test_result', Base.metadata,
                    Column("id_test", BigInteger, ForeignKey("Test.id_test")),
                    Column("id_result", BigInteger, ForeignKey("Result.id_result"))
                    )


class Result(db.Model):
    __tablename__ = 'Result'
    id_result = Column(BigInteger, primary_key=True)
    date_hour = Column(DateTime, server_default=current_timestamp())
    measured_value = Column(Numeric(10, 2), nullable=False)
    result_desc = Column(String(128), nullable=False)
    id_employee = Column(BigInteger, ForeignKey('Employee.id_employee'), nullable=False)
    employee = relationship("Employee", uselist=False, backref="Result", lazy=True)
    id_device = Column(BigInteger, ForeignKey('Device.id_device'), nullable=False)
    device = relationship("Device", uselist=False, backref="Result", lazy=True)
    tests = relationship('Test', secondary="Test_result", backref="Tests", lazy="joined")

    # align with the teacher the business rules
    def __init__(self, measured_value, result_desc, id_employee, id_device, tests) -> None:
        self.measured_value = measured_value
        self.result_desc = result_desc
        self.id_employee = id_employee
        self.id_device = id_device
        self.tests = tests

    @staticmethod
    def get_results(id_device, id_employee, date_hour):
        if id_device:
            if date_hour and id_employee:
                result_list = (Result.query.filter(Result.id_device == id_device)). \
                    filter(Result.id_employee == id_employee). \
                    filter(Result.date_hour.like(date_hour))
            elif date_hour:
                result_list = (Result.query.filter(Result.id_device == id_device)) \
                    .filter(Result.date_hour.like(date_hour))
            elif id_employee:
                result_list = (Result.query.filter(Result.id_device == id_device)).filter(
                    Result.id_employee == id_employee)
            else:
                result_list = Result.query.filter(Result.id_device == id_device)

        elif id_employee:
            if date_hour:
                result_list = (Result.query.filter(Result.id_employee == id_employee)).filter(
                    Result.date_hour.like(date_hour))
            else:
                result_list = Result.query.filter(Result.id_employee == id_employee)
        elif date_hour:
            result_list = Result.query.filter(Result.date_hour.like(date_hour)).all()
        else:
            result_list = Result.query.all()

        return result_list

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __repr__(self):
        return f'<Result: {self.result}'
