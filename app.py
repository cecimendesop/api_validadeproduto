from flask import Flask, jsonify
from flask_pydantic_spec import FlaskPydanticSpec
import datetime
from datetime import datetime
from dateutil.relativedelta import relativedelta

app = Flask(__name__)

spec = FlaskPydanticSpec( 'flask',
                          title = 'Flask API - SENAI',
                          version = '1.0.0',)
spec.register(app)

@app.route('/<tipo>/<quantidade>/')
def validacao(tipo, quantidade):
    """
    Valida o tipo (anos, meses, semanas e dias) para determinar validade a partir da quantidade

    #Endpoint:
    'GET /<tipo>/<quantidade>/'

    :param tipo: anos, meses, semanas e dias
    :param quantidade: número de anos, meses, semanas ou dias
    :return: A data de fabricação em anos, meses, semanas ou dias e determina a validade

    #Resposta:
    {
        "Fabricação em": datetime.today().strftime('%d/%m/%Y'),
        "Validade": validade.strftime('%d/%m/%Y'),
    }


    """
    prazo = int(quantidade)
    meses = datetime.today()+relativedelta(months=prazo)
    #ano
    anos = datetime.today()+relativedelta(years=prazo)
    #semanas
    semanas = datetime.today()+relativedelta(weeks=prazo)
    #dias
    dias = datetime.today()+relativedelta(days=prazo)

    if tipo == 'meses':
        validade = meses
    elif tipo == 'anos':
        validade = anos
    elif tipo == 'semanas':
        validade = semanas
    elif tipo == 'dias':
        validade = dias

    return jsonify ({
        "Fabricação em": datetime.today().strftime('%d/%m/%Y'),
        "Validade": validade.strftime('%d/%m/%Y'),
    })



if __name__ == '__main__':
    app.run(debug=True)