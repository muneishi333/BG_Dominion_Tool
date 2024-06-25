import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as mb
import random as rand


#カード情報テンプレ
class Card:
    def __init__(self,name,set,number,type1,type2,cost,pa,pb,pca,pcs,pv,pcoin,pmrbt,koi,get,lost,selflost,type,color,language,spe1,spe2,spe3):
        self.name = name        #カード名
        self.set = set          #収録されている拡張セットの番号
        self.number = number    #収録されている拡張セット内でのカードの番号
        #ランダマイザー用
        self.type1 = type1      #カードタイプ（主）
        self.type2 = type2      #カードタイプ（副）
        #アキネイター用
        self.cost = cost            #コスト（負債：-n、<大金>：16）
        self.pa = pa                #＋アクション
        self.pb = pb                #＋購入
        self.pca = pca              #＋カードを引く（最大枚数、上限がない場合：10）
        self.pcs = pcs              #＋コスト
        self.pv = pv                #＋勝利点
        self.pcoin = pcoin          #＋財源
        self.pmrbt = pmrbt          #＋村人
        self.koi = koi              #＋好意
        self.get = get              #獲得
        self.lost = lost            #そのカード以外を廃棄（任意の枚数廃棄：10）
        self.selflost = selflost    #そのカード自身を廃棄
        self.type = type            #カードタイプ[]
        #（  1:アクション/ 2:財宝　/ 3:勝利点/ 4:呪い　/ 5:リアクション/ 6:アタック　/ 7:持続　/ 8:恩賞　/ 9:褒賞　/10:廃墟
        #　/11:避難所　　/12:略奪者/13:騎士　/14:命令　/15:リザーブ　　/16:トラベラー/17:集合　/18:城　　/19:幸運　/20:不運
        #　/21:夜行　　　/22:家宝　/23:精霊　/24:ゾンビ/25:連携　　　　/26:城砦　　　/27:衝突　/28:叙事詩/29:町民　/30:卜占官
        #　/31:魔法使い　/32:戦利品）
        self.color = color          #カード背景色（0:ノーマル/1:色つき/2:2色）
        self.language = language    #カード名[ひらがな,カタカナ,漢字]
        self.spe1 = spe1            #特徴的な効果[]（無ければ[0]）
        #（  1:捨て札；手札 / 2:捨て札；山札 / 3:山札操作 / 4:防御 / 5:デメリット有無 / 6:別カード使用 / 7:選択効果 / 8:手札を山札に戻す
        #　  9:コスト減 / 10:使い切り / 11:フルスペックに条件 / 12:分割山札 / 13:他カード準備 / 14:追加ターン / 15:戦利品 / 16:保存
        #　  17:手札に獲得 / 18:交換 / 19:マット / 20:他人の手札に干渉 / 21:山札に獲得 / 22:指定ドロー / 23:山札を捨て札
        #　  24:使用後山に戻る / 25:トークン / 26:時を戻す / 27:負債 / 28:呪い / 29:祝福 / 30:呪詛 / 31:玉座系 / 32:追放 / 33:馬
        #　  34:アーティファクト / 35:使用後山札に戻る / 36:山札を循環 / 37:ポーション
        self.spe2 = spe2            #説明文が横線で区切られている特徴的な効果[]（無ければ[0]）
        #（  1:獲得時効果 / 2:購入時効果 / 3:廃棄時効果 / 4:過払い / 5:リアクション効果 / 6:持続効果 / 7:リザーブ効果 / 8:ゲームに影響
        #　  9:勝利点点数 / 10:トラベラー効果 / 11:コスト変動 / 12:
        self.spe3 = spe3            #アタックに関する特徴的な効果[]（無ければ[0]）
        #（  1:ハンデス / 2,3,4:ハンデス；2,3,4枚まで / 5,6:ハンデス；1,2枚 / 7:ハンデス；指定カード / 8:ハンデス；上限有無
        #　/ 9:ハンデス；山札戻し / 10:ハンデス；手札リセット / 11:呪い / 12:呪い（強制） / 13:廃墟 / 14:指定カード獲得 / 15:強制廃棄
        #　/ 16:山札から捨て札 / 17:妨害トークン / 18:カード書き換え / 19:呪詛 / 20:追放）


#ランダマイザー拡張選択画面
def random_select_set():
    title.pack_forget()
    menu1.pack_forget()
    menu2.pack_forget()
    subtitle1.pack()
    if skip[0] == False:
        random_text1.pack()
        frame_set03.pack()
        frame_set47.pack()
        frame_set811.pack()
        frame_set1215.pack()
        frame_spset03.pack()
        frame_spset47.pack()
        selectcheck.pack(side=tk.LEFT,padx=100)
        allcheck.pack(side=tk.LEFT,padx=100)
        backmenu1a.pack(side=tk.LEFT,padx=100)
    else:
        random_play()

def backmenu_1a():
    subtitle1.pack_forget()
    random_text1.pack_forget()
    frame_set03.pack_forget()
    frame_set47.pack_forget()
    frame_set811.pack_forget()
    frame_set1215.pack_forget()
    frame_spset03.pack_forget()
    frame_spset47.pack_forget()
    selectcheck.pack_forget()
    allcheck.pack_forget()
    backmenu1a.pack_forget()
    title.pack(pady=20)
    menu1.pack(pady=10)
    menu2.pack(pady=10)

#ランダマイザー各拡張選択
def random_selected():
    totalC = 0
    totalSC = 0
    if set0_v.get():
        useset.append(26)
        totalC += 26
        for i in range(26):
            usecard.append(0)
    else:
        useset.append(-26)
        for i in range(26):
            usecard.append(-1)
    if set1_v.get():
        useset.append(26)
        totalC += 26
        for i in range(26):
            usecard.append(0)
    else:
        useset.append(-26)
        for i in range(26):
            usecard.append(-1)
    if set2_v.get():
        totalC += 27
        useset.append(27)
        for i in range(27):
            usecard.append(0)
    else:
        useset.append(-27)
        for i in range(27):
            usecard.append(-1)
    if set3_v.get():
        totalC += 12
        useset.append(12)
        for i in range(12):
            usecard.append(0)
    else:
        useset.append(-22)
        for i in range(12):
            usecard.append(-1)
    if set4_v.get():
        totalC += 25
        useset.append(25)
        for i in range(25):
            usecard.append(0)
    else:
        useset.append(-25)
        for i in range(25):
            usecard.append(-1)
    if set5_v.get():
        totalC += 13
        useset.append(13)
        for i in range(13):
            usecard.append(0)
    else:
        useset.append(-13)
        for i in range(13):
            usecard.append(-1)
    if set6_v.get():
        totalC += 26
        useset.append(26)
        for i in range(26):
            usecard.append(0)
    else:
        useset.append(-26)
        for i in range(26):
            usecard.append(-1)
    if set7_v.get():
        totalC += 35
        useset.append(35)
        for i in range(35):
            usecard.append(0)
    else:
        useset.append(-35)
        for i in range(35):
            usecard.append(-1)
    if set8_v.get():
        totalC += 13
        useset.append(13)
        for i in range(13):
            usecard.append(0)
    else:
        useset.append(-13)
        for i in range(13):
            usecard.append(-1)
    if set9_v.get():
        totalC += 30
        useset.append(30)
        for i in range(30):
            usecard.append(0)
    else:
        useset.append(-30)
        for i in range(30):
            usecard.append(-1)
    if set10_v.get():
        totalC += 24
        useset.append(24)
        for i in range(24):
            usecard.append(0)
    else:
        useset.append(-24)
        for i in range(24):
            usecard.append(-1)
    if set11_v.get():
        totalC += 33
        useset.append(33)
        for i in range(33):
            usecard.append(0)
    else:
        useset.append(-33)
        for i in range(33):
            usecard.append(-1)
    if set12_v.get():
        totalC += 25
        useset.append(25)
        for i in range(25):
            usecard.append(0)
    else:
        useset.append(-25)
        for i in range(25):
            usecard.append(-1)
    if set13_v.get():
        totalC += 30
        useset.append(30)
        for i in range(30):
            usecard.append(0)
    else:
        useset.append(-30)
        for i in range(30):
            usecard.append(-1)
    if set14_v.get():
        totalC += 31
        useset.append(31)
        for i in range(31):
            usecard.append(0)
    else:
        useset.append(-31)
        for i in range(31):
            usecard.append(-1)
    if set15_v.get():
        totalC += 40
        useset.append(40)
        for i in range(40):
            usecard.append(0)
    else:
        useset.append(-40)
        for i in range(40):
            usecard.append(-1)
    if sp0_v.get():
        totalSC += 20
        usespset.append(20)
        for i in range(20):
            usespcard.append(0)
    else:
        usespset.append(-20)
        for i in range(20):
            usespcard.append(-1)
    if sp1_v.get():
        totalSC += 13
        usespset.append(13)
        for i in range(13):
            usespcard.append(0)
    else:
        usespset.append(-13)
        for i in range(13):
            usespcard.append(-1)
    if sp2_v.get():
        totalSC += 21
        usespset.append(21)
        for i in range(21):
            usespcard.append(0)
    else:
        usespset.append(-21)
        for i in range(21):
            usespcard.append(-1)
    if sp3_v.get():
        totalSC += 20
        usespset.append(20)
        for i in range(20):
            usespcard.append(0)
    else:
        usespset.append(-20)
        for i in range(20):
            usespcard.append(-1)
    if sp4_v.get():
        totalSC += 20
        usespset.append(20)
        for i in range(20):
            usespcard.append(0)
    else:
        usespset.append(-20)
        for i in range(20):
            usespcard.append(-1)
    if sp5_v.get():
        totalSC += 20
        usespset.append(20)
        for i in range(20):
            usespcard.append(0)
    else:
        usespset.append(-20)
        for i in range(20):
            usespcard.append(-1)
    if sp6_v.get():
        totalSC += 23
        usespset.append(23)
        for i in range(23):
            usespcard.append(0)
    else:
        usespset.append(-23)
        for i in range(23):
            usespcard.append(-1)
    if sp7_v.get():
        totalSC += 15
        usespset.append(15)
        for i in range(15):
            usespcard.append(0)
    else:
        usespset.append(-15)
        for i in range(15):
            usespcard.append(-1)
    if sp8_v.get():
        totalSC += 15
        usespset.append(15)
        for i in range(15):
            usespcard.append(0)
    else:
        usespset.append(-15)
        for i in range(15):
            usespcard.append(-1)
    totalcard.append(totalC)
    totalcard.append(totalSC)
    random_play()

#ランダマイザー全拡張選択
def random_all_set():
    totalC = 0
    totalSC = 0
    useset.append(26)   #基本
    totalC += 26
    for i in range(26):
        usecard.append(0)
    useset.append(26)   #陰謀
    totalC += 26
    for i in range(26):
        usecard.append(0)
    useset.append(27)   #海辺
    totalC += 27
    for i in range(27):
        usecard.append(0)
    useset.append(12)   #錬金術
    totalC += 12
    for i in range(12):
        usecard.append(0)
    useset.append(25)   #繁栄
    totalC += 25
    for i in range(25):
        usecard.append(0)
    useset.append(13)   #収穫祭
    totalC += 13
    for i in range(13):
        usecard.append(0)
    useset.append(-26)  #異郷
    #totalC += 26
    for i in range(26):
        usecard.append(-1)
    useset.append(-35)  #暗黒時代
    #totalC += 35
    for i in range(35):
        usecard.append(-1)
    useset.append(13)   #ギルド
    totalC += 13
    for i in range(13):
        usecard.append(0)
    useset.append(30)   #冒険
    usespset.append(20)
    totalC += 30
    totalSC += 20
    for i in range(30):
        usecard.append(0)
    for i in range(20): #イベント（冒険）
        usespcard.append(0)
    useset.append(24)   #帝国
    usespset.append(13)
    usespset.append(21)
    totalC += 24
    totalSC += 34
    for i in range(24):
        usecard.append(0)
    for i in range(13): #イベント（帝国）
        usespcard.append(0)
    for i in range(21): #ランドマーク
        usespcard.append(0)
    useset.append(33)   #夜想曲
    totalC += 33
    for i in range(33):
        usecard.append(0)
    useset.append(25)  #ルネサンス
    usespset.append(20)
    totalC += 25
    totalSC += 20
    for i in range(25):
        usecard.append(0)
    for i in range(20): #プロジェクト
        usespcard.append(0)
    useset.append(-30)  #移動動物園
    usespset.append(-20)
    usespset.append(-20)
    #totalC += 30
    #totalSC += 40
    for i in range(30):
        usecard.append(-1)
    for i in range(20): #イベント（移動動物園）
        usespcard.append(-1)
    for i in range(20): #習性
        usespcard.append(-1)
    useset.append(-31)   #同盟
    usespset.append(-23)
    totalC += 31
    #totalSC += 23
    usespset.append(-23)
    for i in range(31):
        usecard.append(-1)
    for i in range(23): #同盟
        usespcard.append(-1)
    useset.append(40)   #略奪
    usespset.append(15)
    usespset.append(15)
    totalC += 40
    totalSC += 30
    for i in range(40):
        usecard.append(0)
    for i in range(15): #イベント（略奪）
        usespcard.append(0)
    for i in range(15): #特性
        usespcard.append(0)
    totalcard.append(totalC)
    totalcard.append(totalSC)
    random_play()

#タイトルに戻る
def backmenu_1b():
    subtitle1.pack_forget()
    frame_geneCard14.pack_forget()
    frame_geneCard58.pack_forget()
    frame_geneCard912.pack_forget()
    frame_randomB.pack_forget()
    frame_geneSP1.pack_forget()
    frame_geneSP2.pack_forget()
    frame_geneSP3.pack_forget()
    frame_geneSP4.pack_forget()
    frame_sprandomB.pack_forget()
    backmenu1b.pack_forget()
    title.pack(pady=20)
    menu1.pack(pady=10)
    menu2.pack(pady=10)

#ランダマイザー：実行画面
def random_play():
    skip[0] = True
    random_text1.pack_forget()
    frame_set03.pack_forget()
    frame_set47.pack_forget()
    frame_set811.pack_forget()
    frame_set1215.pack_forget()
    frame_spset03.pack_forget()
    frame_spset47.pack_forget()
    selectcheck.pack_forget()
    allcheck.pack_forget()
    backmenu1a.pack_forget()
    frame_geneCard14.pack()
    frame_geneCard58.pack()
    frame_geneCard912.pack()
    frame_randomB.pack()
    frame_geneSP1.pack()
    frame_geneSP2.pack()
    frame_geneSP3.pack()
    frame_geneSP4.pack()
    frame_sprandomB.pack()
    backmenu1b.pack()

#カードを生成しきったときの警告
def showAlert_cardgene():
    mb.showinfo('Information', 'リセットをしてください')

#カードが設定されていないときの警告
def showAlert_cardset():
    mb.showinfo('Information', 'カードが設定されていません')

#重複を考慮した乱数を生成する（memo:生成した乱数を記憶しておく配列(配列) MAX:乱数の最大値(数値) C-1:重複許可回数）
def random_number_gene(memo,MAX,C):
    jud = True
    if len(memo) < (MAX*C):
        num = rand.randint(0,MAX-1)
        while jud:
            jud = False
            cnt = 0     #生成した数値が既に何回出力されているかをカウント
            for i in range(len(memo)):
                if memo[i] == num:
                    cnt += 1
                    if C == 1:
                        break
            if cnt == C:
                jud = True
                #乱数生成にかかる計算コスト短縮（確率的にはbad）
                num = (num + 1) % MAX
    else:
        showAlert_cardgene()
    return num

#王国カードをランダムで１枚生成
def random_card_gene_1():
    if totalcard[0] > 0:
        #既に生成されている枚数が11以下であれば生成開始
        if len(random_num) < 12:
            chouhuku = 1    ###この数値は重複を許す回数（1:重複無し、N:各カード(N-1)度のみ重複を許す）
            jud = False
            while jud == False:
                bord = 0
                numb = random_number_gene(random_num_org,totalcard[0],chouhuku)
                numb_org = numb
                for i in range(len(useset)):
                    if useset[i] > 0:
                        bord += useset[i]
                        if bord > numb:
                            break
                    else:
                        bord -= useset[i]
                        numb -= useset[i]
                jud = True
                for i in range(len(random_num)):
                    if random_num[i] == numb:
                        jud = False
                        break
            random_num.append(numb)
            random_num_org.append(numb_org)
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
        chouhuku = 1    ###この数値は重複を許す回数（1:重複無し、N:各カード(N-1)度のみ重複を許す）
        jud = False
        while jud == False:
            bord = 0
            numb = random_number_gene(random_num_org,totalcard[0],chouhuku)
            numb_org = numb
            for i in range(len(useset)):
                if useset[i] > 0:
                    bord += useset[i]
                    if bord > numb:
                        break
                else:
                    bord -= useset[i]
                    numb -= useset[i]
                jud = True
            for i in range(len(random_num)):
                if random_num[i] == numb:
                    jud = False
                    break
        random_num[num-1] = numb
        random_num_org[len(random_num)-num] = numb_org
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
            geneCard[(num*2)-1]["text"] = '基本-' + str(all_card[numb].number) + '　'
            geneCard[(num*2)-1]["background"] = "#e0ffff"
        elif all_card[numb].set == 1:
            geneCard[(num*2)-1]["text"] = '陰謀-' + str(all_card[numb].number) + '　'
            geneCard[(num*2)-1]["background"] = "#ffffe0"
        elif all_card[numb].set == 2:
            geneCard[(num*2)-1]["text"] = '海辺-' + str(all_card[numb].number) + '　'
            geneCard[(num*2)-1]["background"] = "#e0ffff"
        elif all_card[numb].set == 3:
            geneCard[(num*2)-1]["text"] = '錬金術-' + str(all_card[numb].number) + '　'
            geneCard[(num*2)-1]["background"] = "#ffe0ff"
        elif all_card[numb].set == 4:
            geneCard[(num*2)-1]["text"] = '繁栄-' + str(all_card[numb].number) + '　'
            geneCard[(num*2)-1]["background"] = "#e0ffff"
        elif all_card[numb].set == 5:
            geneCard[(num*2)-1]["text"] = '収穫祭-' + str(all_card[numb].number) + '　'
            geneCard[(num*2)-1]["background"] = "#ffe0ff"
        elif all_card[numb].set == 6:
            geneCard[(num*2)-1]["text"] = '異郷-' + str(all_card[numb].number) + '　'
            geneCard[(num*2)-1]["background"] = "#e0ffe0"
        elif all_card[numb].set == 7:
            geneCard[(num*2)-1]["text"] = '暗黒時代-' + str(all_card[numb].number) + '　'
            geneCard[(num*2)-1]["background"] = "#e0ffe0"
        elif all_card[numb].set == 8:
            geneCard[(num*2)-1]["text"] = 'ギルド-' + str(all_card[numb].number) + '　'
            geneCard[(num*2)-1]["background"] = "#ffffe0"
        elif all_card[numb].set == 9:
            geneCard[(num*2)-1]["text"] = '冒険-' + str(all_card[numb].number) + '　'
            geneCard[(num*2)-1]["background"] = "#ffe0ff"
        elif all_card[numb].set == 10:
            geneCard[(num*2)-1]["text"] = '帝国-' + str(all_card[numb].number) + '　'
            geneCard[(num*2)-1]["background"] = "#e0ffff"
        elif all_card[numb].set == 11:
            geneCard[(num*2)-1]["text"] = '夜想曲-' + str(all_card[numb].number) + '　'
            geneCard[(num*2)-1]["background"] = "#ffffe0"
        elif all_card[numb].set == 12:
            geneCard[(num*2)-1]["text"] = 'ルネサンス-' + str(all_card[numb].number) + '　'
            geneCard[(num*2)-1]["background"] = "#ffe0ff"
        elif all_card[numb].set == 13:
            geneCard[(num*2)-1]["text"] = '移動動物園-' + str(all_card[numb].number) + '　'
            geneCard[(num*2)-1]["background"] = "#e0ffe0"
        elif all_card[numb].set == 14:
            geneCard[(num*2)-1]["text"] = '同盟-' + str(all_card[numb].number) + '　'
            geneCard[(num*2)-1]["background"] = "#ffe0ff"
        elif all_card[numb].set == 15:
            geneCard[(num*2)-1]["text"] = '略奪-' + str(all_card[numb].number) + '　'
            geneCard[(num*2)-1]["background"] = "#ffffe0"

#記憶せずにリセット（王国カード）
def reset_unsave():
    for i in range(len(random_num)):
        if i < 10:
            geneCard[i*2]["text"] = ' - '
            geneCard[i*2+1]["text"] = ' '
        else:
            geneCard[i*2]["text"] = ' '
            geneCard[i*2+1]["text"] = ' '
    random_num.clear()
    random_num_org.clear()

#記憶してリセット（王国カード）
def reset_save():
    for i in range(len(random_num)):
        usecard[random_num[i]] += 1
        if i < 10:
            geneCard[i*2]["text"] = ' - '
            geneCard[i*2+1]["text"] = ' '
        else:
            geneCard[i*2]["text"] = ' '
            geneCard[i*2+1]["text"] = ' '
    random_num.clear()

#記憶をリセット（王国カード）
def save_reset():
    base = 0
    for i in range(len(useset)):
        if useset[i] > 0:
            for j in range(useset[i]):
                usecard[base+j] = 0
            base += useset[i]
        else:
            base -= useset[i]
    reset_unsave()

#特殊カードをランダムで１枚生成   
def random_spcard_gene_1():
    if totalcard[1] > 0:
        if len(random_spnum) < 4:
            chouhuku = 1    ###この数値は重複を許す回数（1:重複無し、N:各カード(N-1)度のみ重複を許す）
            jud = False
            while jud == False:
                bord = 0
                numb = random_number_gene(random_spnum_org,totalcard[1],chouhuku)
                numb_org = numb
                for i in range(len(usespset)):
                    if usespset[i] > 0:
                        bord += usespset[i]
                        if bord > numb:
                            break
                    else:
                        bord -= usespset[i]
                        numb -= usespset[i]
                jud = True
                for i in range(len(random_spnum)):
                    if random_spnum[i] == numb:
                        jud = False
                        break
            random_spnum.append(numb)
            random_spnum_org.append(numb_org)
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
        else:
            showAlert_cardgene()
    else:
        showAlert_cardset()
        skip[0] = False
        backmenu_1b()
            
#記憶せずリセット（特殊カード）
def spreset_unsave():
    for i in range(len(random_spnum)):
        if i < 2:
            geneSPCard[i*2]["text"] = ' - '
            geneSPCard[i*2+1]["text"] = ' '
        else:
            geneSPCard[i*2]["text"] = ' '
            geneSPCard[i*2+1]["text"] = ' '
    random_spnum.clear()
    random_spnum_org.clear()

#記憶してリセット（特殊カード）
def spreset_save():
    for i in range(len(random_spnum)):
        usespcard[random_spnum[i]] += 1
        if i < 2:
            geneSPCard[i*2]["text"] = ' - '
            geneSPCard[i*2+1]["text"] = ' '
        else:
            geneSPCard[i*2]["text"] = ' '
            geneSPCard[i*2+1]["text"] = ' '
    random_spnum.clear()

#記憶をリセット（特殊カード）
def spsave_reset():
    base = 0
    for i in range(len(usespset)):
        if usespset[i] > 0:
            for j in range(usespset[i]):
                usespcard[base+j] = 0
            base += usespset[i]
        else:
            base -= usespset[i]
    spreset_unsave()

# target:質問で得られた情報を記録  target_not:違った情報を記録  confirm:質問によって確定した部分  question:質問の候補  
target  = [-1, -10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [], 0, [-1,-1,-1], [], [], [], 1]
#[0:Set 1:Cost 2:+Act 3:+Buy 4:+Card 5:+Cos 6:+VP 7:Coin 8:Mur 9:Kou 10:Get 11:Los 12:SelfLos 13:Typ 14:Col 15:Lan 16:Sp1 17:Sp2 18:Sp3 19:Typnum]
confirm = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
#[0:Set 1:Cost 2:+Act 3:+Buy 4:+Card 5:+Cos 6:+VP 7:Coin 8:Mur 9:Kou 10:Get 11:Los 12:SelfLos 13:Typ 14:Col 15:Lan 16:Sp1 17:Sp2 18:Sp3 19:Typnum]
ati_cnt = [0]
questions = []
#  0 : アクションカード
#  1 : コスト
#  2 : ＋アクション
#  3 : ＋購入
#  4 : ＋カードを引く
#  5 : ＋コスト
#  6 : 勝利点
#  7 : ＋財源
#  8 : ＋村人
#  9 : ＋好意
# 10 : 獲得
# 11 : 廃棄
# 12 : 自身の廃棄
# 13 : カードタイプの数
# 14 : カードの色（無色・1色・2色）
# 15 : カード名（表記）
# 16 : 拡張セット（前半・後半）
# 17 : 拡張セット（指定）
# 18 : スペシャル1
# 19 : スペシャル2（区切り線）
# 20 : スペシャル3（アタック）
# 21 : カードタイプ（特定）

def ati_start():
    title.pack_forget()
    menu1.pack_forget()
    menu2.pack_forget()
    subtitle2.pack()
    frame_ati_main.pack()
    for i in range(len(full_card)):
        true_card.append(full_card[i])

def ati_back1():
    subtitle2.pack_forget()
    frame_ati_main.pack_forget()
    title.pack(pady=20)
    menu1.pack(pady=10)
    menu2.pack(pady=10)

