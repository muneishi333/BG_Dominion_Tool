import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as mb
import random as rand


#カード情報テンプレ
class Card:
    def __init__(self,name,set,number,type1,type2):
        self.name = name        #カード名
        self.set = set          #収録されている拡張セットの番号
        self.number = number    #収録されている拡張セット内でのカードの番号
        self.type1 = type1      #カードタイプ色（主）
        self.type2 = type2      #カードタイプ色（副）


def title_pack():
    title.pack(pady=20)
    menu1.pack(pady=10)
    #menu2.pack(pady=10)
    menu3.pack(pady=10)

def title_forget():
    title.pack_forget()
    menu1.pack_forget()
    #menu2.pack_forget()
    menu3.pack_forget()

#ランダマイザー拡張選択画面
def random_select_set():
    title_forget()
    subtitle1.pack()
    if skip[0]:
        random_play()
    else:
        frame_selectset.pack()
        backmenu1a.pack(side=tk.LEFT,padx=100)

def backmenu_1a():
    subtitle1.pack_forget()
    frame_selectset.pack_forget()
    backmenu1a.pack_forget()
    title_pack()

def card_register(i,all):
    if i == 0:      #基本 26
        all.append(card0001)
        all.append(card0002)
        all.append(card0003)
        all.append(card0004)
        all.append(card0005)
        all.append(card0006)
        all.append(card0007)
        all.append(card0008)
        all.append(card0009)
        all.append(card0010)
        all.append(card0011)
        all.append(card0012)
        all.append(card0013)
        all.append(card0014)
        all.append(card0015)
        all.append(card0016)
        all.append(card0017)
        all.append(card0018)
        all.append(card0019)
        all.append(card0020)
        all.append(card0021)
        all.append(card0022)
        all.append(card0023)
        all.append(card0024)
        all.append(card0025)
        all.append(card0026)
    elif i == 1:        #陰謀 26
        all.append(card0101)
        all.append(card0102)
        all.append(card0103)
        all.append(card0104)
        all.append(card0105)
        all.append(card0106)
        all.append(card0107)
        all.append(card0108)
        all.append(card0109)
        all.append(card0110)
        all.append(card0111)
        all.append(card0112)
        all.append(card0113)
        all.append(card0114)
        all.append(card0115)
        all.append(card0116)
        all.append(card0117)
        all.append(card0118)
        all.append(card0119)
        all.append(card0120)
        all.append(card0121)
        all.append(card0122)
        all.append(card0123)
        all.append(card0124)
        all.append(card0125)
        all.append(card0126)
    elif i == 2:        #海辺 27
        all.append(card0201)
        all.append(card0202)
        all.append(card0203)
        all.append(card0204)
        all.append(card0205)
        all.append(card0206)
        all.append(card0207)
        all.append(card0208)
        all.append(card0209)
        all.append(card0210)
        all.append(card0211)
        all.append(card0212)
        all.append(card0213)
        all.append(card0214)
        all.append(card0215)
        all.append(card0216)
        all.append(card0217)
        all.append(card0218)
        all.append(card0219)
        all.append(card0220)
        all.append(card0221)
        all.append(card0222)
        all.append(card0223)
        all.append(card0224)
        all.append(card0225)
        all.append(card0226)
        all.append(card0227)
    elif i == 3:        #錬金術 12
        all.append(card0301)
        all.append(card0302)
        all.append(card0303)
        all.append(card0304)
        all.append(card0305)
        all.append(card0306)
        all.append(card0307)
        all.append(card0308)
        all.append(card0309)
        all.append(card0310)
        all.append(card0311)
        all.append(card0312)
    elif i == 4:        #繁栄 25
        all.append(card0401)
        all.append(card0402)
        all.append(card0403)
        all.append(card0404)
        all.append(card0405)
        all.append(card0406)
        all.append(card0407)
        all.append(card0408)
        all.append(card0409)
        all.append(card0410)
        all.append(card0411)
        all.append(card0412)
        all.append(card0413)
        all.append(card0414)
        all.append(card0415)
        all.append(card0416)
        all.append(card0417)
        all.append(card0418)
        all.append(card0419)
        all.append(card0420)
        all.append(card0421)
        all.append(card0422)
        all.append(card0423)
        all.append(card0424)
        all.append(card0425)
    elif i == 5:        #収穫祭 13
        all.append(card0501)
        all.append(card0502)
        all.append(card0503)
        all.append(card0504)
        all.append(card0505)
        all.append(card0506)
        all.append(card0507)
        all.append(card0508)
        all.append(card0509)
        all.append(card0510)
        all.append(card0511)
        all.append(card0512)
        all.append(card0513)
    elif i == 6:        #異郷 26
        all.append(card0601)
        all.append(card0602)
        all.append(card0603)
        all.append(card0604)
        all.append(card0605)
        all.append(card0606)
        all.append(card0607)
        all.append(card0608)
        all.append(card0609)
        all.append(card0610)
        all.append(card0611)
        all.append(card0612)
        all.append(card0613)
        all.append(card0614)
        all.append(card0615)
        all.append(card0616)
        all.append(card0617)
        all.append(card0618)
        all.append(card0619)
        all.append(card0620)
        all.append(card0621)
        all.append(card0622)
        all.append(card0623)
        all.append(card0624)
        all.append(card0625)
        all.append(card0626)
    elif i == 7:        #暗黒時代 35
        all.append(card0701)
        all.append(card0702)
        all.append(card0703)
        all.append(card0704)
        all.append(card0705)
        all.append(card0706)
        all.append(card0707)
        all.append(card0708)
        all.append(card0709)
        all.append(card0710)
        all.append(card0711)
        all.append(card0712)
        all.append(card0713)
        all.append(card0714)
        all.append(card0715)
        all.append(card0716)
        all.append(card0717)
        all.append(card0718)
        all.append(card0719)
        all.append(card0720)
        all.append(card0721)
        all.append(card0722)
        all.append(card0723)
        all.append(card0724)
        all.append(card0725)
        all.append(card0726)
        all.append(card0727)
        all.append(card0728)
        all.append(card0729)
        all.append(card0730)
        all.append(card0731)
        all.append(card0732)
        all.append(card0733)
        all.append(card0734)
        all.append(card0735)
    elif i == 8:        #ギルド 13
        all.append(card0801)
        all.append(card0802)
        all.append(card0803)
        all.append(card0804)
        all.append(card0805)
        all.append(card0806)
        all.append(card0807)
        all.append(card0808)
        all.append(card0809)
        all.append(card0810)
        all.append(card0811)
        all.append(card0812)
        all.append(card0813)
    elif i == 9:        #冒険 30
        all.append(card0901)
        all.append(card0902)
        all.append(card0903)
        all.append(card0904)
        all.append(card0905)
        all.append(card0906)
        all.append(card0907)
        all.append(card0908)
        all.append(card0909)
        all.append(card0910)
        all.append(card0911)
        all.append(card0912)
        all.append(card0913)
        all.append(card0914)
        all.append(card0915)
        all.append(card0916)
        all.append(card0917)
        all.append(card0918)
        all.append(card0919)
        all.append(card0920)
        all.append(card0921)
        all.append(card0922)
        all.append(card0923)
        all.append(card0924)
        all.append(card0925)
        all.append(card0926)
        all.append(card0927)
        all.append(card0928)
        all.append(card0929)
        all.append(card0930)
    elif i == 10:       #帝国 24
        all.append(card1001)
        all.append(card1002)
        all.append(card1003)
        all.append(card1004)
        all.append(card1005)
        all.append(card1006)
        all.append(card1007)
        all.append(card1008)
        all.append(card1009)
        all.append(card1010)
        all.append(card1011)
        all.append(card1012)
        all.append(card1013)
        all.append(card1014)
        all.append(card1015)
        all.append(card1016)
        all.append(card1017)
        all.append(card1018)
        all.append(card1019)
        all.append(card1020)
        all.append(card1021)
        all.append(card1022)
        all.append(card1023)
        all.append(card1024)
    elif i == 11:       #夜想曲 33
        all.append(card1101)
        all.append(card1102)
        all.append(card1103)
        all.append(card1104)
        all.append(card1105)
        all.append(card1106)
        all.append(card1107)
        all.append(card1108)
        all.append(card1109)
        all.append(card1110)
        all.append(card1111)
        all.append(card1112)
        all.append(card1113)
        all.append(card1114)
        all.append(card1115)
        all.append(card1116)
        all.append(card1117)
        all.append(card1118)
        all.append(card1119)
        all.append(card1120)
        all.append(card1121)
        all.append(card1122)
        all.append(card1123)
        all.append(card1124)
        all.append(card1125)
        all.append(card1126)
        all.append(card1127)
        all.append(card1128)
        all.append(card1129)
        all.append(card1130)
        all.append(card1131)
        all.append(card1132)
        all.append(card1133)
    elif i == 12:       #ルネサンス　25
        all.append(card1201)
        all.append(card1202)
        all.append(card1203)
        all.append(card1204)
        all.append(card1205)
        all.append(card1206)
        all.append(card1207)
        all.append(card1208)
        all.append(card1209)
        all.append(card1210)
        all.append(card1211)
        all.append(card1212)
        all.append(card1213)
        all.append(card1214)
        all.append(card1215)
        all.append(card1216)
        all.append(card1217)
        all.append(card1218)
        all.append(card1219)
        all.append(card1220)
        all.append(card1221)
        all.append(card1222)
        all.append(card1223)
        all.append(card1224)
        all.append(card1225)
    elif i == 13:       #移動動物園 30
        all.append(card1301)
        all.append(card1302)
        all.append(card1303)
        all.append(card1304)
        all.append(card1305)
        all.append(card1306)
        all.append(card1307)
        all.append(card1308)
        all.append(card1309)
        all.append(card1310)
        all.append(card1311)
        all.append(card1312)
        all.append(card1313)
        all.append(card1314)
        all.append(card1315)
        all.append(card1316)
        all.append(card1317)
        all.append(card1318)
        all.append(card1319)
        all.append(card1320)
        all.append(card1321)
        all.append(card1322)
        all.append(card1323)
        all.append(card1324)
        all.append(card1325)
        all.append(card1326)
        all.append(card1327)
        all.append(card1328)
        all.append(card1329)
        all.append(card1330)
    elif i == 14:       #同盟 31
        all.append(card1401)
        all.append(card1402)
        all.append(card1403)
        all.append(card1404)
        all.append(card1405)
        all.append(card1406)
        all.append(card1407)
        all.append(card1408)
        all.append(card1409)
        all.append(card1410)
        all.append(card1411)
        all.append(card1412)
        all.append(card1413)
        all.append(card1414)
        all.append(card1415)
        all.append(card1416)
        all.append(card1417)
        all.append(card1418)
        all.append(card1419)
        all.append(card1420)
        all.append(card1421)
        all.append(card1422)
        all.append(card1423)
        all.append(card1424)
        all.append(card1425)
        all.append(card1426)
        all.append(card1427)
        all.append(card1428)
        all.append(card1429)
        all.append(card1430)
        all.append(card1431)
        all_spcard_ally.append(spcard0701)
        all_spcard_ally.append(spcard0702)
        all_spcard_ally.append(spcard0703)
        all_spcard_ally.append(spcard0704)
        all_spcard_ally.append(spcard0705)
        all_spcard_ally.append(spcard0706)
        all_spcard_ally.append(spcard0707)
        all_spcard_ally.append(spcard0708)
        all_spcard_ally.append(spcard0709)
        all_spcard_ally.append(spcard0710)
        all_spcard_ally.append(spcard0711)
        all_spcard_ally.append(spcard0712)
        all_spcard_ally.append(spcard0713)
        all_spcard_ally.append(spcard0714)
        all_spcard_ally.append(spcard0715)
        all_spcard_ally.append(spcard0716)
        all_spcard_ally.append(spcard0717)
        all_spcard_ally.append(spcard0718)
        all_spcard_ally.append(spcard0719)
        all_spcard_ally.append(spcard0720)
        all_spcard_ally.append(spcard0721)
        all_spcard_ally.append(spcard0722)
        all_spcard_ally.append(spcard0723)
    elif i == 15:       #略奪 40
        all.append(card1501)
        all.append(card1502)
        all.append(card1503)
        all.append(card1504)
        all.append(card1505)
        all.append(card1506)
        all.append(card1507)
        all.append(card1508)
        all.append(card1509)
        all.append(card1510)
        all.append(card1511)
        all.append(card1512)
        all.append(card1513)
        all.append(card1514)
        all.append(card1515)
        all.append(card1516)
        all.append(card1517)
        all.append(card1518)
        all.append(card1519)
        all.append(card1520)
        all.append(card1521)
        all.append(card1522)
        all.append(card1523)
        all.append(card1524)
        all.append(card1525)
        all.append(card1526)
        all.append(card1527)
        all.append(card1528)
        all.append(card1529)
        all.append(card1530)
        all.append(card1531)
        all.append(card1532)
        all.append(card1533)
        all.append(card1534)
        all.append(card1535)
        all.append(card1536)
        all.append(card1537)
        all.append(card1538)
        all.append(card1539)
        all.append(card1540)
    elif i == 16:       #旭日 25
        all.append(card1601)
        all.append(card1602)
        all.append(card1603)
        all.append(card1604)
        all.append(card1605)
        all.append(card1606)
        all.append(card1607)
        all.append(card1608)
        all.append(card1609)
        all.append(card1610)
        all.append(card1611)
        all.append(card1612)
        all.append(card1613)
        all.append(card1614)
        all.append(card1615)
        all.append(card1616)
        all.append(card1617)
        all.append(card1618)
        all.append(card1619)
        all.append(card1620)
        all.append(card1621)
        all.append(card1622)
        all.append(card1623)
        all.append(card1624)
        all.append(card1625)
        all_spcard_prop.append(spcard1101)
        all_spcard_prop.append(spcard1102)
        all_spcard_prop.append(spcard1103)
        all_spcard_prop.append(spcard1104)
        all_spcard_prop.append(spcard1105)
        all_spcard_prop.append(spcard1106)
        all_spcard_prop.append(spcard1107)
        all_spcard_prop.append(spcard1108)
        all_spcard_prop.append(spcard1109)
        all_spcard_prop.append(spcard1110)
        all_spcard_prop.append(spcard1111)
        all_spcard_prop.append(spcard1112)
        all_spcard_prop.append(spcard1113)
        all_spcard_prop.append(spcard1114)
        all_spcard_prop.append(spcard1115)

