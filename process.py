# TODO: функция, которая загружает модель
def load_model():
    # sklearn 
    # нейронные сети
    # min-max scaler и т.п.
    pass

# TODO: передавать все параметры
def predict(params):
    # TODO: добавить вызов моделей
    model = load_model()
    
    cost = model.predict(params)
    return cost