def ati_main():
    if ati_cnt[0] == 0:
        btn_ati_N["text"] = 'いいえ'
        questions.append(0)
    if ati_cnt[0] == 1:
        questions.append(1)
    if ati_cnt[0] == 3:
        questions.append(2)
        questions.append(3)
        questions.append(4)
        questions.append(5)
        questions.append(16)
    if ati_cnt[0] == 6:
        questions.append(10)
        questions.append(11)
        questions.append(12)

    truecards = len(true_card)
    if truecards > 1:
        rand.shuffle(true_card)
        ati_randcard = true_card[0]
        # Q - 6
        if 3 in target[13] and target[6] == 0 and ati_cnt[0] > 1:
            if 6 in questions:
                questions.remove(6)
            questions.append(6)
        # Q - 18
        if 0 in target[16] and 18 in questions:
            questions.remove(18)
        elif ati_randcard.spe1 > target[16] and ati_cnt[0] > 2:
            if 0 in ati_randcard.spe1:
                if 18 in questions:
                    questions.remove(18)
            else:
                if 18 in questions:
                    questions.remove(18)
                questions.append(18)
                for i in target[16]:
                    if i in ati_randcard.spe1:
                        ati_randcard.spe1.remove(i)
        # Q - 19
        if 0 in target[17] and 19 in questions:
            questions.remove(19)
        else:
            if ati_randcard.spe2 > target[17] and ati_cnt[0] > 5:
                if 19 in questions:
                    questions.remove(19)
                questions.append(19)
                for i in target[17]:
                    if i in ati_randcard.spe2:
                        ati_randcard.spe2.remove(i)
        # Q - 20
        if 6 in target[13]:
            if 20 in questions:
                questions.remove(20)
            if ati_randcard.spe3 > target[18]:
                questions.append(20)
                for i in target[18]:
                    if i in ati_randcard.spe3:
                        ati_randcard.spe3.remove(i)
        # Q - 21
        if 21 in questions:
            questions.remove(21)
        if len(ati_randcard.type) > len(target[13]) and ati_cnt[0] > 2:
            for i in range(len(target[13])):
                if target[13][i] in ati_randcard.type:
                    ati_randcard.type.remove(target[13][i])
            questions.append(21)
        res = questions[rand.randint(1,len(questions)) - 1]
        if len(questions) == 0:
            frame_ati_main.pack_forget()
            text_ati_result["text"] = '思い浮かべているカードがわかりませんでした'
            frame_ati_result.pack()
        ati_main_Q(res,ati_randcard)
    elif truecards == 1:
        truecard = true_card.pop(0)
        frame_ati_main.pack_forget()
        text_ati_result["text"] = '質問回数：' + str(ati_cnt[0]) + '\n思い浮かべているカードは...' 
        text_ati_result1["text"] = '「' + truecard.name + '」\n '
        #カードタイプによる文字色変更（主タイプ）
        if truecard.type1 == 1:   #アクション
            text_ati_result1["foreground"] = "#000090"
        elif truecard.type1 == 2: #財宝
            text_ati_result1["foreground"] = "#f7b400"
        elif truecard.type1 == 3: #勝利点
            text_ati_result1["foreground"] = "#228b22"
        elif truecard.type1 == 4: #リアクション
            text_ati_result1["foreground"] = "#1e90ff"
        elif truecard.type1 == 5: #持続
            text_ati_result1["foreground"] = "#ff7f50"
        elif truecard.type1 == 6: #リザーブ
            text_ati_result1["foreground"] = "#808000"
        elif truecard.type1 == 7: #夜行
            text_ati_result1["foreground"] = "#000000"
        #カードタイプによる背景色変更（副タイプ）
        if truecard.type2 == 1:
            text_ati_result1["background"] = "#d3d3d3"
        elif truecard.type2 == 2:
            text_ati_result1["background"] = "#fffacd"
        elif truecard.type2 == 3:
            text_ati_result1["background"] = "#98fb98"
        elif truecard.type2 == 4:
            text_ati_result1["background"] = "#87cefa"
        elif truecard.type2 == 5:
            text_ati_result1["background"] = "#fae7d2"
        else:   #副タイプ無し
            text_ati_result1["background"] = "#ffffff"
        frame_ati_result.pack()
    else:
        frame_ati_main.pack_forget()
        text_ati_result["text"] = '思い浮かべているカードがわかりませんでした'
        frame_ati_result.pack()


def ati_main_filter_Y(res,point,num):

    ati_cnt[0] += 1
    posi = 0
    kais = len(true_card)

    #アクションカード
    if res == 0:
        for i in range(kais):
            if 1 in true_card[posi].type:
                posi += 1
            else:
                a = true_card.pop(posi)
        target[13].append(1)
        questions.remove(0)
        questions.append(13)

    #コスト
    elif res == 1:
        if point == 1:
            for i in range(kais):
                if true_card[posi].cost > 4 or true_card[posi].cost < 0:
                    a = true_card.pop(posi)
                else:
                    posi += 1
            target[1] = 4
        if point == 2:
            for i in range(kais):
                if true_card[posi].cost > num:
                    a = true_card.pop(posi)
                else:
                    posi += 1
            target[1] = num
        elif point == 3:
            for i in range(kais):
                if true_card[posi].cost < num:
                    a = true_card.pop(posi)
                else:
                    posi += 1
            target[1] = num + 1
            if num == 8:
                true_card.remove(card1009b)
        elif point == 4:
            for i in range(kais):
                if true_card[posi].cost == 1:
                    a = true_card.pop(posi)
                else:
                    posi += 1
            target[1] = 0
            confirm[1] = True
            questions.remove(1)
        elif point == 5:
            for i in range(kais):
                if true_card[posi].cost > 0:
                    a = true_card.pop(posi)
                else:
                    posi += 1
            target[1] = -1
            questions.remove(1)

    #＋アクション
    elif res == 2:
        if point == 1:
            for i in range(kais):
                if true_card[posi].pa > 0:
                    a = true_card.pop(posi)
                else:
                    posi += 1
            target[2] = 0
            confirm[2] = True
            questions.remove(2)
        elif point == 2:
            for i in range(kais):
                if true_card[posi].pa < num:
                    a = true_card.pop(posi)
                else:
                    posi += 1
            target[2] = num
    
    #＋購入
    elif res == 3:
        for i in range(kais):
            if true_card[posi].pb < num:
                a = true_card.pop(posi)
            else:
                posi += 1
        target[3] = num

    #＋カードを引く
    elif res == 4:
        if point == 1:
            for i in range(kais):
                if true_card[posi].pca < num:
                    a = true_card.pop(posi)
                else:
                    posi += 1
            target[4] = num
        elif point == 2:
            for i in range(kais):
                if true_card[posi].pca != num:
                    a = true_card.pop(posi)
                else:
                    posi += 1
            target[4] = 10
            confirm[4] = True
            questions.remove[4]

    #＋コスト
    elif res == 5:
        for i in range(kais):
            if true_card[posi].pcs < num:
                a = true_card.pop(posi)
            else:
                posi += 1
        target[5] = num

    #勝利点
    elif res == 6:
        for i in range(kais):
            if true_card[posi].pv != num:
                a = true_card.pop(posi)
            else:
                posi += 1
        target[6] = num
        confirm[6] = num

    #財源
    elif res == 7:
        for i in range(kais):
            if true_card[posi].pcoin < num:
                a = true_card.pop(posi)
            else:
                posi += 1
        target[7] = num

    #村人
    elif res == 8:
        for i in range(kais):
            if true_card[posi].pmrbt < num:
                a = true_card.pop(posi)
            else:
                posi += 1
        target[8] = num

    #好意
    elif res == 9:
        for i in range(kais):
            if true_card[posi].koi < num:
                a = true_card.pop(posi)
            else:
                posi += 1
        target[9] = num
        questions.remove(9)

    #獲得
    elif res == 10:
        for i in range(kais):
            if true_card[posi].get == (num - 1):
                a = true_card.pop(posi)
            else:
                posi += 1
        target[10] = num

    #他を廃棄
    elif res == 11:
        for i in range(kais):
            if true_card[posi].lost == (num - 1):
                a = true_card.pop(posi)
            else:
                posi += 1
        target[11] = num

    #自身を廃棄
    elif res == 12:
        for i in range(kais):
            if true_card[posi].selflost == (num - 1):
                a = true_card.pop(posi)
            else:
                posi += 1
        target[12] = num
        questions.remove(12)

    #タイプ数
    elif res == 13:
        if point == 1:
            for i in range(kais):
                if len(true_card[posi].type) > 1:
                    posi += 1
                else:
                    a = true_card.pop(posi)
            target[19] = num
            questions.remove(13)
            questions.append(14)
        elif point == 2:
            for i in range(kais):
                if len(true_card[posi].type) > 1:
                    posi += 1
                else:
                    a = true_card.pop(posi)
            target[19] = num
            questions.append(14)
        elif point == 3:
            for i in range(kais):
                if len(true_card[posi].type) >= num:
                    posi += 1
                else:
                    a = true_card.pop(posi)
            target[19] = num

    #カードの色数
    elif res == 14:
        for i in range(kais):
            if true_card[posi].color == num:
                posi += 1
            else:
                a = true_card.pop(posi)
        target[14] = num
        confirm[14] = True
        questions.remove(14)

    #拡張範囲
    elif res == 16:
        for i in range(kais):
                if num >= true_card[posi].set:
                    posi += 1
                else:
                    a = true_card.pop(posi)
        questions.remove(16)
        questions.append(17)

    #拡張指定
    elif res == 17:
        for i in range(kais):
                if num == true_card[posi].set:
                    posi += 1
                else:
                    a = true_card.pop(posi)
        questions.remove(17)
        target[0] = num
        confirm[0] = True

    #細分化1
    elif res == 18:
        for i in range(kais):
            if num in true_card[posi].spe1:
                posi += 1
            else:
                a = true_card.pop(posi)
        target[16].append(num)
        if num == 19:
            questions.append(7)
            questions.append(8)
            questions.append(9)

    #細分化2
    elif res == 19:
        if num == 0:
            for i in range(kais):
                if num in true_card[posi].spe2:
                    a = true_card.pop(posi)
                else:
                    posi += 1
            target[17].append(-1)
        else:
            for i in range(kais):
                if num in true_card[posi].spe2:
                    posi += 1
                else:
                    a = true_card.pop(posi)
            if -1 in target[17]:
                target[17].remove(-1)
            target[17].append(num)

    #細分化3（アタック）
    elif res == 20:
        for i in range(kais):
            if num in true_card[posi].spe3:
                posi += 1
            else:
                a = true_card.pop(posi)
        target[18].append(num)
    
    #カードタイプ
    elif res == 21:
        for i in range(kais):
            if num in true_card[posi].type:
                posi += 1
            else:
                a = true_card.pop(posi)
        target[13].append(num)
        if len(target[13]) == target[19] and confirm[19] == True:
            confirm[13] = True

    ati_main()


def ati_main_filter_N(res,point,num):

    ati_cnt[0] += 1
    posi = 0
    kais = len(true_card)

    #アクションカード
    if res == 0:
        for i in range(kais):
            if 1 in true_card[posi].type:
                a = true_card.pop(posi)
            else:
                posi += 1
        target[14] = 1
        questions.remove(0)
        questions.append(13)

    #コスト
    elif res == 1:
        if point == 1:
            for i in range(kais):
                if true_card[posi].cost < 5 and true_card[posi].cost >= 0:
                    a = true_card.pop(posi)
                else:
                    posi += 1
            target[1] = 6
        if point == 2:
            for i in range(kais):
                if true_card[posi].cost <= num:
                    a = true_card.pop(posi)
                else:
                    posi += 1
            target[1] = num + 1
            confirm[1] = True
            questions.remove(1)
        elif point == 3:
            for i in range(kais):
                    if true_card[posi].cost >= num:
                        a = true_card.pop(posi)
                    else:
                        posi += 1
            target[1] = num - 1
            if num == 9:
                true_card.append(card1009b)
            if num > 6:
                confirm[1] = True
                questions.remove(1)
        elif point == 4:
            for i in range(kais):
                if true_card[posi].cost == 0:
                    a = true_card.pop(posi)
                else:
                    posi += 1
            target[1] = 1
            confirm[1] = True
            questions.remove(1)
        elif point == 5:
            for i in range(kais):
                if true_card[posi].cost < 0:
                    a = true_card.pop(posi)
                else:
                    posi += 1
            target[1] = 5
            confirm[1] = True
            questions.remove(1)

    #＋アクション
    elif res == 2:
        if point == 1:
            for i in range(kais):
                if true_card[posi].pa == 0:
                    a = true_card.pop(posi)
                else:
                    posi += 1
            target[2] = num
        elif point == 2:
            for i in range(kais):
                if true_card[posi].pa > 1:
                    a = true_card.pop(posi)
                else:
                    posi += 1
            target[2] = 1
            confirm[2] = True
            questions.remove(2)
    
    #＋購入
    elif res == 3:
        for i in range(kais):
            if true_card[posi].pb >= num:
                a = true_card.pop(posi)
            else:
                posi += 1
        target[3] = num - 1
        confirm[3] = True
        questions.remove(3)

    #＋カードを引く
    elif res == 4:
        if point == 1:
            for i in range(kais):
                if true_card[posi].pca >= num:
                    a = true_card.pop(posi)
                else:
                    posi += 1
            target[4] = num - 1
            confirm[4] = True
            questions.remove(4)
        elif point == 2:
            for i in range(kais):
                if true_card[posi].pca == num:
                    a = true_card.pop(posi)
                else:
                    posi += 1

    #＋コスト
    elif res == 5:
        for i in range(kais):
            if true_card[posi].pcs >= num:
                a = true_card.pop(posi)
            else:
                posi += 1
        target[5] = num - 1
        confirm[5] = True
        questions.remove(5)

    #勝利点
    elif res == 6:
        for i in range(kais):
            if true_card[posi].pv == num:
                a = true_card.pop(posi)
            else:
                posi += 1

    #財源
    elif res == 7:
        for i in range(kais):
            if true_card[posi].pcoin >= num:
                a = true_card.pop(posi)
            else:
                posi += 1
        target[7] = num - 1
        confirm[7] = True
        questions.remove(7)

    #村人
    elif res == 8:
        for i in range(kais):
            if true_card[posi].pmrbt < num:
                a = true_card.pop(posi)
            else:
                posi += 1
        target[8] = num - 1
        confirm[8] = True
        questions.remove(8)

    #好意
    elif res == 9:
        for i in range(kais):
            if true_card[posi].koi < num:
                a = true_card.pop(posi)
            else:
                posi += 1
        target[9] = num - 1
        confirm[9] = True
        questions.remove(9)

    #獲得
    elif res == 10:
        for i in range(kais):
            if true_card[posi].get > (num - 1):
                a = true_card.pop(posi)
            else:
                posi += 1
        target[10] = num - 1
        confirm[10] = True
        questions.remove(10)

    #他を廃棄
    elif res == 11:
        for i in range(kais):
            if true_card[posi].lost > (num - 1):
                a = true_card.pop(posi)
            else:
                posi += 1
        target[11] = num - 1
        confirm[11] = True
        questions.remove(11)

    #自身を廃棄
    elif res == 12:
        for i in range(kais):
            if true_card[posi].selflost > (num - 1):
                a = true_card.pop(posi)
            else:
                posi += 1
        target[12] = num - 1
        confirm[12] = True
        questions.remove(12)
            
    #タイプ数
    elif res == 13:
        if point == 1:
            for i in range(kais):
                if len(true_card[posi].type) > 1:
                    a = true_card.pop(posi)
                else:
                    posi += 1
            target[14] = 0
            confirm[14] = True
            target[19] = num - 1
            confirm[19] = True
            questions.remove(13)
        elif point == 2:
            for i in range(kais):
                if len(true_card[posi].type) > 1:
                    a = true_card.pop(posi)
                else:
                    posi += 1
            target[14] = 1
            confirm[14] = True
            target[19] = num - 1
            confirm[19] = True
            questions.remove(13)
        elif point == 3:
            for i in range(kais):
                if len(true_card[posi].type) >= num:
                    a = true_card.pop(posi)
                else:
                    posi += 1
            target[19] = num - 1
            confirm[19] = True
            questions.remove(13)
    
    #カードの色数
    elif res == 14:
        for i in range(kais):
            if true_card[posi].color == num:
                a = true_card.pop(posi)
            else:
                posi += 1
            target[14] = num + 1
        if num == 1:
            target[14] = 2
            confirm[14] = True
            questions.remove(14)

    #拡張範囲
    elif res == 16:
        for i in range(kais):
                if num < true_card[posi].set:
                    posi += 1
                else:
                    a = true_card.pop(posi)
        questions.remove(16)
        questions.append(17)

    #拡張指定
    elif res == 17:
        for i in range(kais):
                if num == true_card[posi].set:
                    a = true_card.pop(posi)
                else:
                    posi += 1

    #細分化1
    elif res == 18:
        for i in range(kais):
            if num in true_card[posi].spe1:
                a = true_card.pop(posi)
            else:
                posi += 1

    #細分化2
    elif res == 19:
        if num == 0:
            for i in range(kais):
                if num in true_card[posi].spe2:
                    posi += 1
                else:
                    a = true_card.pop(posi)
            target[17].append(num)
            confirm[17] = True
        else:
            for i in range(kais):
                if num in true_card[posi].spe2:
                    a = true_card.pop(posi)
                else:
                    posi += 1

    #細分化3（アタック）
    elif res == 20:
        for i in range(kais):
            if num in true_card[posi].spe3:
                a = true_card.pop(posi)
            else:
                posi += 1

    #カードタイプ
    elif res == 21:
        for i in range(kais):
            if num in true_card[posi].type:
                a = true_card.pop(posi)
            else:
                posi += 1

    ati_main()

def ati_main_Q(res, ati_randcard):

    #アクションカード
    if res == 0:
        border = 1
        text_ati_Q["text"] = 'アクションカードですか？'
        btn_ati_Y["command"] = lambda :ati_main_filter_Y(res,1,border)
        btn_ati_N["command"] = lambda :ati_main_filter_N(res,1,border)

    #コスト
    elif res == 1:
        #最初
        if target[1] == -10:
            border = 4
            text_ati_Q["text"] = 'コストは' + str(border) + '以下ですか？'
            btn_ati_Y["command"] = lambda :ati_main_filter_Y(res,1,border)
            btn_ati_N["command"] = lambda :ati_main_filter_N(res,1,border)
        #コスト 0 or 1
        elif target[1] == 1:
            border = 0
            text_ati_Q["text"] = 'コストは' + str(border) + '以下ですか？'
            btn_ati_Y["command"] = lambda :ati_main_filter_Y(res,4,border)
            btn_ati_N["command"] = lambda :ati_main_filter_N(res,4,border)
        #コスト N 以下
        elif target[1] < 5:
            border = target[1] - 1
            text_ati_Q["text"] = 'コストは' + str(border) + '以下ですか？'
            btn_ati_Y["command"] = lambda :ati_main_filter_Y(res,2,border)
            btn_ati_N["command"] = lambda :ati_main_filter_N(res,2,border)
        #コスト N 以上
        elif target[1] > 5:
            border = target[1]
            text_ati_Q["text"] = 'コストは' + str(border) + '以上ですか？'
            btn_ati_Y["command"] = lambda :ati_main_filter_Y(res,3,border)
            btn_ati_N["command"] = lambda :ati_main_filter_N(res,3,border)
        #負債トークンを用いるか or コスト 5
        else:
            border = target[1]
            text_ati_Q["text"] = '負債トークンは用いますか？'
            btn_ati_Y["command"] = lambda :ati_main_filter_Y(res,5,border)
            btn_ati_N["command"] = lambda :ati_main_filter_N(res,5,border)

    #＋アクション
    elif res == 2:
        border = target[2] + 1
        if border == 1:
            text_ati_Q["text"] = 'ターミナルですか？'
            btn_ati_Y["command"] = lambda :ati_main_filter_Y(res,1,border)
            btn_ati_N["command"] = lambda :ati_main_filter_N(res,1,border)
        else:
            text_ati_Q["text"] = '＋' + str(border) + 'アクション以上ですか？'
            btn_ati_Y["command"] = lambda :ati_main_filter_Y(res,2,border)
            btn_ati_N["command"] = lambda :ati_main_filter_N(res,2,border)
    
    #＋購入
    elif res == 3:
        border = target[3] + 1
        text_ati_Q["text"] = '＋' + str(border) + '購入以上はありますか？'
        btn_ati_Y["command"] = lambda :ati_main_filter_Y(res,1,border)
        btn_ati_N["command"] = lambda :ati_main_filter_N(res,1,border)
    
    #＋カードを引く
    elif res == 4:
        if ati_randcard.pca != 10:
            border = target[4] + 1
            text_ati_Q["text"] = str(border) + '枚以上カードを引くことはできますか？'
            btn_ati_Y["command"] = lambda :ati_main_filter_Y(res,1,border)
            btn_ati_N["command"] = lambda :ati_main_filter_N(res,1,border)
        else:
            border = 10
            text_ati_Q["text"] = 'カードを引く枚数に上限がないですか？'
            btn_ati_Y["command"] = lambda :ati_main_filter_Y(res,2,border)
            btn_ati_N["command"] = lambda :ati_main_filter_N(res,2,border)
    
    #＋コスト
    elif res == 5:
        border = target[5] + 1
        text_ati_Q["text"] = '＋' + str(border) + 'コスト以上付きますか？'
        btn_ati_Y["command"] = lambda :ati_main_filter_Y(res,1,border)
        btn_ati_N["command"] = lambda :ati_main_filter_N(res,1,border)

    #勝利点
    elif res == 6:
        border = target[6]
        if border == 15:
            text_ati_Q["text"] = '得られる勝利点が固定ではないですか？'
        else:
            text_ati_Q["text"] = '得られる勝利点は' + str(border) + '点ですか？'
        btn_ati_Y["command"] = lambda :ati_main_filter_Y(res,1,border)
        btn_ati_N["command"] = lambda :ati_main_filter_N(res,1,border)

    #獲得
    elif res == 10:
        border = target[10] + 1
        text_ati_Q["text"] = 'カードを' + str(border) + '枚獲得する効果がありますか？'
        btn_ati_Y["command"] = lambda :ati_main_filter_Y(res,1,border)
        btn_ati_N["command"] = lambda :ati_main_filter_N(res,1,border)

    #他を廃棄
    elif res == 11:
        border = target[11] + 1
        text_ati_Q["text"] = '自身以外を' + str(border) + '枚廃棄する効果はありますか？'
        btn_ati_Y["command"] = lambda :ati_main_filter_Y(res,1,border)
        btn_ati_N["command"] = lambda :ati_main_filter_N(res,1,border)

    #自身を廃棄
    elif res == 12:
        border = target[12] + 1
        text_ati_Q["text"] = '自身を' + str(border) + '枚廃棄する効果はありますか？'
        btn_ati_Y["command"] = lambda :ati_main_filter_Y(res,1,border)
        btn_ati_N["command"] = lambda :ati_main_filter_N(res,1,border)

    #カードタイプ数
    elif res == 13:
        border = target[19] + 1
        text_ati_Q["text"] = 'カードタイプは' + str(border) + '種以上ですか？'
        if target[19] == 1:
            if 1 in target[13]:
                btn_ati_Y["command"] = lambda :ati_main_filter_Y(res,1,border)
                btn_ati_N["command"] = lambda :ati_main_filter_N(res,1,border)
            else:
                btn_ati_Y["command"] = lambda :ati_main_filter_Y(res,2,border)
                btn_ati_N["command"] = lambda :ati_main_filter_N(res,2,border)
        else:
            btn_ati_Y["command"] = lambda :ati_main_filter_Y(res,3,border)
            btn_ati_N["command"] = lambda :ati_main_filter_N(res,3,border)

    #カードの色数
    elif res == 14:
        border = target[14]
        if border == 0:
            text_ati_Q["text"] = 'カードの背景色は無色（白色）ですか？'
        else:
            text_ati_Q["text"] = 'カードの背景色は' + str(border) + '色ですか？'
        btn_ati_Y["command"] = lambda :ati_main_filter_Y(res,1,border)
        btn_ati_N["command"] = lambda :ati_main_filter_N(res,1,border)

    #拡張範囲
    elif res == 16:
        text_ati_Q["text"] = '拡張セットは前半（前半：ギルド以前、後半：冒険以降）ですか？'
        btn_ati_Y["command"] = lambda :ati_main_filter_Y(res,1,8)
        btn_ati_N["command"] = lambda :ati_main_filter_N(res,1,8)

    #拡張指定
    elif res == 17:
        border = ati_randcard.set
        typename = '' 
        if border == 0:
            typename = '基本'
        elif border == 1:
            typename = '陰謀'
        elif border == 2:
            typename = '海辺'
        elif border == 3:
            typename = '錬金術'
        elif border == 4:
            typename = '繁栄'
        elif border == 5:
            typename = '収穫祭'
        elif border == 6:
            typename = '異郷'
        elif border == 7:
            typename = '暗黒時代'
        elif border == 8:
            typename = 'ギルド'
        elif border == 9:
            typename = '冒険'
        elif border == 10:
            typename = '帝国'
        elif border == 11:
            typename = '夜想曲'
        elif border == 12:
            typename = 'ルネサンス'
        elif border == 13:
            typename = '移動動物園'
        elif border == 14:
            typename = '同盟'
        elif border == 15:
            typename = '略奪'
        text_ati_Q["text"] = '拡張セットは' + typename + 'ですか？'
        btn_ati_Y["command"] = lambda :ati_main_filter_Y(res,1,border)
        btn_ati_N["command"] = lambda :ati_main_filter_N(res,1,border)

    #細分化1
    elif res == 18:
        rand.shuffle(ati_randcard.spe2)
        border = ati_randcard.spe1[0]
        point = 1
        if border == 0:
            text_ati_Q["text"] = '（アタック、リアクション効果、区切り線以外で）＋○○ 獲得 廃棄以外にカード効果の文章を含みますか？\nもしくはマットやサプライ外カードなどの準備が必要ですか？'
        elif border == 1:
            text_ati_Q["text"] = '手札を捨て札にする効果はありますか？'
        elif border == 2:
            text_ati_Q["text"] = '山札から捨て札にする効果はありますか？'
        elif border == 3:
            text_ati_Q["text"] = '山札操作が可能（山札確認を含む）効果ですか？'
        elif border == 4:
            text_ati_Q["text"] = 'アタックを防御できる効果ですか？'
        elif border == 5:
            text_ati_Q["text"] = '（手札を捨て札にする効果を除く）デメリットを含む効果ですか？'
        elif border == 6:
            text_ati_Q["text"] = '別カードを使用することができますか？（ex.家臣・玉座の間）'
        elif border == 7:
            text_ati_Q["text"] = '選択効果が含まれますか？'
        elif border == 8:
            text_ati_Q["text"] = '手札を山札に戻す効果はありますか？'
        elif border == 9:
            text_ati_Q["text"] = '他カードのコストを減らす効果がありますか？'
        elif border == 10:
            text_ati_Q["text"] = 'そのカードは使い切りですか？'
        elif border == 11:
            text_ati_Q["text"] = 'フルスペックで使用するには条件がありますか？'
        elif border == 12:
            text_ati_Q["text"] = '分割山札ですか？'
        elif border == 13:
            text_ati_Q["text"] = '別カードを準備する必要がありますか？（祝福・呪詛・ポーション・戦利品・廃墟は除く）'
        elif border == 14:
            text_ati_Q["text"] = '追加ターンを得ることができますか？'
        elif border == 15:
            text_ati_Q["text"] = '戦利品を獲得する効果が含まれますか？'
        elif border == 16:
            text_ati_Q["text"] = '手札を保存しておく効果ですか？'
        elif border == 17:
            text_ati_Q["text"] = '手札に獲得する効果ですか？'
        elif border == 18:
            text_ati_Q["text"] = '交換する効果が含まれますか？（ex.仮面舞踏会・吸血鬼）'
        elif border == 19:
            text_ati_Q["text"] = 'マットを用いますか？'
        elif border == 20:
            text_ati_Q["text"] = '他人の手札に干渉する効果は含まれますか？'
        elif border == 21:
            text_ati_Q["text"] = '獲得したカードを山札に加えますか？'
        elif border == 22:
            text_ati_Q["text"] = 'カードを引く際に癖がありますか？'
        elif border == 23:
            text_ati_Q["text"] = '山札を捨て札にする効果はありますか？'
        elif border == 24:
            text_ati_Q["text"] = '使用後サプライの山に戻る'
        elif border == 25:
            text_ati_Q["text"] = 'トークンを用いる効果ですか？（アタック以外）'
        elif border == 26:
            text_ati_Q["text"] = 'フェイズを遡る効果がありますか？'
        elif border == 27:
            text_ati_Q["text"] = '使用時に負債を用いる効果がありますか？'
        elif border == 28:
            text_ati_Q["text"] = '自分で呪いを獲得する効果が含まれますか？'
        elif border == 29:
            text_ati_Q["text"] = '祝福を用いますか？'
        elif border == 30:
            text_ati_Q["text"] = '呪詛を用いますか？'
        elif border == 31:
            text_ati_Q["text"] = '玉座系カードですか？（2回以上使用できる効果）'
        elif border == 32:
            text_ati_Q["text"] = '追放する効果が含まれますか？'
        elif border == 33:
            text_ati_Q["text"] = '馬を用いますか？'
        elif border == 34:
            text_ati_Q["text"] = 'アーティファクトを用いますか？'
        elif border == 35:
            text_ati_Q["text"] = '使用後自身の山札に戻る効果がありますか？'
        elif border == 36:
            text_ati_Q["text"] = 'サプライの分割山札を循環する効果が含まれますか？'
        elif border == 37:
            text_ati_Q["text"] = 'コストにポーションは含まれますか？'
        btn_ati_Y["command"] = lambda :ati_main_filter_Y(res,point,border)
        btn_ati_N["command"] = lambda :ati_main_filter_N(res,point,border)

    #細分化2（区切り線）
    elif res == 19:
        if len(target[17]) == 0:
            border = 0
        else:
            rand.shuffle(ati_randcard.spe2)
            border = ati_randcard.spe2[0]
        if border == 0:
            text_ati_Q["text"] = 'カード効果に区切り線はありますか？'
        elif border == 1:
            text_ati_Q["text"] = '獲得時効果がありますか？'
        elif border == 2:
            text_ati_Q["text"] = '購入時効果がありますか？'
        elif border == 3:
            text_ati_Q["text"] = '廃棄時効果がありますか？'
        elif border == 4:
            text_ati_Q["text"] = '過払い効果がありますか？'
        elif border == 5:
            text_ati_Q["text"] = 'リアクション効果がありますか？'
        elif border == 6:
            text_ati_Q["text"] = ''
        elif border == 7:
            text_ati_Q["text"] = 'リザーブ効果がありますか？'
        elif border == 8:
            text_ati_Q["text"] = 'ゲームに影響する効果がありますか？'
        elif border == 9:
            text_ati_Q["text"] = '区切り線以降は勝利点の点数に関する記述ですか？'
        elif border == 10:
            text_ati_Q["text"] = 'トラベラー効果がありますか？'
        elif border == 11:
            text_ati_Q["text"] = '区切り線以降は自身のコストが変動する効果ですか？'
        btn_ati_Y["command"] = lambda :ati_main_filter_Y(res,1,border)
        btn_ati_N["command"] = lambda :ati_main_filter_N(res,1,border)

    #細分化3（アタック）
    elif res == 20:
        rand.shuffle(ati_randcard.spe3)
        border = ati_randcard.spe3[0]
        if border == 1:
            text_ati_Q["text"] = 'アタック効果に手札を捨てさせる効果はありますか？'
        elif border == 2:
            text_ati_Q["text"] = 'アタック効果は手札を2枚まで捨てさせる効果ですか？'
        elif border == 3:
            text_ati_Q["text"] = 'アタック効果は手札を3枚まで捨てさせる効果ですか？'
        elif border == 4:
            text_ati_Q["text"] = 'アタック効果は手札を4枚まで捨てさせる効果ですか？'
        elif border == 5:
            text_ati_Q["text"] = 'アタック効果は手札を1枚捨てさせる効果ですか？'
        elif border == 6:
            text_ati_Q["text"] = 'アタック効果は手札を2枚捨てさせる効果ですか？'
        elif border == 7:
            text_ati_Q["text"] = 'アタック効果は手札の指定カードを捨てさせる効果ですか？'
        elif border == 8:
            text_ati_Q["text"] = 'アタック効果で手札を捨てさせる際に上限がないですか？'
        elif border == 9:
            text_ati_Q["text"] = 'アタック効果は手札を山札に戻させる効果ですか？'
        elif border == 10:
            text_ati_Q["text"] = 'アタック効果は手札をリセットさせる効果ですか？'
        elif border == 11:
            text_ati_Q["text"] = 'アタック効果は呪いを与えることができる効果がありますか？'
        elif border == 12:
            text_ati_Q["text"] = 'アタック効果は呪いを強制で配布させる効果ですか？'
        elif border == 13:
            text_ati_Q["text"] = 'アタック効果は廃墟を配布する効果ですか？'
        elif border == 14:
            text_ati_Q["text"] = 'アタック効果は特定カード（呪い・廃墟 以外）を配布する効果ですか？'
        elif border == 15:
            text_ati_Q["text"] = 'アタック効果は廃棄（デッキ破壊）させる効果ですか？'
        elif border == 16:
            text_ati_Q["text"] = 'アタック効果は相手の山札を捨て札にする効果ですか？'
        elif border == 17:
            text_ati_Q["text"] = 'アタック効果は妨害トークンを用いますか？'
        elif border == 18:
            text_ati_Q["text"] = 'アタック効果はカード効果を上書きする効果ですか？'
        elif border == 19:
            text_ati_Q["text"] = 'アタック効果は呪詛を用いる効果ですか？'
        elif border == 20:
            text_ati_Q["text"] = 'アタック効果は追放に関する効果ですか？'
        btn_ati_Y["command"] = lambda :ati_main_filter_Y(res,1,border)
        btn_ati_N["command"] = lambda :ati_main_filter_N(res,1,border)

    #カードタイプ
    elif res == 21:
        border = ati_randcard.type[0]
        typename = '' 
        if border == 2:
            typename = '財宝'
        elif border == 3:
            typename = '勝利点'
        elif border == 4:
            typename = '呪い'
        elif border == 5:
            typename = 'リアクション'
        elif border == 6:
            typename = 'アタック'
        elif border == 7:
            typename = '持続'
        elif border == 8:
            typename = '恩賞'
        elif border == 9:
            typename = '褒賞'
        elif border == 10:
            typename = '廃墟'
        elif border == 11:
            typename = '避難所'
        elif border == 12:
            typename = '略奪者'
        elif border == 13:
            typename = '騎士'
        elif border == 14:
            typename = '命令'
        elif border == 15:
            typename = 'リザーブ'
        elif border == 16:
            typename = 'トラベラー'
        elif border == 17:
            typename = '集合'
        elif border == 18:
            typename = '城'
        elif border == 19:
            typename = '幸運'
        elif border == 20:
            typename = '不運'
        elif border == 21:
            typename = '夜行'
        elif border == 22:
            typename = '家宝'
        elif border == 23:
            typename = '精霊'
        elif border == 24:
            typename = 'ゾンビ'
        elif border == 25:
            typename = '連携'
        elif border == 26:
            typename = '城砦'
        elif border == 27:
            typename = '衝突'
        elif border == 28:
            typename = '叙事詩'
        elif border == 29:
            typename = '町民'
        elif border == 30:
            typename = '卜占官'
        elif border == 31:
            typename = '魔法使い'
        elif border == 32:
            typename = '戦利品'
        text_ati_Q["text"] = typename + 'カードですか？'
        btn_ati_Y["command"] = lambda :ati_main_filter_Y(res,1,border)
        btn_ati_N["command"] = lambda :ati_main_filter_N(res,1,border)


