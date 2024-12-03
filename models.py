class DuplaMotTroLinhaFixa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    linha_fixa = db.Column(db.String(50), nullable=False)

class HorarioEMotoristaRio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    linha_fixa = db.Column(db.String(50), nullable=False)

class HorariosManhuacu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cidade = db.Column(db.String(50), nullable=False)
    horario = db.Column(db.String(5), nullable=False)

class MotoristaRodizio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    rodizio = db.Column(db.String(50), nullable=False)

class TrocadoresRodizio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    rodizio = db.Column(db.String(50), nullable=False)
