from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.dispatcher.fsm.state import State, StatesGroup

class GetPhone(StatesGroup):
    get_phone = State()
    
class question(StatesGroup):
    get_answer = State()
class mailing(StatesGroup):
    get_answer = State()