def spcard_register(i):
    if i == 1:      #イベント-冒険
        all_spcard.append(spcard0101)
        all_spcard.append(spcard0102)
        all_spcard.append(spcard0103)
        all_spcard.append(spcard0104)
        all_spcard.append(spcard0105)
        all_spcard.append(spcard0106)
        all_spcard.append(spcard0107)
        all_spcard.append(spcard0108)
        all_spcard.append(spcard0109)
        all_spcard.append(spcard0110)
        all_spcard.append(spcard0111)
        all_spcard.append(spcard0112)
        all_spcard.append(spcard0113)
        all_spcard.append(spcard0114)
        all_spcard.append(spcard0115)
        all_spcard.append(spcard0116)
        all_spcard.append(spcard0117)
        all_spcard.append(spcard0118)
        all_spcard.append(spcard0119)
        all_spcard.append(spcard0120)
    elif i == 2:    #イベント-帝国
        all_spcard.append(spcard0201)
        all_spcard.append(spcard0202)
        all_spcard.append(spcard0203)
        all_spcard.append(spcard0204)
        all_spcard.append(spcard0205)
        all_spcard.append(spcard0206)
        all_spcard.append(spcard0207)
        all_spcard.append(spcard0208)
        all_spcard.append(spcard0209)
        all_spcard.append(spcard0210)
        all_spcard.append(spcard0211)
        all_spcard.append(spcard0212)
        all_spcard.append(spcard0213)
    elif i == 3:    #ランドマーク
        all_spcard.append(spcard0301)
        all_spcard.append(spcard0302)
        all_spcard.append(spcard0303)
        all_spcard.append(spcard0304)
        all_spcard.append(spcard0305)
        all_spcard.append(spcard0306)
        all_spcard.append(spcard0307)
        all_spcard.append(spcard0308)
        all_spcard.append(spcard0309)
        all_spcard.append(spcard0310)
        all_spcard.append(spcard0311)
        all_spcard.append(spcard0312)
        all_spcard.append(spcard0313)
        all_spcard.append(spcard0314)
        all_spcard.append(spcard0315)
        all_spcard.append(spcard0316)
        all_spcard.append(spcard0317)
        all_spcard.append(spcard0318)
        all_spcard.append(spcard0319)
        all_spcard.append(spcard0320)
        all_spcard.append(spcard0321)
    elif i == 4:    #プロジェクト
        all_spcard.append(spcard0401)
        all_spcard.append(spcard0402)
        all_spcard.append(spcard0403)
        all_spcard.append(spcard0404)
        all_spcard.append(spcard0405)
        all_spcard.append(spcard0406)
        all_spcard.append(spcard0407)
        all_spcard.append(spcard0408)
        all_spcard.append(spcard0409)
        all_spcard.append(spcard0410)
        all_spcard.append(spcard0411)
        all_spcard.append(spcard0412)
        all_spcard.append(spcard0413)
        all_spcard.append(spcard0414)
        all_spcard.append(spcard0415)
        all_spcard.append(spcard0416)
        all_spcard.append(spcard0417)
        all_spcard.append(spcard0418)
        all_spcard.append(spcard0419)
        all_spcard.append(spcard0420)
    elif i == 5:    #イベント-移動動物園
        all_spcard.append(spcard0501)
        all_spcard.append(spcard0502)
        all_spcard.append(spcard0503)
        all_spcard.append(spcard0504)
        all_spcard.append(spcard0505)
        all_spcard.append(spcard0506)
        all_spcard.append(spcard0507)
        all_spcard.append(spcard0508)
        all_spcard.append(spcard0509)
        all_spcard.append(spcard0510)
        all_spcard.append(spcard0511)
        all_spcard.append(spcard0512)
        all_spcard.append(spcard0513)
        all_spcard.append(spcard0514)
        all_spcard.append(spcard0515)
        all_spcard.append(spcard0516)
        all_spcard.append(spcard0517)
        all_spcard.append(spcard0518)
        all_spcard.append(spcard0519)
        all_spcard.append(spcard0520)
    elif i == 6:    #習性
        all_spcard.append(spcard0601)
        all_spcard.append(spcard0602)
        all_spcard.append(spcard0603)
        all_spcard.append(spcard0604)
        all_spcard.append(spcard0605)
        all_spcard.append(spcard0606)
        all_spcard.append(spcard0607)
        all_spcard.append(spcard0608)
        all_spcard.append(spcard0609)
        all_spcard.append(spcard0610)
        all_spcard.append(spcard0611)
        all_spcard.append(spcard0612)
        all_spcard.append(spcard0613)
        all_spcard.append(spcard0614)
        all_spcard.append(spcard0615)
        all_spcard.append(spcard0616)
        all_spcard.append(spcard0617)
        all_spcard.append(spcard0618)
        all_spcard.append(spcard0619)
        all_spcard.append(spcard0620)
    elif i == 8:    #イベント-略奪
        all_spcard.append(spcard0801)
        all_spcard.append(spcard0802)
        all_spcard.append(spcard0803)
        all_spcard.append(spcard0804)
        all_spcard.append(spcard0805)
        all_spcard.append(spcard0806)
        all_spcard.append(spcard0807)
        all_spcard.append(spcard0808)
        all_spcard.append(spcard0809)
        all_spcard.append(spcard0810)
        all_spcard.append(spcard0811)
        all_spcard.append(spcard0812)
        all_spcard.append(spcard0813)
        all_spcard.append(spcard0814)
        all_spcard.append(spcard0815)
    elif i == 9:    #特性
        all_spcard.append(spcard0901)
        all_spcard.append(spcard0902)
        all_spcard.append(spcard0903)
        all_spcard.append(spcard0904)
        all_spcard.append(spcard0905)
        all_spcard.append(spcard0906)
        all_spcard.append(spcard0907)
        all_spcard.append(spcard0908)
        all_spcard.append(spcard0909)
        all_spcard.append(spcard0910)
        all_spcard.append(spcard0911)
        all_spcard.append(spcard0912)
        all_spcard.append(spcard0913)
        all_spcard.append(spcard0914)
        all_spcard.append(spcard0915)
    elif i == 10:   #イベント-旭日
        all_spcard.append(spcard1001)
        all_spcard.append(spcard1002)
        all_spcard.append(spcard1003)
        all_spcard.append(spcard1004)
        all_spcard.append(spcard1005)
        all_spcard.append(spcard1006)
        all_spcard.append(spcard1007)
        all_spcard.append(spcard1008)
        all_spcard.append(spcard1009)
        all_spcard.append(spcard1010)

#ランダマイザー各拡張選択
def random_selected():
    if set0_v.get():
        card_register(0, all_card)
    if set1_v.get():
        card_register(1, all_card)
    if set2_v.get():
        card_register(2, all_card)
    if set3_v.get():
        card_register(3, all_card)
    if set4_v.get():
        card_register(4, all_card)
    if set5_v.get():
        card_register(5, all_card)
    if set6_v.get():
        card_register(6, all_card)
    if set7_v.get():
        card_register(7, all_card)
    if set8_v.get():
        card_register(8, all_card)
    if set9_v.get():
        card_register(9, all_card)
    if set10_v.get():
        card_register(10, all_card)
    if set11_v.get():
        card_register(11, all_card)
    if set12_v.get():
        card_register(12, all_card)
    if set13_v.get():
        card_register(13, all_card)
    if set14_v.get():
        card_register(14, all_card)
    if set15_v.get():
        card_register(15, all_card)
    if set16_v.get():
        card_register(16, all_card)
    if sp1_v.get():
        spcard_register(1)
    if sp2_v.get():
        spcard_register(2)
    if sp3_v.get():
        spcard_register(3)
    if sp4_v.get():
        spcard_register(4)
    if sp5_v.get():
        spcard_register(5)
    if sp6_v.get():
        spcard_register(6)
    if sp8_v.get():
        spcard_register(8)
    if sp9_v.get():
        spcard_register(9)
    if sp10_v.get():
        spcard_register(10)
    random_play()

#ランダマイザー全拡張選択
def random_all_set():
    all_card.clear()
    card_register(0, all_card)
    card_register(1, all_card)
    card_register(2, all_card)
    card_register(3, all_card)
    card_register(4, all_card)
    card_register(5, all_card)
    card_register(6, all_card)
    card_register(7, all_card)
    card_register(8, all_card)
    card_register(9, all_card)
    card_register(10, all_card)
    card_register(11, all_card)
    card_register(12, all_card)
    card_register(13, all_card)
    card_register(14, all_card)
    card_register(15, all_card)
    card_register(16, all_card)
    all_card.append(cardP001)
    all_card.append(cardP002)
    all_spcard.clear()
    spcard_register(1)
    spcard_register(2)
    spcard_register(3)
    spcard_register(4)
    spcard_register(5)
    spcard_register(6)
    spcard_register(8)
    spcard_register(9)
    spcard_register(10)
    random_play()

#タイトルに戻る
def backmenu_1b():
    subtitle1.pack_forget()
    frame_randomizer1.pack_forget()
    frame_randomizer2.pack_forget()
    backmenu1b.pack_forget()
    backmenu1c.pack_forget()
    title_pack()

#タイトルに戻る
def backmenu_1c():
    subtitle1.pack_forget()
    frame_randomizer1.pack_forget()
    frame_randomizer2.pack_forget()
    backmenu1b.pack_forget()
    backmenu1c.pack_forget()
    skip[0] = False
    random_select_set()

#ランダマイザー：実行画面
def random_play():
    skip[0] = True
    frame_selectset.pack_forget()
    backmenu1a.pack_forget()
    frame_randomizer1.pack()
    frame_randomizer2.pack()
    backmenu1b.pack()
    backmenu1c.pack()

#カードを生成しきったときの警告
def showAlert_cardgene():
    mb.showinfo('Information', 'リセットしました')

#カードが設定されていないときの警告
def showAlert_cardset():
    mb.showinfo('Information', 'カードが設定されていません')

#王国カードをランダムで１枚生成
def random_card_gene_1():
    if len(all_card) > 0:
        #既に生成されている枚数が11以下であれば生成開始
        if len(random_num) < 12:
            jud = True
            while jud:
                numb = rand.randint(0,len(all_card)-1)
                jud = False
                for i in range(len(random_num)):
                    if random_num[i] == numb:
                        jud = True
                        break
            random_num.append(numb)
            random_card.append(all_card[numb])
            #カードタイプによる文字色変更（主タイプ）
            if all_card[numb].type1 == 1:   #アクション
                geneCard[(len(random_num)*2)-2]["foreground"] = "#000090"
            elif all_card[numb].type1 == 2: #財宝
                geneCard[(len(random_num)*2)-2]["foreground"] = "#f7b400"
            elif all_card[numb].type1 == 3: #勝利点
                geneCard[(len(random_num)*2)-2]["foreground"] = "#228b22"
            elif all_card[numb].type1 == 4: #リアクション
                geneCard[(len(random_num)*2)-2]["foreground"] = "#1e90ff"
            elif all_card[numb].type1 == 5: #持続
                geneCard[(len(random_num)*2)-2]["foreground"] = "#ff7f50"
            elif all_card[numb].type1 == 6: #リザーブ
                geneCard[(len(random_num)*2)-2]["foreground"] = "#808000"
            elif all_card[numb].type1 == 7: #夜行
                geneCard[(len(random_num)*2)-2]["foreground"] = "#000000"
            #カードタイプによる背景色変更（副タイプ）
            if all_card[numb].type2 == 1:
                geneCard[(len(random_num)*2)-2]["background"] = "#d3d3d3"
            elif all_card[numb].type2 == 2:
                geneCard[(len(random_num)*2)-2]["background"] = "#fffacd"
            elif all_card[numb].type2 == 3:
                geneCard[(len(random_num)*2)-2]["background"] = "#98fb98"
            elif all_card[numb].type2 == 4:
                geneCard[(len(random_num)*2)-2]["background"] = "#87cefa"
            elif all_card[numb].type2 == 5:
                geneCard[(len(random_num)*2)-2]["background"] = "#fae7d2"
            else:   #副タイプ無し
                geneCard[(len(random_num)*2)-2]["background"] = "#ffffff"
            #カード名の貼り付け
            geneCard[(len(random_num)*2)-2]["text"] = all_card[numb].name
            #セットの収納BOXを背景色で視覚化
            if all_card[numb].set == 0:
                geneCard[(len(random_num)*2)-1]["text"] = '00-' + str(all_card[numb].number)
                geneCard[(len(random_num)*2)-1]["background"] = "#e0ffff"
            elif all_card[numb].set == 1:
                geneCard[(len(random_num)*2)-1]["text"] = '01-' + str(all_card[numb].number)
                geneCard[(len(random_num)*2)-1]["background"] = "#ffffe0"
            elif all_card[numb].set == 2:
                geneCard[(len(random_num)*2)-1]["text"] = '02-' + str(all_card[numb].number)
                geneCard[(len(random_num)*2)-1]["background"] = "#e0ffff"
            elif all_card[numb].set == 3:
                geneCard[(len(random_num)*2)-1]["text"] = '03-' + str(all_card[numb].number)
                geneCard[(len(random_num)*2)-1]["background"] = "#ffe0ff"
            elif all_card[numb].set == 4:
                geneCard[(len(random_num)*2)-1]["text"] = '04-' + str(all_card[numb].number)
                geneCard[(len(random_num)*2)-1]["background"] = "#e0ffff"
            elif all_card[numb].set == 5:
                geneCard[(len(random_num)*2)-1]["text"] = '05-' + str(all_card[numb].number)
                geneCard[(len(random_num)*2)-1]["background"] = "#ffe0ff"
            elif all_card[numb].set == 6:
                geneCard[(len(random_num)*2)-1]["text"] = '06-' + str(all_card[numb].number)
                geneCard[(len(random_num)*2)-1]["background"] = "#e0ffe0"
            elif all_card[numb].set == 7:
                geneCard[(len(random_num)*2)-1]["text"] = '07-' + str(all_card[numb].number)
                geneCard[(len(random_num)*2)-1]["background"] = "#e0ffe0"
            elif all_card[numb].set == 8:
                geneCard[(len(random_num)*2)-1]["text"] = '08-' + str(all_card[numb].number)
                geneCard[(len(random_num)*2)-1]["background"] = "#ffffe0"
            elif all_card[numb].set == 9:
                geneCard[(len(random_num)*2)-1]["text"] = '09-' + str(all_card[numb].number)
                geneCard[(len(random_num)*2)-1]["background"] = "#ffe0ff"
            elif all_card[numb].set == 10:
                geneCard[(len(random_num)*2)-1]["text"] = '10-' + str(all_card[numb].number)
                geneCard[(len(random_num)*2)-1]["background"] = "#e0ffff"
            elif all_card[numb].set == 11:
                geneCard[(len(random_num)*2)-1]["text"] = '11-' + str(all_card[numb].number)
                geneCard[(len(random_num)*2)-1]["background"] = "#ffffe0"
            elif all_card[numb].set == 12:
                geneCard[(len(random_num)*2)-1]["text"] = '12-' + str(all_card[numb].number)
                geneCard[(len(random_num)*2)-1]["background"] = "#ffe0ff"
            elif all_card[numb].set == 13:
                geneCard[(len(random_num)*2)-1]["text"] = '13-' + str(all_card[numb].number)
                geneCard[(len(random_num)*2)-1]["background"] = "#e0ffe0"
            elif all_card[numb].set == 14:
                geneCard[(len(random_num)*2)-1]["text"] = '14-' + str(all_card[numb].number)
                geneCard[(len(random_num)*2)-1]["background"] = "#ffe0ff"
            elif all_card[numb].set == 15:
                geneCard[(len(random_num)*2)-1]["text"] = '15-' + str(all_card[numb].number)
                geneCard[(len(random_num)*2)-1]["background"] = "#ffffe0"
            elif all_card[numb].set == 16:
                geneCard[(len(random_num)*2)-1]["text"] = '16-' + str(all_card[numb].number)
                geneCard[(len(random_num)*2)-1]["background"] = "#e0ffe0"
        else:
            showAlert_cardgene()
    else:
        showAlert_cardset()
        skip[0] = False
        backmenu_1b()


#王国カードをランダムで10個になるように生成
def random_card_gene_10():
    while len(random_num) < 10:
        random_card_gene_1()

