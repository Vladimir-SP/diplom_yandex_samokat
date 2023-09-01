from stand import create_order, get_order_by_track

def test_get_order_by_track():
    # Создаем заказ и получаем трекинговый номер
    track = create_order()

    # Проверяем, что трекинговый номер не является пустым
    assert track is not None

    # Получаем статус код и JSON-ответ при запросе информации о заказе по трекинговому номеру
    status_code, _ = get_order_by_track(track)

    # Проверяем, что статус код равен 200 (успешный запрос)
    assert status_code == 200