def ati_fin_result():
    title.pack(pady=20)
    menu1.pack(pady=10)
    menu2.pack(pady=10)
    subtitle2.pack_forget()
    frame_ati_result.pack_forget()
    target.clear()
    target.append(-1)
    target.append(-10)
    target.append(0)
    target.append(0)
    target.append(0)
    target.append(0)
    target.append(0)
    target.append(0)
    target.append(0)
    target.append(0)
    target.append(0)
    target.append(0)
    target.append(0)
    target.append([])
    target.append(0)
    target.append([-1,-1,-1])
    target.append([])
    target.append([])
    target.append([])
    target.append(1)
    confirm.clear()
    for i in range(20):
        confirm.append(False)
    ati_cnt.clear()
    ati_cnt.append(0)
    questions.clear()
    text_ati_Q["text"] = 'カードを1枚思い浮かべましたか？'
    btn_ati_N["text"] = 'やめる'
    btn_ati_Y["command"] = ati_main
    btn_ati_N["command"] = ati_back1


#王国カード情報登録
all_card = []
full_card = []
true_card = []
#基本
card0000a = Card('銅貨',0,0,2,0,0,0,0,0,1,0,0,0,0,0,0,0,[2],1,[0,0,1],[0],[0],[0])
card0000b = Card('銀貨',0,0,2,0,3,0,0,0,2,0,0,0,0,0,0,0,[2],1,[0,0,1],[0],[0],[0])
card0000c = Card('金貨',0,0,2,0,6,0,0,0,3,0,0,0,0,0,0,0,[2],1,[0,0,1],[0],[0],[0])
card0000d = Card('屋敷',0,0,3,0,2,0,0,0,0,1,0,0,0,0,0,0,[3],1,[0,0,1],[0],[0],[0])
card0000e = Card('公領',0,0,3,0,5,0,0,0,0,3,0,0,0,0,0,0,[3],1,[0,0,1],[0],[0],[0])
card0000f = Card('属州',0,0,3,0,8,0,0,0,0,6,0,0,0,0,0,0,[3],1,[0,0,1],[0],[0],[0])
card0000g = Card('呪い',0,0,0,0,0,0,0,0,-1,0,0,0,0,0,0,0,[4],1,[1,0,1],[0],[0],[0])
card0001 = Card('堀',0,1,4,0,2,0,0,2,0,0,0,0,0,0,0,0,[1,5],1,[0,0,1],[4],[5],[0])
all_card.append(card0001)
card0002 = Card('職人',0,2,1,0,6,0,0,0,0,0,0,0,0,1,0,0,[1],0,[0,0,1],[8,17],[0],[0])
all_card.append(card0002)
card0003 = Card('山賊',0,3,1,0,5,0,0,0,0,0,0,0,0,1,0,0,[1,6],0,[0,0,1],[0],[0],[15,16])
all_card.append(card0003)
card0004 = Card('役人',0,4,1,0,4,0,0,0,0,0,0,0,0,1,0,0,[1,6],0,[0,0,1],[0],[0],[9])
all_card.append(card0004)
card0005 = Card('地下貯蔵庫',0,5,1,0,2,1,0,10,0,0,0,0,0,0,0,0,[1],0,[0,0,1],[1],[0],[0])
all_card.append(card0005)
card0006 = Card('礼拝堂',0,6,1,0,2,0,0,0,0,0,0,0,0,0,4,0,[1],0,[0,0,1],[0],[0],[0])
all_card.append(card0006)
card0007 = Card('議事堂',0,7,1,0,5,0,1,4,0,0,0,0,0,0,0,0,[1],0,[0,0,1],[5,20],[0],[0])
all_card.append(card0007)
card0008 = Card('祝祭',0,8,1,0,5,2,1,0,2,0,0,0,0,0,0,0,[1],0,[0,0,1],[0],[0],[0])
all_card.append(card0008)
card0009 = Card('前駆者',0,9,1,0,3,1,0,1,0,0,0,0,0,0,0,0,[1],0,[0,0,1],[3],[0],[0])
all_card.append(card0009)
card0010 = Card('研究所',0,10,1,0,5,1,0,2,0,0,0,0,0,0,0,0,[1],0,[0,0,1],[0],[0],[0])
all_card.append(card0010)
card0011 = Card('書庫',0,11,1,0,5,0,0,7,0,0,0,0,0,0,0,0,[1],0,[0,0,1],[0],[0],[0])
all_card.append(card0011)
card0012 = Card('市場',0,12,1,0,5,1,1,1,1,0,0,0,0,0,0,0,[1],0,[0,0,1],[0],[0],[0])
all_card.append(card0012)
card0013 = Card('商人',0,13,1,0,3,1,0,1,1,0,0,0,0,0,0,0,[1],0,[0,0,1],[11],[0],[0])
all_card.append(card0013)
card0014 = Card('民兵',0,14,1,0,4,0,0,0,2,0,0,0,0,0,0,0,[1,6],0,[0,0,1],[0],[0],[1,3])
all_card.append(card0014)
card0015 = Card('鉱山',0,15,1,0,5,0,0,0,0,0,0,0,0,1,1,0,[1],0,[0,0,1],[17],[0],[0])
all_card.append(card0015)
card0016 = Card('金貸し',0,16,1,0,4,0,0,0,3,0,0,0,0,0,1,0,[1],0,[1,0,1],[11],[0],[0])
all_card.append(card0016)
card0017 = Card('密猟者',0,17,1,0,1,1,0,1,1,0,0,0,0,0,0,0,[1],0,[0,0,1],[1,5,11],[0],[0])
all_card.append(card0017)
card0018 = Card('改築',0,18,1,0,4,0,0,0,0,0,0,0,0,1,1,0,[1],0,[0,0,1],[0],[0],[0])
all_card.append(card0018)
card0019 = Card('衛兵',0,19,1,0,5,1,0,1,0,0,0,0,0,0,2,0,[1],0,[0,0,1],[2,3],[0],[0])
all_card.append(card0019)
card0020 = Card('鍛冶屋',0,20,1,0,4,0,0,3,0,0,0,0,0,0,0,0,[1],0,[0,0,1],[0],[0],[0])
all_card.append(card0020)
card0021 = Card('玉座の間',0,21,1,0,4,0,0,0,0,0,0,0,0,0,0,0,[1],0,[1,0,1],[6,31],[0],[0])
all_card.append(card0021)
card0022 = Card('家臣',0,22,1,0,3,0,0,0,2,0,0,0,0,0,0,0,[1],0,[0,0,1],[2,6,11],[0],[0])
all_card.append(card0022)
card0023 = Card('村',0,23,1,0,3,2,0,1,0,0,0,0,0,0,0,0,[1],0,[0,0,1],[0],[0],[0])
all_card.append(card0023)
card0024 = Card('魔女',0,24,1,0,5,0,0,2,0,0,0,0,0,0,0,0,[1,6],0,[0,0,1],[0],[0],[11,12])
all_card.append(card0024)
card0025 = Card('工房',0,25,1,0,3,0,0,0,0,0,0,0,0,1,0,0,[1],0,[0,0,1],[0],[0],[0])
all_card.append(card0025)
card0026 = Card('庭園',0,26,3,0,4,0,0,0,0,15,0,0,0,0,0,0,[3],1,[0,0,1],[0],[0],[0])
all_card.append(card0026)
full_card.append(card0000a)
full_card.append(card0000b)
full_card.append(card0000c)
full_card.append(card0000d)
full_card.append(card0000e)
full_card.append(card0000f)
full_card.append(card0000g)
full_card.append(card0001)
full_card.append(card0002)
full_card.append(card0003)
full_card.append(card0004)
full_card.append(card0005)
full_card.append(card0006)
full_card.append(card0007)
full_card.append(card0008)
full_card.append(card0009)
full_card.append(card0010)
full_card.append(card0011)
full_card.append(card0012)
full_card.append(card0013)
full_card.append(card0014)
full_card.append(card0015)
full_card.append(card0016)
full_card.append(card0017)
full_card.append(card0018)
full_card.append(card0019)
full_card.append(card0020)
full_card.append(card0021)
full_card.append(card0022)
full_card.append(card0023)
full_card.append(card0024)
full_card.append(card0025)
full_card.append(card0026)
#陰謀
card0101 = Card('外交官',1,1,4,0,4,2,0,2,0,0,0,0,0,0,0,0,[1,5],1,[0,0,1],[11],[5],[0])
all_card.append(card0101)
card0102 = Card('改良',1,2,1,0,5,1,0,1,0,0,0,0,0,1,1,0,[1],0,[0,0,1],[0],[0],[0])
all_card.append(card0102)
card0103 = Card('隠し通路',1,3,1,0,4,1,0,2,0,0,0,0,0,0,0,0,[1],0,[1,0,1],[5,8],[0],[0])
all_card.append(card0103)
card0104 = Card('仮面舞踏会',1,4,1,0,3,0,0,2,0,0,0,0,0,0,1,0,[1],0,[0,0,1],[18,20],[0],[0])
all_card.append(card0104)
card0105 = Card('共謀者',1,5,1,0,4,1,0,1,2,0,0,0,0,0,0,0,[1],0,[0,0,1],[11],[0],[0])
all_card.append(card0105)
card0106 = Card('交易場',1,6,1,0,5,0,0,0,0,0,0,0,0,1,2,0,[1],0,[0,0,1],[17],[0],[0])
all_card.append(card0106)
card0107 = Card('鉱山の村',1,7,1,0, 4,2,0,1,2,0,0,0,0,0,0,1,[1],0,[1,0,1],[11],[0],[0])
all_card.append(card0107)
card0108 = Card('拷問人',1,8,1,0, 5,0,0,3,0,0,0,0,0,0,0,0,[1,6],0,[0,0,1],[0],[0],[1,6,8,11])
all_card.append(card0108)
card0109 = Card('詐欺師',1,9,1,0,3,0,0,0,2,0,0,0,0,0,0,0,[1,6],0,[0,0,1],[0],[0],[11,12,14,15])
all_card.append(card0109)
card0110 = Card('執事',1,10,1,0,3,0,0,2,2,0,0,0,0,0,2,0,[1],0,[0,0,1],[7],[0],[0])
all_card.append(card0110)
card0111 = Card('男爵',1,11,1,0,4,0,1,0,4,0,0,0,0,1,0,0,[1],0,[0,0,1],[0],[0],[0])
all_card.append(card0111)
card0112 = Card('寵臣',1,12,1,0,5,1,0,4,2,0,0,0,0,0,0,0,[1,6],0,[0,0,1],[1,7],[0],[1,10])
all_card.append(card0112)
card0113 = Card('廷臣',1,13,1,0,5,1,1,0,3,0,0,0,0,1,0,0,[1],0,[0,0,1],[7],[0],[0])
all_card.append(card0113)
card0114 = Card('手先',1,14,1,0,2,1,1,1,1,0,0,0,0,0,0,0,[1],0,[0,0,1],[7],[0],[0])
all_card.append(card0114)
card0115 = Card('鉄工所',1,15,1,0,4,1,0,1,1,0,0,0,0,0,0,0,[1],0,[0,0,1],[7],[0],[0])
all_card.append(card0115)
card0116 = Card('中庭',1,16,1,0,2,0,0,3,0,0,0,0,0,0,0,0,[1],0,[0,0,1],[5,8],[0],[0])
all_card.append(card0116)
card0117 = Card('願いの井戸',1,17,1,0,3,1,0,2,0,0,0,0,0,0,0,0,[1],0,[1,0,1],[3,11],[0],[0])
all_card.append(card0117)
card0118 = Card('橋',1,18,1,0,4,0,1,0,1,0,0,0,0,0,0,0,[1],0,[0,0,1],[9],[0],[0])
all_card.append(card0118)
card0119 = Card('パトロール',1,19,1,0,5,0,0,7,0,0,0,0,0,0,0,0,[1],0,[0,1,0],[3,11,22],[0],[0])
all_card.append(card0119)
card0120 = Card('貧民街',1,20,1,0,3,2,0,2,0,0,0,0,0,0,0,0,[1],0,[0,0,1],[11],[0],[0])
all_card.append(card0120)
card0121 = Card('待ち伏せ',1,21,1,0,2,1,0,0,0,0,0,0,0,1,1,0,[1],0,[1,0,1],[7],[0],[0])
all_card.append(card0121)
card0122 = Card('身代わり',1,22,1,0,5,0,0,0,0,0,0,0,0,1,1,0,[1,6],0,[1,0,1],[21],[0],[11,12])
all_card.append(card0122)
card0123 = Card('貴族',1,23,1,3,6,2,0,3,0,2,0,0,0,0,0,0,[1,3],2,[0,0,1],[7],[9],[0])
all_card.append(card0123)
card0124 = Card('風車',1,24,1,3,4,1,0,1,2,1,0,0,0,0,0,0,[1,3],2,[0,0,1],[1,11],[9],[0])
all_card.append(card0124)
card0125 = Card('ハーレム',1,25,2,3,6,0,0,0,2,2,0,0,0,0,0,0,[2,3],2,[0,1,0],[0],[0],[0])
all_card.append(card0125)
card0126 = Card('公爵',1,26,3,0,5,0,0,0,0,15,0,0,0,0,0,0,[2],1,[0,0,1],[0],[0],[0])
all_card.append(card0126)
full_card.append(card0101)
full_card.append(card0102)
full_card.append(card0103)
full_card.append(card0104)
full_card.append(card0105)
full_card.append(card0106)
full_card.append(card0107)
full_card.append(card0108)
full_card.append(card0109)
full_card.append(card0110)
full_card.append(card0111)
full_card.append(card0112)
full_card.append(card0113)
full_card.append(card0114)
full_card.append(card0115)
full_card.append(card0116)
full_card.append(card0117)
full_card.append(card0118)
full_card.append(card0119)
full_card.append(card0120)
full_card.append(card0121)
full_card.append(card0122)
full_card.append(card0123)
full_card.append(card0124)
full_card.append(card0125)
full_card.append(card0126)
#海辺
card0201 = Card('海賊',2,1,5,4,5,0,0,0,0,0,0,0,0,1,1,0,[1,5,7],2,[0,0,1],[0],[5],[0])
all_card.append(card0201)
card0202 = Card('海の魔女',2,2,5,0,5,0,0,2,0,0,0,0,0,0,0,0,[1,6,7],1,[1,0,1],[1],[0],[11,12])
all_card.append(card0202)
card0203 = Card('漁村',2,3,5,0,3,2,0,0,1,0,0,0,0,0,0,0,[1,7],1,[0,0,1],[0],[0],[0])
all_card.append(card0203)
card0204 = Card('コルセア',2,4,5,0,5,0,0,1,2,0,0,0,0,0,0,0,[1,6,7],1,[0,1,0],[0],[0],[15])
all_card.append(card0204)
card0205 = Card('策士',2,5,5,0,5,1,1,5,0,0,0,0,0,0,0,0,[1,7],1,[0,0,1],[1],[0],[0])
all_card.append(card0205)
card0206 = Card('サル',2,6,5,0,3,0,0,10,0,0,0,0,0,0,0,0,[1,7],1,[0,1,0],[0],[0],[0])
all_card.append(card0206)
card0207 = Card('潮溜り',2,7,5,0,4,1,0,3,0,0,0,0,0,0,0,0,[1,7],1,[1,0,1],[1],[0],[0])
all_card.append(card0207)
card0208 = Card('商船',2,8,5,0,5,0,0,0,2,0,0,0,0,0,0,0,[1,7],1,[0,0,1],[0],[0],[0])
all_card.append(card0208)
card0209 = Card('前哨地',2,9,5,0,5,0,0,0,0,0,0,0,0,0,0,0,[1,7],1,[0,0,1],[14],[0],[0])
all_card.append(card0209)
card0210 = Card('隊商',2,10,5,0,4,1,0,1,0,0,0,0,0,0,0,0,[1,7],1,[0,0,1],[0],[0],[0])
all_card.append(card0210)
card0211 = Card('停泊所',2,11,5,0,2,1,0,1,0,0,0,0,0,0,0,0,[1,7],1,[0,0,1],[16],[0],[0])
all_card.append(card0211)
card0212 = Card('灯台',2,12,5,0,1,1,0,0,1,0,0,0,0,0,0,0,[1,7],1,[0,0,1],[4],[0],[0])
all_card.append(card0212)
card0213 = Card('封鎖',2,13,5,0,4,0,0,0,0,0,0,0,0,1,0,0,[1,6,7],1,[0,0,1],[17],[0],[11])
all_card.append(card0213)
card0214 = Card('船着場',2,14,5,0,5,0,1,2,0,0,0,0,0,0,0,0,[1,7],1,[0,0,1],[0],[0],[0])
all_card.append(card0214)
card0215 = Card('船乗り',2,15,5,0,4,1,0,0,2,0,0,0,0,0,1,0,[1,7],1,[1,0,1],[0],[0],[0])
all_card.append(card0215)
card0216 = Card('海図',2,16,1,0,3,1,0,2,0,0,0,0,0,0,0,0,[1],0,[0,0,1],[11],[0],[0])
all_card.append(card0216)
card0217 = Card('巾着切り',2,17,1,0,4,0,0,0,2,0,0,0,0,0,0,0,[1,6],0,[1,0,1],[0],[0],[1,7,8])
all_card.append(card0217)
card0218 = Card('原住民の村',2,18,1,0,2,2,0,0,0,0,0,0,0,0,0,0,[1],0,[1,0,1],[7,19],[0],[0])
all_card.append(card0218)
card0219 = Card('倉庫',2,19,1,0,3,1,0,3,0,0,0,0,0,0,0,0,[1],0,[0,0,1],[1],[0],[0])
all_card.append(card0219)
card0220 = Card('宝の地図',2,20,1,0,4,0,0,0,0,0,0,0,0,4,1,1,[1],0,[1,0,1],[0],[0],[0])
all_card.append(card0220)
card0221 = Card('バザー',2,21,1,0,5,2,0,1,1,0,0,0,0,0,0,0,[1],0,[0,1,0],[0],[0],[0])
all_card.append(card0221)
card0222 = Card('引揚水夫',2,22,1,0,4,0,1,0,10,0,0,0,0,0,1,0,[1],0,[0,0,1],[0],[0],[0])
all_card.append(card0222)
card0223 = Card('宝物庫',2,23,1,0,5,1,0,1,1,0,0,0,0,0,0,0,[1],0,[0,0,1],[35],[0],[0])
all_card.append(card0223)
card0224 = Card('密輸人',2,24,1,0,3,0,0,0,0,0,0,0,0,1,0,0,[1],0,[0,0,1],[0],[0],[0])
all_card.append(card0224)
card0225 = Card('見張り',2,25,1,0,3,1,0,0,0,0,0,0,0,0,1,0,[1],0,[1,0,1],[2,3],[0],[0])
all_card.append(card0225)
card0226 = Card('島',2,26,1,3,4,0,0,0,0,0,0,0,0,0,0,0,[1,3],2,[0,0,1],[19],[9],[0])
all_card.append(card0226)
card0227 = Card('アストロラーベ',2,27,2,5,3,0,1,0,1,0,0,0,0,0,0,0,[2,7],2,[0,1,0],[0],[0],[0])
all_card.append(card0227)
full_card.append(card0201)
full_card.append(card0202)
full_card.append(card0203)
full_card.append(card0204)
full_card.append(card0205)
full_card.append(card0206)
full_card.append(card0207)
full_card.append(card0208)
full_card.append(card0209)
full_card.append(card0210)
full_card.append(card0211)
full_card.append(card0212)
full_card.append(card0213)
full_card.append(card0214)
full_card.append(card0215)
full_card.append(card0216)
full_card.append(card0217)
full_card.append(card0218)
full_card.append(card0219)
full_card.append(card0220)
full_card.append(card0221)
full_card.append(card0222)
full_card.append(card0223)
full_card.append(card0224)
full_card.append(card0225)
full_card.append(card0226)
full_card.append(card0227)
#錬金術
card0301 = Card('薬師',3,1,1,0,2,1,0,5,0,0,0,0,0,0,0,0,[1],0,[0,0,1],[3,11,22,37],[0],[0])
all_card.append(card0301)
card0302 = Card('ゴーレム',3,2,1,0,4,0,0,0,0,0,0,0,0,0,0,0,[1],0,[0,1,0],[2,6,37],[0],[0])
all_card.append(card0302)
card0303 = Card('支配',3,3,1,0,6,0,0,0,0,0,0,0,0,1,0,0,[1],0,[0,0,1],[14,37],[0],[0])
all_card.append(card0303)
card0304 = Card('大学',3,4,1,0,2,2,0,0,0,0,0,0,0,1,0,0,[1],0,[0,0,1],[37],[0],[0])
all_card.append(card0304)
card0305 = Card('使い魔',3,5,1,0,3,1,0,1,0,0,0,0,0,0,0,0,[1],0,[1,0,1],[37],[0],[11,12])
all_card.append(card0305)
card0306 = Card('弟子',3,6,1,0,5,1,0,10,0,0,0,0,0,0,1,0,[1],0,[0,0,1],[11],[0],[0])
all_card.append(card0306)
card0307 = Card('念視の泉',3,7,1,0,2,1,0,10,0,0,0,0,0,0,0,0,[1],0,[1,0,1],[2,3,37],[0],[16])
all_card.append(card0307)
card0308 = Card('変成',3,8,1,0,0,0,0,0,0,0,0,0,0,1,1,0,[1],0,[0,0,1],[7,37],[0],[0])
all_card.append(card0308)
card0309 = Card('薬草商',3,9,1,0,2,0,1,0,1,0,0,0,0,0,0,0,[1],0,[0,0,1],[3],[0],[0])
all_card.append(card0309)
card0310 = Card('錬金術師',3,10,1,0,3,1,0,2,0,0,0,0,0,0,0,0,[1],0,[0,0,1],[3,37],[0],[0])
all_card.append(card0310)
card0311 = Card('賢者の石',3,11,2,0,3,0,0,0,10,0,0,0,0,0,0,0,[2],1,[1,0,1],[37],[0],[0])
all_card.append(card0311)
card0312 = Card('ブドウ園',3,12,3,0,0,0,0,0,0,15,0,0,0,0,0,0,[3],1,[0,1,1],[37],[0],[0])
all_card.append(card0312)
full_card.append(card0301)
full_card.append(card0302)
full_card.append(card0303)
full_card.append(card0304)
full_card.append(card0305)
full_card.append(card0306)
full_card.append(card0307)
full_card.append(card0308)
full_card.append(card0309)
full_card.append(card0310)
full_card.append(card0311)
full_card.append(card0312)
#繁栄
card0400a = Card('白金貨',0,0,2,0,9,0,0,0,5,0,0,0,0,0,0,0,[2],1,[0,0,1],[0],[0],[0])
card0400b = Card('植民地',0,0,3,0,11,0,0,0,0,10,0,0,0,0,0,0,[3],1,[0,0,1],[0],[0],[0])
card0401 = Card('書記',4,1,4,0,4,0,0,0,2,0,0,0,0,0,0,0,[1,5,6],1,[0,0,1],[0],[5],[1,9])
all_card.append(card0401)
card0402 = Card('望楼',4,2,4,0,3,0,0,6,0,0,0,0,0,0,1,0,[1,5],1,[0,0,1],[0],[5],[0])
all_card.append(card0402)
card0403 = Card('拡張',4,3,1,0,7,0,0,0,0,0,0,0,0,1,1,0,[1],0,[0,0,1],[0],[0],[0])
all_card.append(card0403)
card0404 = Card('記念碑',4,4,1,0,4,0,0,0,2,1,0,0,0,0,0,0,[1],0,[0,0,1],[0],[0],[0])
all_card.append(card0404)
card0405 = Card('宮廷',4,5,1,0,7,0,0,0,0,0,0,0,0,0,0,0,[1],0,[0,0,1],[6,31],[0],[0])
all_card.append(card0405)
card0406 = Card('行商人',4,6,1,0,8,1,0,1,1,0,0,0,0,0,0,0,[1],0,[0,0,1],[0],[11],[0])
all_card.append(card0406)
card0407 = Card('司教',4,7,1,0,4,0,0,0,1,15,0,0,0,0,1,0,[1],0,[0,0,1],[5,20],[0],[0])
all_card.append(card0407)
card0408 = Card('造幣所',4,8,1,0,5,0,0,0,0,0,0,0,0,1,10,0,[1],0,[0,0,1],[0],[1],[0])
all_card.append(card0408)
card0409 = Card('大市場',4,9,1,0,6,1,1,1,2,0,0,0,0,0,0,0,[1],0,[0,0,1],[0],[1],[0])
all_card.append(card0409)
card0410 = Card('大衆',4,10,1,0,5,0,0,3,0,0,0,0,0,0,0,0,[1,6],0,[0,0,1],[0],[0],[16])
all_card.append(card0410)
card0411 = Card('鍛造',4,11,1,0,7,0,0,0,0,0,0,0,0,1,10,0,[1],0,[0,0,1],[0],[0],[0])
all_card.append(card0411)
card0412 = Card('都市',4,12,1,0,5,2,1,1,1,0,0,0,0,0,0,0,[1],0,[0,0,1],[11],[0],[0])
all_card.append(card0412)
card0413 = Card('保管庫',4,13,1,0,5,0,0,2,10,0,0,0,0,0,0,0,[1],0,[0,0,1],[0],[0],[0])
all_card.append(card0413)
card0414 = Card('山師',4,14,1,0,5,0,0,0,3,0,0,0,0,0,0,0,[1,6],0,[0,0,1],[0],[0],[11,12])
all_card.append(card0414)
card0415 = Card('有力者',4,15,1,0,5,0,0,10,0,0,0,0,0,0,0,0,[1],0,[0,0,1],[0],[0],[0])
all_card.append(card0415)
card0416 = Card('労働者の村',4,16,1,0,4,2,1,1,0,0,0,0,0,0,0,0,[1],0,[1,0,1],[0],[0],[0])
all_card.append(card0416)
card0417 = Card('石切場',4,17,2,0,4,0,0,0,1,0,0,0,0,0,0,0,[2],1,[0,0,1],[9],[0],[0])
all_card.append(card0417)
card0418 = Card('隠し財産',4,18,2,0,6,0,0,0,2,0,0,0,0,1,0,0,[2],1,[1,0,1],[11],[0],[0])
all_card.append(card0418)
card0419 = Card('金床',4,19,2,0,3,0,0,0,1,0,0,0,0,1,0,0,[2],1,[0,0,1],[0],[0],[0])
all_card.append(card0419)
card0420 = Card('銀行',4,20,2,0,7,0,0,0,10,0,0,0,0,0,0,0,[2],1,[0,0,1],[0],[0],[0])
all_card.append(card0420)
card0421 = Card('軍用金',4,21,2,0,5,0,0,0,0,0,0,0,0,1,0,0,[2],1,[0,0,1],[0],[0],[0])
all_card.append(card0421)
card0422 = Card('収集品',4,22,2,0,5,0,1,0,2,1,0,0,0,0,0,0,[2],1,[0,0,1],[11],[0],[0])
all_card.append(card0422)
card0423 = Card('出資',4,23,2,0,4,0,0,0,1,15,0,0,0,0,1,1,[2],1,[0,0,1],[7],[0],[0])
all_card.append(card0423)
card0424 = Card('水晶球',4,24,2,0,5,0,0,0,1,0,0,0,0,0,1,0,[2],1,[0,0,1],[2,6],[0],[0])
all_card.append(card0424)
card0425 = Card('ティアラ',4,25,2,0,4,0,1,0,0,0,0,0,0,0,0,0,[2],1,[0,1,0],[6,21,31],[0],[0])
all_card.append(card0425)
full_card.append(card0400a)
full_card.append(card0400b)
full_card.append(card0401)
full_card.append(card0402)
full_card.append(card0403)
full_card.append(card0404)
full_card.append(card0405)
full_card.append(card0406)
full_card.append(card0407)
full_card.append(card0408)
full_card.append(card0409)
full_card.append(card0410)
full_card.append(card0411)
full_card.append(card0412)
full_card.append(card0413)
full_card.append(card0414)
full_card.append(card0415)
full_card.append(card0416)
full_card.append(card0417)
full_card.append(card0418)
full_card.append(card0419)
full_card.append(card0420)
full_card.append(card0421)
full_card.append(card0422)
full_card.append(card0423)
full_card.append(card0424)
full_card.append(card0425)
#収穫祭
card0501 = Card('馬商人',5,1,4,0,4,0,1,1,3,0,0,0,0,0,0,0,[1,5],1,[0,0,1],[1],[5],[0])
all_card.append(card0501)
card0502 = Card('移動動物園',5,2,1,0,3,1,0,3,0,0,0,0,0,0,0,0,[1],0,[0,0,1],[11],[0],[0])
all_card.append(card0502)
card0503 = Card('占い師',5,3,1,0,3,0,0,0,2,0,0,0,0,0,0,0,[1,6],0,[1,0,1],[0],[0],[16])
all_card.append(card0503)
card0504 = Card('再建',5,4,1,0,4,0,0,0,0,0,0,0,0,2,2,0,[1],0,[0,0,1],[0],[0],[0])
all_card.append(card0504)
card0505 = Card('収穫',5,5,1,0,5,0,0,0,4,0,0,0,0,0,0,0,[1],0,[0,0,1],[2,11],[0],[0])
all_card.append(card0505)
card0506 = Card('狩猟団',5,6,1,0,5,1,0,2,0,0,0,0,0,0,0,0,[1],0,[0,0,1],[22],[0],[0])
all_card.append(card0506)
card0507 = Card('村落',5,7,1,0,3,2,1,1,0,0,0,0,0,0,0,0,[1],0,[0,0,1],[1,11],[0],[0])
all_card.append(card0507)
card0508 = Card('道化師',5,8,1,0,5,0,0,0,2,0,0,0,0,3,0,0,[1,6],0,[0,0,1],[0],[0],[11,12,14,16])
all_card.append(card0508)
card0509 = Card('農村',5,9,1,0,4,2,0,1,0,0,0,0,0,0,0,0,[1],0,[0,0,1],[2,22],[0],[0])
all_card.append(card0509)
card0510 = Card('馬上槍試合',5,10,1,0,4,1,0,1,1,0,0,0,0,1,0,0,[1],0,[0,0,1],[11,13,21],[0],[0])
card0510a = Card('王女',5,10,1,0,0,0,1,0,0,0,0,0,0,0,0,0,[1,9],0,[0,0,1],[9],[0],[0])
card0510b = Card('金貨袋',5,10,2,0,0,1,0,0,0,0,0,0,0,1,0,0,[1,9],0,[0,0,1],[21],[0],[0])
card0510c = Card('名馬',5,10,1,0,0,2,0,2,2,0,0,0,0,4,0,0,[1,9],0,[0,0,1],[7,23],[0],[0])
card0510d = Card('郎党',5,10,1,0,0,0,0,2,0,0,0,0,0,1,0,0,[1,6,9],0,[0,0,1],[0],[0],[1,3,11,12])
card0510e = Card('王冠',5,10,2,0,0,0,0,0,10,0,0,0,0,0,0,0,[2,9],1,[0,0,1],[0],[0],[0])
all_card.append(card0510)
card0511 = Card('魔女娘',5,11,1,0,4,0,0,2,0,0,0,0,0,0,0,0,[1,6],0,[0,0,1],[1],[8],[11,12])
all_card.append(card0511)
card0512 = Card('豊穣の角笛',5,12,2,0,5,0,0,0,0,0,0,0,0,1,0,1,[2],1,[1,0,1],[0],[0],[0])
all_card.append(card0512)
card0513 = Card('品評会',5,13,3,0,6,0,0,0,0,15,0,0,0,0,0,0,[3],1,[0,0,1],[0],[0],[0])
all_card.append(card0513)
full_card.append(card0501)
full_card.append(card0502)
full_card.append(card0503)
full_card.append(card0504)
full_card.append(card0505)
full_card.append(card0506)
full_card.append(card0507)
full_card.append(card0508)
full_card.append(card0509)
full_card.append(card0510)
full_card.append(card0510a)
full_card.append(card0510b)
full_card.append(card0510c)
full_card.append(card0510d)
full_card.append(card0510e)
full_card.append(card0511)
full_card.append(card0512)
full_card.append(card0513)
#異郷
card0601 = Card('交易人',6,1,4,0,4,0,0,0,0,0,0,0,0,10,1,0,[1,5],1,[0,0,1],[0],[5],[0])
all_card.append(card0601)
card0602 = Card('織工',6,2,4,0,4,0,0,0,0,0,0,0,0,1,0,0,[1,5],1,[0,0,1],[0],[5],[0])
all_card.append(card0602)
card0603 = Card('進路',6,3,4,0,4,1,0,1,0,0,0,0,0,0,0,0,[1,5],1,[0,0,1],[0],[1,2,3,5],[0])
all_card.append(card0603)
card0604 = Card('番犬',6,4,4,0,3,0,0,4,0,0,0,0,0,0,0,0,[1,5],1,[0,0,1],[11],[5],[0])
all_card.append(card0604)
card0605 = Card('オアシス',6,5,1,0,3,1,0,1,1,0,0,0,0,0,0,0,[1],0,[0,1,0],[1],[0],[0])
all_card.append(card0605)
card0606 = Card('街道',6,6,1,0,5,1,0,1,0,0,0,0,0,0,0,0,[1],0,[0,0,1],[9],[0],[0])
all_card.append(card0606)
card0607 = Card('開発',6,7,1,0,3,0,0,0,0,0,0,0,0,2,1,0,[1],0,[0,0,1],[21],[0],[0])
all_card.append(card0607)
card0608 = Card('画策',6,8,1,0,3,1,0,1,0,0,0,0,0,0,0,0,[1],0,[0,0,1],[3],[0],[0])
all_card.append(card0608)
card0609 = Card('厩舎',6,9,1,0,5,1,0,3,0,0,0,0,0,0,0,0,[1],0,[0,0,1],[1,11],[0],[0])
all_card.append(card0609)
card0610 = Card('狂戦士',6,10,1,0,5,0,0,0,0,0,0,0,0,1,0,0,[1,6],0,[0,0,1],[0],[1,2],[1,3])
all_card.append(card0610)
card0611 = Card('岐路',6,11,1,0,2,3,0,10,0,0,0,0,0,0,0,0,[1],0,[0,0,1],[11],[0],[0])
all_card.append(card0611)
card0612 = Card('車大工',6,12,1,0,5,1,0,1,0,0,0,0,0,1,0,0,[1],0,[0,0,1],[1],[0],[0])
all_card.append(card0612)
card0613 = Card('香辛料理人',6,13,1,0,4,1,1,2,2,0,0,0,0,0,1,0,[1],0,[0,0,1],[7],[0],[0])
all_card.append(card0613)
card0614 = Card('国境の村',6,14,1,0,6,2,0,1,0,0,0,0,0,1,0,0,[1],0,[1,0,1],[0],[1,2],[0])
all_card.append(card0614)
card0615 = Card('スーク',6,15,1,0,5,0,1,0,7,0,0,0,0,0,2,0,[1],0,[0,1,0],[11],[1,2],[0])
all_card.append(card0615)
card0616 = Card('地図職人',6,16,1,0,5,1,0,1,0,0,0,0,0,0,0,0,[1],0,[0,0,1],[2,3],[0],[0])
all_card.append(card0616)
card0617 = Card('値切り屋',6,17,1,0,5,0,0,0,2,0,0,0,0,1,0,0,[1],0,[1,0,1],[0],[0],[0])
all_card.append(card0617)
card0618 = Card('辺境伯',6,18,1,0,5,0,1,3,0,0,0,0,0,0,0,0,[1,6],0,[0,0,1],[20],[0],[1,3])
all_card.append(card0618)
card0619 = Card('魔女の小屋',6,19,1,0,5,0,0,4,0,0,0,0,0,0,0,0,[1,6],0,[1,0,1],[1,11],[0],[11,12])
all_card.append(card0619)
card0620 = Card('宿屋',6,20,1,0,5,2,0,2,0,0,0,0,0,0,0,0,[1],0,[0,0,1],[1],[1,2],[0])
all_card.append(card0620)
card0621 = Card('遊牧民',6,21,1,0,4,0,1,0,2,0,0,0,0,0,0,0,[1],0,[0,0,1],[0],[1,2,3],[0])
all_card.append(card0621)
card0622 = Card('よろずや',6,22,1,0,4,0,0,5,0,0,0,0,0,0,1,0,[1],0,[1,0,0],[2,3,11],[0],[0])
all_card.append(card0622)
card0623 = Card('愚者の黄金',6,23,4,2,2,0,0,0,4,0,0,0,0,0,0,0,[2,5],2,[1,0,1],[11,21],[5],[0])
all_card.append(card0623)
card0624 = Card('大釜',6,24,2,0,5,0,1,0,2,0,0,0,0,0,0,0,[2,6],1,[0,0,1],[11],[0],[11,12])
all_card.append(card0624)
card0625 = Card('坑道',6,25,4,3,3,0,0,0,0,2,0,0,0,1,0,0,[3,5],2,[0,0,1],[0],[5],[0])
all_card.append(card0625)
card0626 = Card('農地',6,26,3,0,6,0,0,0,0,2,0,0,0,1,1,0,[3],1,[0,0,1],[0],[1,2],[0])
all_card.append(card0626)
full_card.append(card0601)
full_card.append(card0602)
full_card.append(card0603)
full_card.append(card0604)
full_card.append(card0605)
full_card.append(card0606)
full_card.append(card0607)
full_card.append(card0608)
full_card.append(card0609)
full_card.append(card0610)
full_card.append(card0611)
full_card.append(card0612)
full_card.append(card0613)
full_card.append(card0614)
full_card.append(card0615)
full_card.append(card0616)
full_card.append(card0617)
full_card.append(card0618)
full_card.append(card0619)
full_card.append(card0620)
full_card.append(card0621)
full_card.append(card0622)
full_card.append(card0623)
full_card.append(card0624)
full_card.append(card0625)
full_card.append(card0626)
#暗黒時代
card0700a = Card('廃村',7,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,[1,10],1,[0,0,1],[0],[0],[0])
card0700b = Card('市場跡地',7,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,[1,10],1,[0,0,1],[0],[0],[0])
card0700c = Card('図書館跡地',7,1,1,0,0,0,0,1,0,0,0,0,0,0,0,0,[1,10],1,[0,0,1],[0],[0],[0])
card0700d = Card('廃坑',7,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,[1,10],1,[0,0,1],[0],[0],[0])
card0700e = Card('生存者',7,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,[1,10],1,[0,0,1],[2,3],[0],[0])
card0700f = Card('共同墓地',7,0,1,0,1,2,0,0,0,0,0,0,0,0,0,0,[1,11],2,[0,0,1],[0],[0],[0])
card0700g = Card('草茂る屋敷',7,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,[3,11],2,[1,0,1],[0],[3],[0])
card0700h = Card('納屋',7,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,[5,11],2,[0,0,1],[0],[0],[0])
card0701 = Card('青空市場',7,1,4,0,3,1,1,1,0,0,0,0,0,1,0,0,[1,5],1,[0,0,1],[0],[5],[0])
all_card.append(card0701)
card0702 = Card('物乞い',7,2,4,0,2,0,0,0,0,0,0,0,0,3,0,0,[1,5],1,[1,0,1],[17,21],[5],[0])
all_card.append(card0702)
card0703 = Card('隠遁者',7,3,1,0,3,0,0,0,0,0,0,0,0,1,1,0,[1],0,[0,0,1],[13],[0],[0])
card0703a = Card('狂人',7,3,1,0,0,2,0,10,0,0,0,0,0,0,0,0,[1],0,[0,0,1],[24],[0],[0])
all_card.append(card0703)
card0704 = Card('金物商',7,4,1,0,4,2,0,2,1,0,0,0,0,0,0,0,[1],0,[0,0,1],[2,3,7,11],[0],[0])
all_card.append(card0704)
card0705 = Card('狩場',7,5,1,0,6,0,0,4,0,0,0,0,0,3,0,0,[1],0,[0,0,1],[0],[3],[0])
all_card.append(card0705)
card0706 = Card('騎士',7,6,1,0,5,0,0,0,0,0,0,0,0,0,0,0,[1],0,[0,0,1],[12],[0],[0])
card0706a = Card('デイム・アンナ',7,6,1,0,3,2,0,1,0,0,0,0,0,0,2,1,[1,6,13],0,[0,1,0],[12],[0],[15,16])
card0706b = Card('デイム・ジョセフィーヌ',7,6,1,3,5,0,0,0,0,2,0,0,0,0,0,1,[1,6,13],2,[0,1,0],[12],[9],[15,16])
card0706c = Card('デイム・シルビア',7,6,1,0,5,2,0,0,0,0,0,0,0,0,0,1,[1,6,13],2,[0,1,0],[12],[0],[15,16])
card0706d = Card('デイム・ナタリー',7,6,1,0,5,0,0,0,0,0,0,0,0,1,0,1,[1,6,13],2,[0,1,0],[12],[0],[15,16])
card0706e = Card('デイム・モリー',7,6,1,0,5,0,0,0,2,0,0,0,0,0,0,1,[1,6,13],2,[0,1,0],[12],[0],[15,16])
card0706f = Card('サー・ヴァンデル',7,6,1,0,5,0,0,0,0,0,0,0,0,1,0,1,[1,6,13],2,[0,1,0],[12],[3],[15,16])
card0706g = Card('サー・デストリー',7,6,1,0,5,0,0,2,0,0,0,0,0,0,0,1,[1,6,13],2,[0,1,0],[12],[0],[15,16])
card0706h = Card('サー・ベイリー',7,6,1,0,5,1,0,1,0,0,0,0,0,0,0,1,[1,6,13],2,[0,1,0],[12],[0],[15,16])
card0706i = Card('サー・マーチン',7,6,1,0,5,0,2,0,0,0,0,0,0,0,0,1,[1,6,13],2,[0,1,0],[12],[0],[15,16])
card0706j = Card('サー・マイケル',7,6,1,0,5,0,0,0,0,0,0,0,0,0,0,1,[1,6,13],2,[0,1,0],[12],[0],[1,3,15,16])
all_card.append(card0706)
card0707 = Card('救貧院',7,7,1,0,1,0,0,0,4,0,0,0,0,0,0,0,[1],0,[0,0,1],[11],[0],[0])
all_card.append(card0707)
card0708 = Card('狂信者',7,8,1,0,5,0,0,2,0,0,0,0,0,0,0,0,[1,6,12],0,[0,0,1],[6],[3],[13])
all_card.append(card0708)
card0709 = Card('吟遊詩人',7,9,1,0,4,2,0,1,0,0,0,0,0,0,0,0,[1],0,[0,0,1],[2,3],[0],[0])
all_card.append(card0709)
card0710 = Card('屑屋',7,10,1,0,5,1,0,1,1,0,0,0,0,0,1,0,[1],0,[0,0,1],[0],[0],[0])
all_card.append(card0710)
card0711 = Card('賢者',7,11,1,0,3,1,0,1,0,0,0,0,0,0,0,0,[1],0,[0,0,1],[2,22],[0],[0])
all_card.append(card0711)
card0712 = Card('行進',7,12,1,0,4,0,0,0,0,0,0,0,0,1,1,0,[1],0,[0,0,1],[6,31],[0],[0])
all_card.append(card0712)
card0713 = Card('ゴミあさり',7,13,1,0,4,0,0,0,2,0,0,0,0,0,0,0,[1],0,[1,1,0],[3,23],[0],[0])
all_card.append(card0713)
card0714 = Card('採集者',7,14,1,0,3,1,1,0,10,0,0,0,0,0,1,0,[1],0,[0,0,1],[0],[0],[0])
all_card.append(card0714)
card0715 = Card('祭壇',7,15,1,0,6,0,0,0,0,0,0,0,0,1,1,0,[1],0,[0,0,1],[0],[0],[0])
all_card.append(card0715)
card0716 = Card('山賊の宿営地',7,16,1,0,5,2,0,1,0,0,0,0,0,1,0,0,[1],0,[1,0,1],[13],[0],[0])
card0716a = Card('略奪品',7,16,2,0,0,0,0,0,3,0,0,0,0,0,0,0,[2],1,[0,0,1],[24],[0],[0])
all_card.append(card0716)
card0717 = Card('死の荷車',7,17,1,0,4,0,0,0,5,0,0,0,0,0,1,1,[1,12],0,[1,0,1],[13],[1,2],[0])
all_card.append(card0717)
card0718 = Card('襲撃者',7,18,1,0,4,0,0,0,0,0,0,0,0,1,0,0,[1,6,12],0,[0,0,1],[13],[0],[13])
all_card.append(card0718)
card0719 = Card('従者',7,19,1,0,2,2,2,0,1,0,0,0,0,1,0,0,[1],0,[0,0,1],[7],[3],[0])
all_card.append(card0719)
card0720 = Card('城塞',7,20,1,0,4,2,0,1,0,0,0,0,0,0,0,0,[1],0,[0,0,1],[0],[3],[0])
all_card.append(card0720)
card0721 = Card('建て直し',7,21,1,0,5,1,0,0,0,0,0,0,0,1,1,0,[1],0,[1,0,1],[2],[0],[0])
all_card.append(card0721)
card0722 = Card('地下墓所',7,22,1,0,5,0,0,3,0,0,0,0,0,0,0,0,[1],0,[0,0,1],[2,7,22],[3],[0])
all_card.append(card0722)
card0723 = Card('盗賊',7,23,1,0,5,0,0,0,2,0,0,0,0,1,0,0,[1,6],0,[0,0,1],[0],[0],[15,16])
all_card.append(card0723)
card0724 = Card('ネズミ',7,24,1,0,4,1,0,1,0,0,0,0,0,1,1,0,[1],0,[0,1,0],[0],[3],[0])
all_card.append(card0724)
card0725 = Card('墓暴き',7,25,1,0,5,0,0,0,0,0,0,0,0,1,1,0,[1],0,[1,0,1],[7,21],[0],[0])
all_card.append(card0725)
card0726 = Card('伯爵',7,26,1,0,5,0,0,0,3,0,0,0,0,1,10,0,[1],0,[0,0,1],[1,5,7,8],[0],[0])
all_card.append(card0726)
card0727 = Card('はみだし者',7,27,1,0,5,0,0,0,0,0,0,0,0,0,0,0,[1,14],0,[1,0,1],[6],[0],[0])
all_card.append(card0727)
card0728 = Card('秘術師',7,28,1,0,5,1,0,1,2,0,0,0,0,0,0,0,[1],0,[0,0,1],[3,11],[0],[0])
all_card.append(card0728)
card0729 = Card('武器庫',7,29,1,0,4,0,0,0,0,0,0,0,0,1,0,0,[1],0,[0,0,1],[21],[0],[0])
all_card.append(card0729)
card0730 = Card('浮浪児',7,30,1,0,3,1,0,1,0,0,0,0,0,0,0,0,[1,6],0,[0,0,1],[13],[0],[1,4])
card0730a = Card('傭兵',7,30,1,0,0,0,0,2,2,0,0,0,0,0,2,0,[1],0,[0,0,1],[0],[0],[1,3])
all_card.append(card0730)
card0731 = Card('浮浪者',7,31,1,0,2,1,0,2,0,0,0,0,0,0,0,0,[1],0,[0,0,1],[11,22],[0],[0])
all_card.append(card0731)
card0732 = Card('物置',7,32,1,0,3,0,1,10,10,0,0,0,0,0,0,0,[1],0,[0,0,1],[1],[0],[0])
all_card.append(card0732)
card0733 = Card('略奪',7,33,1,0,5,0,0,0,0,0,0,0,0,2,0,1,[1,6],0,[0,0,1],[13],[0],[1,5,7])
all_card.append(card0733)
card0734 = Card('偽造通貨',7,34,1,0,5,0,1,0,1,0,0,0,0,0,1,0,[2],1,[0,0,1],[6],[0],[0])
all_card.append(card0734)
card0735 = Card('封土',7,35,1,0,4,0,0,0,0,15,0,0,0,3,0,0,[3],1,[0,0,1],[0],[3],[0])
all_card.append(card0735)
full_card.append(card0700a)
full_card.append(card0700b)
full_card.append(card0700c)
full_card.append(card0700d)
full_card.append(card0700e)
full_card.append(card0700f)
full_card.append(card0700g)
full_card.append(card0700h)
full_card.append(card0701)
full_card.append(card0702)
full_card.append(card0703)
full_card.append(card0703a)
full_card.append(card0704)
full_card.append(card0705)
full_card.append(card0706a)
full_card.append(card0706b)
full_card.append(card0706c)
full_card.append(card0706d)
full_card.append(card0706e)
full_card.append(card0706f)
full_card.append(card0706g)
full_card.append(card0706h)
full_card.append(card0706i)
full_card.append(card0706j)
full_card.append(card0707)
full_card.append(card0708)
full_card.append(card0709)
full_card.append(card0710)
full_card.append(card0711)
full_card.append(card0712)
full_card.append(card0713)
full_card.append(card0714)
full_card.append(card0715)
full_card.append(card0716)
full_card.append(card0716a)
full_card.append(card0717)
full_card.append(card0718)
full_card.append(card0719)
full_card.append(card0720)
full_card.append(card0721)
full_card.append(card0722)
full_card.append(card0723)
full_card.append(card0724)
full_card.append(card0725)
full_card.append(card0726)
full_card.append(card0727)
full_card.append(card0728)
full_card.append(card0729)
full_card.append(card0730)
full_card.append(card0730a)
full_card.append(card0731)
full_card.append(card0732)
full_card.append(card0733)
full_card.append(card0734)
full_card.append(card0735)
#ギルド
card0801 = Card('石工',8,1,1,0,2,0,0,0,0,0,0,0,0,2,1,0,[1],0,[0,0,1],[0],[4],[0])
all_card.append(card0801)
card0802 = Card('医者',8,2,1,0,3,0,0,0,0,0,0,0,0,0,10,0,[1],0,[0,0,1],[2,3],[4],[0])
all_card.append(card0802)
card0803 = Card('収税吏',8,3,1,0,4,0,0,0,0,0,0,0,0,1,1,0,[1,6],0,[0,0,1],[21],[0],[1,7])
all_card.append(card0803)
card0804 = Card('熟練工',8,4,1,0,5,0,0,3,0,0,0,0,0,0,0,0,[1],0,[0,0,1],[2,22],[0],[0])
all_card.append(card0804)
card0805 = Card('商人ギルド',8,5,1,0,5,0,1,0,1,0,10,0,0,0,0,0,[1],0,[0,1,1],[19],[0],[0])
all_card.append(card0805)
card0806 = Card('助言者',8,6,1,0,4,1,0,2,0,0,0,0,0,0,0,0,[1],0,[0,0,1],[2,22],[0],[0])
all_card.append(card0806)
card0807 = Card('伝令官',8,7,1,0,4,1,0,1,0,0,0,0,0,0,0,0,[1],0,[0,0,1],[3,6],[4],[0])
all_card.append(card0807)
card0808 = Card('肉屋',8,8,1,0,5,0,0,0,0,0,2,0,0,1,1,0,[1],0,[0,0,1],[19],[0],[0])
all_card.append(card0808)
card0809 = Card('パン屋',8,9,1,0,5,1,0,1,0,0,1,0,0,0,0,0,[1],0,[0,1,1],[19],[8],[0])
all_card.append(card0809)
card0810 = Card('広場',8,10,1,0,4,2,0,1,0,0,1,0,0,0,0,0,[1],0,[0,0,1],[1,11,19],[0],[0])
all_card.append(card0810)
card0811 = Card('予言者',8,11,1,0,5,0,0,0,0,0,0,0,0,1,0,0,[1,6],0,[0,0,1],[5,20],[0],[11,12])
all_card.append(card0811)
card0812 = Card('蝋燭職人',8,12,1,0,2,1,1,0,0,0,1,0,0,0,0,0,[1],0,[0,0,1],[19],[0],[0])
all_card.append(card0812)
card0813 = Card('名品',8,13,2,0,3,0,0,0,1,0,0,0,0,10,0,0,[2],1,[0,0,1],[0],[4],[0])
all_card.append(card0813)
full_card.append(card0801)
full_card.append(card0802)
full_card.append(card0803)
full_card.append(card0804)
full_card.append(card0805)
full_card.append(card0806)
full_card.append(card0807)
full_card.append(card0808)
full_card.append(card0809)
full_card.append(card0810)
full_card.append(card0811)
full_card.append(card0812)
full_card.append(card0813)
#冒険
card0901 = Card('隊商の護衛',9,1,5,4,3,1,0,1,1,0,0,0,0,0,0,0,[1,5,7],2,[1,0,1],[0],[5],[0])
all_card.append(card0901)
card0902 = Card('地下牢',9,2,5,0,3,1,0,2,0,0,0,0,0,0,0,0,[1,7],1,[0,0,1],[1],[0],[0])
all_card.append(card0902)
card0903 = Card('道具',9,3,5,0,3,0,0,2,0,0,0,0,0,0,0,0,[1,7],1,[0,0,1],[16],[0],[0])
all_card.append(card0903)
card0904 = Card('沼の妖婆',9,4,5,0,5,0,0,0,3,0,0,0,0,0,0,0,[1,6,7],1,[1,0,1],[0],[0],[11])
all_card.append(card0904)
card0905 = Card('呪いの森',9,5,5,0,5,0,0,3,0,0,0,0,0,0,0,0,[1,6,7],1,[1,0,1],[0],[0],[1,9])
all_card.append(card0905)
card0906 = Card('橋の下のトロル',9,6,5,0,5,0,1,0,0,0,0,0,0,0,0,0,[1,6,7],1,[1,1,1],[9,25],[0],[17])
all_card.append(card0906)
card0907 = Card('魔除け',9,7,5,0,3,0,0,0,1,0,0,0,0,1,1,0,[1,7],1,[1,0,1],[7],[0],[0])
all_card.append(card0907)
card0908 = Card('雇人',9,8,5,0,6,0,0,1,0,0,0,0,0,0,0,0,[1,7],1,[0,0,1],[0],[0],[0])
all_card.append(card0908)
card0909 = Card('案内人',9,9,6,0,3,1,0,1,0,0,0,0,0,0,0,0,[1,15],1,[0,0,1],[1,19],[0],[0])
all_card.append(card0909)
card0910 = Card('御料車',9,10,6,0,5,1,0,0,0,0,0,0,0,0,0,0,[1,15],1,[0,0,1],[6,19,31],[0],[0])
all_card.append(card0910)
card0911 = Card('鼠取り',9,11,6,0,2,1,0,1,0,0,0,0,0,0,1,0,[1,15],1,[1,0,1],[19],[0],[0])
all_card.append(card0911)
card0912 = Card('複製',9,12,6,0,4,0,0,0,0,0,0,0,0,1,0,0,[1,15],1,[0,0,1],[19],[0],[0])
all_card.append(card0912)
card0913 = Card('変容',9,13,6,0,4,1,0,0,0,0,0,0,0,1,1,0,[1,15],1,[0,0,1],[17,19],[0],[0])
all_card.append(card0913)
card0914 = Card('ワイン商',9,14,6,0,5,0,1,0,4,0,0,0,0,0,0,0,[1,15],1,[0,1,1],[19],[0],[0])
all_card.append(card0914)
card0915 = Card('遠隔地',9,15,6,3,5,0,0,0,0,4,0,0,0,0,0,0,[1,3,15],2,[0,0,1],[11,19],[0],[0])
all_card.append(card0915)
card0916 = Card('騎士見習い',9,16,1,0, 2,1,0,1,0,0,0,0,0,0,0,0,[1,16],0,[1,0,1],[13,18],[10],[0])
card0916a = Card('トレジャーハンター',9,16,1,0, 3,1,0,0,1,0,0,0,0,10,0,0,[1,16],0,[0,1,0],[18],[10],[0])
card0916b = Card('ウォリアー',9,16,1,0, 4,0,0,2,0,0,0,0,0,0,0,0,[1,6,16],0,[0,1,0],[18],[10],[15,16])
card0916c = Card('ヒーロー',9,16,1,0, 5,0,0,0,2,0,0,0,0,1,0,0,[1,16],0,[0,1,0],[18],[0],[10])
card0916d = Card('チャンピオン',9,16,4,0, 6,1,0,0,0,0,0,0,0,0,0,0,[1,7],1,[0,1,0],[4],[0],[0])
all_card.append(card0916)
card0917 = Card('農民',9,17,1,0,2,0,1,0,1,0,0,0,0,0,0,0,[1,16],0,[0,0,1],[13,18],[10],[0])
card0917a = Card('兵士',9,17,1,0,3,0,0,0,10,0,0,0,0,0,0,0,[1,6,16],0,[0,0,1],[18],[10],[1,5])
card0917b = Card('脱走兵',9,17,1,0,4,1,0,2,0,0,0,0,0,0,0,0,[1,16],0,[0,0,1],[1,18],[10],[0])
card0917c = Card('門下生',9,17,1,0,5,0,0,0,0,0,0,0,0,1,0,0,[1,16],0,[0,0,1],[6,18,31],[10],[0])
card0917d = Card('教師',9,17,6,0,6,0,0,0,0,0,0,0,0,0,0,0,[1,15],1,[0,0,1],[19,25],[0],[0])
all_card.append(card0917)
card0918 = Card('失われし都市',9,18,1,0,5,2,0,2,0,0,0,0,0,0,0,0,[1],0,[1,0,1],[5,20],[1,2],[0])
all_card.append(card0918)
card0919 = Card('カササギ',9,19,1,0,4,1,0,2,0,0,0,0,0,1,0,0,[1],0,[0,1,0],[11],[0],[0])
all_card.append(card0919)
card0920 = Card('語り部',9,20,1,0,5,1,0,10,0,0,0,0,0,0,0,0,[1],0,[1,0,1],[6],[0],[0])
all_card.append(card0920)
card0921 = Card('巨人',9,21,1,0,5,0,0,0,5,0,0,0,0,0,0,0,[1,6],0,[0,0,1],[11,25],[0],[11,12,15,16])
all_card.append(card0921)
card0922 = Card('工匠',9,22,1,0,5,1,0,1,1,0,0,0,0,1,0,0,[1],0,[0,0,1],[1],[0],[0])
all_card.append(card0922)
card0923 = Card('使者',9,23,1,0,4,0,1,0,2,0,0,0,0,1,0,0,[1],0,[0,0,1],[23],[2],[0])
all_card.append(card0923)
card0924 = Card('守銭奴',9,24,1,0,4,0,0,0,10,0,0,0,0,0,0,0,[1],0,[0,0,1],[7,19],[0],[0])
all_card.append(card0924)
card0925 = Card('倒壊',9,25,1,0,2,1,0,1,0,0,0,0,0,0,1,1,[1],0,[0,0,1],[2,22],[0],[0])
all_card.append(card0925)
card0926 = Card('港町',9,26,1,0,4,2,0,1,0,0,0,0,0,1,0,0,[1],0,[0,0,1],[0],[1,2],[0])
all_card.append(card0926)
card0927 = Card('山守',9,27,1,0,4,0,1,5,0,0,0,0,0,0,0,0,[1],0,[0,0,1],[25],[0],[0])
all_card.append(card0927)
card0928 = Card('法貨',9,28,6,2,2,2,0,0,1,0,0,0,0,0,0,0,[2,15],2,[0,0,1],[19],[0],[0])
all_card.append(card0928)
card0929 = Card('遺物',9,29,2,0,5,0,0,0,2,0,0,0,0,0,0,0,[2,6],1,[0,0,1],[25],[0],[17])
all_card.append(card0929)
card0930 = Card('掘出物',9,30,2,0,5,0,0,0,2,0,0,0,0,2,0,0,[2],1,[0,0,1],[0],[0],[0])
all_card.append(card0930)
full_card.append(card0901)
full_card.append(card0902)
full_card.append(card0903)
full_card.append(card0904)
full_card.append(card0905)
full_card.append(card0906)
full_card.append(card0907)
full_card.append(card0908)
full_card.append(card0909)
full_card.append(card0910)
full_card.append(card0911)
full_card.append(card0912)
full_card.append(card0913)
full_card.append(card0914)
full_card.append(card0915)
full_card.append(card0916)
full_card.append(card0916a)
full_card.append(card0916b)
full_card.append(card0916c)
full_card.append(card0916d)
full_card.append(card0917)
full_card.append(card0917a)
full_card.append(card0917b)
full_card.append(card0917c)
full_card.append(card0917d)
full_card.append(card0918)
full_card.append(card0919)
full_card.append(card0920)
full_card.append(card0921)
full_card.append(card0922)
full_card.append(card0923)
full_card.append(card0924)
full_card.append(card0925)
full_card.append(card0926)
full_card.append(card0927)
full_card.append(card0928)
full_card.append(card0929)
full_card.append(card0930)
#帝国
card1001 = Card('女魔術師',10,1,5,0,3,0,0,2,0,0,0,0,0,0,0,0,[1,6,7],1,[0,0,1],[0],[0],[18])
all_card.append(card1001)
card1002 = Card('資料庫',10,2,5,0,5,1,0,1,0,0,0,0,0,0,0,0,[1,7],1,[0,0,1],[16,22],[0],[0])
all_card.append(card1002)
card1003 = Card('生け贄',10,3,1,0,4,2,0,2,2,2,0,0,0,0,1,0,[1],0,[1,0,1],[7],[0],[0])
all_card.append(card1003)
card1004 = Card('ヴィラ',10,4,1,0,4,2,1,0,1,0,0,0,0,0,0,0,[1],0,[0,1,0],[17,26],[1,2],[0])
all_card.append(card1004)
card1005 = Card('王室の鍛冶屋',10,5,1,0,-8,0,0,5,0,0,0,0,0,0,0,0,[1],0,[1,0,1],[1],[0],[0])
all_card.append(card1005)
card1006 = Card('開拓者/騒がしい村',10,6,1,0,3,2,0,1,0,0,0,0,0,0,0,0,[1],0,[0,0,1],[0],[0],[0])
card1006a = Card('開拓者',10,6,1,0,2,1,0,2,0,0,0,0,0,0,0,0,[1],0,[0,0,1],[11,12],[0],[0])
card1006b = Card('騒がしい村',10,6,1,0,5,3,0,2,0,0,0,0,0,0,0,0,[1],0,[1,0,1],[11,12],[0],[0])
all_card.append(card1006)
card1007 = Card('技術者',10,7,1,0,-4,0,0,0,0,0,0,0,0,2,0,1,[1],0,[0,0,1],[11],[0],[0])
all_card.append(card1007)
card1008 = Card('軍団兵',10,8,1,0,5,0,0,0,3,0,0,0,0,0,0,0,[1,6],0,[0,0,1],[11,20],[0],[1,2])
all_card.append(card1008)
card1009 = Card('剣闘士/大金',10,9,1,0,3,2,0,1,0,0,0,0,0,0,0,0,[1],0,[0,0,1],[0],[0],[0])
card1009a = Card('剣闘士',10,6,1,0,3,0,0,0,3,0,0,0,0,0,0,0,[1],0,[0,0,1],[11,12],[0],[0])
card1009b = Card('大金',10,6,1,0,16,0,1,0,10,0,0,0,0,5,0,0,[2],1,[0,0,1],[12],[1,2],[0])
all_card.append(card1009)
card1010 = Card('公共広場',10,10,1,0,5,1,1,3,0,0,0,0,0,0,0,0,[1],0,[0,0,1],[1],[1,2],[0])
all_card.append(card1010)
card1011 = Card('市街',10,11,1,0,-8,2,0,10,0,0,0,0,0,0,0,0,[1],0,[0,0,1],[0],[0],[0])
all_card.append(card1011)
card1012 = Card('陣地/鹵獲品',10,12,1,0,3,2,0,1,0,0,0,0,0,0,0,0,[1],0,[0,0,1],[0],[0],[0])
card1012a = Card('陣地',10,6,1,0,2,2,0,2,0,0,0,0,0,0,0,0,[1],0,[0,0,1],[11,12],[0],[0])
card1012b = Card('鹵獲品',10,6,1,0,5,0,0,0,2,1,0,0,0,0,0,0,[2],1,[0,0,1],[12],[0],[0])
all_card.append(card1012)
card1013 = Card('神殿',10,13,1,0,4,0,0,0,0,1,0,0,0,0,3,0,[1,17],0,[0,0,1],[0],[1,2],[0])
all_card.append(card1013)
card1014 = Card('戦車競走',10,14,1,0,3,1,0,1,1,1,0,0,0,0,0,0,[1],0,[0,0,1],[11],[0],[0])
all_card.append(card1014)
card1015 = Card('大君主',10,15,1,0,-8,0,0,0,0,0,0,0,0,0,0,0,[1],0,[0,0,1],[6],[0],[0])
all_card.append(card1015)
card1016 = Card('投石機/石',10,16,1,0,3,2,0,1,0,0,0,0,0,0,0,0,[1],0,[0,0,1],[0],[0],[0])
card1016a = Card('投石機',10,6,1,0,3,0,0,0,1,0,0,0,0,0,1,0,[1,6],0,[0,0,1],[11,12],[0],[1,3,11,12])
card1016b = Card('石',10,6,1,0,4,0,0,0,1,0,0,0,0,1,0,0,[2],1,[0,0,1],[12],[1,2,3],[0])
all_card.append(card1016)
card1017 = Card('庭師',10,17,1,0,5,1,0,1,0,1,0,0,0,0,0,0,[1],0,[0,0,1],[11],[0],[0])
all_card.append(card1017)
card1018 = Card('農家の市場',10,18,1,0,3,0,1,0,4,4,0,0,0,0,0,1,[1,17],0,[1,0,1],[11],[0],[0])
all_card.append(card1018)
card1019 = Card('パトリキ/エンポリウム',10,19,1,0,3,2,0,1,0,0,0,0,0,0,0,0,[1],0,[0,0,1],[0],[0],[0])
card1019a = Card('パトリキ',10,6,1,0,2,1,0,2,0,0,0,0,0,0,0,0,[1],0,[0,1,0],[3,11,12],[0],[0])
card1019b = Card('エンポリウム',10,6,1,0,5,1,0,1,1,2,0,0,0,0,0,0,[1],0,[0,1,0],[11,12],[1,2],[0])
all_card.append(card1019)
card1020 = Card('ワイルドハント',10,20,1,0,5,0,0,3,0,15,0,0,0,1,0,0,[1,17],0,[0,1,0],[7],[0],[0])
all_card.append(card1020)
card1021 = Card('冠',10,21,1,2,5,0,0,0,0,0,0,0,0,0,0,0,[1,2],2,[0,0,1],[6,31],[0],[0])
all_card.append(card1021)
card1022 = Card('御守り',10,22,2,0,5,0,1,0,2,0,0,0,0,1,0,0,[2],1,[0,0,1],[7],[0],[0])
all_card.append(card1022)
card1023 = Card('元手',10,23,2,0,5,0,1,0,6,0,0,0,0,0,0,0,[2],1,[0,0,1],[27],[0],[0])
all_card.append(card1023)
card1024 = Card('城',10,24,3,0,3,2,0,1,0,0,0,0,0,0,0,0,[1],0,[0,0,1],[0],[0],[0])
card1024a = Card('粗末な城',10,24,3,0,3,0,0,0,1,15,0,0,0,0,0,0,[2,3,18],2,[1,0,1],[0],[9],[0])
card1024b = Card('崩れた城',10,24,3,0,4,0,0,0,0,1,0,0,0,1,0,0,[3,18],1,[1,0,1],[0],[1,2,3],[0])
card1024c = Card('小さな城',10,24,3,0,5,0,0,0,0,2,0,0,0,1,1,1,[1,3,18],2,[1,0,1],[0],[9],[0])
card1024d = Card('幽霊城',10,24,3,0,6,0,0,0,0,2,0,0,0,1,0,0,[3,18],1,[0,0,1],[0],[1,2],[9])
card1024e = Card('華やかな城',10,24,3,0,7,0,0,0,10,3,0,0,0,0,0,0,[1,3,18],2,[1,0,1],[1],[9],[0])
card1024f = Card('広大な城',10,24,3,0,8,0,0,0,0,4,0,0,0,3,0,0,[3,18],1,[1,0,1],[0],[1,2],[0])
card1024g = Card('壮大な城',10,24,3,0,9,0,0,0,0,5,0,0,0,0,0,0,[3,18],1,[1,0,1],[0],[1,2],[0])
card1024h = Card('王城',10,24,3,0,10,0,0,0,0,15,0,0,0,0,0,0,[3,18],1,[0,0,1],[0],[0],[0])
all_card.append(card1024)
full_card.append(card1001)
full_card.append(card1002)
full_card.append(card1003)
full_card.append(card1004)
full_card.append(card1005)
full_card.append(card1006a)
full_card.append(card1006b)
full_card.append(card1007)
full_card.append(card1008)
full_card.append(card1009a)
full_card.append(card1009b)
full_card.append(card1010)
full_card.append(card1011)
full_card.append(card1012a)
full_card.append(card1012b)
full_card.append(card1013)
full_card.append(card1014)
full_card.append(card1015)
full_card.append(card1016a)
full_card.append(card1016b)
full_card.append(card1017)
full_card.append(card1018)
full_card.append(card1019a)
full_card.append(card1019b)
full_card.append(card1020)
full_card.append(card1021)
full_card.append(card1022)
full_card.append(card1023)
full_card.append(card1024a)
full_card.append(card1024b)
full_card.append(card1024c)
full_card.append(card1024d)
full_card.append(card1024e)
full_card.append(card1024f)
full_card.append(card1024g)
full_card.append(card1024h)
#夜想曲
card1100a = Card('願い',11,0,1,0,0,1,0,0,0,0,0,0,0,1,0,0,[1],0,[1,0,1],[17,24],[0],[0])
card1100b = Card('ウィル・オ・ウィスプ',11,0,1,0,0,1,0,2,0,0,0,0,0,0,0,0,[1,23],0,[0,1,0],[3,11],[0],[0])
card1100c = Card('インプ',11,0,1,0,2,0,0,2,0,0,0,0,0,0,0,0,[1,23],0,[0,1,0],[6,11],[0],[0])
card1100d = Card('幽霊',11,0,7,5,4,0,0,0,0,0,0,0,0,0,0,0,[7,21,23],2,[0,0,1],[2,6,31],[0],[0])
card1101 = Card('忠犬',11,1,4,0,2,0,0,2,0,0,0,0,0,0,0,0,[1,5],1,[0,0,1],[16],[5],[0])
all_card.append(card1101)
card1102 = Card('秘密の洞窟',11,2,5,0,3,1,0,1,3,0,0,0,0,0,0,0,[1,7],1,[1,0,1],[1,11,13],[0],[0])
card1102a = Card('魔法のランプ',11,2,2,0,0,0,0,0,1,0,0,0,0,3,0,0,[2,22],1,[1,1,1],[11,13],[0],[0])
all_card.append(card1102)
card1103 = Card('暗躍者',11,3,1,0,4,0,1,0,0,0,0,0,0,1,0,0,[1,6,20],0,[0,0,1],[0],[1,2],[19])
all_card.append(card1103)
card1104 = Card('愚者',11,4,1,0,3,0,0,0,0,0,0,0,0,0,0,0,[1,19],0,[0,0,1],[13,29],[0],[0])
card1104a = Card('幸運のコイン',11,4,2,0,4,0,0,0,1,0,0,0,0,1,0,0,[2,22],1,[1,1,1],[0],[0],[0])
all_card.append(card1104)
card1105 = Card('コンクラーベ',11,5,1,0,4,1,0,0,2,0,0,0,0,0,0,0,[1],0,[0,1,0],[6,11],[0],[0])
all_card.append(card1105)
card1106 = Card('詩人',11,6,1,0,4,0,0,0,2,0,0,0,0,0,0,0,[1,19],0,[0,0,1],[29],[0],[0])
all_card.append(card1106)
card1107 = Card('聖なる木立ち',11,7,1,0,5,0,1,0,3,0,0,0,0,0,0,0,[1,19],0,[1,0,1],[5,29],[0],[0])
all_card.append(card1107)
card1108 = Card('追跡者',11,8,1,0,2,0,0,0,1,0,0,0,0,0,0,0,[1,19],0,[0,0,1],[13,21,29],[0],[0])
card1108a = Card('革袋',11,4,2,0,2,0,1,0,1,0,0,0,0,0,0,0,[2,22],1,[0,0,1],[0],[0],[0])
all_card.append(card1108)
card1109 = Card('ドルイド',11,9,1,0,2,0,1,0,0,0,0,0,0,0,0,0,[1,19],0,[0,1,0],[29],[8],[0])
all_card.append(card1109)
card1110 = Card('ネクロマンサー',11,10,1,0,4,0,0,0,0,0,0,0,0,0,0,0,[1],0,[0,1,0],[6,13],[8],[0])
card1110a = Card('ゾンビの弟子',11,10,1,0,3,1,0,3,0,0,0,0,0,0,1,0,[1,24],0,[1,1,1],[11],[0],[0])
card1110b = Card('ゾンビの石工',11,10,1,0,3,0,0,0,0,0,0,0,0,1,1,0,[1,24],0,[1,1,1],[11],[0],[0])
card1110c = Card('ゾンビの密偵',11,10,1,0,3,1,0,1,0,0,0,0,0,0,0,0,[1,24],0,[1,1,1],[2,3],[0],[0])
all_card.append(card1110)
card1111 = Card('呪われた村',11,11,1,0,5,2,0,6,0,0,0,0,0,0,0,0,[1,20],0,[1,0,1],[11,30],[1,2],[0])
all_card.append(card1111)
card1112 = Card('迫害者',11,12,1,0,5,0,0,0,2,0,0,0,0,1,0,0,[1,6,20],0,[0,0,1],[7,13],[0],[19])
all_card.append(card1112)
card1113 = Card('ピクシー',11,13,1,0,2,1,0,1,0,0,0,0,0,0,0,1,[1,19],0,[0,1,0],[13,29],[0],[0])
card1113a = Card('ヤギ',11,4,2,0,2,0,0,0,1,0,0,0,0,0,1,0,[2,22],1,[0,1,0],[0],[0],[0])
all_card.append(card1113)
card1114 = Card('悲劇のヒーロー',11,14,1,0,5,0,1,3,0,0,0,0,0,1,0,1,[1],0,[1,1,1],[11],[0],[0])
all_card.append(card1114)
card1115 = Card('羊飼い',11,15,1,0,4,1,0,10,0,0,0,0,0,0,0,0,[1],0,[1,0,1],[1,13],[0],[0])
card1115a = Card('牧草地',11,4,2,3,2,0,0,0,1,15,0,0,0,1,0,0,[2,3,22],2,[0,0,1],[0],[9],[0])
all_card.append(card1115)
card1116 = Card('プーカ',11,16,1,0,5,0,0,4,0,0,0,0,0,0,1,0,[1],0,[0,1,0],[13],[0],[0])
card1116a = Card('呪われた金貨',11,4,2,0,4,0,0,0,3,0,0,0,0,1,0,0,[2,22],1,[1,0,1],[28],[0],[0])
all_card.append(card1116)
card1117 = Card('恵みの村',11,17,1,0,4,2,0,1,0,0,0,0,0,0,0,0,[1,19],0,[1,0,1],[29],[0],[0])
all_card.append(card1117)
card1118 = Card('レプラコーン',11,18,1,0,3,0,0,0,0,0,0,0,0,1,0,0,[1,20],0,[0,1,0],[11,13,30],[0],[0])
all_card.append(card1118)
card1119 = Card('偶像',11,19,2,0,5,0,0,0,2,0,0,0,0,0,0,0,[1,6,19],1,[0,0,1],[11,29],[0],[11,12])
all_card.append(card1119)
card1120 = Card('墓地',11,20,3,0,4,0,0,0,0,2,0,0,0,0,4,0,[3],1,[0,0,1],[13],[1,2],[0])
card1120a = Card('呪いの鏡',11,4,2,0,0,0,0,0,1,0,0,0,0,1,0,0,[2,22],1,[1,0,1],[11,13],[3],[0])
all_card.append(card1120)
card1121 = Card('悪人のアジト',11,21,7,5,5,0,0,2,0,0,0,0,0,0,0,0,[7,21],2,[1,1,1],[17],[1,2],[0])
all_card.append(card1121)
card1122 = Card('カブラー',11,22,7,5,5,0,0,0,0,0,0,0,0,1,0,0,[7,21],2,[0,1,0],[17],[0],[0])
all_card.append(card1122)
card1123 = Card('ゴーストタウン',11,23,7,5,3,1,0,1,0,0,0,0,0,0,0,0,[7,21],2,[0,1,0],[17],[1,2],[0])
all_card.append(card1123)
card1124 = Card('守護者',11,24,7,5,2,0,0,0,1,0,0,0,0,0,0,0,[7,21],2,[0,0,1],[4,17],[1,2],[0])
all_card.append(card1124)
card1125 = Card('納骨堂',11,25,7,5,5,0,0,1,0,0,0,0,0,0,0,0,[7,21],2,[0,0,1],[16,22],[0],[0])
all_card.append(card1125)
card1126 = Card('夜襲',11,26,7,5,6,0,0,0,3,0,0,0,0,0,0,0,[6,7,21],2,[0,0,1],[0],[0],[1,7])
all_card.append(card1126)
card1127 = Card('人狼',11,27,7,1,5,0,0,3,0,0,0,0,0,0,0,0,[1,6,20,21],2,[0,0,1],[7],[0],[20])
all_card.append(card1127)
card1128 = Card('悪魔の工房',11,28,7,0,4,0,0,0,0,0,0,0,0,1,0,0,[21],1,[1,0,1],[7,13],[0],[0])
all_card.append(card1128)
card1129 = Card('悪魔祓い',11,29,7,0,4,0,0,0,0,0,0,0,0,1,1,0,[21],1,[0,0,1],[13],[0],[0])
all_card.append(card1129)
card1130 = Card('吸血鬼',11,30,7,0,5,0,0,0,0,0,0,0,0,1,0,0,[6,20,21],1,[0,0,1],[13,18],[0],[20])
card1130a = Card('コウモリ',11,30,7,0,2,0,0,0,0,0,0,0,0,0,2,0,[21],1,[0,1,0],[18],[0],[0])
all_card.append(card1130)
card1131 = Card('修道院',11,31,7,0,2,0,0,0,0,0,0,0,0,0,10,0,[21],1,[0,0,1],[0],[0],[0])
all_card.append(card1131)
card1132 = Card('取り替え子',11,32,7,0,3,0,0,0,0,0,0,0,0,1,0,1,[21],1,[1,0,1],[0],[8],[0])
all_card.append(card1132)
card1133 = Card('夜警',11,33,7,0,3,0,0,0,0,0,0,0,0,0,0,0,[21],1,[0,0,1],[2,3,17],[1,2],[0])
all_card.append(card1133)
full_card.append(card1100a)
full_card.append(card1100b)
full_card.append(card1100c)
full_card.append(card1100d)
full_card.append(card1101)
full_card.append(card1102)
full_card.append(card1102a)
full_card.append(card1103)
full_card.append(card1104)
full_card.append(card1104a)
full_card.append(card1105)
full_card.append(card1106)
full_card.append(card1107)
full_card.append(card1108)
full_card.append(card1108a)
full_card.append(card1109)
full_card.append(card1110)
full_card.append(card1110a)
full_card.append(card1110b)
full_card.append(card1110c)
full_card.append(card1111)
full_card.append(card1112)
full_card.append(card1113)
full_card.append(card1113a)
full_card.append(card1114)
full_card.append(card1115)
full_card.append(card1115a)
full_card.append(card1116)
full_card.append(card1116a)
full_card.append(card1117)
full_card.append(card1118)
full_card.append(card1119)
full_card.append(card1120)
full_card.append(card1120a)
full_card.append(card1121)
full_card.append(card1122)
full_card.append(card1123)
full_card.append(card1124)
full_card.append(card1125)
full_card.append(card1126)
full_card.append(card1127)
full_card.append(card1128)
full_card.append(card1129)
full_card.append(card1130)
full_card.append(card1130a)
full_card.append(card1131)
full_card.append(card1132)
full_card.append(card1133)
#ルネサンス
card1201 = Card('パトロン',12,1,4,0, 4,0,0,0,2,0,1,1,0,0,0,0,[1,5],1,[0,1,0],[19],[5],[0])
all_card.append(card1201)
card1202 = Card('貨物船',12,2,5,0,3,0,0,0,2,0,0,0,0,0,0,0,[1,7],1,[0,0,1],[16],[0],[0])
all_card.append(card1202)
card1203 = Card('研究',12,3,5,0,4,1,0,10,0,0,0,0,0,0,1,0,[1,7],1,[0,0,1],[16,22],[0],[0])
all_card.append(card1203)
card1204 = Card('悪党',12,4,1,0,5,0,0,0,0,0,2,0,0,0,0,0,[1,6],0,[0,0,1],[19],[0],[1,7])
all_card.append(card1204)
card1205 = Card('学者',12,5,1,0,5,0,0,7,0,0,0,0,0,0,0,0,[1],0,[0,0,1],[1],[0],[0])
all_card.append(card1205)
card1206 = Card('旗手',12,6,1,0,4,0,0,0,2,0,0,0,0,0,0,0,[1],0,[0,0,1],[34],[1,2,3],[0])
all_card.append(card1206)
card1207 = Card('絹商人',12,7,1,0,4,0,1,2,0,0,1,1,0,0,0,0,[1],0,[0,0,1],[19],[1,2,3],[0])
all_card.append(card1207)
card1208 = Card('劇団',12,8,1,0,3,0,0,0,0,0,0,4,0,0,0,1,[1],0,[0,0,1],[19],[0],[0])
all_card.append(card1208)
card1209 = Card('剣客',12,9,1,0,5,0,0,3,0,0,1,0,0,0,0,0,[1],0,[0,0,1],[11,19,34],[0],[0])
all_card.append(card1209)
card1210 = Card('国境警備隊',12,10,1,0,2,1,0,1,0,0,0,0,0,0,0,0,[1],0,[0,0,1],[2,22,34],[0],[0])
all_card.append(card1210)
card1211 = Card('山村',12,11,1,0,4,2,0,1,0,0,0,0,0,0,0,0,[1],0,[0,0,1],[22],[0],[0])
all_card.append(card1211)
card1212 = Card('司祭',12,12,1,0,4,0,0,0,4,0,0,0,0,0,1,0,[1],0,[0,0,1],[11],[0],[0])
all_card.append(card1212)
card1213 = Card('実験',12,13,1,0,3,1,0,2,0,0,0,0,0,0,0,0,[1],0,[0,0,1],[24],[1,2],[0])
all_card.append(card1213)
card1214 = Card('出納官',12,14,1,0,5,0,0,0,3,0,0,0,0,1,1,0,[1],0,[0,0,1],[7,34],[0],[0])
all_card.append(card1214)
card1215 = Card('先見者',12,15,1,0,5,1,0,2,0,0,0,0,0,0,0,0,[1],0,[0,0,1],[11,22],[0],[0])
all_card.append(card1215)
card1216 = Card('増築',12,16,1,0,3,0,0,0,2,0,0,0,0,1,1,1,[1],0,[0,0,1],[0],[0],[0])
all_card.append(card1216)
card1217 = Card('彫刻家',12,17,1,0,5,0,0,0,0,0,0,1,0,1,0,0,[1],0,[0,0,1],[11,19],[0],[0])
all_card.append(card1217)
card1218 = Card('徴募官',12,18,1,0,5,0,0,2,0,0,0,10,0,0,1,0,[1],0,[0,0,1],[19],[0],[0])
all_card.append(card1218)
card1219 = Card('追従者',12,19,1,0,2,0,0,2,0,0,0,2,0,0,0,0,[1],0,[0,0,1],[0],[1,2],[0])
all_card.append(card1219)
card1220 = Card('根城',12,20,1,0,4,2,0,1,0,0,0,0,0,1,1,0,[1],0,[0,0,1],[7,28],[0],[0])
all_card.append(card1220)
card1221 = Card('発明家',12,21,1,0,4,0,0,0,0,0,0,0,0,1,0,0,[1],0,[0,0,1],[9],[0],[0])
all_card.append(card1221)
card1222 = Card('老魔女',12,22,1,0,5,0,0,3,0,0,0,0,0,0,0,0,[1,6],0,[0,0,1],[5,20],[0],[11,12])
all_card.append(card1222)
card1223 = Card('王笏',12,23,2,0,5,0,0,0,2,0,0,0,0,0,0,0,[2],1,[0,0,1],[6,7],[0],[0])
all_card.append(card1223)
card1224 = Card('香辛料',12,24,2,0,5,0,1,0,2,0,2,0,0,0,0,0,[2],1,[0,0,1],[0],[1,2],[0])
all_card.append(card1224)
card1225 = Card('ドゥカート金貨',12,25,2,0, 2,0,1,0,0,0,1,0,0,0,1,0,[2],1,[0,1,1],[0],[1,2],[0])
all_card.append(card1225)
full_card.append(card1201)
full_card.append(card1202)
full_card.append(card1203)
full_card.append(card1204)
full_card.append(card1205)
full_card.append(card1206)
full_card.append(card1207)
full_card.append(card1208)
full_card.append(card1209)
full_card.append(card1210)
full_card.append(card1211)
full_card.append(card1212)
full_card.append(card1213)
full_card.append(card1214)
full_card.append(card1215)
full_card.append(card1216)
full_card.append(card1217)
full_card.append(card1218)
full_card.append(card1219)
full_card.append(card1220)
full_card.append(card1221)
full_card.append(card1222)
full_card.append(card1223)
full_card.append(card1224)
full_card.append(card1225)
#移動動物園
card1300 = Card('馬',13,0,1,0, 3,1,0,2,0,0,0,0,0,0,0,0,[1],0,[0,0,1],[24],[0],[0])
card1301 = Card('黒猫',13,1,4,0, 2,0,0,2,0,0,0,0,0,0,0,0,[1,5,6],1,[0,0,1],[0],[5],[11,12])
all_card.append(card1301)
card1302 = Card('そり',13,2,4,0, 2,0,0,0,0,0,0,0,0,2,0,0,[1,5],1,[1,0,0],[13,17,21,33],[5],[0])
all_card.append(card1302)
card1303 = Card('鷹匠',13,3,4,0, 5,0,0,0,0,0,0,0,0,1,0,0,[1,5],1,[0,0,1],[17],[5],[0])
all_card.append(card1303)
card1304 = Card('牧羊犬',13,4,4,0, 3,0,0,2,0,0,0,0,0,0,0,0,[1,5],1,[0,0,1],[0],[5],[0])
all_card.append(card1304)
card1305 = Card('村有緑地',13,5,5,4, 4,2,0,1,0,0,0,0,0,0,0,0,[1,5,7],2,[0,0,1],[7],[5],[0])
all_card.append(card1305)
card1306 = Card('首謀者',13,6,5,0, 5,0,0,0,0,0,0,0,0,0,0,0,[1,7],1,[0,0,1],[31],[0],[0])
all_card.append(card1306)
card1307 = Card('艀',13,7,5,0, 5,0,1,3,0,0,0,0,0,0,0,0,[1,7],1,[0,0,1],[7],[0],[0])
all_card.append(card1307)
card1308 = Card('門番',13,8,5,0, 5,0,0,0,3,0,0,0,0,0,0,0,[1,6,7],1,[0,0,1],[19],[0],[20])
all_card.append(card1308)
card1309 = Card('貸し馬屋',13,9,1,0, 5,0,0,0,3,0,0,0,0,1,0,0,[1],0,[1,0,1],[13,33],[0],[0])
all_card.append(card1309)
card1310 = Card('がらくた',13,10,1,0, 3,1,1,1,1,0,0,0,0,2,1,0,[1],0,[1,0,0],[7,11],[0],[0])
all_card.append(card1310)
card1311 = Card('騎兵隊',13,11,1,0, 4,0,1,2,0,0,0,0,0,2,0,0,[1],0,[0,0,1],[13,26,33],[1,2],[0])
all_card.append(card1311)
card1312 = Card('強制退去',13,12,1,0, 5,0,0,0,0,0,0,0,0,1,0,0,[1],0,[0,0,1],[19,32],[0],[0])
all_card.append(card1312)
card1313 = Card('行人',13,13,1,0, 6,0,0,3,0,0,0,0,0,1,0,0,[1],0,[0,0,1],[0],[11],[0])
all_card.append(card1313)
card1314 = Card('狩猟小屋',13,14,1,0, 5,2,0,5,0,0,0,0,0,0,0,0,[1],0,[0,0,1],[1,11],[0],[0])
all_card.append(card1314)
card1315 = Card('賞金稼ぎ',13,15,1,0, 4,1,0,0,3,0,0,0,0,0,0,0,[1],0,[1,0,1],[11,19,32],[0],[0])
all_card.append(card1315)
card1316 = Card('枢機卿',13,16,1,0, 4,0,0,0,2,0,0,0,0,0,0,0,[1],0,[0,0,1],[19],[0],[16,20])
all_card.append(card1316)
card1317 = Card('聖域',13,17,1,0, 5,1,1,1,0,0,0,0,0,0,0,0,[1],0,[0,0,1],[19,32],[0],[0])
all_card.append(card1317)
card1318 = Card('デストリエ',13,18,1,0, 6,1,0,2,0,0,0,0,0,0,0,0,[1],0,[0,1,0],[0],[11],[0])
all_card.append(card1318)
card1319 = Card('動物見本市',13,19,1,0, 7,0,10,0,4,0,0,0,0,0,1,0,[1],0,[0,0,1],[11],[2],[0])
all_card.append(card1319)
card1320 = Card('旅籠',13,20,1,0, 4,2,0,1,0,0,0,0,0,0,0,0,[1],0,[0,0,1],[33],[1,2],[0])
all_card.append(card1320)
card1321 = Card('馬丁',13,21,1,0, 4,1,0,1,0,0,0,0,0,1,0,0,[1],0,[0,0,1],[7,13,33],[0],[0])
all_card.append(card1321)
card1322 = Card('パドック',13,22,1,0, 5,10,0,0,2,0,0,0,0,2,0,0,[1],0,[0,1,0],[11,13,33],[0],[0])
all_card.append(card1322)
card1323 = Card('魔女の集会',13,23,1,0, 5,1,0,0,2,0,0,0,0,0,0,0,[1],0,[1,0,1],[19],[0],[11,12,20])
all_card.append(card1323)
card1324 = Card('ヤギ飼い',13,24,1,0, 3,1,0,10,0,0,0,0,0,0,1,0,[1],0,[1,1,1],[11],[0],[0])
all_card.append(card1324)
card1325 = Card('雪深い村',13,25,5,0, 3,4,1,1,0,0,0,0,0,0,0,0,[1],0,[1,0,1],[5],[0],[0])
all_card.append(card1325)
card1326 = Card('ラクダの隊列',13,26,1,0, 3,0,0,0,0,0,0,0,0,0,0,0,[1],0,[1,1,1],[32],[1,2],[0])
all_card.append(card1326)
card1327 = Card('漁師',13,27,1,0, 5,1,0,1,1,0,0,0,0,0,0,0,[1],0,[0,0,1],[0],[11],[0])
all_card.append(card1327)
card1328 = Card('炉',13,28,1,0, 5,0,0,0,2,0,0,0,0,1,0,0,[1],0,[0,0,1],[0],[0],[0])
all_card.append(card1328)
card1329 = Card('配給品',13,29,1,0, 2,0,0,0,1,0,0,0,0,0,0,0,[2],1,[0,0,1],[13,21,33],[0],[0])
all_card.append(card1329)
card1330 = Card('備蓄品',13,30,1,0, 3,0,1,0,3,0,0,0,0,0,0,0,[2],1,[0,0,1],[32],[0],[0])
all_card.append(card1330)
full_card.append(card1300)
full_card.append(card1301)
full_card.append(card1302)
full_card.append(card1303)
full_card.append(card1304)
full_card.append(card1305)
full_card.append(card1306)
full_card.append(card1307)
full_card.append(card1308)
full_card.append(card1309)
full_card.append(card1310)
full_card.append(card1311)
full_card.append(card1312)
full_card.append(card1313)
full_card.append(card1314)
full_card.append(card1315)
full_card.append(card1316)
full_card.append(card1317)
full_card.append(card1318)
full_card.append(card1319)
full_card.append(card1320)
full_card.append(card1321)
full_card.append(card1322)
full_card.append(card1323)
full_card.append(card1324)
full_card.append(card1325)
full_card.append(card1326)
full_card.append(card1327)
full_card.append(card1328)
full_card.append(card1329)
full_card.append(card1330)
#同盟
card1401 = Card('城砦',14,1,1,0, 3,2,0,1,0,0,0,0,0,0,0,0,[1,26],0,[0,0,1],[0],[0],[0])
card1401a = Card('天幕',14,1,1,0, 3,0,0,0,2,0,0,0,0,0,0,0,[1,26],0,[0,0,1],[12,35,36],[0],[0])
card1401b = Card('駐屯地',14,1,5,0, 4,0,0,10,2,0,0,0,0,0,0,0,[1,7,26],1,[0,0,1],[12],[0],[0])
card1401c = Card('堡塁',14,1,1,0, 5,1,0,1,0,0,0,0,0,1,0,0,[1,26],0,[0,0,1],[7,12,17],[0],[0])
card1401d = Card('要塞',14,1,5,3, 6,0,0,3,3,0,0,0,0,0,0,0,[1,3,7,26],2,[0,0,1],[7,12],[9],[0])
all_card.append(card1401)
card1402 = Card('衝突',14,2,1,0, 3,2,0,1,0,0,0,0,0,0,0,0,[1,27],0,[0,0,1],[0],[0],[0])
card1402a = Card('戦闘計画',14,2,1,0, 3,1,0,2,0,0,0,0,0,0,0,0,[1,6,27],0,[0,0,1],[11,12,36],[0],[0])
card1402b = Card('射手',14,2,1,0, 4,0,0,0,2,0,0,0,0,0,0,0,[1,27],0,[0,0,1],[12],[0],[1,7])
card1402c = Card('将軍',14,2,5,0, 5,1,0,2,0,0,0,0,0,0,0,0,[1,6,7,27],1,[0,0,1],[12],[0],[22])
card1402d = Card('領土',14,2,3,0, 6,0,0,0,0,15,0,0,0,10,0,0,[3,27],1,[0,0,1],[12],[1,2],[0])
all_card.append(card1402)
card1403 = Card('叙事詩',14,3,1,0, 3,2,0,1,0,0,0,0,0,0,0,0,[1,28],0,[0,0,1],[0],[0],[0])
card1403a = Card('古地図',14,3,1,0, 3,1,0,1,0,0,0,0,0,0,0,0,[1,28],0,[0,0,1],[1,12,36],[0],[0])
card1403b = Card('航海',14,3,5,0, 4,1,0,1,0,0,0,0,0,0,0,0,[1,7,28],1,[0,0,1],[12,14],[0],[0])
card1403c = Card('沈没船の財宝',14,3,2,0, 5,0,0,0,0,0,0,0,0,1,0,0,[2,28],1,[1,0,1],[12],[0],[0])
card1403d = Card('遠い海岸',14,3,1,3, 6,1,0,2,0,2,0,0,0,1,0,0,[1,3,28],2,[1,0,1],[12],[9],[0])
all_card.append(card1403)
card1404 = Card('町民',14,4,1,0, 3,2,0,1,0,0,0,0,0,0,0,0,[1,29],0,[0,0,1],[0],[0],[0])
card1404a = Card('触れ役',14,4,1,0, 2,1,0,1,2,0,0,0,0,1,0,0,[1,29],0,[1,0,1],[7,12,36],[0],[0])
card1404b = Card('蹄鉄工',14,4,1,0, 3,1,0,6,0,0,0,0,0,0,0,0,[1,29],0,[0,0,1],[7,12],[0],[0])
card1404c = Card('粉屋',14,4,1,0, 4,1,0,1,0,0,0,0,0,0,0,0,[1,29],0,[0,0,1],[2,12,22],[0],[0])
card1404d = Card('長老',14,4,1,0, 5,0,0,0,2,0,0,0,0,0,0,0,[1,29],0,[0,0,1],[6,12],[0],[0])
all_card.append(card1404)
card1405 = Card('卜占官',14,5,1,0, 3,2,0,1,0,0,0,0,0,0,0,0,[1,30],0,[0,0,1],[0],[0],[0])
card1405a = Card('薬草集め',14,5,1,0, 3,0,1,0,0,0,0,0,0,0,0,0,[1,30],0,[1,0,1],[6,12,36],[0],[0])
card1405b = Card('侍祭',14,5,1,0, 4,0,0,0,0,0,0,0,0,2,1,1,[1,30],0,[0,0,1],[11,12],[0],[0])
card1405c = Card('女魔道士',14,5,1,0, 5,1,0,1,0,0,0,0,0,0,0,0,[1,6,30],0,[0,0,1],[11,12],[0],[11,12])
card1405d = Card('女予言者',14,5,1,0, 6,1,0,4,0,0,0,0,0,0,0,0,[1,30],0,[0,0,1],[8,12],[0],[0])
all_card.append(card1405)
card1406 = Card('魔法使い',14,6,1,0, 3,2,0,1,0,0,0,0,0,0,0,0,[1,31],0,[0,0,1],[0],[0],[0])
card1406a = Card('生徒',14,6,1,0, 3,1,0,0,0,0,0,0,1,0,1,0,[1,25,31],0,[0,0,1],[11,12,19,35,36],[0],[0])
card1406b = Card('霊術士',14,6,5,0, 4,0,0,0,0,0,0,0,0,1,0,0,[1,31],0,[0,0,1],[12],[0],[0])
card1406c = Card('魔導士',14,6,1,0, 5,1,0,1,0,0,0,0,0,0,0,0,[1,6,31],0,[0,0,1],[12],[0],[11])
card1406d = Card('リッチ',14,6,1,0, 6,2,0,6,0,0,0,0,0,1,0,0,[1,31],0,[0,0,1],[5,12],[3],[0])
all_card.append(card1406)
card1407 = Card('追いはぎ',14,7,5,0, 5,0,0,3,0,0,0,0,0,0,0,0,[1,6,7],1,[0,0,1],[0],[0],[21])
all_card.append(card1407)
card1408 = Card('王家のガレー船',14,8,5,0, 4,0,0,1,0,0,0,0,0,0,0,0,[1,7],1,[1,1,1],[6],[0],[0])
all_card.append(card1408)
card1409 = Card('輸入者',14,9,5,0, 5,0,0,0,0,0,0,0,4,1,0,0,[1,7,25],1,[0,0,1],[19],[8],[0])
all_card.append(card1409)
card1410 = Card('改造',14,10,1,0, 5,1,0,1,0,0,0,0,0,1,1,0,[1],0,[0,0,1],[7],[0],[0])
all_card.append(card1410)
card1411 = Card('狩人',14,11,1,0, 5,1,0,3,0,0,0,0,0,0,0,0,[1],0,[0,0,1],[2,11,22],[0],[0])
all_card.append(card1411)
card1412 = Card('ガレリア',14,12,1,0, 5,0,1,0,3,0,0,0,0,0,0,0,[1],0,[0,1,0],[11],[0],[0])
all_card.append(card1412)
card1413 = Card('急使',14,13,1,0, 4,0,0,0,1,0,0,0,0,0,0,0,[1],0,[0,0,1],[2,6],[0],[0])
all_card.append(card1413)
card1414 = Card('ギルドマスター',14,14,1,0, 5,0,0,0,3,0,0,0,10,0,0,0,[1,25],0,[0,1,0],[11,19],[0],[0])
all_card.append(card1414)
card1415 = Card('交換',14,15,1,0, 5,1,0,1,0,0,0,0,0,1,0,0,[1],0,[0,0,1],[17],[0],[0])
all_card.append(card1415)
card1416 = Card('侯爵',14,16,1,0, 6,0,1,10,0,0,0,0,0,0,0,0,[1],0,[0,0,1],[1],[0],[0])
all_card.append(card1416)
card1417 = Card('ごますり',14,17,1,0, 2,1,0,0,3,0,0,0,2,0,0,0,[1,25],0,[1,0,0],[1,19],[1,2,3],[0])
all_card.append(card1417)
card1418 = Card('散兵',14,18,1,0, 5,1,0,1,1,0,0,0,0,0,0,0,[1],0,[0,0,1],[11],[0],[1,3])
all_card.append(card1418)
card1419 = Card('下役',14,19,1,0, 3,1,0,1,0,0,0,0,1,0,0,0,[1,25],0,[0,0,1],[19],[0],[0])
all_card.append(card1419)
card1420 = Card('首都',14,20,1,0, 3,2,0,1,2,0,0,0,0,0,0,0,[1],0,[0,0,1],[1,11],[0],[0])
all_card.append(card1420)
card1421 = Card('商人の野営地',14,21,1,0, 3,2,0,0,1,0,0,0,0,0,0,0,[1],0,[1,0,1],[35],[0],[0])
all_card.append(card1421)
card1422 = Card('専門家',14,22,1,0, 5,0,0,0,0,0,0,0,0,1,0,0,[1],0,[0,0,1],[6,7,31],[0],[0])
all_card.append(card1422)
card1423 = Card('大工',14,23,1,0, 4,1,0,0,0,0,0,0,0,1,1,0,[1],0,[0,0,1],[7],[0],[0])
all_card.append(card1423)
card1424 = Card('仲買人',14,24,1,0, 4,10,0,10,10,0,0,0,10,0,1,0,[1,25],0,[0,0,1],[7,19],[0],[0])
all_card.append(card1424)
card1425 = Card('蛮族',14,25,5,0, 5,0,0,0,2,0,0,0,0,0,0,0,[1,6],0,[0,0,1],[0],[0],[11,12,15])
all_card.append(card1425)
card1426 = Card('歩哨',14,26,1,0, 3,0,0,0,0,0,0,0,0,0,2,0,[1],0,[0,0,1],[3],[0],[0])
all_card.append(card1426)
card1427 = Card('町',14,27,1,0, 4,2,1,1,2,0,0,0,0,0,0,0,[1],0,[0,0,1],[7],[0],[0])
all_card.append(card1427)
card1428 = Card('密使',14,28,1,0, 5,1,0,3,0,0,0,0,2,0,0,0,[1,25],0,[0,0,1],[11,19],[0],[0])
all_card.append(card1428)
card1429 = Card('宿屋の主人',14,29,1,0, 4,1,0,5,0,0,0,0,0,0,0,0,[1],0,[1,0,1],[1,7],[0],[0])
all_card.append(card1429)
card1430 = Card('契約書',14,30,2,5, 5,0,0,0,2,0,0,0,1,0,0,0,[2,7,25],2,[0,0,1],[16,19],[0],[0])
all_card.append(card1430)
card1431 = Card('道化棒',14,31,2,0, 2,0,1,0,1,0,0,0,1,0,0,0,[2,25],1,[0,0,1],[7,19,21],[0],[0])
all_card.append(card1431)
full_card.append(card1401a)
full_card.append(card1401b)
full_card.append(card1401c)
full_card.append(card1401d)
full_card.append(card1402a)
full_card.append(card1402b)
full_card.append(card1402c)
full_card.append(card1402d)
full_card.append(card1403a)
full_card.append(card1403b)
full_card.append(card1403c)
full_card.append(card1403d)
full_card.append(card1404a)
full_card.append(card1404b)
full_card.append(card1404c)
full_card.append(card1404d)
full_card.append(card1405a)
full_card.append(card1405b)
full_card.append(card1405c)
full_card.append(card1405d)
full_card.append(card1406a)
full_card.append(card1406b)
full_card.append(card1406c)
full_card.append(card1406d)
full_card.append(card1407)
full_card.append(card1408)
full_card.append(card1409)
full_card.append(card1410)
full_card.append(card1411)
full_card.append(card1412)
full_card.append(card1413)
full_card.append(card1414)
full_card.append(card1415)
full_card.append(card1416)
full_card.append(card1417)
full_card.append(card1418)
full_card.append(card1419)
full_card.append(card1420)
full_card.append(card1421)
full_card.append(card1422)
full_card.append(card1423)
full_card.append(card1424)
full_card.append(card1425)
full_card.append(card1426)
full_card.append(card1427)
full_card.append(card1428)
full_card.append(card1429)
full_card.append(card1430)
full_card.append(card1431)
#略奪
card1500a = Card('アンフォラ',15,0,2,5, 7,0,1,0,3,0,0,0,0,0,0,0,[2,7,32],2,[0,1,0],[7],[0],[0])
card1500b = Card('ダブロン金貨',15,0,2,0, 7,0,0,0,3,0,0,0,0,1,0,0,[2,32],1,[0,1,1],[0],[1],[0])
card1500c = Card('尽きぬ杯',15,0,2,5, 7,0,1,0,1,0,0,0,0,0,0,0,[2,7,32],2,[1,0,1],[0],[0],[0])
card1500d = Card('船首像',15,0,2,5, 7,0,0,2,3,0,0,0,0,0,0,0,[2,7,32],2,[0,0,1],[0],[0],[0])
card1500e = Card('ハンマー',15,0,2,0, 7,0,0,0,3,0,0,0,0,1,0,0,[2,32],1,[0,0,1],[0],[0],[0])
card1500f = Card('勲章',15,0,2,0, 7,0,0,0,3,0,0,0,0,0,0,0,[2,32],1,[0,0,1],[21],[0],[0])
card1500g = Card('宝石',15,0,2,5, 7,0,1,0,3,0,0,0,0,0,0,0,[2,7,32],2,[0,0,1],[35],[0],[0])
card1500h = Card('宝珠',15,0,2,0, 7,0,1,0,3,0,0,0,0,0,0,0,[2,32],1,[0,0,1],[6,7],[0],[0])
card1500i = Card('賞品のヤギ',15,0,2,0, 7,0,1,0,3,0,0,0,0,0,1,0,[2,32],1,[1,1,1],[0],[0],[0])
card1500j = Card('パズルボックス',15,0,2,0, 7,0,1,0,3,0,0,0,0,0,0,0,[2,32],1,[0,1,0],[16],[0],[0])
card1500k = Card('六分儀',15,0,2,0, 7,0,1,0,3,0,0,0,0,0,0,0,[2,32],1,[0,0,1],[2,3],[0],[0])
card1500l = Card('盾',15,0,2,4, 7,0,1,0,3,0,0,0,0,0,0,0,[2,5,32],2,[0,0,1],[4],[0],[0])
card1500m = Card('呪符の巻物',15,0,1,2, 7,0,0,0,0,0,0,0,0,1,0,1,[1,2,32],2,[1,0,1],[0],[0],[0])
card1500n = Card('杖',15,0,2,0, 7,0,1,0,3,0,0,0,0,0,0,0,[2,32],2,[0,0,1],[6],[0],[0])
card1500o = Card('剣',15,0,2,0, 7,0,1,0,3,0,0,0,0,0,0,0,[2,6,32],2,[0,0,1],[0],[0],[1,4])
card1501 = Card('地図作り',15,1,4,0, 4,0,0,2,0,0,0,0,0,0,0,0,[1,5],1,[0,0,1],[2,22],[5],[0])
all_card.append(card1501)
card1502 = Card('密航者',15,2,5,4, 3,0,0,2,0,0,0,0,0,0,0,0,[1,5,7],2,[0,0,1],[0],[5],[0])
all_card.append(card1502)
card1503 = Card('岩屋',15,3,5,0, 2,1,0,4,0,0,0,0,0,0,0,0,[1,7],1,[0,0,1],[16],[0],[0])
all_card.append(card1503)
card1504 = Card('拡大',15,4,5,0, 5,0,0,0,0,0,0,0,0,1,1,0,[1,7],1,[0,0,1],[0],[0],[0])
all_card.append(card1504)
card1505 = Card('旗艦',15,5,5,0, 4,0,0,0,2,0,0,0,0,0,0,0,[1,7,14],1,[0,0,1],[31],[0],[0])
all_card.append(card1505)
card1506 = Card('キャビンボーイ',15,6,5,0, 4,1,0,1,2,0,0,0,0,1,0,1,[1,7],1,[0,1,0],[7],[0],[0])
all_card.append(card1506)
card1507 = Card('切り裂き魔',15,7,5,0, 5,0,0,0,0,0,0,0,0,1,0,0,[1,6,7],1,[1,0,1],[15],[0],[1,3])
all_card.append(card1507)
card1508 = Card('現場監督',15,8,5,0, 3,1,0,0,1,0,0,0,0,0,0,0,[1,7],1,[0,0,1],[11],[0],[0])
all_card.append(card1508)
card1509 = Card('上陸部隊',15,9,5,0, 4,2,0,2,0,0,0,0,0,0,0,0,[1,7],1,[0,0,1],[11,35],[0],[0])
all_card.append(card1509)
card1510 = Card('セイレーン',15,10,5,0, 3,0,0,8,0,0,0,0,0,0,0,1,[1,6,7],1,[0,1,0],[0],[1,2],[11,12])
all_card.append(card1510)
card1511 = Card('操舵手',15,11,5,0, 5,0,0,0,0,0,0,0,0,1,0,0,[1,7],1,[0,0,1],[16],[0],[0])
all_card.append(card1511)
card1512 = Card('調査',15,12,5,0, 2,0,0,0,2,0,0,0,0,1,0,1,[1,7],1,[0,0,1],[15],[0],[0])
all_card.append(card1512)
card1513 = Card('乗組員',15,13,5,0, 5,0,0,3,0,0,0,0,0,0,0,0,[1,7],1,[0,0,1],[35],[0],[0])
all_card.append(card1513)
card1514 = Card('秘境の社',15,14,5,0, 3,0,0,0,1,0,0,0,0,0,2,0,[1,7],1,[1,0,1],[11],[0],[0])
all_card.append(card1514)
card1515 = Card('フリゲート船',15,15,5,0, 5,0,0,0,3,0,0,0,0,0,0,0,[1,6,7],1,[0,1,1],[0],[0],[1,4])
all_card.append(card1515)
card1516 = Card('ロングシップ',15,16,5,0, 5,2,0,2,0,0,0,0,0,0,0,0,[1,7],1,[0,1,0],[11],[0],[0])
all_card.append(card1516)
card1517 = Card('一等航海士',15,17,1,0, 5,0,0,6,0,0,0,0,0,0,0,0,[1],0,[0,0,1],[6,11],[0],[0])
all_card.append(card1517)
card1518 = Card('置き去り',15,18,1,0, 4,0,0,10,0,0,0,0,0,0,1,0,[1],0,[1,0,1],[0],[0],[0])
all_card.append(card1518)
card1519 = Card('価値ある村',15,19,1,0, 5,2,0,1,0,0,0,0,0,1,0,0,[1],0,[1,0,1],[15],[1,2],[0])
all_card.append(card1519)
card1520 = Card('鉱山道路',15,20,1,0, 5,1,1,0,2,0,0,0,0,0,0,0,[1],0,[0,0,1],[6],[0],[0])
all_card.append(card1520)
card1521 = Card('財産目当て',15,21,1,0, 3,0,0,0,2,0,0,0,0,0,0,0,[1],0,[1,0,1],[3,6],[0],[0])
all_card.append(card1521)
card1522 = Card('シャーマン',15,22,1,0, 2,1,0,0,1,0,0,0,0,0,1,0,[1],0,[0,1,0],[0],[8],[0])
all_card.append(card1522)
card1523 = Card('巡礼者',15,23,1,0, 5,0,0,4,0,0,0,0,0,0,0,0,[1],0,[0,0,1],[8],[0],[0])
all_card.append(card1523)
card1524 = Card('トリックスター',15,24,1,0, 5,0,0,0,0,0,0,0,0,0,0,0,[1],0,[0,0,1],[16],[0],[11,12])
all_card.append(card1524)
card1525 = Card('沼地の小屋',15,25,1,0, 4,2,0,10,0,0,0,0,0,0,0,0,[1],0,[1,0,1],[0],[0],[0])
all_card.append(card1525)
card1526 = Card('港の村',15,26,1,0, 4,2,0,1,1,0,0,0,0,0,0,0,[1],0,[1,0,1],[11],[0],[0])
all_card.append(card1526)
card1527 = Card('埋められた財宝',15,27,2,5, 5,0,1,0,3,0,0,0,0,0,0,0,[2,7],2,[1,0,1],[0],[1,2],[0])
all_card.append(card1527)
card1528 = Card('檻',15,28,2,5, 2,0,0,0,0,0,0,0,0,0,0,1,[2,7],2,[0,0,1],[16],[0],[0])
all_card.append(card1528)
card1529 = Card('ゴンドラ',15,29,2,5, 4,0,0,0,2,0,0,0,0,0,0,0,[2,7],2,[0,1,0],[6,7],[1,2],[0])
all_card.append(card1529)
card1530 = Card('縄',15,30,2,5, 4,0,1,1,1,0,0,0,0,0,1,0,[2,7],2,[0,0,1],[0],[0],[0])
all_card.append(card1530)
card1531 = Card('豊穣',15,31,2,5, 4,0,1,0,3,0,0,0,0,0,0,0,[2,7],2,[0,0,1],[11],[0],[0])
all_card.append(card1531)
card1532 = Card('王の隠し財産',15,32,2,0, 7,0,0,0,0,0,0,0,0,0,0,0,[2],1,[1,0,1],[6,31],[0],[0])
all_card.append(card1532)
card1533 = Card('銀山',15,33,2,0, 5,0,0,0,0,0,0,0,0,1,0,0,[2],1,[0,0,1],[17],[0],[0])
all_card.append(card1533)
card1534 = Card('工具',15,34,2,0, 4,0,0,0,0,0,0,0,0,1,0,0,[2],1,[0,0,1],[0],[0],[0])
all_card.append(card1534)
card1535 = Card('小像',15,35,2,0, 5,0,1,2,1,0,0,0,0,0,0,0,[2],1,[0,0,1],[1,11],[0],[0])
all_card.append(card1535)
card1536 = Card('戦利品の袋',15,36,2,0, 6,0,1,0,1,0,0,0,0,1,0,0,[2],1,[1,0,1],[15],[0],[0])
all_card.append(card1536)
card1537 = Card('つるはし',15,37,2,0, 5,0,0,0,1,0,0,0,0,1,1,0,[2],1,[1,0,0],[11,15],[0],[0])
all_card.append(card1537)
card1538 = Card('ペンダント',15,38,2,0, 5,0,0,0,10,0,0,0,0,0,0,0,[2],1,[0,1,0],[0],[0],[0])
all_card.append(card1538)
card1539 = Card('宝飾卵',15,39,2,0, 2,0,1,0,1,0,0,0,0,1,0,0,[2],1,[0,0,1],[11,15],[3],[0])
all_card.append(card1539)
card1540 = Card('坩堝',15,40,2,0, 4,0,0,0,10,0,0,0,0,0,1,0,[2],1,[0,0,1],[0],[0],[0])
all_card.append(card1540)
full_card.append(card1500a)
full_card.append(card1500b)
full_card.append(card1500c)
full_card.append(card1500d)
full_card.append(card1500e)
full_card.append(card1500f)
full_card.append(card1500g)
full_card.append(card1500h)
full_card.append(card1500i)
full_card.append(card1500j)
full_card.append(card1500k)
full_card.append(card1500l)
full_card.append(card1500m)
full_card.append(card1500n)
full_card.append(card1500o)
full_card.append(card1501)
full_card.append(card1502)
full_card.append(card1503)
full_card.append(card1504)
full_card.append(card1505)
full_card.append(card1506)
full_card.append(card1507)
full_card.append(card1508)
full_card.append(card1509)
full_card.append(card1510)
full_card.append(card1511)
full_card.append(card1512)
full_card.append(card1513)
full_card.append(card1514)
full_card.append(card1515)
full_card.append(card1516)
full_card.append(card1517)
full_card.append(card1518)
full_card.append(card1519)
full_card.append(card1520)
full_card.append(card1521)
full_card.append(card1522)
full_card.append(card1523)
full_card.append(card1524)
full_card.append(card1525)
full_card.append(card1526)
full_card.append(card1527)
full_card.append(card1528)
full_card.append(card1529)
full_card.append(card1530)
full_card.append(card1531)
full_card.append(card1532)
full_card.append(card1533)
full_card.append(card1534)
full_card.append(card1535)
full_card.append(card1536)
full_card.append(card1537)
full_card.append(card1538)
full_card.append(card1539)
full_card.append(card1540)