#生成された王国カード1枚を入れ替える
def delete_card():
    num = int(delete_one_area.get())
    if num <= len(random_num):
        jud = True
        while jud:
            numb = rand.randint(0,len(all_card)-1)
            jud = False
            for i in range(len(random_num)):
                if random_num[i] == numb:
                    jud = True
                    break
        random_num[num-1] = numb
        random_card[num-1] = all_card[numb]
        #カードタイプによる文字色変更（主タイプ）
        if all_card[numb].type1 == 1:   #アクション
            geneCard[(num*2)-2]["foreground"] = "#000090"
        elif all_card[numb].type1 == 2: #財宝
            geneCard[(num*2)-2]["foreground"] = "#f7b400"
        elif all_card[numb].type1 == 3: #勝利点
            geneCard[(num*2)-2]["foreground"] = "#228b22"
        elif all_card[numb].type1 == 4: #リアクション
            geneCard[(num*2)-2]["foreground"] = "#1e90ff"
        elif all_card[numb].type1 == 5: #持続
            geneCard[(num*2)-2]["foreground"] = "#ff7f50"
        elif all_card[numb].type1 == 6: #リザーブ
            geneCard[(num*2)-2]["foreground"] = "#808000"
        elif all_card[numb].type1 == 7: #夜行
            geneCard[(num*2)-2]["foreground"] = "#000000"
        #カードタイプによる背景色変更（副タイプ）
        if all_card[numb].type2 == 1:
            geneCard[(num*2)-2]["background"] = "#d3d3d3"
        elif all_card[numb].type2 == 2:
            geneCard[(num*2)-2]["background"] = "#fffacd"
        elif all_card[numb].type2 == 3:
            geneCard[(num*2)-2]["background"] = "#98fb98"
        elif all_card[numb].type2 == 4:
            geneCard[(num*2)-2]["background"] = "#87cefa"
        elif all_card[numb].type2 == 5:
            geneCard[(num*2)-2]["background"] = "#fae7d2"
        else:   #副タイプ無し
            geneCard[(num*2)-2]["background"] = "#ffffff"
        #カード名の貼り付け
        geneCard[(num*2)-2]["text"] = all_card[numb].name
        #セットの収納BOXを背景色で視覚化
        if all_card[numb].set == 0:
            geneCard[(num*2)-1]["text"] = '00-' + str(all_card[numb].number)
            geneCard[(num*2)-1]["background"] = "#e0ffff"
        elif all_card[numb].set == 1:
            geneCard[(num*2)-1]["text"] = '01-' + str(all_card[numb].number)
            geneCard[(num*2)-1]["background"] = "#ffffe0"
        elif all_card[numb].set == 2:
            geneCard[(num*2)-1]["text"] = '02-' + str(all_card[numb].number)
            geneCard[(num*2)-1]["background"] = "#e0ffff"
        elif all_card[numb].set == 3:
            geneCard[(num*2)-1]["text"] = '03-' + str(all_card[numb].number)
            geneCard[(num*2)-1]["background"] = "#ffe0ff"
        elif all_card[numb].set == 4:
            geneCard[(num*2)-1]["text"] = '04-' + str(all_card[numb].number)
            geneCard[(num*2)-1]["background"] = "#e0ffff"
        elif all_card[numb].set == 5:
            geneCard[(num*2)-1]["text"] = '05-' + str(all_card[numb].number)
            geneCard[(num*2)-1]["background"] = "#ffe0ff"
        elif all_card[numb].set == 6:
            geneCard[(num*2)-1]["text"] = '06-' + str(all_card[numb].number)
            geneCard[(num*2)-1]["background"] = "#e0ffe0"
        elif all_card[numb].set == 7:
            geneCard[(num*2)-1]["text"] = '07-' + str(all_card[numb].number)
            geneCard[(num*2)-1]["background"] = "#e0ffe0"
        elif all_card[numb].set == 8:
            geneCard[(num*2)-1]["text"] = '08-' + str(all_card[numb].number)
            geneCard[(num*2)-1]["background"] = "#ffffe0"
        elif all_card[numb].set == 9:
            geneCard[(num*2)-1]["text"] = '09-' + str(all_card[numb].number)
            geneCard[(num*2)-1]["background"] = "#ffe0ff"
        elif all_card[numb].set == 10:
            geneCard[(num*2)-1]["text"] = '10-' + str(all_card[numb].number)
            geneCard[(num*2)-1]["background"] = "#e0ffff"
        elif all_card[numb].set == 11:
            geneCard[(num*2)-1]["text"] = '11-' + str(all_card[numb].number)
            geneCard[(num*2)-1]["background"] = "#ffffe0"
        elif all_card[numb].set == 12:
            geneCard[(num*2)-1]["text"] = '12-' + str(all_card[numb].number)
            geneCard[(num*2)-1]["background"] = "#ffe0ff"
        elif all_card[numb].set == 13:
            geneCard[(num*2)-1]["text"] = '13-' + str(all_card[numb].number)
            geneCard[(num*2)-1]["background"] = "#e0ffe0"
        elif all_card[numb].set == 14:
            geneCard[(num*2)-1]["text"] = '14-' + str(all_card[numb].number)
            geneCard[(num*2)-1]["background"] = "#ffe0ff"
        elif all_card[numb].set == 15:
            geneCard[(num*2)-1]["text"] = '15-' + str(all_card[numb].number)
            geneCard[(num*2)-1]["background"] = "#ffffe0"
        elif all_card[numb].set == 16:
            geneCard[(num*2)-1]["text"] = '16-' + str(all_card[numb].number)
            geneCard[(num*2)-1]["background"] = "#e0ffe0"
        elif all_card[numb].set == -1:
            geneCard[(num*2)-1]["text"] = 'P-' + str(all_card[numb].number)
            geneCard[(num*2)-1]["background"] = "#e0ffff"

#記憶せずにリセット（王国カード）
def reset_unsave():
    for i in range(len(random_num)):
        geneCard[i*2]["foreground"] = "#000000"
        geneCard[i*2]["background"] = "#ffffff"
        geneCard[i*2+1]["background"] = "#ffffff"
        if i < 10:
            geneCard[i*2]["text"] = ' - '
        else:
            geneCard[i*2]["text"] = ' '
        geneCard[i*2+1]["text"] = ' '
    random_num.clear()
    random_card.clear()

#記憶してリセット（王国カード）
def reset_save():
    for i in range(len(random_card)):
        all_card.remove(random_card[i])
    reset_unsave()

#記憶をリセット（王国カード）
def save_reset():
    all_card.clear()
    card_register(0, all_card)
    card_register(1, all_card)
    card_register(2, all_card)
    card_register(3, all_card)
    card_register(4, all_card)
    card_register(5, all_card)
    card_register(6, all_card)
    card_register(7, all_card)
    card_register(8, all_card)
    card_register(9, all_card)
    card_register(10, all_card)
    card_register(11, all_card)
    card_register(12, all_card)
    card_register(13, all_card)
    card_register(14, all_card)
    card_register(15, all_card)
    card_register(16, all_card)
    all_card.append(cardP001)
    all_card.append(cardP002)
    reset_unsave()

#特殊カードをランダムで１枚生成   
def random_spcard_gene_1():
    if len(all_spcard) > 0:
        if len(random_spnum) < 4:
            jud = True
            while jud:
                numb = rand.randint(0,len(all_spcard)-1)
                jud = False
                for i in range(len(random_spnum)):
                    if random_spnum[i] == numb:
                        jud = True
                        break
            random_spnum.append(numb)
            random_spcard.append(all_spcard[numb])
            #カードタイプによる文字色変更
            if all_spcard[numb].type1 == 1:     #イベント
                geneSPCard[(len(random_spnum)*2)-2]["foreground"] = "#808080"
            elif all_spcard[numb].type1 == 2:   #ランドマーク
                geneSPCard[(len(random_spnum)*2)-2]["foreground"] = "#228b22"
            elif all_spcard[numb].type1 == 3:   #プロジェクト
                geneSPCard[(len(random_spnum)*2)-2]["foreground"] = "#c74645"
            elif all_spcard[numb].type1 == 4:   #習性
                geneSPCard[(len(random_spnum)*2)-2]["foreground"] = "#4682b4"
            elif all_spcard[numb].type1 == 5:   #同盟
                geneSPCard[(len(random_spnum)*2)-2]["foreground"] = "#556b2f"
            elif all_spcard[numb].type1 == 6:   #特性
                geneSPCard[(len(random_spnum)*2)-2]["foreground"] = "#745399"
            geneSPCard[len(random_spnum)*2-2]["text"] = all_spcard[numb].name
            if all_spcard[numb].set == 9:
                geneSPCard[len(random_spnum)*2-1]["text"] = '冒険-' + str(all_spcard[numb].number) + '　'
            elif all_spcard[numb].set == 10:
                geneSPCard[len(random_spnum)*2-1]["text"] = '帝国-' + str(all_spcard[numb].number) + '　'
            elif all_spcard[numb].set == 12:
                geneSPCard[len(random_spnum)*2-1]["text"] = 'ルネサンス-' + str(all_spcard[numb].number) + '　'
            elif all_spcard[numb].set == 13:
                geneSPCard[len(random_spnum)*2-1]["text"] = '移動動物園-' + str(all_spcard[numb].number) + '　'
            elif all_spcard[numb].set == 14:
                geneSPCard[len(random_spnum)*2-1]["text"] = '同盟-' + str(all_spcard[numb].number) + '　'
            elif all_spcard[numb].set == 15:
                geneSPCard[len(random_spnum)*2-1]["text"] = '略奪-' + str(all_spcard[numb].number) + '　'
            elif all_spcard[numb].set == 16:
                geneSPCard[len(random_spnum)*2-1]["text"] = '旭日-' + str(all_spcard[numb].number) + '　'
        else:
            showAlert_cardgene()
    else:
        showAlert_cardset()
        skip[0] = False
        backmenu_1b()
            
#記憶せずリセット（特殊カード）
def spreset_unsave():
    for i in range(len(random_spnum)):
        geneSPCard[i*2]["foreground"] = "#000000"
        geneSPCard[i*2]["background"] = "#ffffff"
        geneSPCard[i*2+1]["background"] = "#ffffff"
        if i < 2:
            geneSPCard[i*2]["text"] = ' - '
        else:
            geneSPCard[i*2]["text"] = ' '
        geneSPCard[i*2+1]["text"] = ' '
    random_spnum.clear()
    random_spcard.clear()

#記憶してリセット（特殊カード）
def spreset_save():
    for i in range(len(random_spcard)):
        all_spcard.remove(random_spcard[i])
    spreset_unsave()

#記憶をリセット（特殊カード）
def spsave_reset():
    all_spcard.clear()
    spcard_register(1)
    spcard_register(2)
    spcard_register(3)
    spcard_register(4)
    spcard_register(5)
    spcard_register(6)
    spcard_register(8)
    spcard_register(9)
    spcard_register(10)
    spreset_unsave()



#BlackMarket
def BlackMarket_setup():
    blackMarketCards.clear()
    #基本
    card_register(0, blackMarketCards)
    #陰謀
    card_register(1, blackMarketCards)
    #海辺
    card_register(2, blackMarketCards)
    #錬金術
    card_register(3, blackMarketCards)
    #繁栄
    card_register(4, blackMarketCards)
    #収穫祭
    card_register(5, blackMarketCards)
    #異郷
    card_register(6, blackMarketCards)
    #暗黒時代
    card_register(7, blackMarketCards)
    blackMarketCards.remove(card0706)
    blackMarketCards.append(card0706a)
    blackMarketCards.append(card0706b)
    blackMarketCards.append(card0706c)
    blackMarketCards.append(card0706d)
    blackMarketCards.append(card0706e)
    blackMarketCards.append(card0706f)
    blackMarketCards.append(card0706g)
    blackMarketCards.append(card0706h)
    blackMarketCards.append(card0706i)
    blackMarketCards.append(card0706j)
    #ギルド
    card_register(8, blackMarketCards)
    #冒険
    card_register(9, blackMarketCards)
    #帝国
    card_register(10, blackMarketCards)
    blackMarketCards.remove(card1006)
    blackMarketCards.append(card1006a)
    blackMarketCards.append(card1006b)
    blackMarketCards.remove(card1009)
    blackMarketCards.append(card1009a)
    blackMarketCards.append(card1009b)
    blackMarketCards.remove(card1012)
    blackMarketCards.append(card1012a)
    blackMarketCards.append(card1012b)
    blackMarketCards.remove(card1016)
    blackMarketCards.append(card1016a)
    blackMarketCards.append(card1016b)
    blackMarketCards.remove(card1019)
    blackMarketCards.append(card1019a)
    blackMarketCards.append(card1019b)
    blackMarketCards.remove(card1024)
    blackMarketCards.append(card1024a)
    blackMarketCards.append(card1024b)
    blackMarketCards.append(card1024c)
    blackMarketCards.append(card1024d)
    blackMarketCards.append(card1024e)
    blackMarketCards.append(card1024f)
    blackMarketCards.append(card1024g)
    blackMarketCards.append(card1024h)
    #夜想曲
    card_register(11, blackMarketCards)
    #ルネサンス
    card_register(12, blackMarketCards)
    #移動動物園
    card_register(13, blackMarketCards)
    #同盟
    card_register(14, blackMarketCards)
    blackMarketCards.remove(card1401)
    blackMarketCards.append(card1401a)
    blackMarketCards.append(card1401b)
    blackMarketCards.append(card1401c)
    blackMarketCards.append(card1401d)
    blackMarketCards.remove(card1402)
    blackMarketCards.append(card1402a)
    blackMarketCards.append(card1402b)
    blackMarketCards.append(card1402c)
    blackMarketCards.append(card1402d)
    blackMarketCards.remove(card1403)
    blackMarketCards.append(card1403a)
    blackMarketCards.append(card1403b)
    blackMarketCards.append(card1403c)
    blackMarketCards.append(card1403d)
    blackMarketCards.remove(card1404)
    blackMarketCards.append(card1404a)
    blackMarketCards.append(card1404b)
    blackMarketCards.append(card1404c)
    blackMarketCards.append(card1404d)
    blackMarketCards.remove(card1405)
    blackMarketCards.append(card1405a)
    blackMarketCards.append(card1405b)
    blackMarketCards.append(card1405c)
    blackMarketCards.append(card1405d)
    blackMarketCards.remove(card1406)
    blackMarketCards.append(card1406a)
    blackMarketCards.append(card1406b)
    blackMarketCards.append(card1406c)
    blackMarketCards.append(card1406d)
    #略奪
    card_register(15, blackMarketCards)
    #旭日
    card_register(16, blackMarketCards)
    #プロモ
    blackMarketCards.append(cardP002)

def BlackMarket_start():
    BlackMarket_setup()
    title_forget()
    subtitle3.pack(pady=20)
    frame_geneCard_blackMarket.pack(pady=10)
    frame_blackMarket.pack(pady=10)
    btn_blackMarket_fin.pack(pady=30)

