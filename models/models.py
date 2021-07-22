from sqlalchemy import Column, Text, Text, Integer
from models.database import Base

class Stats(Base):
    __tablename__="stats"

    id=Column(Integer,primary_key=True)
    Player=Column(Text)
    PTS=Column(Text)
    FGM=Column(Text)
    FGA=Column(Text)
    F3GM=Column(Text)
    F3GA=Column(Text)
    FTM=Column(Text)
    FTA=Column(Text)
    Oreb=Column(Text)
    DR=Column(Text)
    TR=Column(Text)
    AST=Column(Text)
    TOV=Column(Text)
    BS=Column(Text)
    EFF=Column(Text)
    OE=Column(Text)
    TS=Column(Text)
    eFG=Column(Text)
    PPP=Column(Text)

    def __init__(self,Player=None,PTS=None,FGM=None,FGA=None,F3GM=None,F3GA=None,FTM=None,FTA=None,Oreb=None,DR=None,TR=None,AST=None,TOV=None,BS=None,EFF=None,OE=None,TS=None,eFG=None,PPP=None):
        self.Player=Player
        self.PTS=PTS
        self.FGM=FGM
        self.FGA=FGA
        self.F3GM=F3GM
        self.F3GA=F3GA
        self.FTM=FTM
        self.FTA=FTA
        self.Oreb=Oreb
        self.DR=DR
        self.TR=TR
        self.AST=AST
        self.TOV=TOV
        self.BS=BS
        self.EFF=EFF
        self.OE=OE
        self.TS=TS
        self.eFG=eFG
        self.PPP=PPP