#特殊カード情報登録
all_spcard = []
#イベント-冒険
spcard0101 = Card('借入',9,1,1,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0101)
spcard0102 = Card('探索',9,2,1,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0102)
spcard0103 = Card('施し',9,3,1,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0103)
spcard0104 = Card('保存',9,4,1,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0104)
spcard0105 = Card('移動遊園地',9,5,1,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0105)
spcard0106 = Card('偵察隊',9,6,1,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0106)
spcard0107 = Card('焚火',9,7,1,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0107)
spcard0108 = Card('探検',9,8,1,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0108)
spcard0109 = Card('立案',9,9,1,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0109)
spcard0110 = Card('渡し船',9,10,1,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0110)
spcard0111 = Card('使節団',9,11,1,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0111)
spcard0112 = Card('巡礼',9,12,1,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0112)
spcard0113 = Card('海路',9,13,1,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0113)
spcard0114 = Card('奇襲',9,14,1,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0114)
spcard0115 = Card('交易',9,15,1,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0115)
spcard0116 = Card('舞踏会',9,16,1,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0116)
spcard0117 = Card('失われた技術',9,17,1,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0117)
spcard0118 = Card('鍛錬',9,18,1,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0118)
spcard0119 = Card('相続',9,19,1,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0119)
spcard0120 = Card('誘導',9,20,1,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0120)
#イベント-帝国
spcard0201 = Card('昇進',10,1,1,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0201)
spcard0202 = Card('掘進',10,2,1,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0202)
spcard0203 = Card('徴税',10,3,1,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0203)
spcard0204 = Card('宴会',10,4,1,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0204)
spcard0205 = Card('儀式',10,5,1,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0205)
spcard0206 = Card('大地への塩まき',10,6,1,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0206)
spcard0207 = Card('結婚式',10,7,1,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0207)
spcard0208 = Card('意外な授かり物',10,8,1,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0208)
spcard0209 = Card('凱旋',10,9,1,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0209)
spcard0210 = Card('征服',10,10,1,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0210)
spcard0211 = Card('制圧',10,11,1,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0211)
spcard0212 = Card('寄付',10,12,1,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0212)
spcard0213 = Card('併合',10,13,1,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0213)
#ランドマーク-帝国
spcard0301 = Card('狼の巣',10,1,2,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0301)
spcard0302 = Card('オベリスク',10,2,2,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0302)
spcard0303 = Card('凱旋門',10,3,2,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0303)
spcard0304 = Card('果樹園',10,4,2,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0304)
spcard0305 = Card('壁',10,5,2,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0305)
spcard0306 = Card('宮殿',10,6,2,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0306)
spcard0307 = Card('汚された神殿',10,7,2,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0307)
spcard0308 = Card('公会堂',10,8,2,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0308)
spcard0309 = Card('山賊の砦',10,9,2,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0309)
spcard0310 = Card('水道橋',10,10,2,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0310)
spcard0311 = Card('戦場',10,11,2,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0311)
spcard0312 = Card('塔',10,12,2,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0312)
spcard0313 = Card('闘技場',10,13,2,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0313)
spcard0314 = Card('峠',10,14,2,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0314)
spcard0315 = Card('砦',10,15,2,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0315)
spcard0316 = Card('博物館',10,16,2,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0316)
spcard0317 = Card('噴水',10,17,2,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0317)
spcard0318 = Card('墓標',10,18,2,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0318)
spcard0319 = Card('迷宮',10,19,2,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0319)
spcard0320 = Card('浴場',10,20,2,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0320)
spcard0321 = Card('列柱',10,21,2,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0321)
#プロジェクト-ルネサンス
spcard0401 = Card('運河',12,1,3,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0401)
spcard0402 = Card('縁日',12,2,3,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0402)
spcard0403 = Card('学園',12,3,3,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0403)
spcard0404 = Card('艦隊',12,4,3,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0404)
spcard0405 = Card('技術革新',12,5,3,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0405)
spcard0406 = Card('ギルド集会所',12,6,3,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0406)
spcard0407 = Card('下水道',12,7,3,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0407)
spcard0408 = Card('サイロ',12,8,3,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0408)
spcard0409 = Card('山砦',12,9,3,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0409)
spcard0410 = Card('資本主義',12,10,3,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0410)
spcard0411 = Card('城門',12,11,3,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0411)
spcard0412 = Card('星図',12,12,3,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0412)
spcard0413 = Card('大聖堂',12,13,3,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0413)
spcard0414 = Card('探査',12,14,3,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0414)
spcard0415 = Card('道路網',12,15,3,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0415)
spcard0416 = Card('ピアッツァ',12,16,3,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0416)
spcard0417 = Card('兵舎',12,17,3,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0417)
spcard0418 = Card('野外劇',12,18,3,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0418)
spcard0419 = Card('輪作',12,19,3,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0419)
spcard0420 = Card('悪巧み',12,20,3,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0420)
#イベント-移動動物園
spcard0501 = Card('遅延',13,1,1,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0501)
spcard0502 = Card('絶望',13,2,1,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0502)
spcard0503 = Card('博打',13,3,1,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0503)
spcard0504 = Card('追求',13,4,1,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0504)
spcard0505 = Card('乗馬',13,5,1,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0505)
spcard0506 = Card('苦労',13,6,1,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0506)
spcard0507 = Card('増大',13,7,1,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0507)
spcard0508 = Card('進軍',13,8,1,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0508)
spcard0509 = Card('輸送',13,9,1,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0509)
spcard0510 = Card('放逐',13,10,1,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0510)
spcard0511 = Card('特価品',13,11,1,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0511)
spcard0512 = Card('投資',13,12,1,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0512)
spcard0513 = Card('今を生きる',13,13,1,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0513)
spcard0514 = Card('商売',13,14,1,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0514)
spcard0515 = Card('要求',13,15,1,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0515)
spcard0516 = Card('暴走',13,16,1,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0516)
spcard0517 = Card('刈り入れ',13,17,1,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0517)
spcard0518 = Card('包領',13,18,1,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0518)
spcard0519 = Card('同盟',13,19,1,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0519)
spcard0520 = Card('植民',13,20,1,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0520)
#習性-移動動物園
spcard0601 = Card('チョウの習性',10,1,4,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0601)
spcard0602 = Card('ラクダの習性',13,2,4,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0602)
spcard0603 = Card('カメレオンの習性',13,3,4,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0603)
spcard0604 = Card('カエルの習性',13,4,4,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0604)
spcard0605 = Card('ヤギの習性',13,5,4,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0605)
spcard0606 = Card('馬の習性',13,6,4,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0606)
spcard0607 = Card('モグラの習性',13,7,4,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0607)
spcard0608 = Card('サルの習性',13,8,4,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0608)
spcard0609 = Card('ハツカネズミの習性',13,9,4,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0609)
spcard0610 = Card('ラバの習性',13,10,4,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0610)
spcard0611 = Card('カワウソの習性',13,11,4,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0611)
spcard0612 = Card('フクロウの習性',13,12,4,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0612)
spcard0613 = Card('雄牛の習性',13,13,4,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0613)
spcard0614 = Card('豚の習性',13,14,4,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0614)
spcard0615 = Card('ドブネズミの習性',13,15,4,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0615)
spcard0616 = Card('アザラシの習性',13,16,4,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0616)
spcard0617 = Card('羊の習性',13,17,4,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0617)
spcard0618 = Card('リスの習性',13,18,4,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0618)
spcard0619 = Card('ウミガメの習性',13,19,4,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0619)
spcard0620 = Card('ミミズの習性',13,20,4,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0620)
#同盟-同盟
spcard0701 = Card('建築家ギルド',14,1,5,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
#'カード獲得時、2好意を使用してそのカードのコスト未満の勝利点以外のカード1枚を獲得できる')
all_spcard.append(spcard0701)
spcard0702 = Card('遊牧民団',14,2,5,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
#'3コスト以上のカード獲得時、1好意を使用して+1カード、+1アクション、+1購入のどれか1つの効果を得られる')
all_spcard.append(spcard0702)
spcard0703 = Card('穴居民',14,3,5,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
#'ターン開始時、1好意を使用して手札を1枚捨てて1ドローすることを好きな回数行える')
all_spcard.append(spcard0703)
spcard0704 = Card('魔女の輪',14,4,5,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
#'連携カードを使用後、3好意を使用して他のプレイヤー全員に呪いを獲得させられる')
all_spcard.append(spcard0704)
spcard0705 = Card('都市国家',14,5,5,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
#'自分のターンのアクションカード獲得時、2好意を使用してそのカードを使用できる')
all_spcard.append(spcard0705)
spcard0706 = Card('沿岸の避難港',14,6,5,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
#'クリーンアップフェイズに手札を捨てる時、使用した好意の数だけ手札を脇に置き、ターン終了時に手札に加える')
all_spcard.append(spcard0706)
spcard0707 = Card('工芸家ギルド',14,7,5,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
#'ターン開始時、2好意を使用して4コスト以下のカード1枚を山札の上に獲得できる')
all_spcard.append(spcard0707)
spcard0708 = Card('砂漠の案内人',14,8,5,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
#'ターン開始時、1好意を使用して手札をすべて捨てて山札から5枚引くことを好きな回数行える')
all_spcard.append(spcard0708)
spcard0709 = Card('発明家の家族',14,9,5,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
#'購入フェイズ開始時、勝利点以外の山に1好意を置ける / カードのコストはその山に置かれている(全員の)好意だけ減る')
all_spcard.append(spcard0709)
spcard0710 = Card('写本士の仲間たち',14,10,5,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
#'アクションカードを使用した後に手札が4枚以下の場合、1好意を使用すれば+1カード')
all_spcard.append(spcard0710)
spcard0711 = Card('森の居住者',14,11,5,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
#'ターン開始時、1好意を使用し山札の上から3枚を見て好きな枚数を捨て札、残りはデッキの上に好きな順番で置ける')
all_spcard.append(spcard0711)
spcard0712 = Card('すり師団',14,12,5,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
#'ターン開始時、1好意を使用しなければ手札が4枚になるまで捨て札にする')
all_spcard.append(spcard0712)
spcard0713 = Card('島民',14,13,5,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
#'ターン終了時、5好意を使用して追加ターンを得られる (ただし連続3ターンとなる場合は得られない)')
all_spcard.append(spcard0713)
spcard0714 = Card('銀行家連盟',14,14,5,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
#'購入フェイズ開始時、持っている好意4つにつき+1コスト')
all_spcard.append(spcard0714)
spcard0715 = Card('小売店主連盟',14,15,5,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
#'連携カードを使用した後、5好意以上あれば+1コスト、10好意以上あればさらに+1アクション+1購入')
all_spcard.append(spcard0715)
spcard0716 = Card('市場の町',14,16,5,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
#'購入フェイズ開始時、1好意を使用して手札のアクションカード1枚を使用することを好きな回数行える')
all_spcard.append(spcard0716)
spcard0717 = Card('山の民',14,17,5,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
#'ターン開始時、5好意を使用して+3カード')
all_spcard.append(spcard0717)
spcard0718 = Card('占星術師団',14,18,5,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
#'シャッフル時、使用する好意の数まで捨て札からカードを選び、山札の上に置ける')
all_spcard.append(spcard0718)
spcard0719 = Card('メイソン団',14,19,5,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
#'シャッフル時、使用する好意の数につき2枚までカードを捨て札に置ける')
all_spcard.append(spcard0719)
spcard0720 = Card('平和的教団',14,20,5,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
#'購入フェイズ開始時、使用した好意の数だけ手札を廃棄できる')
all_spcard.append(spcard0720)
spcard0721 = Card('高原の羊飼い',14,21,5,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
#'得点計算時、1好意と2コストのカード1枚のセットにつき2点')
all_spcard.append(spcard0721)
spcard0722 = Card('罠師の小屋',14,22,5,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
#'カード獲得時、1好意を使用して山札の上に置ける')
all_spcard.append(spcard0722)
spcard0723 = Card('木工ギルド',14,23,5,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
#'購入フェイズ開始時、1好意を使用して手札からアクションカード1枚廃棄、アクションカード1枚獲得できる')
all_spcard.append(spcard0723)
#イベント-略奪
spcard0801 = Card('埋葬',15,1,1,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0801)
spcard0802 = Card('回避',15,2,1,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0802)
spcard0803 = Card('配達',15,3,1,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0803)
spcard0804 = Card('危難',15,4,1,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0804)
spcard0805 = Card('突貫',15,5,1,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0805)
spcard0806 = Card('襲撃',15,6,1,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0806)
spcard0807 = Card('発進',15,7,1,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0807)
spcard0808 = Card('鏡映',15,8,1,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0808)
spcard0809 = Card('準備',15,9,1,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0809)
spcard0810 = Card('物色',15,10,1,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0810)
spcard0811 = Card('旅行',15,11,1,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0811)
spcard0812 = Card('大渦巻',15,12,1,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0812)
spcard0813 = Card('略奪行為',15,13,1,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0813)
spcard0814 = Card('侵略',15,14,1,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0814)
spcard0815 = Card('繁栄',15,15,1,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0815)
#特性-略奪
spcard0901 = Card('安価な',15,1,6,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0901)
spcard0902 = Card('受け継がれた',15,2,6,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0902)
spcard0903 = Card('内気な',15,3,6,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0903)
spcard0904 = Card('運命の',15,4,6,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0904)
spcard0905 = Card('近隣の',15,5,6,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0905)
spcard0906 = Card('敬虔な',15,6,6,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0906)
spcard0907 = Card('鼓舞する',15,7,6,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0907)
spcard0908 = Card('せっかちな',15,8,6,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0908)
spcard0909 = Card('疲れ知らずの',15,9,6,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0909)
spcard0910 = Card('忍耐強い',15,10,6,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0910)
spcard0911 = Card('呪われた',15,11,6,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0911)
spcard0912 = Card('へつらう',15,12,6,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0912)
spcard0913 = Card('無謀な',15,13,6,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0913)
spcard0914 = Card('友好的な',15,14,6,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0914)
spcard0915 = Card('豊かな',15,15,6,0, 0,0,0,0,0,0,0,0,0,0,1,0,[0],0,[0,0,1],[0],[0],[0])
all_spcard.append(spcard0915)


#メインウインドウ
root = tk.Tk()
root.title("Dominion Randomizer")
root.geometry('1200x700+0+0')
page = 0

#メニュー画面
title = tk.Label(root, text="Dominion Tool Menu", font=("Helvetica",36))
title.pack(pady=20)
menu1 = tk.Button(root, text='ランダマイザー',command=random_select_set, font=("Helvetica",20))
menu1.pack(pady=10)
menu2 = tk.Button(root, text='アティネイター',command=ati_start, font=("Helvetica",20))
menu2.pack(pady=10)

#ランダマイザー：拡張セット選択画面
skip = [False]   #二度目の選択となる場合スキップするための変数
subtitle1 = tk.Label(root, text="Dominion Randomizer", font=("Helvetica",18))
random_text1 = tk.Label(root, text="用いる拡張セットを選択してください")
frame_set03 = tk.Frame(root, pady=10)
set0_v = tk.BooleanVar(value=False)
cb0 = tk.Checkbutton(frame_set03, text='基本', font=("Helvetica",12), variable=set0_v)
set1_v = tk.BooleanVar(value=False)
cb1 = tk.Checkbutton(frame_set03, text='陰謀', font=("Helvetica",12), variable=set1_v)
set2_v = tk.BooleanVar(value=False)
cb2 = tk.Checkbutton(frame_set03, text='海辺', font=("Helvetica",12), variable=set2_v)
set3_v = tk.BooleanVar(value=False)
cb3 = tk.Checkbutton(frame_set03, text='錬金術', font=("Helvetica",12), variable=set3_v)
cb0.pack(side=tk.LEFT,padx=25,anchor=tk.W)
cb1.pack(side=tk.LEFT,padx=25,anchor=tk.W)
cb2.pack(side=tk.LEFT,padx=25,anchor=tk.W)
cb3.pack(side=tk.LEFT,padx=25,anchor=tk.W)
frame_set47 = tk.Frame(root, pady=10)
set4_v = tk.BooleanVar(value=False)
cb4 = tk.Checkbutton(frame_set47, text='繁栄', font=("Helvetica",12), variable=set4_v)
set5_v = tk.BooleanVar(value=False)
cb5 = tk.Checkbutton(frame_set47, text='収穫祭', font=("Helvetica",12), variable=set5_v)
set6_v = tk.BooleanVar(value=False)
cb6 = tk.Checkbutton(frame_set47, text='異郷', font=("Helvetica",12), variable=set6_v)
set7_v = tk.BooleanVar(value=False)
cb7 = tk.Checkbutton(frame_set47, text='暗黒時代', font=("Helvetica",12), variable=set7_v)
cb4.pack(side=tk.LEFT,padx=25,anchor=tk.W)
cb5.pack(side=tk.LEFT,padx=25,anchor=tk.W)
cb6.pack(side=tk.LEFT,padx=25,anchor=tk.W)
cb7.pack(side=tk.LEFT,padx=25,anchor=tk.W)
frame_set811 = tk.Frame(root, pady=10)
set8_v = tk.BooleanVar(value=False)
cb8 = tk.Checkbutton(frame_set811, text='ギルド', font=("Helvetica",12), variable=set8_v)
set9_v = tk.BooleanVar(value=False)
cb9 = tk.Checkbutton(frame_set811, text='冒険', font=("Helvetica",12), variable=set9_v)
set10_v = tk.BooleanVar(value=False)
cb10 = tk.Checkbutton(frame_set811, text='帝国', font=("Helvetica",12), variable=set10_v)
set11_v = tk.BooleanVar(value=False)
cb11 = tk.Checkbutton(frame_set811, text='夜想曲', font=("Helvetica",12), variable=set11_v)
cb8.pack(side=tk.LEFT,padx=25,anchor=tk.W)
cb9.pack(side=tk.LEFT,padx=25,anchor=tk.W)
cb10.pack(side=tk.LEFT,padx=25,anchor=tk.W)
cb11.pack(side=tk.LEFT,padx=25,anchor=tk.W)
frame_set1215 = tk.Frame(root, pady=10)
set12_v = tk.BooleanVar(value=False)
cb12 = tk.Checkbutton(frame_set1215, text='ルネサンス', font=("Helvetica",12), variable=set12_v)
set13_v = tk.BooleanVar(value=False)
cb13 = tk.Checkbutton(frame_set1215, text='移動動物園', font=("Helvetica",12), variable=set13_v)
set14_v = tk.BooleanVar(value=False)
cb14 = tk.Checkbutton(frame_set1215, text='同盟', font=("Helvetica",12), variable=set14_v)
set15_v = tk.BooleanVar(value=False)
cb15 = tk.Checkbutton(frame_set1215, text='略奪', font=("Helvetica",12), variable=set15_v)
cb12.pack(side=tk.LEFT,padx=25,anchor=tk.W)
cb13.pack(side=tk.LEFT,padx=25,anchor=tk.W)
cb14.pack(side=tk.LEFT,padx=25,anchor=tk.W)
cb15.pack(side=tk.LEFT,padx=25,anchor=tk.W)
frame_spset03 = tk.Frame(root, pady=10)
sp0_v = tk.BooleanVar(value=False)
sp0 = tk.Checkbutton(frame_spset03, text='イベント（冒険）', font=("Helvetica",12), variable=sp0_v)
sp1_v = tk.BooleanVar(value=False)
sp1 = tk.Checkbutton(frame_spset03, text='イベント（帝国）', font=("Helvetica",12), variable=sp1_v)
sp2_v = tk.BooleanVar(value=False)
sp2 = tk.Checkbutton(frame_spset03, text='ランドマーク', font=("Helvetica",12), variable=sp2_v)
sp3_v = tk.BooleanVar(value=False)
sp3 = tk.Checkbutton(frame_spset03, text='プロジェクト', font=("Helvetica",12), variable=sp3_v)
sp0.pack(side=tk.LEFT,padx=15,anchor=tk.W)
sp1.pack(side=tk.LEFT,padx=15,anchor=tk.W)
sp2.pack(side=tk.LEFT,padx=15,anchor=tk.W)
sp3.pack(side=tk.LEFT,padx=15,anchor=tk.W)
frame_spset47 = tk.Frame(root, pady=10)
sp4_v = tk.BooleanVar(value=False)
sp4 = tk.Checkbutton(frame_spset47, text='イベント（移動動物園）', font=("Helvetica",12), variable=sp4_v)
sp5_v = tk.BooleanVar(value=False)
sp5 = tk.Checkbutton(frame_spset47, text='習性', font=("Helvetica",12), variable=sp5_v)
sp6_v = tk.BooleanVar(value=False)
sp6 = tk.Checkbutton(frame_spset47, text='同盟', font=("Helvetica",12), variable=sp6_v)
sp7_v = tk.BooleanVar(value=False)
sp7 = tk.Checkbutton(frame_spset47, text='イベント（略奪）', font=("Helvetica",12), variable=sp7_v)
sp8_v = tk.BooleanVar(value=False)
sp8 = tk.Checkbutton(frame_spset47, text='特性', font=("Helvetica",12), variable=sp8_v)
sp4.pack(side=tk.LEFT,padx=25,anchor=tk.W)
sp5.pack(side=tk.LEFT,padx=25,anchor=tk.W)
sp6.pack(side=tk.LEFT,padx=25,anchor=tk.W)
sp7.pack(side=tk.LEFT,padx=25,anchor=tk.W)
sp8.pack(side=tk.LEFT,padx=25,anchor=tk.W)
selectcheck = tk.Button(root, text='選択完了', font=(18), command=random_selected)
allcheck = tk.Button(root, text='所持セット全使用', font=(18), command=random_all_set)
useset = []
usecard = []
usespset = []
usespcard = []
totalcard = []
backmenu1a = tk.Button(root, text='タイトルに戻る',command=backmenu_1a, font=("Helvetica",20))

#ランダマイザー：実行画面1
frame_randomB = tk.Frame(root, pady=10)
frame_delete = tk.Frame(frame_randomB, pady=10)
make_one = tk.Button(frame_randomB, text='生成：1',command=random_card_gene_1)
make_ten = tk.Button(frame_randomB, text='生成：10',command=random_card_gene_10)
delete_one = tk.Button(frame_delete, text='削除：',command=delete_card)
delete_one_area = tk.Entry(frame_delete, width = 5)
reset = tk.Button(frame_randomB, text='保存せずリセット',command=reset_unsave)
nextset = tk.Button(frame_randomB, text='保存してリセット',command=reset_save)
savereset = tk.Button(frame_randomB, text='記憶リセット',command=save_reset)
make_one.pack(side=tk.LEFT,padx=25,anchor=tk.W)
make_ten.pack(side=tk.LEFT,padx=25,anchor=tk.W)
delete_one.pack(side=tk.LEFT,anchor=tk.W)
delete_one_area.pack(side=tk.LEFT,anchor=tk.W)
frame_delete.pack(side=tk.LEFT,padx=25,anchor=tk.W)
reset.pack(side=tk.LEFT,padx=25,anchor=tk.W)
nextset.pack(side=tk.LEFT,padx=25,anchor=tk.W)
savereset.pack(side=tk.LEFT,padx=25,anchor=tk.W)
frame_geneCard14 = tk.Frame(root, pady=20)
card1 = tk.Label(frame_geneCard14, text=" - ", font=("Helvetica",24))
card1d = tk.Label(frame_geneCard14, text=" ", font=("Helvetica",12))
card2 = tk.Label(frame_geneCard14, text=" - ", font=("Helvetica",24))
card2d = tk.Label(frame_geneCard14, text=" ", font=("Helvetica",12))
card3 = tk.Label(frame_geneCard14, text=" - ", font=("Helvetica",24))
card3d = tk.Label(frame_geneCard14, text=" ", font=("Helvetica",12))
card4 = tk.Label(frame_geneCard14, text=" - ", font=("Helvetica",24))
card4d = tk.Label(frame_geneCard14, text=" ", font=("Helvetica",12))
card1.pack(side=tk.LEFT,anchor=tk.W)
card1d.pack(side=tk.LEFT,anchor=tk.W)
card2.pack(side=tk.LEFT,anchor=tk.W)
card2d.pack(side=tk.LEFT,anchor=tk.W)
card3.pack(side=tk.LEFT,anchor=tk.W)
card3d.pack(side=tk.LEFT,anchor=tk.W)
card4.pack(side=tk.LEFT,anchor=tk.W)
card4d.pack(side=tk.LEFT,anchor=tk.W)
frame_geneCard58 = tk.Frame(root, pady=20)
card5 = tk.Label(frame_geneCard58, text=" - ", font=("Helvetica",24))
card5d = tk.Label(frame_geneCard58, text=" ", font=("Helvetica",12))
card6 = tk.Label(frame_geneCard58, text=" - ", font=("Helvetica",24))
card6d = tk.Label(frame_geneCard58, text=" ", font=("Helvetica",12))
card7 = tk.Label(frame_geneCard58, text=" - ", font=("Helvetica",24))
card7d = tk.Label(frame_geneCard58, text=" ", font=("Helvetica",12))
card8 = tk.Label(frame_geneCard58, text=" - ", font=("Helvetica",24))
card8d = tk.Label(frame_geneCard58, text=" ", font=("Helvetica",12))
card5.pack(side=tk.LEFT,anchor=tk.W)
card5d.pack(side=tk.LEFT,anchor=tk.W)
card6.pack(side=tk.LEFT,anchor=tk.W)
card6d.pack(side=tk.LEFT,anchor=tk.W)
card7.pack(side=tk.LEFT,anchor=tk.W)
card7d.pack(side=tk.LEFT,anchor=tk.W)
card8.pack(side=tk.LEFT,anchor=tk.W)
card8d.pack(side=tk.LEFT,anchor=tk.W)
frame_geneCard912 = tk.Frame(root, pady=20)
card9 = tk.Label(frame_geneCard912, text=" - ", font=("Helvetica",24))
card9d = tk.Label(frame_geneCard912, text=" ", font=("Helvetica",12))
card10 = tk.Label(frame_geneCard912, text=" - ", font=("Helvetica",24))
card10d = tk.Label(frame_geneCard912, text=" ", font=("Helvetica",12))
card11 = tk.Label(frame_geneCard912, text=" ", font=("Helvetica",24))
card11d = tk.Label(frame_geneCard912, text=" ", font=("Helvetica",12))
card12 = tk.Label(frame_geneCard912, text=" ", font=("Helvetica",24))
card12d = tk.Label(frame_geneCard912, text=" ", font=("Helvetica",12))
card9.pack(side=tk.LEFT,anchor=tk.W)
card9d.pack(side=tk.LEFT,anchor=tk.W)
card10.pack(side=tk.LEFT,anchor=tk.W)
card10d.pack(side=tk.LEFT,anchor=tk.W)
card11.pack(side=tk.LEFT,anchor=tk.W)
card11d.pack(side=tk.LEFT,anchor=tk.W)
card12.pack(side=tk.LEFT,anchor=tk.W)
card12d.pack(side=tk.LEFT,anchor=tk.W)
geneCard = [card1,card1d,card2,card2d,card3,card3d,card4,card4d,card5,card5d,card6,card6d,card7,card7d,card8,card8d,card9,card9d,card10,card10d,card11,card11d,card12,card12d]
random_num_org = []
random_num = []
#ランダマイザー：実行画面2
frame_sprandomB = tk.Frame(root, pady=10)
make_spone = tk.Button(frame_sprandomB, text='生成：1',command=random_spcard_gene_1)
spreset = tk.Button(frame_sprandomB, text='保存せずリセット',command=spreset_unsave)
spnextset = tk.Button(frame_sprandomB, text='保存してリセット',command=spreset_save)
spsavereset = tk.Button(frame_sprandomB, text='記憶リセット',command=spsave_reset)
make_spone.pack(side=tk.LEFT,padx=25,anchor=tk.W)
spreset.pack(side=tk.LEFT,padx=25,anchor=tk.W)
spnextset.pack(side=tk.LEFT,padx=25,anchor=tk.W)
spsavereset.pack(side=tk.LEFT,padx=25,anchor=tk.W)
frame_geneSP1 = tk.Frame(root, pady=5)
spcard1 = tk.Label(frame_geneSP1, text=" - ", font=("Helvetica",24))
spcard1d = tk.Label(frame_geneSP1, text=" ", font=("Helvetica",12))
spcard1.pack(side=tk.LEFT,anchor=tk.W)
spcard1d.pack(side=tk.LEFT,anchor=tk.W)
frame_geneSP2 = tk.Frame(root, pady=5)
spcard2 = tk.Label(frame_geneSP2, text=" - ", font=("Helvetica",24))
spcard2d = tk.Label(frame_geneSP2, text=" ", font=("Helvetica",12))
spcard2.pack(side=tk.LEFT,anchor=tk.W)
spcard2d.pack(side=tk.LEFT,anchor=tk.W)
frame_geneSP3 = tk.Frame(root, pady=5)
spcard3 = tk.Label(frame_geneSP3, text=" ", font=("Helvetica",24))
spcard3d = tk.Label(frame_geneSP3, text=" ", font=("Helvetica",12))
spcard3.pack(side=tk.LEFT,anchor=tk.W)
spcard3d.pack(side=tk.LEFT,anchor=tk.W)
frame_geneSP4 = tk.Frame(root, pady=5)
spcard4 = tk.Label(frame_geneSP4, text=" ", font=("Helvetica",24))
spcard4d = tk.Label(frame_geneSP4, text=" ", font=("Helvetica",12))
spcard4.pack(side=tk.LEFT,anchor=tk.W)
spcard4d.pack(side=tk.LEFT,anchor=tk.W)
geneSPCard = [spcard1,spcard1d,spcard2,spcard2d,spcard3,spcard3d,spcard4,spcard4d]
random_spnum_org = []
random_spnum = []
backmenu1b = tk.Button(root, text='タイトルに戻る',command=backmenu_1b, font=("Helvetica",20))


#アティネイター：開始時
questions = []
subtitle2 = tk.Label(root, text="Dominion Artinater", font=("Helvetica",18))
frame_ati_main = tk.Frame(root)
text_ati_Q = tk.Label(frame_ati_main, text='カードを1枚思い浮かべましたか？',font=("Helvetica",16))
text_ati_Q.pack()
frame_ati_btn = tk.Frame(frame_ati_main)
btn_ati_Y = tk.Button(frame_ati_btn, text='はい',font=("Helvetica",20), command=ati_main)
btn_ati_N = tk.Button(frame_ati_btn, text='やめる',command=ati_back1, font=("Helvetica",20))
btn_ati_Y.pack(side=tk.LEFT,padx=50)
btn_ati_N.pack(side=tk.LEFT,padx=50)
frame_ati_btn.pack()
#アティネイター：終了時
frame_ati_result = tk.Frame(root)
text_ati_result = tk.Label(frame_ati_result, text='',font=("Helvetica",24))
text_ati_result1 = tk.Label(frame_ati_result, text=' ',font=("Helvetica",32))
btn_ati_result = tk.Button(frame_ati_result, text='TOPメニューに戻る',font=("Helvetica",20),command=ati_fin_result)
text_ati_result.pack()
text_ati_result1.pack()
btn_ati_result.pack()

#アティネイターメイン画面：Left
#frame_art_main = tk.Frame(root)
#frame_art_mainleft = tk.Frame(frame_art_main,width=500)
#canvas_art_record = tk.Canvas(frame_art_mainleft)
#frame_art_record = tk.Frame(canvas_art_record)
#scrollbar_art_record = tk.Scrollbar(canvas_art_record,orient=tk.VERTICAL,command=canvas_art_record.yview)
#canvas_art_record.configure(scrollregion=(0,0,500,900))
#canvas_art_record.configure(yscrollcommand=scrollbar_art_record.set)
#scrollbar_art_record.pack(side=tk.RIGHT,fill=tk.Y)
#canvas_art_record.pack(expand=True,fill=tk.BOTH)
#test = tk.Label(frame_art_record, text="CCCCCCCCCCCCCCCCC", font=("Helvetica",18))
#test.pack()
#canvas_art_record.create_window((0,0),window=frame_art_record,anchor="nw",width=500,height=900)
#frame_art_mainleft.pack(side=tk.LEFT,fill=tk.Y)
#アティネイターメイン画面：Right
#frame_art_mainright = tk.Frame(frame_art_main,width=500)
#canvas_art_question = tk.Canvas(frame_art_mainright)
#frame_art_question = tk.Frame(canvas_art_question)
#scrollbar_art_question = tk.Scrollbar(canvas_art_question,orient=tk.VERTICAL,command=canvas_art_question.yview)
#canvas_art_question.configure(scrollregion=(0,0,500,900))
#canvas_art_question.configure(yscrollcommand=scrollbar_art_question.set)
#scrollbar_art_question.pack(side=tk.RIGHT,fill=tk.Y)
#canvas_art_question.pack(expand=True,fill=tk.BOTH)
#testQ = tk.Label(frame_art_mainleft, text="TTTTTTTTT", font=("Helvetica",18))
#testQ.pack()
#canvas_art_question.create_window((0,0),window=frame_art_question,anchor="nw",width=500,height=900)
#frame_art_mainright.pack(side=tk.LEFT,fill=tk.Y)

#ウインドウの表示
root.mainloop()