def BlackMarket_random_card():
    for i in range(3):
        if len(blackMarketCards) > 0:
            rand.shuffle(blackMarketCards)
            randBM = blackMarketCards.pop(0)
            #カードタイプによる文字色変更（主タイプ）
            if randBM.type1 == 1:   #アクション
                geneCard_blackMarket[(i*2)-2]["foreground"] = "#000090"
            elif randBM.type1 == 2: #財宝
                geneCard_blackMarket[(i*2)-2]["foreground"] = "#f7b400"
            elif randBM.type1 == 3: #勝利点
                geneCard_blackMarket[(i*2)-2]["foreground"] = "#228b22"
            elif randBM.type1 == 4: #リアクション
                geneCard_blackMarket[(i*2)-2]["foreground"] = "#1e90ff"
            elif randBM.type1 == 5: #持続
                geneCard_blackMarket[(i*2)-2]["foreground"] = "#ff7f50"
            elif randBM.type1 == 6: #リザーブ
                geneCard_blackMarket[(i*2)-2]["foreground"] = "#808000"
            elif randBM.type1 == 7: #夜行
                geneCard_blackMarket[(i*2)-2]["foreground"] = "#000000"
            #カードタイプによる背景色変更（副タイプ）
            if randBM.type2 == 1:
                geneCard_blackMarket[(i*2)-2]["background"] = "#d3d3d3"
            elif randBM.type2 == 2:
                geneCard_blackMarket[(i*2)-2]["background"] = "#fffacd"
            elif randBM.type2 == 3:
                geneCard_blackMarket[(i*2)-2]["background"] = "#98fb98"
            elif randBM.type2 == 4:
                geneCard_blackMarket[(i*2)-2]["background"] = "#87cefa"
            elif randBM.type2 == 5:
                geneCard_blackMarket[(i*2)-2]["background"] = "#fae7d2"
            else:   #副タイプ無し
                geneCard_blackMarket[(i*2)-2]["background"] = "#ffffff"
            #カード名の貼り付け
            geneCard_blackMarket[(i*2)-2]["text"] = randBM.name
            #セットの収納BOXを背景色で視覚化
            if randBM.set == 0:
                geneCard_blackMarket[(i*2)-1]["text"] = '00-' + str(randBM.number)
                geneCard_blackMarket[(i*2)-1]["background"] = "#e0ffff"
            elif randBM.set == 1:
                geneCard_blackMarket[(i*2)-1]["text"] = '01-' + str(randBM.number)
                geneCard_blackMarket[(i*2)-1]["background"] = "#ffffe0"
            elif randBM.set == 2:
                geneCard_blackMarket[(i*2)-1]["text"] = '02-' + str(randBM.number)
                geneCard_blackMarket[(i*2)-1]["background"] = "#e0ffff"
            elif randBM.set == 3:
                geneCard_blackMarket[(i*2)-1]["text"] = '03-' + str(randBM.number)
                geneCard_blackMarket[(i*2)-1]["background"] = "#ffe0ff"
            elif randBM.set == 4:
                geneCard_blackMarket[(i*2)-1]["text"] = '04-' + str(randBM.number)
                geneCard_blackMarket[(i*2)-1]["background"] = "#e0ffff"
            elif randBM.set == 5:
                geneCard_blackMarket[(i*2)-1]["text"] = '05-' + str(randBM.number)
                geneCard_blackMarket[(i*2)-1]["background"] = "#ffe0ff"
            elif randBM.set == 6:
                geneCard_blackMarket[(i*2)-1]["text"] = '06-' + str(randBM.number)
                geneCard_blackMarket[(i*2)-1]["background"] = "#e0ffe0"
            elif randBM.set == 7:
                geneCard_blackMarket[(i*2)-1]["text"] = '07-' + str(randBM.number)
                geneCard_blackMarket[(i*2)-1]["background"] = "#e0ffe0"
            elif randBM.set == 8:
                geneCard_blackMarket[(i*2)-1]["text"] = '08-' + str(randBM.number)
                geneCard_blackMarket[(i*2)-1]["background"] = "#ffffe0"
            elif randBM.set == 9:
                geneCard_blackMarket[(i*2)-1]["text"] = '09-' + str(randBM.number)
                geneCard_blackMarket[(i*2)-1]["background"] = "#ffe0ff"
            elif randBM.set == 10:
                geneCard_blackMarket[(i*2)-1]["text"] = '10-' + str(randBM.number)
                geneCard_blackMarket[(i*2)-1]["background"] = "#e0ffff"
            elif randBM.set == 11:
                geneCard_blackMarket[(i*2)-1]["text"] = '11-' + str(randBM.number)
                geneCard_blackMarket[(i*2)-1]["background"] = "#ffffe0"
            elif randBM.set == 12:
                geneCard_blackMarket[(i*2)-1]["text"] = '12-' + str(randBM.number)
                geneCard_blackMarket[(i*2)-1]["background"] = "#ffe0ff"
            elif randBM.set == 13:
                geneCard_blackMarket[(i*2)-1]["text"] = '13-' + str(randBM.number)
                geneCard_blackMarket[(i*2)-1]["background"] = "#e0ffe0"
            elif randBM.set == 14:
                geneCard_blackMarket[(i*2)-1]["text"] = '14-' + str(randBM.number)
                geneCard_blackMarket[(i*2)-1]["background"] = "#ffe0ff"
            elif randBM.set == 15:
                geneCard_blackMarket[(i*2)-1]["text"] = '15-' + str(randBM.number)
                geneCard_blackMarket[(i*2)-1]["background"] = "#ffffe0"
            elif randBM.set == 16:
                geneCard_blackMarket[(i*2)-1]["text"] = '16-' + str(randBM.number)
                geneCard_blackMarket[(i*2)-1]["background"] = "#e0ffe0"
        else:
            BlackMarket_setup()
            i = i - 1

def BlackMarket_delete_card():
    if len(blackMarketCards) > 0:
        i = int(delete_one_blackMarket_area.get())
        rand.shuffle(blackMarketCards)
        randBM = blackMarketCards.pop(0)
        #カードタイプによる文字色変更（主タイプ）
        if randBM.type1 == 1:   #アクション
            geneCard_blackMarket[(i*2)-2]["foreground"] = "#000090"
        elif randBM.type1 == 2: #財宝
            geneCard_blackMarket[(i*2)-2]["foreground"] = "#f7b400"
        elif randBM.type1 == 3: #勝利点
            geneCard_blackMarket[(i*2)-2]["foreground"] = "#228b22"
        elif randBM.type1 == 4: #リアクション
            geneCard_blackMarket[(i*2)-2]["foreground"] = "#1e90ff"
        elif randBM.type1 == 5: #持続
            geneCard_blackMarket[(i*2)-2]["foreground"] = "#ff7f50"
        elif randBM.type1 == 6: #リザーブ
            geneCard_blackMarket[(i*2)-2]["foreground"] = "#808000"
        elif randBM.type1 == 7: #夜行
            geneCard_blackMarket[(i*2)-2]["foreground"] = "#000000"
        #カードタイプによる背景色変更（副タイプ）
        if randBM.type2 == 1:
            geneCard_blackMarket[(i*2)-2]["background"] = "#d3d3d3"
        elif randBM.type2 == 2:
            geneCard_blackMarket[(i*2)-2]["background"] = "#fffacd"
        elif randBM.type2 == 3:
            geneCard_blackMarket[(i*2)-2]["background"] = "#98fb98"
        elif randBM.type2 == 4:
            geneCard_blackMarket[(i*2)-2]["background"] = "#87cefa"
        elif randBM.type2 == 5:
            geneCard_blackMarket[(i*2)-2]["background"] = "#fae7d2"
        else:   #副タイプ無し
            geneCard_blackMarket[(i*2)-2]["background"] = "#ffffff"
        #カード名の貼り付け
        geneCard_blackMarket[(i*2)-2]["text"] = randBM.name
        #セットの収納BOXを背景色で視覚化
        if randBM.set == 0:
            geneCard_blackMarket[(i*2)-1]["text"] = '00-' + str(randBM.number)
            geneCard_blackMarket[(i*2)-1]["background"] = "#e0ffff"
        elif randBM.set == 1:
            geneCard_blackMarket[(i*2)-1]["text"] = '01-' + str(randBM.number)
            geneCard_blackMarket[(i*2)-1]["background"] = "#ffffe0"
        elif randBM.set == 2:
            geneCard_blackMarket[(i*2)-1]["text"] = '02-' + str(randBM.number)
            geneCard_blackMarket[(i*2)-1]["background"] = "#e0ffff"
        elif randBM.set == 3:
            geneCard_blackMarket[(i*2)-1]["text"] = '03-' + str(randBM.number)
            geneCard_blackMarket[(i*2)-1]["background"] = "#ffe0ff"
        elif randBM.set == 4:
            geneCard_blackMarket[(i*2)-1]["text"] = '04-' + str(randBM.number)
            geneCard_blackMarket[(i*2)-1]["background"] = "#e0ffff"
        elif randBM.set == 5:
            geneCard_blackMarket[(i*2)-1]["text"] = '05-' + str(randBM.number)
            geneCard_blackMarket[(i*2)-1]["background"] = "#ffe0ff"
        elif randBM.set == 6:
            geneCard_blackMarket[(i*2)-1]["text"] = '06-' + str(randBM.number)
            geneCard_blackMarket[(i*2)-1]["background"] = "#e0ffe0"
        elif randBM.set == 7:
            geneCard_blackMarket[(i*2)-1]["text"] = '07-' + str(randBM.number)
            geneCard_blackMarket[(i*2)-1]["background"] = "#e0ffe0"
        elif randBM.set == 8:
            geneCard_blackMarket[(i*2)-1]["text"] = '08-' + str(randBM.number)
            geneCard_blackMarket[(i*2)-1]["background"] = "#ffffe0"
        elif randBM.set == 9:
            geneCard_blackMarket[(i*2)-1]["text"] = '09-' + str(randBM.number)
            geneCard_blackMarket[(i*2)-1]["background"] = "#ffe0ff"
        elif randBM.set == 10:
            geneCard_blackMarket[(i*2)-1]["text"] = '10-' + str(randBM.number)
            geneCard_blackMarket[(i*2)-1]["background"] = "#e0ffff"
        elif randBM.set == 11:
            geneCard_blackMarket[(i*2)-1]["text"] = '11-' + str(randBM.number)
            geneCard_blackMarket[(i*2)-1]["background"] = "#ffffe0"
        elif randBM.set == 12:
            geneCard_blackMarket[(i*2)-1]["text"] = '12-' + str(randBM.number)
            geneCard_blackMarket[(i*2)-1]["background"] = "#ffe0ff"
        elif randBM.set == 13:
            geneCard_blackMarket[(i*2)-1]["text"] = '13-' + str(randBM.number)
            geneCard_blackMarket[(i*2)-1]["background"] = "#e0ffe0"
        elif randBM.set == 14:
            geneCard_blackMarket[(i*2)-1]["text"] = '14-' + str(randBM.number)
            geneCard_blackMarket[(i*2)-1]["background"] = "#ffe0ff"
        elif randBM.set == 15:
            geneCard_blackMarket[(i*2)-1]["text"] = '15-' + str(randBM.number)
            geneCard_blackMarket[(i*2)-1]["background"] = "#ffffe0"
        elif randBM.set == 16:
            geneCard_blackMarket[(i*2)-1]["text"] = '16-' + str(randBM.number)
            geneCard_blackMarket[(i*2)-1]["background"] = "#e0ffe0"
    else:
        BlackMarket_setup()
        BlackMarket_delete_card()

def BlackMarket_fin():
    title_pack()
    subtitle3.pack_forget()
    frame_geneCard_blackMarket.pack_forget()
    frame_blackMarket.pack_forget()
    btn_blackMarket_fin.pack_forget()



