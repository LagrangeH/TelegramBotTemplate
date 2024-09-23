from aiogram import Dispatcher, Router


def register_handlers(dp: Dispatcher) -> None:
    main_router = Router()

    main_router.include_router(...)

    dp.include_router(main_router)
