# # from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import create_engine

# engine = create_engine('sqlite:///\\flaskApp4\\app\\sqlite\\database.db')


# def load_eliteBatters():
#     with engine.connect() as conn:
#         statsEB = conn.execute('SELECT * FROM elite_batters')
#         stats_dict = []
#         for stat in statsEB.all():
#             stats_dict.append(dict(stat))
#         return stats_dict


# def load_eliteBowlers():
#     with engine.connect() as conn:
#         statsEBo = conn.execute('SELECT * FROM elite_bowlers')
#         stats_dict = []
#         for stat in statsEBo.all():
#             stats_dict.append(dict(stat))
#         return stats_dict


# def load_eliteARs():
#     with engine.connect() as conn:
#         statsAR = conn.execute('SELECT * FROM elite_allrounders')
#         stats_dict = []
#         for stat in statsAR.all():
#             stats_dict.append(dict(stat))
#         return stats_dict


# def load_batter(id):
#     with engine.connect() as conn:
#         statsEB = conn.execute(
#             'SELECT * FROM elite_batters WHERE id= :val', val=id)
#         row = statsEB.all()
#         if row == 0:
#             return None
#         else:
#             return dict(row[0])


# def load_bowler(id):
#     with engine.connect() as conn:
#         statsEBo = conn.execute(
#             'SELECT * FROM elite_bowlers WHERE id= :val', val=id)
#         row = statsEBo.all()
#         if row == 0:
#             return None
#         else:
#             return dict(row[0])


# def load_AR(id):
#     with engine.connect() as conn:
#         statsAR = conn.execute(
#             'SELECT * FROM elite_allrounders WHERE id= :val', val=id)
#         row = statsAR.all()
#         if row == 0:
#             return None
#         else:
#             return dict(row[0])


# def load_article(id):
#     with engine.connect() as conn:
#         statsEB = conn.execute('SELECT * FROM articles WHERE id= :val', val=id)
#         row = statsEB.all()
#         if row == 0:
#             return None
#         else:
#             return dict(row[0])