#王国カード情報登録
all_card = []
full_card = []
true_card = []
#基本
card0000a = Card('銅貨',0,0,2,0)
card0000b = Card('銀貨',0,0,2,0)
card0000c = Card('金貨',0,0,2,0)
card0000d = Card('屋敷',0,0,3,0)
card0000e = Card('公領',0,0,3,0)
card0000f = Card('属州',0,0,3,0)
card0000g = Card('呪い',0,0,0,0)
card0001 = Card('堀',0,1,4,0)
card0002 = Card('職人',0,2,1,0)
card0003 = Card('山賊',0,3,1,0)
card0004 = Card('役人',0,4,1,0)
card0005 = Card('地下貯蔵庫',0,5,1,0)
card0006 = Card('礼拝堂',0,6,1,0)
card0007 = Card('議事堂',0,7,1,0)
card0008 = Card('祝祭',0,8,1,0)
card0009 = Card('前駆者',0,9,1,0)
card0010 = Card('研究所',0,10,1,0)
card0011 = Card('書庫',0,11,1,0)
card0012 = Card('市場',0,12,1,0)
card0013 = Card('商人',0,13,1,0)
card0014 = Card('民兵',0,14,1,0)
card0015 = Card('鉱山',0,15,1,0)
card0016 = Card('金貸し',0,16,1,0)
card0017 = Card('密猟者',0,17,1,0)
card0018 = Card('改築',0,18,1,0)
card0019 = Card('衛兵',0,19,1,0)
card0020 = Card('鍛冶屋',0,20,1,0)
card0021 = Card('玉座の間',0,21,1,0)
card0022 = Card('家臣',0,22,1,0)
card0023 = Card('村',0,23,1,0)
card0024 = Card('魔女',0,24,1,0)
card0025 = Card('工房',0,25,1,0)
card0026 = Card('庭園',0,26,3,0)
#陰謀
card0101 = Card('外交官',1,1,4,0)
card0102 = Card('改良',1,2,1,0)
card0103 = Card('隠し通路',1,3,1,0)
card0104 = Card('仮面舞踏会',1,4,1,0)
card0105 = Card('共謀者',1,5,1,0)
card0106 = Card('交易場',1,6,1,0)
card0107 = Card('鉱山の村',1,7,1,0)
card0108 = Card('拷問人',1,8,1,0)
card0109 = Card('詐欺師',1,9,1,0)
card0110 = Card('執事',1,10,1,0)
card0111 = Card('男爵',1,11,1,0)
card0112 = Card('寵臣',1,12,1,0)
card0113 = Card('廷臣',1,13,1,0)
card0114 = Card('手先',1,14,1,0)
card0115 = Card('鉄工所',1,15,1,0)
card0116 = Card('中庭',1,16,1,0)
card0117 = Card('願いの井戸',1,17,1,0)
card0118 = Card('橋',1,18,1,0)
card0119 = Card('パトロール',1,19,1,0)
card0120 = Card('貧民街',1,20,1,0)
card0121 = Card('待ち伏せ',1,21,1,0)
card0122 = Card('身代わり',1,22,1,0)
card0123 = Card('貴族',1,23,1,3)
card0124 = Card('風車',1,24,1,3)
card0125 = Card('ハーレム',1,25,2,3)
card0126 = Card('公爵',1,26,3,0)
#海辺
card0201 = Card('海賊',2,1,5,4)
card0202 = Card('海の魔女',2,2,5,0)
card0203 = Card('漁村',2,3,5,0)
card0204 = Card('コルセア',2,4,5,0)
card0205 = Card('策士',2,5,5,0)
card0206 = Card('サル',2,6,5,0)
card0207 = Card('潮溜り',2,7,5,0)
card0208 = Card('商船',2,8,5,0)
card0209 = Card('前哨地',2,9,5,0)
card0210 = Card('隊商',2,10,5,0)
card0211 = Card('停泊所',2,11,5,0)
card0212 = Card('灯台',2,12,5,0)
card0213 = Card('封鎖',2,13,5,0)
card0214 = Card('船着場',2,14,5,0)
card0215 = Card('船乗り',2,15,5,0)
card0216 = Card('海図',2,16,1,0)
card0217 = Card('巾着切り',2,17,1,0)
card0218 = Card('原住民の村',2,18,1,0)
card0219 = Card('倉庫',2,19,1,0)
card0220 = Card('宝の地図',2,20,1,0)
card0221 = Card('バザー',2,21,1,0)
card0222 = Card('引揚水夫',2,22,1,0)
card0223 = Card('宝物庫',2,23,1,0)
card0224 = Card('密輸人',2,24,1,0)
card0225 = Card('見張り',2,25,1,0)
card0226 = Card('島',2,26,1,3)
card0227 = Card('アストロラーベ',2,27,2,5)
#錬金術
card0301 = Card('薬師',3,1,1,0)
card0302 = Card('ゴーレム',3,2,1,0)
card0303 = Card('支配',3,3,1,0)
card0304 = Card('大学',3,4,1,0)
card0305 = Card('使い魔',3,5,1,0)
card0306 = Card('弟子',3,6,1,0)
card0307 = Card('念視の泉',3,7,1,0)
card0308 = Card('変成',3,8,1,0)
card0309 = Card('薬草商',3,9,1,0)
card0310 = Card('錬金術師',3,10,1,0)
card0311 = Card('賢者の石',3,11,2,0)
card0312 = Card('ブドウ園',3,12,3,0)
#繁栄
card0400a = Card('白金貨',4,0,2,0)
card0400b = Card('植民地',4,0,3,0)
card0401 = Card('書記',4,1,4,0)
card0402 = Card('望楼',4,2,4,0)
card0403 = Card('拡張',4,3,1,0)
card0404 = Card('記念碑',4,4,1,0)
card0405 = Card('宮廷',4,5,1,0)
card0406 = Card('行商人',4,6,1,0)
card0407 = Card('司教',4,7,1,0)
card0408 = Card('造幣所',4,8,1,0)
card0409 = Card('大市場',4,9,1,0)
card0410 = Card('大衆',4,10,1,0)
card0411 = Card('鍛造',4,11,1,0)
card0412 = Card('都市',4,12,1,0)
card0413 = Card('保管庫',4,13,1,0)
card0414 = Card('山師',4,14,1,0)
card0415 = Card('有力者',4,15,1,0)
card0416 = Card('労働者の村',4,16,1,0)
card0417 = Card('石切場',4,17,2,0)
card0418 = Card('隠し財産',4,18,2,0)
card0419 = Card('金床',4,19,2,0)
card0420 = Card('銀行',4,20,2,0)
card0421 = Card('軍用金',4,21,2,0)
card0422 = Card('収集品',4,22,2,0)
card0423 = Card('出資',4,23,2,0)
card0424 = Card('水晶球',4,24,2,0)
card0425 = Card('ティアラ',4,25,2,0)
#収穫祭
card0501 = Card('馬商人',5,1,4,0)
card0502 = Card('移動動物園',5,2,1,0)
card0503 = Card('占い師',5,3,1,0)
card0504 = Card('再建',5,4,1,0)
card0505 = Card('収穫',5,5,1,0)
card0506 = Card('狩猟団',5,6,1,0)
card0507 = Card('村落',5,7,1,0)
card0508 = Card('道化師',5,8,1,0)
card0509 = Card('農村',5,9,1,0)
card0510 = Card('馬上槍試合',5,10,1,0)
card0510a = Card('王女',5,10,1,0)
card0510b = Card('金貨袋',5,10,2,0)
card0510c = Card('名馬',5,10,1,0)
card0510d = Card('郎党',5,10,1,0)
card0510e = Card('王冠',5,10,2,0)
card0511 = Card('魔女娘',5,11,1,0)
card0512 = Card('豊穣の角笛',5,12,2,0)
card0513 = Card('品評会',5,13,3,0)
#異郷
card0601 = Card('交易人',6,1,4,0)
card0602 = Card('織工',6,2,4,0)
card0603 = Card('進路',6,3,4,0)
card0604 = Card('番犬',6,4,4,0)
card0605 = Card('オアシス',6,5,1,0)
card0606 = Card('街道',6,6,1,0)
card0607 = Card('開発',6,7,1,0)
card0608 = Card('画策',6,8,1,0)
card0609 = Card('厩舎',6,9,1,0)
card0610 = Card('狂戦士',6,10,1,0)
card0611 = Card('岐路',6,11,1,0)
card0612 = Card('車大工',6,12,1,0)
card0613 = Card('香辛料理人',6,13,1,0)
card0614 = Card('国境の村',6,14,1,0)
card0615 = Card('スーク',6,15,1,0)
card0616 = Card('地図職人',6,16,1,0)
card0617 = Card('値切り屋',6,17,1,0)
card0618 = Card('辺境伯',6,18,1,0)
card0619 = Card('魔女の小屋',6,19,1,0)
card0620 = Card('宿屋',6,20,1,0)
card0621 = Card('遊牧民',6,21,1,0)
card0622 = Card('よろずや',6,22,1,0)
card0623 = Card('愚者の黄金',6,23,4,2)
card0624 = Card('大釜',6,24,2,0)
card0625 = Card('坑道',6,25,4,3)
card0626 = Card('農地',6,26,3,0)
#暗黒時代
card0700a = Card('廃村',7,1,1,0)
card0700b = Card('市場跡地',7,1,1,0)
card0700c = Card('図書館跡地',7,1,1,0)
card0700d = Card('廃坑',7,1,1,0)
card0700e = Card('生存者',7,1,1,0)
card0700f = Card('共同墓地',7,0,1,0)
card0700g = Card('草茂る屋敷',7,0,1,0)
card0700h = Card('納屋',7,0,1,0)
card0701 = Card('青空市場',7,1,4,0)
card0702 = Card('物乞い',7,2,4,0)
card0703 = Card('隠遁者',7,3,1,0)
card0703a = Card('狂人',7,3,1,0)
card0704 = Card('金物商',7,4,1,0)
card0705 = Card('狩場',7,5,1,0)
card0706 = Card('騎士',7,6,1,0)
card0706a = Card('デイム・アンナ',7,6,1,0)
card0706b = Card('デイム・ジョセフィーヌ',7,6,1,3)
card0706c = Card('デイム・シルビア',7,6,1,0)
card0706d = Card('デイム・ナタリー',7,6,1,0)
card0706e = Card('デイム・モリー',7,6,1,0)
card0706f = Card('サー・ヴァンデル',7,6,1,0)
card0706g = Card('サー・デストリー',7,6,1,0)
card0706h = Card('サー・ベイリー',7,6,1,0)
card0706i = Card('サー・マーチン',7,6,1,0)
card0706j = Card('サー・マイケル',7,6,1,0)
card0707 = Card('救貧院',7,7,1,0)
card0708 = Card('狂信者',7,8,1,0)
card0709 = Card('吟遊詩人',7,9,1,0)
card0710 = Card('屑屋',7,10,1,0)
card0711 = Card('賢者',7,11,1,0)
card0712 = Card('行進',7,12,1,0)
card0713 = Card('ゴミあさり',7,13,1,0)
card0714 = Card('採集者',7,14,1,0)
card0715 = Card('祭壇',7,15,1,0)
card0716 = Card('山賊の宿営地',7,16,1,0)
card0716a = Card('略奪品',7,16,2,0)
card0717 = Card('死の荷車',7,17,1,0)
card0718 = Card('襲撃者',7,18,1,0)
card0719 = Card('従者',7,19,1,0)
card0720 = Card('城塞',7,20,1,0)
card0721 = Card('建て直し',7,21,1,0)
card0722 = Card('地下墓所',7,22,1,0)
card0723 = Card('盗賊',7,23,1,0)
card0724 = Card('ネズミ',7,24,1,0)
card0725 = Card('墓暴き',7,25,1,0)
card0726 = Card('伯爵',7,26,1,0)
card0727 = Card('はみだし者',7,27,1,0)
card0728 = Card('秘術師',7,28,1,0)
card0729 = Card('武器庫',7,29,1,0)
card0730 = Card('浮浪児',7,30,1,0)
card0730a = Card('傭兵',7,30,1,0)
card0731 = Card('浮浪者',7,31,1,0)
card0732 = Card('物置',7,32,1,0)
card0733 = Card('略奪',7,33,1,0)
card0734 = Card('偽造通貨',7,34,1,0)
card0735 = Card('封土',7,35,1,0)
#ギルド
card0801 = Card('石工',8,1,1,0)
card0802 = Card('医者',8,2,1,0)
card0803 = Card('収税吏',8,3,1,0)
card0804 = Card('熟練工',8,4,1,0)
card0805 = Card('商人ギルド',8,5,1,0)
card0806 = Card('助言者',8,6,1,0)
card0807 = Card('伝令官',8,7,1,0)
card0808 = Card('肉屋',8,8,1,0)
card0809 = Card('パン屋',8,9,1,0)
card0810 = Card('広場',8,10,1,0)
card0811 = Card('予言者',8,11,1,0)
card0812 = Card('蝋燭職人',8,12,1,0)
card0813 = Card('名品',8,13,2,0)
#冒険
card0901 = Card('隊商の護衛',9,1,5,4)
card0902 = Card('地下牢',9,2,5,0)
card0903 = Card('道具',9,3,5,0)
card0904 = Card('沼の妖婆',9,4,5,0)
card0905 = Card('呪いの森',9,5,5,0)
card0906 = Card('橋の下のトロル',9,6,5,0)
card0907 = Card('魔除け',9,7,5,0)
card0908 = Card('雇人',9,8,5,0)
card0909 = Card('案内人',9,9,6,0)
card0910 = Card('御料車',9,10,6,0)
card0911 = Card('鼠取り',9,11,6,0)
card0912 = Card('複製',9,12,6,0)
card0913 = Card('変容',9,13,6,0)
card0914 = Card('ワイン商',9,14,6,0)
card0915 = Card('遠隔地',9,15,6,3)
card0916 = Card('騎士見習い',9,16,1,0)
card0916a = Card('トレジャーハンター',9,16,1,0)
card0916b = Card('ウォリアー',9,16,1,0)
card0916c = Card('ヒーロー',9,16,1,0)
card0916d = Card('チャンピオン',9,16,4,0)
card0917 = Card('農民',9,17,1,0)
card0917a = Card('兵士',9,17,1,0)
card0917b = Card('脱走兵',9,17,1,0)
card0917c = Card('門下生',9,17,1,0)
card0917d = Card('教師',9,17,6,0)
card0918 = Card('失われし都市',9,18,1,0)
card0919 = Card('カササギ',9,19,1,0)
card0920 = Card('語り部',9,20,1,0)
card0921 = Card('巨人',9,21,1,0)
card0922 = Card('工匠',9,22,1,0)
card0923 = Card('使者',9,23,1,0)
card0924 = Card('守銭奴',9,24,1,0)
card0925 = Card('倒壊',9,25,1,0)
card0926 = Card('港町',9,26,1,0)
card0927 = Card('山守',9,27,1,0)
card0928 = Card('法貨',9,28,6,2)
card0929 = Card('遺物',9,29,2,0)
card0930 = Card('掘出物',9,30,2,0)
#帝国
card1001 = Card('女魔術師',10,1,5,0)
card1002 = Card('資料庫',10,2,5,0)
card1003 = Card('生贄',10,3,1,0)
card1004 = Card('ヴィラ',10,4,1,0)
card1005 = Card('王室の鍛冶屋',10,5,1,0)
card1006 = Card('開拓者/騒がしい村',10,6,1,0)
card1006a = Card('開拓者',10,6,1,0)
card1006b = Card('騒がしい村',10,6,1,0)
card1007 = Card('技術者',10,7,1,0)
card1008 = Card('軍団兵',10,8,1,0)
card1009 = Card('剣闘士/大金',10,9,1,0)
card1009a = Card('剣闘士',10,6,1,0)
card1009b = Card('大金',10,6,2,0)
card1010 = Card('公共広場',10,10,1,0)
card1011 = Card('市街',10,11,1,0)
card1012 = Card('陣地/鹵獲品',10,12,1,0)
card1012a = Card('陣地',10,6,1,0)
card1012b = Card('鹵獲品',10,6,2,0)
card1013 = Card('神殿',10,13,1,0)
card1014 = Card('戦車競走',10,14,1,0)
card1015 = Card('大君主',10,15,1,0)
card1016 = Card('投石機/石',10,16,1,0)
card1016a = Card('投石機',10,6,1,0)
card1016b = Card('石',10,6,2,0)
card1017 = Card('庭師',10,17,1,0)
card1018 = Card('農家の市場',10,18,1,0)
card1019 = Card('パトリキ/エンポリウム',10,19,1,0)
card1019a = Card('パトリキ',10,6,1,0)
card1019b = Card('エンポリウム',10,6,1,0)
card1020 = Card('ワイルドハント',10,20,1,0)
card1021 = Card('冠',10,21,1,2)
card1022 = Card('御守り',10,22,2,0)
card1023 = Card('元手',10,23,2,0)
card1024 = Card('城',10,24,3,0)
card1024a = Card('粗末な城',10,24,3,2)
card1024b = Card('崩れた城',10,24,3,0)
card1024c = Card('小さな城',10,24,3,1)
card1024d = Card('幽霊城',10,24,3,0)
card1024e = Card('華やかな城',10,24,3,1)
card1024f = Card('広大な城',10,24,3,0)
card1024g = Card('壮大な城',10,24,3,0)
card1024h = Card('王城',10,24,3,0)
#夜想曲
card1100a = Card('願い',11,0,1,0)
card1100b = Card('ウィル・オ・ウィスプ',11,0,1,0)
card1100c = Card('インプ',11,0,1,0)
card1100d = Card('幽霊',11,0,7,5)
card1101 = Card('忠犬',11,1,4,0)
card1102 = Card('秘密の洞窟',11,2,5,0)
card1102a = Card('魔法のランプ',11,2,2,0)
card1103 = Card('暗躍者',11,3,1,0)
card1104 = Card('愚者',11,4,1,0)
card1104a = Card('幸運のコイン',11,4,2,0)
card1105 = Card('コンクラーベ',11,5,1,0)
card1106 = Card('詩人',11,6,1,0)
card1107 = Card('聖なる木立ち',11,7,1,0)
card1108 = Card('追跡者',11,8,1,0)
card1108a = Card('革袋',11,8,2,0)
card1109 = Card('ドルイド',11,9,1,0)
card1110 = Card('ネクロマンサー',11,10,1,0)
card1110a = Card('ゾンビの弟子',11,10,1,0)
card1110b = Card('ゾンビの石工',11,10,1,0)
card1110c = Card('ゾンビの密偵',11,10,1,0)
card1111 = Card('呪われた村',11,11,1,0)
card1112 = Card('迫害者',11,12,1,0)
card1113 = Card('ピクシー',11,13,1,0)
card1113a = Card('ヤギ',11,13,2,0)
card1114 = Card('悲劇のヒーロー',11,14,1,0)
card1115 = Card('羊飼い',11,15,1,0)
card1115a = Card('牧草地',11,15,2,3)
card1116 = Card('プーカ',11,16,1,0)
card1116a = Card('呪われた金貨',11,16,2,0)
card1117 = Card('恵みの村',11,17,1,0)
card1118 = Card('レプラコーン',11,18,1,0)
card1119 = Card('偶像',11,19,2,0)
card1120 = Card('墓地',11,20,3,0)
card1120a = Card('呪いの鏡',11,20,2,0)
card1121 = Card('悪人のアジト',11,21,7,5)
card1122 = Card('カブラー',11,22,7,5)
card1123 = Card('ゴーストタウン',11,23,7,5)
card1124 = Card('守護者',11,24,7,5)
card1125 = Card('納骨堂',11,25,7,5)
card1126 = Card('夜襲',11,26,7,5)
card1127 = Card('人狼',11,27,7,1)
card1128 = Card('悪魔の工房',11,28,7,0)
card1129 = Card('悪魔祓い',11,29,7,0)
card1130 = Card('吸血鬼',11,30,7,0)
card1130a = Card('コウモリ',11,30,7,0)
card1131 = Card('修道院',11,31,7,0)
card1132 = Card('取り替え子',11,32,7,0)
card1133 = Card('夜警',11,33,7,0)
#ルネサンス
card1201 = Card('パトロン',12,1,4,0)
card1202 = Card('貨物船',12,2,5,0)
card1203 = Card('研究',12,3,5,0)
card1204 = Card('悪党',12,4,1,0)
card1205 = Card('学者',12,5,1,0)
card1206 = Card('旗手',12,6,1,0)
card1207 = Card('絹商人',12,7,1,0)
card1208 = Card('劇団',12,8,1,0)
card1209 = Card('剣客',12,9,1,0)
card1210 = Card('国境警備隊',12,10,1,0)
card1211 = Card('山村',12,11,1,0)
card1212 = Card('司祭',12,12,1,0)
card1213 = Card('実験',12,13,1,0)
card1214 = Card('出納官',12,14,1,0)
card1215 = Card('先見者',12,15,1,0)
card1216 = Card('増築',12,16,1,0)
card1217 = Card('彫刻家',12,17,1,0)
card1218 = Card('徴募官',12,18,1,0)
card1219 = Card('追従者',12,19,1,0)
card1220 = Card('根城',12,20,1,0)
card1221 = Card('発明家',12,21,1,0)
card1222 = Card('老魔女',12,22,1,0)
card1223 = Card('王笏',12,23,2,0)
card1224 = Card('香辛料',12,24,2,0)
card1225 = Card('ドゥカート金貨',12,25,2,0)
#移動動物園
card1300 = Card('馬',13,0,1,0)
card1301 = Card('黒猫',13,1,4,0)
card1302 = Card('そり',13,2,4,0)
card1303 = Card('鷹匠',13,3,4,0)
card1304 = Card('牧羊犬',13,4,4,0)
card1305 = Card('村有緑地',13,5,5,4)
card1306 = Card('首謀者',13,6,5,0)
card1307 = Card('艀',13,7,5,0)
card1308 = Card('門番',13,8,5,0)
card1309 = Card('貸し馬屋',13,9,1,0)
card1310 = Card('がらくた',13,10,1,0)
card1311 = Card('騎兵隊',13,11,1,0)
card1312 = Card('強制退去',13,12,1,0)
card1313 = Card('行人',13,13,1,0)
card1314 = Card('狩猟小屋',13,14,1,0)
card1315 = Card('賞金稼ぎ',13,15,1,0)
card1316 = Card('枢機卿',13,16,1,0)
card1317 = Card('聖域',13,17,1,0)
card1318 = Card('デストリエ',13,18,1,0)
card1319 = Card('動物見本市',13,19,1,0)
card1320 = Card('旅籠',13,20,1,0)
card1321 = Card('馬丁',13,21,1,0)
card1322 = Card('パドック',13,22,1,0)
card1323 = Card('魔女の集会',13,23,1,0)
card1324 = Card('ヤギ飼い',13,24,1,0)
card1325 = Card('雪深い村',13,25,5,0)
card1326 = Card('ラクダの隊列',13,26,1,0)
card1327 = Card('漁師',13,27,1,0)
card1328 = Card('炉',13,28,1,0)
card1329 = Card('配給品',13,29,1,0)
card1330 = Card('備蓄品',13,30,1,0)
#同盟
card1401 = Card('城砦',14,1,1,0)
card1401a = Card('天幕',14,1,1,0)
card1401b = Card('駐屯地',14,1,5,0)
card1401c = Card('堡塁',14,1,1,0)
card1401d = Card('要塞',14,1,5,3)
card1402 = Card('衝突',14,2,1,0)
card1402a = Card('戦闘計画',14,2,1,0)
card1402b = Card('射手',14,2,1,0)
card1402c = Card('将軍',14,2,5,0)
card1402d = Card('領土',14,2,3,0)
card1403 = Card('叙事詩',14,3,1,0)
card1403a = Card('古地図',14,3,1,0)
card1403b = Card('航海',14,3,5,0)
card1403c = Card('沈没船の財宝',14,3,2,0)
card1403d = Card('遠い海岸',14,3,1,3)
card1404 = Card('町民',14,4,1,0)
card1404a = Card('触れ役',14,4,1,0)
card1404b = Card('蹄鉄工',14,4,1,0)
card1404c = Card('粉屋',14,4,1,0)
card1404d = Card('長老',14,4,1,0)
card1405 = Card('卜占官',14,5,1,0)
card1405a = Card('薬草集め',14,5,1,0)
card1405b = Card('侍祭',14,5,1,0)
card1405c = Card('女魔道士',14,5,1,0)
card1405d = Card('女予言者',14,5,1,0)
card1406 = Card('魔法使い',14,6,1,0)
card1406a = Card('生徒',14,6,1,0)
card1406b = Card('霊術士',14,6,5,0)
card1406c = Card('魔導士',14,6,1,0)
card1406d = Card('リッチ',14,6,1,0)
card1407 = Card('追いはぎ',14,7,5,0)
card1408 = Card('王家のガレー船',14,8,5,0)
card1409 = Card('輸入者',14,9,5,0)
card1410 = Card('改造',14,10,1,0)
card1411 = Card('狩人',14,11,1,0)
card1412 = Card('ガレリア',14,12,1,0)
card1413 = Card('急使',14,13,1,0)
card1414 = Card('ギルドマスター',14,14,1,0)
card1415 = Card('交換',14,15,1,0)
card1416 = Card('侯爵',14,16,1,0)
card1417 = Card('ごますり',14,17,1,0)
card1418 = Card('散兵',14,18,1,0)
card1419 = Card('下役',14,19,1,0)
card1420 = Card('首都',14,20,1,0)
card1421 = Card('商人の野営地',14,21,1,0)
card1422 = Card('専門家',14,22,1,0)
card1423 = Card('大工',14,23,1,0)
card1424 = Card('仲買人',14,24,1,0)
card1425 = Card('蛮族',14,25,5,0)
card1426 = Card('歩哨',14,26,1,0)
card1427 = Card('町',14,27,1,0)
card1428 = Card('密使',14,28,1,0)
card1429 = Card('宿屋の主人',14,29,1,0)
card1430 = Card('契約書',14,30,2,5)
card1431 = Card('道化棒',14,31,2,0)
#略奪
card1500a = Card('アンフォラ',15,0,2,5)
card1500b = Card('ダブロン金貨',15,0,2,0)
card1500c = Card('尽きぬ杯',15,0,2,5)
card1500d = Card('船首像',15,0,2,5)
card1500e = Card('ハンマー',15,0,2,0)
card1500f = Card('勲章',15,0,2,0)
card1500g = Card('宝石',15,0,2,5)
card1500h = Card('宝珠',15,0,2,0)
card1500i = Card('賞品のヤギ',15,0,2,0)
card1500j = Card('パズルボックス',15,0,2,0)
card1500k = Card('六分儀',15,0,2,0)
card1500l = Card('盾',15,0,2,4)
card1500m = Card('呪符の巻物',15,0,1,2)
card1500n = Card('杖',15,0,2,0)
card1500o = Card('剣',15,0,2,0)
card1501 = Card('地図作り',15,1,4,0)
card1502 = Card('密航者',15,2,5,4)
card1503 = Card('岩屋',15,3,5,0)
card1504 = Card('拡大',15,4,5,0)
card1505 = Card('旗艦',15,5,5,0)
card1506 = Card('キャビンボーイ',15,6,5,0)
card1507 = Card('切り裂き魔',15,7,5,0)
card1508 = Card('現場監督',15,8,5,0)
card1509 = Card('上陸部隊',15,9,5,0)
card1510 = Card('セイレーン',15,10,5,0)
card1511 = Card('操舵手',15,11,5,0)
card1512 = Card('調査',15,12,5,0)
card1513 = Card('乗組員',15,13,5,0)
card1514 = Card('秘境の社',15,14,5,0)
card1515 = Card('フリゲート船',15,15,5,0)
card1516 = Card('ロングシップ',15,16,5,0)
card1517 = Card('一等航海士',15,17,1,0)
card1518 = Card('置き去り',15,18,1,0)
card1519 = Card('価値ある村',15,19,1,0)
card1520 = Card('鉱山道路',15,20,1,0)
card1521 = Card('財産目当て',15,21,1,0)
card1522 = Card('シャーマン',15,22,1,0)
card1523 = Card('巡礼者',15,23,1,0)
card1524 = Card('トリックスター',15,24,1,0)
card1525 = Card('沼地の小屋',15,25,1,0)
card1526 = Card('港の村',15,26,1,0)
card1527 = Card('埋められた財宝',15,27,2,5)
card1528 = Card('檻',15,28,2,5)
card1529 = Card('ゴンドラ',15,29,2,5)
card1530 = Card('縄',15,30,2,5)
card1531 = Card('豊穣',15,31,2,5)
card1532 = Card('王の隠し財産',15,32,2,0)
card1533 = Card('銀山',15,33,2,0)
card1534 = Card('工具',15,34,2,0)
card1535 = Card('小像',15,35,2,0)
card1536 = Card('戦利品の袋',15,36,2,0)
card1537 = Card('つるはし',15,37,2,0)
card1538 = Card('ペンダント',15,38,2,0)
card1539 = Card('宝飾卵',15,39,2,0)
card1540 = Card('坩堝',15,40,2,0)
#旭日
card1601 = Card('川船',16,1,5,0)
card1602 = Card('侍',16,2,5,0)
card1603 = Card('田舎の村',16,3,1,0)
card1604 = Card('絵師',16,4,1,0)
card1605 = Card('駕籠',16,5,1,0)
card1606 = Card('歌人',16,6,1,0)
card1607 = Card('川の社',16,7,1,0)
card1608 = Card('狐',16,8,1,0)
card1609 = Card('金山',16,9,1,0)
card1610 = Card('公家',16,10,1,0)
card1611 = Card('交替',16,11,1,0)
card1612 = Card('小路',16,12,1,0)
card1613 = Card('魚屋',16,13,1,0)
card1614 = Card('大名',16,14,1,0)
card1615 = Card('狸',16,15,1,0)
card1616 = Card('茶屋',16,16,1,0)
card1617 = Card('勅使',16,17,1,0)
card1618 = Card('忍者',16,18,1,0)
card1619 = Card('濡女',16,19,1,0)
card1620 = Card('札差',16,20,1,0)
card1621 = Card('室',16,21,1,0)
card1622 = Card('名匠',16,22,1,0)
card1623 = Card('山の社',16,23,1,0)
card1624 = Card('浪人',16,24,1,0)
card1625 = Card('米',16,25,2,0)
#プロモ
cardP001 = Card('闇市場',-1,1,1,0)
cardP002 = Card('境界地',-1,2,3,0)

