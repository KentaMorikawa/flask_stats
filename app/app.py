from flask import Flask,render_template,request
from models.models import Stats
import pandas as pd
import matplotlib.pyplot as plt
import base64
from io import BytesIO
import matplotlib
matplotlib.use("Agg")

app=Flask(__name__)

def fig_to_base64_img(fig):
    io=BytesIO()
    fig.savefig(io,format="png")
    io.seek(0)
    base64_img=base64.b64encode(io.read()).decode()

    return base64_img

def create_graph(stats_pd,stats_type1,stats_type2):
    x=stats_pd[stats_type1]
    y=stats_pd[stats_type2]

    fig,ax=plt.subplots()
    ax.plot(x,y,"o")
    ax.set_title("correlation "+stats_type1+" between "+stats_type2)
    ax.set_xlabel(stats_type1)
    ax.set_ylabel(stats_type2)

    return fig

def make_dataset(all_stats):

    Player=[]
    PTS=[]
    FGM=[]
    FGA=[]
    F3GM=[]
    F3GA=[]
    FTM=[]
    FTA=[]
    Oreb=[]
    DR=[]
    TR=[]
    AST=[]
    TOV=[]
    BS=[]
    EFF=[]
    OE=[]
    TS=[]
    eFG=[]
    PPP=[]


    for stat in all_stats:
        Player.append(stat.Player)
        PTS.append(round(float(stat.PTS),2))
        FGM.append(round(float(stat.FGM),2))
        FGA.append(round(float(stat.FGA),2))
        F3GM.append(round(float(stat.F3GM),2))
        F3GA.append(round(float(stat.F3GA),2))
        FTM.append(round(float(stat.FTM),2))
        FTA.append(round(float(stat.FTA),2))
        Oreb.append(round(float(stat.Oreb),2))
        DR.append(round(float(stat.DR),2))
        TR.append(round(float(stat.TR),2))
        AST.append(round(float(stat.AST),2))
        TOV.append(round(float(stat.TOV),2))
        BS.append(round(float(stat.BS),2))
        EFF.append(round(float(stat.EFF),2))
        OE.append(round(float(stat.OE),2))
        TS.append(round(float(stat.TS),2))
        eFG.append(round(float(stat.eFG),2))
        PPP.append(round(float(stat.PPP),2))
    
    #データフレームに各スタッツを格納
    Player=pd.Series(Player)
    PTS=pd.Series(PTS)
    FGM=pd.Series(FGM)
    FGA=pd.Series(FGA)
    F3GM=pd.Series(F3GM)
    F3GA=pd.Series(F3GA)
    FTM=pd.Series(FTM)
    FTA=pd.Series(FTA)
    Oreb=pd.Series(Oreb)
    DR=pd.Series(DR)
    TR=pd.Series(TR)
    AST=pd.Series(AST)
    TOV=pd.Series(TOV)
    BS=pd.Series(BS)
    EFF=pd.Series(EFF)
    OE=pd.Series(OE)
    TS=pd.Series(TS)
    eFG=pd.Series(eFG)
    PPP=pd.Series(PPP)
    stats_pd=pd.concat([Player,PTS,FGM,FGA,F3GM,F3GA,FTM,FTA,Oreb,DR,TR,AST,TOV,BS,EFF,OE,TS,eFG,PPP],axis=1)
    stats_pd=stats_pd.set_axis(["Player","PTS","FGM","FGA","F3GM","F3GA","FTM","FTA","Oreb","DR","TR","AST","TOV","BS","EFF","OE","TS","eFG","PPP"],axis=1)

    return stats_pd


@app.route("/")
def index():
    all_stats=Stats.query.all()

    for stat in all_stats:
        stat.PTS=round(float(stat.PTS),2)
        stat.FGM=round(float(stat.FGM),2)
        stat.FGA=round(float(stat.FGA),2)
        stat.F3GM=round(float(stat.F3GM),2)
        stat.F3GA=round(float(stat.F3GA),2)
        stat.FTM=round(float(stat.FTM),2)
        stat.FTA=round(float(stat.FTA),2)
        stat.Oreb=round(float(stat.Oreb),2)
        stat.DR=round(float(stat.DR),2)
        stat.TR=round(float(stat.TR),2)
        stat.AST=round(float(stat.AST),2)
        stat.TOV=round(float(stat.TOV),2)
        stat.BS=round(float(stat.BS),2)
        stat.EFF=round(float(stat.EFF),2)
        stat.OE=round(float(stat.OE),2)
        stat.TS=round(float(stat.TS),2)
        stat.eFG=round(float(stat.eFG),2)
        stat.PPP=round(float(stat.PPP),2)

        
    return render_template("index.html",all_stats=all_stats)

@app.route("/arrange",methods=["POST"])
def arrange():
    stats_type=request.form.get("stats_type")
    
    all_stats=Stats.query.all()

    stats_pd=make_dataset(all_stats)

    stats_arrange=stats_pd.sort_values(stats_type,ascending=False)
    stats=[]

    for player,pts,fgm,fga,f3gm,f3ga,ftm,fta,oreb,dr,tr,ast,tov,bs,eff,oe,ts,efg,ppp in zip(stats_arrange["Player"],stats_arrange["PTS"],stats_arrange["FGM"],stats_arrange["FGA"],stats_arrange["F3GM"],stats_arrange["F3GA"],stats_arrange["FTM"],stats_arrange["FTA"],stats_arrange["Oreb"],stats_arrange["DR"],stats_arrange["TR"],stats_arrange["AST"],stats_arrange["TOV"],stats_arrange["BS"],stats_arrange["EFF"],stats_arrange["OE"],stats_arrange["TS"],stats_arrange["eFG"],stats_arrange["PPP"]):
        stats.append([player,pts,fgm,fga,f3gm,f3ga,ftm,fta,oreb,dr,tr,ast,tov,bs,eff,oe,ts,efg,ppp])


    return render_template("arrange.html",stats=stats)


@app.route("/figure",methods=["POST"])
def figure():
        all_stats=Stats.query.all()

        stats_type1=request.form.get("stats_type1")
        stats_type2=request.form.get("stats_type2")

        stats_pd=make_dataset(all_stats)

        cor=round(stats_pd[stats_type1].corr(stats_pd[stats_type2]),2)#相関係数
        cor=str(cor)#文字列型にキャスト

        fig=create_graph(stats_pd,stats_type1,stats_type2)
        
        img=fig_to_base64_img(fig)


        return render_template("figure.html",cor=cor,stats_type1=stats_type1,stats_type2=stats_type2,img=img)

if __name__=="__main__":
    app.run(debug=True)