#特殊カード情報登録
all_spcard = []
#イベント-冒険
spcard0101 = Card('借入',9,1,1,0)
spcard0102 = Card('探索',9,2,1,0)
spcard0103 = Card('施し',9,3,1,0)
spcard0104 = Card('保存',9,4,1,0)
spcard0105 = Card('移動遊園地',9,5,1,0)
spcard0106 = Card('偵察隊',9,6,1,0)
spcard0107 = Card('焚火',9,7,1,0)
spcard0108 = Card('探検',9,8,1,0)
spcard0109 = Card('立案',9,9,1,0)
spcard0110 = Card('渡し船',9,10,1,0)
spcard0111 = Card('使節団',9,11,1,0)
spcard0112 = Card('巡礼',9,12,1,0)
spcard0113 = Card('海路',9,13,1,0)
spcard0114 = Card('奇襲',9,14,1,0)
spcard0115 = Card('交易',9,15,1,0)
spcard0116 = Card('舞踏会',9,16,1,0)
spcard0117 = Card('失われた技術',9,17,1,0)
spcard0118 = Card('鍛錬',9,18,1,0)
spcard0119 = Card('相続',9,19,1,0)
spcard0120 = Card('誘導',9,20,1,0)
#イベント-帝国
spcard0201 = Card('昇進',10,1,1,0)
spcard0202 = Card('掘進',10,2,1,0)
spcard0203 = Card('徴税',10,3,1,0)
spcard0204 = Card('宴会',10,4,1,0)
spcard0205 = Card('儀式',10,5,1,0)
spcard0206 = Card('大地への塩まき',10,6,1,0)
spcard0207 = Card('結婚式',10,7,1,0)
spcard0208 = Card('意外な授かり物',10,8,1,0)
spcard0209 = Card('凱旋',10,9,1,0)
spcard0210 = Card('征服',10,10,1,0)
spcard0211 = Card('制圧',10,11,1,0)
spcard0212 = Card('寄付',10,12,1,0)
spcard0213 = Card('併合',10,13,1,0)
#ランドマーク-帝国
spcard0301 = Card('狼の巣',10,1,2,0)
spcard0302 = Card('オベリスク',10,2,2,0)
spcard0303 = Card('凱旋門',10,3,2,0)
spcard0304 = Card('果樹園',10,4,2,0)
spcard0305 = Card('壁',10,5,2,0)
spcard0306 = Card('宮殿',10,6,2,0)
spcard0307 = Card('汚された神殿',10,7,2,0)
spcard0308 = Card('公会堂',10,8,2,0)
spcard0309 = Card('山賊の砦',10,9,2,0)
spcard0310 = Card('水道橋',10,10,2,0)
spcard0311 = Card('戦場',10,11,2,0)
spcard0312 = Card('塔',10,12,2,0)
spcard0313 = Card('闘技場',10,13,2,0)
spcard0314 = Card('峠',10,14,2,0)
spcard0315 = Card('砦',10,15,2,0)
spcard0316 = Card('博物館',10,16,2,0)
spcard0317 = Card('噴水',10,17,2,0)
spcard0318 = Card('墓標',10,18,2,0)
spcard0319 = Card('迷宮',10,19,2,0)
spcard0320 = Card('浴場',10,20,2,0)
spcard0321 = Card('列柱',10,21,2,0)
#プロジェクト-ルネサンス
spcard0401 = Card('運河',12,1,3,0)
spcard0402 = Card('縁日',12,2,3,0)
spcard0403 = Card('学園',12,3,3,0)
spcard0404 = Card('艦隊',12,4,3,0)
spcard0405 = Card('技術革新',12,5,3,0)
spcard0406 = Card('ギルド集会所',12,6,3,0)
spcard0407 = Card('下水道',12,7,3,0)
spcard0408 = Card('サイロ',12,8,3,0)
spcard0409 = Card('山砦',12,9,3,0)
spcard0410 = Card('資本主義',12,10,3,0)
spcard0411 = Card('城門',12,11,3,0)
spcard0412 = Card('星図',12,12,3,0)
spcard0413 = Card('大聖堂',12,13,3,0)
spcard0414 = Card('探査',12,14,3,0)
spcard0415 = Card('道路網',12,15,3,0)
spcard0416 = Card('ピアッツァ',12,16,3,0)
spcard0417 = Card('兵舎',12,17,3,0)
spcard0418 = Card('野外劇',12,18,3,0)
spcard0419 = Card('輪作',12,19,3,0)
spcard0420 = Card('悪巧み',12,20,3,0)
#イベント-移動動物園
spcard0501 = Card('遅延',13,1,1,0)
spcard0502 = Card('絶望',13,2,1,0)
spcard0503 = Card('博打',13,3,1,0)
spcard0504 = Card('追求',13,4,1,0)
spcard0505 = Card('乗馬',13,5,1,0)
spcard0506 = Card('苦労',13,6,1,0)
spcard0507 = Card('増大',13,7,1,0)
spcard0508 = Card('進軍',13,8,1,0)
spcard0509 = Card('輸送',13,9,1,0)
spcard0510 = Card('放逐',13,10,1,0)
spcard0511 = Card('特価品',13,11,1,0)
spcard0512 = Card('投資',13,12,1,0)
spcard0513 = Card('今を生きる',13,13,1,0)
spcard0514 = Card('商売',13,14,1,0)
spcard0515 = Card('要求',13,15,1,0)
spcard0516 = Card('暴走',13,16,1,0)
spcard0517 = Card('刈り入れ',13,17,1,0)
spcard0518 = Card('包領',13,18,1,0)
spcard0519 = Card('同盟',13,19,1,0)
spcard0520 = Card('植民',13,20,1,0)
#習性-移動動物園
spcard0601 = Card('チョウの習性',10,1,4,0)
spcard0602 = Card('ラクダの習性',13,2,4,0)
spcard0603 = Card('カメレオンの習性',13,3,4,0)
spcard0604 = Card('カエルの習性',13,4,4,0)
spcard0605 = Card('ヤギの習性',13,5,4,0)
spcard0606 = Card('馬の習性',13,6,4,0)
spcard0607 = Card('モグラの習性',13,7,4,0)
spcard0608 = Card('サルの習性',13,8,4,0)
spcard0609 = Card('ハツカネズミの習性',13,9,4,0)
spcard0610 = Card('ラバの習性',13,10,4,0)
spcard0611 = Card('カワウソの習性',13,11,4,0)
spcard0612 = Card('フクロウの習性',13,12,4,0)
spcard0613 = Card('雄牛の習性',13,13,4,0)
spcard0614 = Card('豚の習性',13,14,4,0)
spcard0615 = Card('ドブネズミの習性',13,15,4,0)
spcard0616 = Card('アザラシの習性',13,16,4,0)
spcard0617 = Card('羊の習性',13,17,4,0)
spcard0618 = Card('リスの習性',13,18,4,0)
spcard0619 = Card('ウミガメの習性',13,19,4,0)
spcard0620 = Card('ミミズの習性',13,20,4,0)
#同盟-同盟
all_spcard_ally = []
spcard0701 = Card('建築家ギルド',14,1,5,0)
spcard0702 = Card('遊牧民団',14,2,5,0)
spcard0703 = Card('穴居民',14,3,5,0)
spcard0704 = Card('魔女の輪',14,4,5,0)
spcard0705 = Card('都市国家',14,5,5,0)
spcard0706 = Card('沿岸の避難港',14,6,5,0)
spcard0707 = Card('工芸家ギルド',14,7,5,0)
spcard0708 = Card('砂漠の案内人',14,8,5,0)
spcard0709 = Card('発明家の家族',14,9,5,0)
spcard0710 = Card('写本士の仲間たち',14,10,5,0)
spcard0711 = Card('森の居住者',14,11,5,0)
spcard0712 = Card('すり師団',14,12,5,0)
spcard0713 = Card('島民',14,13,5,0)
spcard0714 = Card('銀行家連盟',14,14,5,0)
spcard0715 = Card('小売店主連盟',14,15,5,0)
spcard0716 = Card('市場の町',14,16,5,0)
spcard0717 = Card('山の民',14,17,5,0)
spcard0718 = Card('占星術師団',14,18,5,0)
spcard0719 = Card('メイソン団',14,19,5,0)
spcard0720 = Card('平和的教団',14,20,5,0)
spcard0721 = Card('高原の羊飼い',14,21,5,0)
spcard0722 = Card('罠師の小屋',14,22,5,0)
spcard0723 = Card('木工ギルド',14,23,5,0)
#イベント-略奪
spcard0801 = Card('埋葬',15,1,1,0)
spcard0802 = Card('回避',15,2,1,0)
spcard0803 = Card('配達',15,3,1,0)
spcard0804 = Card('危難',15,4,1,0)
spcard0805 = Card('突貫',15,5,1,0)
spcard0806 = Card('襲撃',15,6,1,0)
spcard0807 = Card('発進',15,7,1,0)
spcard0808 = Card('鏡映',15,8,1,0)
spcard0809 = Card('準備',15,9,1,0)
spcard0810 = Card('物色',15,10,1,0)
spcard0811 = Card('旅行',15,11,1,0)
spcard0812 = Card('大渦巻',15,12,1,0)
spcard0813 = Card('略奪行為',15,13,1,0)
spcard0814 = Card('侵略',15,14,1,0)
spcard0815 = Card('繁栄',15,15,1,0)
#特性-略奪
spcard0901 = Card('安価な',15,1,6,0)
spcard0902 = Card('受け継がれた',15,2,6,0)
spcard0903 = Card('内気な',15,3,6,0)
spcard0904 = Card('運命の',15,4,6,0)
spcard0905 = Card('近隣の',15,5,6,0)
spcard0906 = Card('敬虔な',15,6,6,0)
spcard0907 = Card('鼓舞する',15,7,6,0)
spcard0908 = Card('せっかちな',15,8,6,0)
spcard0909 = Card('疲れ知らずの',15,9,6,0)
spcard0910 = Card('忍耐強い',15,10,6,0)
spcard0911 = Card('呪われた',15,11,6,0)
spcard0912 = Card('へつらう',15,12,6,0)
spcard0913 = Card('無謀な',15,13,6,0)
spcard0914 = Card('友好的な',15,14,6,0)
spcard0915 = Card('豊かな',15,15,6,0)
#イベント-旭日
spcard1001 = Card('蓄財',16,1,1,0)
spcard1002 = Card('苦行',16,2,1,0)
spcard1003 = Card('信用',16,3,1,0)
spcard1004 = Card('洞察',16,4,1,0)
spcard1005 = Card('金継ぎ',16,5,1,0)
spcard1006 = Card('稽古',16,6,1,0)
spcard1007 = Card('海上交易',16,7,1,0)
spcard1008 = Card('賛辞',16,8,1,0)
spcard1009 = Card('参集',16,9,1,0)
spcard1010 = Card('継続',16,10,1,0)
#予言-旭日
all_spcard_prop = []
spcard1101 = Card('来寇',16,1,7,0)
spcard1102 = Card('好機到来',16,2,7,0)
spcard1103 = Card('官僚制',16,3,7,0)
spcard1104 = Card('神風',16,4,7,0)
spcard1105 = Card('悟り',16,5,7,0)
spcard1106 = Card('盛大な取引',16,6,7,0)
spcard1107 = Card('豊作',16,7,7,0)
spcard1108 = Card('偉大な指導者',16,8,7,0)
spcard1109 = Card('成長',16,9,7,0)
spcard1110 = Card('厳冬',16,10,7,0)
spcard1111 = Card('神器',16,11,7,0)
spcard1112 = Card('狼狽',16,12,7,0)
spcard1113 = Card('進歩',16,13,7,0)
spcard1114 = Card('急速拡大',16,14,7,0)
spcard1115 = Card('病',16,15,7,0)

def exit_fullscreen(event):
    root.attributes("-fullscreen", False)

#メインウインドウ
root = tk.Tk()
root.title("Dominion Randomizer")
#root.geometry('1200x700+0+0')
root.attributes("-fullscreen", True)
root.bind("<Escape>", exit_fullscreen)

#メニュー画面
title = tk.Label(root, text="Dominion Tool Menu", font=("Helvetica",36))
title.pack(pady=20)
menu1 = tk.Button(root, text='ランダマイザー', command=random_select_set, font=("Helvetica",20))
menu1.pack(pady=10)
#menu2 = tk.Button(root, text='アティネイター', command=ati_start, font=("Helvetica",20))
#menu2.pack(pady=10)
menu3 = tk.Button(root, text='闇市場', command=BlackMarket_start, font=("Helvetica",20))
menu3.pack(pady=10)

#ランダマイザー：拡張セット選択画面
skip = [False]   #二度目の選択となる場合スキップするための変数
subtitle1 = tk.Label(root, text="Dominion Randomizer", font=("Helvetica",18))
frame_selectset = tk.Frame(root, pady=10)
text_selectset = tk.Label(frame_selectset, text="用いる拡張セットを選択してください")
text_selectset.pack()
frame_selectset1 = tk.Frame(frame_selectset, pady=10)
frame_selectset1.pack()
set0_v = tk.BooleanVar(value=False)
cb0 = tk.Checkbutton(frame_selectset1, text='基本', font=("Helvetica",12), variable=set0_v)
set1_v = tk.BooleanVar(value=False)
cb1 = tk.Checkbutton(frame_selectset1, text='陰謀', font=("Helvetica",12), variable=set1_v)
set2_v = tk.BooleanVar(value=False)
cb2 = tk.Checkbutton(frame_selectset1, text='海辺', font=("Helvetica",12), variable=set2_v)
set3_v = tk.BooleanVar(value=False)
cb3 = tk.Checkbutton(frame_selectset1, text='錬金術', font=("Helvetica",12), variable=set3_v)
cb0.pack(side=tk.LEFT,padx=25,anchor=tk.W)
cb1.pack(side=tk.LEFT,padx=25,anchor=tk.W)
cb2.pack(side=tk.LEFT,padx=25,anchor=tk.W)
cb3.pack(side=tk.LEFT,padx=25,anchor=tk.W)
frame_selectset2 = tk.Frame(frame_selectset, pady=10)
frame_selectset2.pack()
set4_v = tk.BooleanVar(value=False)
cb4 = tk.Checkbutton(frame_selectset2, text='繁栄', font=("Helvetica",12), variable=set4_v)
set5_v = tk.BooleanVar(value=False)
cb5 = tk.Checkbutton(frame_selectset2, text='収穫祭', font=("Helvetica",12), variable=set5_v)
set6_v = tk.BooleanVar(value=False)
cb6 = tk.Checkbutton(frame_selectset2, text='異郷', font=("Helvetica",12), variable=set6_v)
set7_v = tk.BooleanVar(value=False)
cb7 = tk.Checkbutton(frame_selectset2, text='暗黒時代', font=("Helvetica",12), variable=set7_v)
cb4.pack(side=tk.LEFT,padx=25,anchor=tk.W)
cb5.pack(side=tk.LEFT,padx=25,anchor=tk.W)
cb6.pack(side=tk.LEFT,padx=25,anchor=tk.W)
cb7.pack(side=tk.LEFT,padx=25,anchor=tk.W)
frame_selectset3 = tk.Frame(frame_selectset, pady=10)
frame_selectset3.pack()
set8_v = tk.BooleanVar(value=False)
cb8 = tk.Checkbutton(frame_selectset3, text='ギルド', font=("Helvetica",12), variable=set8_v)
set9_v = tk.BooleanVar(value=False)
cb9 = tk.Checkbutton(frame_selectset3, text='冒険', font=("Helvetica",12), variable=set9_v)
set10_v = tk.BooleanVar(value=False)
cb10 = tk.Checkbutton(frame_selectset3, text='帝国', font=("Helvetica",12), variable=set10_v)
set11_v = tk.BooleanVar(value=False)
cb11 = tk.Checkbutton(frame_selectset3, text='夜想曲', font=("Helvetica",12), variable=set11_v)
cb8.pack(side=tk.LEFT,padx=25,anchor=tk.W)
cb9.pack(side=tk.LEFT,padx=25,anchor=tk.W)
cb10.pack(side=tk.LEFT,padx=25,anchor=tk.W)
cb11.pack(side=tk.LEFT,padx=25,anchor=tk.W)
frame_selectset4 = tk.Frame(frame_selectset, pady=10)
frame_selectset4.pack()
set12_v = tk.BooleanVar(value=False)
cb12 = tk.Checkbutton(frame_selectset4, text='ルネサンス', font=("Helvetica",12), variable=set12_v)
set13_v = tk.BooleanVar(value=False)
cb13 = tk.Checkbutton(frame_selectset4, text='移動動物園', font=("Helvetica",12), variable=set13_v)
set14_v = tk.BooleanVar(value=False)
cb14 = tk.Checkbutton(frame_selectset4, text='同盟', font=("Helvetica",12), variable=set14_v)
set15_v = tk.BooleanVar(value=False)
cb15 = tk.Checkbutton(frame_selectset4, text='略奪', font=("Helvetica",12), variable=set15_v)
set16_v = tk.BooleanVar(value=False)
cb16 = tk.Checkbutton(frame_selectset4, text='旭日', font=("Helvetica",12), variable=set16_v)
cb12.pack(side=tk.LEFT,padx=25,anchor=tk.W)
cb13.pack(side=tk.LEFT,padx=25,anchor=tk.W)
cb14.pack(side=tk.LEFT,padx=25,anchor=tk.W)
cb15.pack(side=tk.LEFT,padx=25,anchor=tk.W)
cb16.pack(side=tk.LEFT,padx=25,anchor=tk.W)
frame_selectspset1 = tk.Frame(frame_selectset, pady=10)
frame_selectspset1.pack()
sp1_v = tk.BooleanVar(value=False)
sp1 = tk.Checkbutton(frame_selectspset1, text='イベント-冒険', font=("Helvetica",12), variable=sp1_v)
sp2_v = tk.BooleanVar(value=False)
sp2 = tk.Checkbutton(frame_selectspset1, text='イベント-帝国', font=("Helvetica",12), variable=sp2_v)
sp3_v = tk.BooleanVar(value=False)
sp3 = tk.Checkbutton(frame_selectspset1, text='ランドマーク', font=("Helvetica",12), variable=sp3_v)
sp4_v = tk.BooleanVar(value=False)
sp4 = tk.Checkbutton(frame_selectspset1, text='プロジェクト', font=("Helvetica",12), variable=sp4_v)
sp1.pack(side=tk.LEFT,padx=15,anchor=tk.W)
sp2.pack(side=tk.LEFT,padx=15,anchor=tk.W)
sp3.pack(side=tk.LEFT,padx=15,anchor=tk.W)
sp4.pack(side=tk.LEFT,padx=15,anchor=tk.W)
frame_selectspset2 = tk.Frame(frame_selectset, pady=10)
frame_selectspset2.pack()
sp5_v = tk.BooleanVar(value=False)
sp5 = tk.Checkbutton(frame_selectspset2, text='イベント-移動動物園', font=("Helvetica",12), variable=sp5_v)
sp6_v = tk.BooleanVar(value=False)
sp6 = tk.Checkbutton(frame_selectspset2, text='習性', font=("Helvetica",12), variable=sp6_v)
#sp7_v = tk.BooleanVar(value=False)
#sp7 = tk.Checkbutton(frame_selectspset2, text='同盟', font=("Helvetica",12), variable=sp7_v)
sp8_v = tk.BooleanVar(value=False)
sp8 = tk.Checkbutton(frame_selectspset2, text='イベント-略奪', font=("Helvetica",12), variable=sp8_v)
sp9_v = tk.BooleanVar(value=False)
sp9 = tk.Checkbutton(frame_selectspset2, text='特性', font=("Helvetica",12), variable=sp9_v)
sp10_v = tk.BooleanVar(value=False)
sp10 = tk.Checkbutton(frame_selectspset2, text='イベント-旭日', font=("Helvetica",12), variable=sp10_v)
sp5.pack(side=tk.LEFT,padx=25,anchor=tk.W)
sp6.pack(side=tk.LEFT,padx=25,anchor=tk.W)
sp8.pack(side=tk.LEFT,padx=25,anchor=tk.W)
sp9.pack(side=tk.LEFT,padx=25,anchor=tk.W)
sp10.pack(side=tk.LEFT,padx=25,anchor=tk.W)
selectcheck = tk.Button(frame_selectset, text='選択完了', font=(18), command=random_selected)
selectcheck.pack(side=tk.LEFT,padx=100)
allcheck = tk.Button(frame_selectset, text='所持セット全使用', font=(18), command=random_all_set)
allcheck.pack(side=tk.LEFT,padx=100)
backmenu1a = tk.Button(root, text='タイトルに戻る',command=backmenu_1a, font=("Helvetica",20))


#ランダマイザー：実行画面1
frame_randomizer1 = tk.Frame(root)
frame_geneCard1 = tk.Frame(frame_randomizer1, pady=20)
frame_geneCard1.pack()
frame_geneCard_1 = tk.Frame(frame_geneCard1, padx=10)
frame_geneCard_2 = tk.Frame(frame_geneCard1, padx=10)
frame_geneCard_3 = tk.Frame(frame_geneCard1, padx=10)
frame_geneCard_4 = tk.Frame(frame_geneCard1, padx=10)
frame_geneCard_1.pack(side=tk.LEFT,anchor=tk.W)
frame_geneCard_2.pack(side=tk.LEFT,anchor=tk.W)
frame_geneCard_3.pack(side=tk.LEFT,anchor=tk.W)
frame_geneCard_4.pack(side=tk.LEFT,anchor=tk.W)
card1 = tk.Label(frame_geneCard_1, text=" - ", font=("Helvetica",24), bg='white')
card1d = tk.Label(frame_geneCard_1, text=" ", font=("Helvetica",12), bg='white')
card2 = tk.Label(frame_geneCard_2, text=" - ", font=("Helvetica",24), bg='white')
card2d = tk.Label(frame_geneCard_2, text=" ", font=("Helvetica",12), bg='white')
card3 = tk.Label(frame_geneCard_3, text=" - ", font=("Helvetica",24), bg='white')
card3d = tk.Label(frame_geneCard_3, text=" ", font=("Helvetica",12), bg='white')
card4 = tk.Label(frame_geneCard_4, text=" - ", font=("Helvetica",24), bg='white')
card4d = tk.Label(frame_geneCard_4, text=" ", font=("Helvetica",12), bg='white')
card1.pack(side=tk.LEFT,anchor=tk.W)
card1d.pack(side=tk.LEFT,anchor=tk.W)
card2.pack(side=tk.LEFT,anchor=tk.W)
card2d.pack(side=tk.LEFT,anchor=tk.W)
card3.pack(side=tk.LEFT,anchor=tk.W)
card3d.pack(side=tk.LEFT,anchor=tk.W)
card4.pack(side=tk.LEFT,anchor=tk.W)
card4d.pack(side=tk.LEFT,anchor=tk.W)
frame_geneCard2 = tk.Frame(frame_randomizer1, pady=20)
frame_geneCard2.pack()
frame_geneCard_5 = tk.Frame(frame_geneCard2, padx=10)
frame_geneCard_6 = tk.Frame(frame_geneCard2, padx=10)
frame_geneCard_7 = tk.Frame(frame_geneCard2, padx=10)
frame_geneCard_8 = tk.Frame(frame_geneCard2, padx=10)
frame_geneCard_5.pack(side=tk.LEFT,anchor=tk.W)
frame_geneCard_6.pack(side=tk.LEFT,anchor=tk.W)
frame_geneCard_7.pack(side=tk.LEFT,anchor=tk.W)
frame_geneCard_8.pack(side=tk.LEFT,anchor=tk.W)
card5 = tk.Label(frame_geneCard_5, text=" - ", font=("Helvetica",24), bg='white')
card5d = tk.Label(frame_geneCard_5, text=" ", font=("Helvetica",12), bg='white')
card6 = tk.Label(frame_geneCard_6, text=" - ", font=("Helvetica",24), bg='white')
card6d = tk.Label(frame_geneCard_6, text=" ", font=("Helvetica",12), bg='white')
card7 = tk.Label(frame_geneCard_7, text=" - ", font=("Helvetica",24), bg='white')
card7d = tk.Label(frame_geneCard_7, text=" ", font=("Helvetica",12), bg='white')
card8 = tk.Label(frame_geneCard_8, text=" - ", font=("Helvetica",24), bg='white')
card8d = tk.Label(frame_geneCard_8, text=" ", font=("Helvetica",12), bg='white')
card5.pack(side=tk.LEFT,anchor=tk.W)
card5d.pack(side=tk.LEFT,anchor=tk.W)
card6.pack(side=tk.LEFT,anchor=tk.W)
card6d.pack(side=tk.LEFT,anchor=tk.W)
card7.pack(side=tk.LEFT,anchor=tk.W)
card7d.pack(side=tk.LEFT,anchor=tk.W)
card8.pack(side=tk.LEFT,anchor=tk.W)
card8d.pack(side=tk.LEFT,anchor=tk.W)
frame_geneCard3 = tk.Frame(frame_randomizer1, pady=20)
frame_geneCard3.pack()
frame_geneCard_9 = tk.Frame(frame_geneCard3, padx=10)
frame_geneCard_10 = tk.Frame(frame_geneCard3, padx=10)
frame_geneCard_11 = tk.Frame(frame_geneCard3, padx=10)
frame_geneCard_12 = tk.Frame(frame_geneCard3, padx=10)
frame_geneCard_9.pack(side=tk.LEFT,anchor=tk.W)
frame_geneCard_10.pack(side=tk.LEFT,anchor=tk.W)
frame_geneCard_11.pack(side=tk.LEFT,anchor=tk.W)
frame_geneCard_12.pack(side=tk.LEFT,anchor=tk.W)
card9 = tk.Label(frame_geneCard_9, text=" - ", font=("Helvetica",24), bg='white')
card9d = tk.Label(frame_geneCard_9, text=" ", font=("Helvetica",12), bg='white')
card10 = tk.Label(frame_geneCard_10, text=" - ", font=("Helvetica",24), bg='white')
card10d = tk.Label(frame_geneCard_10, text=" ", font=("Helvetica",12), bg='white')
card11 = tk.Label(frame_geneCard_11, text=" ", font=("Helvetica",24), bg='white')
card11d = tk.Label(frame_geneCard_11, text=" ", font=("Helvetica",12), bg='white')
card12 = tk.Label(frame_geneCard_12, text=" ", font=("Helvetica",24), bg='white')
card12d = tk.Label(frame_geneCard_12, text=" ", font=("Helvetica",12), bg='white')
card9.pack(side=tk.LEFT,anchor=tk.W)
card9d.pack(side=tk.LEFT,anchor=tk.W)
card10.pack(side=tk.LEFT,anchor=tk.W)
card10d.pack(side=tk.LEFT,anchor=tk.W)
card11.pack(side=tk.LEFT,anchor=tk.W)
card11d.pack(side=tk.LEFT,anchor=tk.W)
card12.pack(side=tk.LEFT,anchor=tk.W)
card12d.pack(side=tk.LEFT,anchor=tk.W)
geneCard = [card1,card1d,card2,card2d,card3,card3d,card4,card4d,card5,card5d,card6,card6d,card7,card7d,card8,card8d,card9,card9d,card10,card10d,card11,card11d,card12,card12d]
frame_randomB = tk.Frame(frame_randomizer1, pady=10)
frame_randomB.pack()
make_one = tk.Button(frame_randomB, text='生成：1',command=random_card_gene_1)
make_one.pack(side=tk.LEFT,padx=25,anchor=tk.W)
make_ten = tk.Button(frame_randomB, text='生成：10',command=random_card_gene_10)
make_ten.pack(side=tk.LEFT,padx=25,anchor=tk.W)
frame_delete = tk.Frame(frame_randomB, pady=10)
delete_one = tk.Button(frame_delete, text='削除：',command=delete_card)
delete_one.pack(side=tk.LEFT,anchor=tk.W)
delete_one_area = tk.Entry(frame_delete, width = 5)
delete_one_area.pack(side=tk.LEFT,anchor=tk.W)
frame_delete.pack(side=tk.LEFT,padx=25,anchor=tk.W)
reset = tk.Button(frame_randomB, text='保存せずリセット',command=reset_unsave)
reset.pack(side=tk.LEFT,padx=25,anchor=tk.W)
nextset = tk.Button(frame_randomB, text='保存してリセット',command=reset_save)
nextset.pack(side=tk.LEFT,padx=25,anchor=tk.W)
savereset = tk.Button(frame_randomB, text='記憶リセット',command=save_reset)
savereset.pack(side=tk.LEFT,padx=25,anchor=tk.W)
random_card = []
random_num = []
#ランダマイザー：実行画面2
frame_randomizer2 = tk.Frame(root)
frame_geneSP12 = tk.Frame(frame_randomizer2, padx=20)
frame_geneSP12.pack()
frame_geneSP1 = tk.Frame(frame_geneSP12, pady=5)
frame_geneSP1.pack(side=tk.LEFT,anchor=tk.W)
spcard1 = tk.Label(frame_geneSP1, text=" - ", font=("Helvetica",24), bg='white')
spcard1d = tk.Label(frame_geneSP1, text=" ", font=("Helvetica",12), bg='white')
spcard1.pack(side=tk.LEFT,anchor=tk.W)
spcard1d.pack(side=tk.LEFT,anchor=tk.W)
frame_geneSP2 = tk.Frame(frame_geneSP12, pady=5)
frame_geneSP2.pack(side=tk.LEFT,anchor=tk.W)
spcard2 = tk.Label(frame_geneSP2, text=" - ", font=("Helvetica",24), bg='white')
spcard2d = tk.Label(frame_geneSP2, text=" ", font=("Helvetica",12), bg='white')
spcard2.pack(side=tk.LEFT,anchor=tk.W)
spcard2d.pack(side=tk.LEFT,anchor=tk.W)
frame_geneSP34 = tk.Frame(frame_randomizer2, padx=20)
frame_geneSP34.pack()
frame_geneSP3 = tk.Frame(frame_geneSP34, pady=5)
frame_geneSP3.pack(side=tk.LEFT,anchor=tk.W)
spcard3 = tk.Label(frame_geneSP3, text=" ", font=("Helvetica",24), bg='white')
spcard3d = tk.Label(frame_geneSP3, text=" ", font=("Helvetica",12), bg='white')
spcard3.pack(side=tk.LEFT,anchor=tk.W)
spcard3d.pack(side=tk.LEFT,anchor=tk.W)
frame_geneSP4 = tk.Frame(frame_geneSP34, pady=5)
frame_geneSP4.pack(side=tk.LEFT,anchor=tk.W)
spcard4 = tk.Label(frame_geneSP4, text=" ", font=("Helvetica",24), bg='white')
spcard4d = tk.Label(frame_geneSP4, text=" ", font=("Helvetica",12), bg='white')
spcard4.pack(side=tk.LEFT,anchor=tk.W)
spcard4d.pack(side=tk.LEFT,anchor=tk.W)
geneSPCard = [spcard1,spcard1d,spcard2,spcard2d,spcard3,spcard3d,spcard4,spcard4d]
frame_sprandomB = tk.Frame(frame_randomizer2, pady=10)
frame_sprandomB.pack()
make_spone = tk.Button(frame_sprandomB, text='生成：1',command=random_spcard_gene_1)
spreset = tk.Button(frame_sprandomB, text='保存せずリセット',command=spreset_unsave)
spnextset = tk.Button(frame_sprandomB, text='保存してリセット',command=spreset_save)
spsavereset = tk.Button(frame_sprandomB, text='記憶リセット',command=spsave_reset)
make_spone.pack(side=tk.LEFT,padx=25,anchor=tk.W)
spreset.pack(side=tk.LEFT,padx=25,anchor=tk.W)
spnextset.pack(side=tk.LEFT,padx=25,anchor=tk.W)
spsavereset.pack(side=tk.LEFT,padx=25,anchor=tk.W)
random_spcard = []
random_spnum = []
backmenu1b = tk.Button(root, text='タイトルに戻る',command=backmenu_1b, font=("Helvetica",20))
backmenu1c = tk.Button(root, text='拡張セット選択画面に戻る',command=backmenu_1c, font=("Helvetica",20))


#闇市場
frame_blackMarket = tk.Frame(root)
subtitle3 = tk.Label(root, text="Dominion BlackMarket", font=("Helvetica",18))
frame_delete_blackMarket = tk.Frame(frame_blackMarket, pady=10)
make_blackMarket = tk.Button(frame_blackMarket, text='生成',command=BlackMarket_random_card)
delete_one_blackMarket = tk.Button(frame_delete_blackMarket, text='変更：',command=BlackMarket_delete_card)
delete_one_blackMarket_area = tk.Entry(frame_delete_blackMarket, width = 5)
make_blackMarket.pack(side=tk.LEFT, padx=25, anchor=tk.W)
delete_one_blackMarket.pack(side=tk.LEFT, anchor=tk.W)
delete_one_blackMarket_area.pack(side=tk.LEFT, anchor=tk.W)
frame_delete_blackMarket.pack(side=tk.LEFT, padx=25, anchor=tk.W)
frame_geneCard_blackMarket = tk.Frame(root, pady=20)
frame_geneCard_blackMarket_1 = tk.Frame(frame_geneCard_blackMarket, padx=10)
frame_geneCard_blackMarket_2 = tk.Frame(frame_geneCard_blackMarket, padx=10)
frame_geneCard_blackMarket_3 = tk.Frame(frame_geneCard_blackMarket, padx=10)
frame_geneCard_blackMarket_1.pack(side=tk.LEFT, anchor=tk.W)
frame_geneCard_blackMarket_2.pack(side=tk.LEFT, anchor=tk.W)
frame_geneCard_blackMarket_3.pack(side=tk.LEFT, anchor=tk.W)
card1_blackMarket = tk.Label(frame_geneCard_blackMarket_1, text=" - ", font=("Helvetica",30))
card1d_blackMarket = tk.Label(frame_geneCard_blackMarket_1, text=" ", font=("Helvetica",15))
card2_blackMarket = tk.Label(frame_geneCard_blackMarket_2, text=" - ", font=("Helvetica",30))
card2d_blackMarket = tk.Label(frame_geneCard_blackMarket_2, text=" ", font=("Helvetica",15))
card3_blackMarket = tk.Label(frame_geneCard_blackMarket_3, text=" - ", font=("Helvetica",30))
card3d_blackMarket = tk.Label(frame_geneCard_blackMarket_3, text=" ", font=("Helvetica",15))
card1_blackMarket.pack(side=tk.LEFT,anchor=tk.W)
card1d_blackMarket.pack(side=tk.LEFT,anchor=tk.W)
card2_blackMarket.pack(side=tk.LEFT,anchor=tk.W)
card2d_blackMarket.pack(side=tk.LEFT,anchor=tk.W)
card3_blackMarket.pack(side=tk.LEFT,anchor=tk.W)
card3d_blackMarket.pack(side=tk.LEFT,anchor=tk.W)
geneCard_blackMarket = [card1_blackMarket,card1d_blackMarket,card2_blackMarket,card2d_blackMarket,card3_blackMarket,card3d_blackMarket]
blackMarketCards = []
btn_blackMarket_fin = tk.Button(root, text='TOPメニューに戻る',font=("Helvetica",20),command=BlackMarket_fin)

#ウインドウの表示
root.mainloop()
